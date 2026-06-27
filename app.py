from flask import Flask, render_template, request, jsonify
import joblib, numpy as np, pandas as pd, json, os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.joblib')
model = joblib.load(MODEL_PATH)

FEATURE_COLS = [
    'battery_power','blue','clock_speed','dual_sim','fc','four_g',
    'int_memory','m_dep','mobile_wt','n_cores','pc','px_height',
    'px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi'
]

PRICE_LABELS = {
    0: {'label': 'Low Cost',       'range': '₹5,000 – ₹15,000',  'color': '#22c55e', 'icon': '💚'},
    1: {'label': 'Medium Cost',    'range': '₹15,000 – ₹25,000', 'color': '#3b82f6', 'icon': '💙'},
    2: {'label': 'High Cost',      'range': '₹25,000 – ₹40,000', 'color': '#f59e0b', 'icon': '🧡'},
    3: {'label': 'Very High Cost', 'range': '₹40,000+',           'color': '#ef4444', 'icon': '❤️'},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [float(data[col]) for col in FEATURE_COLS]
        df = pd.DataFrame([features], columns=FEATURE_COLS)
        pred = int(model.predict(df)[0])
        proba = model.predict_proba(df)[0].tolist()
        info = PRICE_LABELS[pred]
        return jsonify({
            'success': True,
            'prediction': pred,
            'label': info['label'],
            'range': info['range'],
            'color': info['color'],
            'icon': info['icon'],
            'probabilities': [round(p * 100, 1) for p in proba],
            'prob_labels': [PRICE_LABELS[i]['label'] for i in range(4)],
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/feature_importance')
def feature_importance():
    with open('static/feature_importance.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

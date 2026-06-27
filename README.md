# 📱 Mobile Price Predictor

A machine learning web app that predicts the **price range** of a mobile phone based on its hardware specifications.

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the app
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## 🗂️ Project Structure

```
mobile-price-app/
│
├── app.py                        ← Flask backend + ML model
├── model.joblib                  ← Trained Random Forest model
├── requirements.txt              ← Python dependencies
│
├── templates/
│   └── index.html                ← Frontend UI
│
└── static/
    └── feature_importance.json   ← Feature importance data
```

---

## 🤖 ML Details

| Item | Value |
|------|-------|
| Algorithm | Random Forest Classifier |
| Dataset | [Kaggle – Mobile Price Classification](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification) |
| Features | 20 hardware specs (RAM, battery, pixels, etc.) |
| Target | Price Range: 0 (Low) → 3 (Very High) |
| Test Accuracy | ~73% |

### Top Features
1. **RAM** — strongest predictor by far
2. Battery Power
3. Pixel Height / Width
4. Internal Memory

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, scikit-learn, joblib
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Model:** Random Forest (trained on 2000 samples, 200 estimators)

---

## 📸 Features of the App

- 🎚️ Interactive sliders for all 20 phone specs
- 🔘 Toggle buttons for Yes/No features (4G, Bluetooth, WiFi etc.)
- 🔮 Real-time price range prediction
- 📊 Confidence bars showing probability for each class
- 📈 Feature importance chart (top 10 features)

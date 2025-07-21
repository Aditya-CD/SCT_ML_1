# 🏠 House Price Predictor (India) using Linear Regression

A Machine Learning-powered web application that predicts house prices in India based on various user inputs such as the number of bedrooms, bathrooms, square footage, and location. Built using **Linear Regression** and deployed with **Streamlit** for an intuitive user interface.

---

## 📌 Table of Contents

- [Demo](#-demo)
- [Overview](#-overview)
- [Data Insights](#-data-insights)
  - [Feature Distribution](#-feature-distribution)
  - [Feature Correlation](#-feature-correlation)
- [Web App Preview](#-web-app-preview)
- [Tech Stack](#-tech-stack)
- [How to Run Locally](#-how-to-run-locally)
- [Project Structure](#-project-structure)
- [Future Work](#-future-work)
- [License](#-license)

---

## 🚀 Demo

Live demo (optional): [Streamlit App](#) *(Coming Soon)*

---

## 🧠 Overview

This project utilizes **Linear Regression** from `scikit-learn` to build a predictive model for housing prices. It uses basic real estate features commonly found in Indian datasets and provides instant price estimations via a simple web interface.

---

## 📊 Data Insights

### 📈 Feature Distribution

Here you can visualize the distribution of features such as bedrooms, bathrooms, size, etc.


![Feature Histogram Placeholder](https://github.com/Aditya-CD/SCT_ML_1/blob/main/visuals/histogram.png)

---

### 🔥 Feature Correlation

A heatmap to analyze the correlation between different features in the dataset.


![Correlation Heatmap Placeholder](https://github.com/Aditya-CD/SCT_ML_1/blob/main/visuals/heatmap.png)

---

## 🌐 Web App Preview

Below is the screenshot of the web-based interface created using Streamlit.

> 📌 Replace the image below with your actual web app screenshot.

![Web App UI Placeholder]<img width="1365" height="635" alt="Screenshot 2025-07-19 160143" src="https://github.com/user-attachments/assets/2fff8368-fe52-4293-9938-705e66076bde" />


---

## 🛠 Tech Stack

- **Python** 🐍
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Linear Regression model
- **Joblib** – Model serialization
- **Streamlit** – Frontend Web App

---

## 🏁 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/ADITYA-CD/house-price-predictor.git
   cd house-price-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
house-price-predictor/
│
├── data/                  # Dataset (CSV or Excel)
├── model/                 
│   └── model.pkl          # Trained Linear Regression and Random Forest model
├── visuals/               
│   ├── histogram.png      # Feature distribution plots
│   └── heatmap.png        # Feature correlation heatmap
├── app.py                 # Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🔮 Future Work

- Integrate more advanced models like XGBoost.
- Include geolocation-based predictions.
- Deploy on **Streamlit Cloud** or **Hugging Face Spaces**.
- Add a comparison dashboard for different model performances.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

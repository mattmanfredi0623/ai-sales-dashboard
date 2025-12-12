# AI-Powered Sales Dashboard 📊

An interactive sales analytics dashboard built with [Streamlit](https://streamlit.io), enhanced with AI features like automatic insight generation and sales forecasting.

---

## 🔍 Features

- ✅ Upload your own CSV files with flexible column name matching  
- 📊 Filter by month and region using intuitive checkboxes  
- 🧠 AI-generated insight summaries based on your uploaded data  
- 📈 30-day sales forecasting using linear regression  
- 💡 Clean, interactive visualizations with Plotly  

---

## 🚀 How to Run Locally

1. **Clone the repository**
2. **Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start the Streamlit app**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── core/
│   ├── analysis.py
│   ├── data_loader.py
│   └── insights.py
├── components/
│   └── charts.py
├── config/
│   └── settings.py
├── utils/
│   └── helper.py
├── pages/
│   └── page_eda.py
└── data/
    └── sales_data.csv
```

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

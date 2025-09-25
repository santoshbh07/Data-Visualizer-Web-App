# 📊 Data Visualizer

A simple **Streamlit web app** to upload CSV/Excel files and quickly create basic data visualizations.

---

## 🚀 Features

* Upload a **CSV** or **Excel** file
* Preview the dataset
* Choose columns for **X and Y axes**
* Plot common charts: Line, Bar, Scatter, Histogram, Count
* Download generated plots as PNG

---

## ▶️ How to Run

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:

   ```bash
   streamlit run main.py
   ```

3. **Open in browser**:

   ```
   http://localhost:8501/
   ```

---

## 📥 Download Plot

After generating a chart, click the **“Download Plot”** button to save it as PNG.

---

# 📦 requirements.txt

```
pandas
numpy
matplotlib
seaborn
streamlit
openpyxl
```

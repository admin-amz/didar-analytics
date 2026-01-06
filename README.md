# didar-analytics
# Biomedical Research Data Analysis (Python)

## 📌 Project Overview
This project demonstrates how biomedical research data can be cleaned,
validated, analyzed, and summarized using **Python (Pandas + NumPy)**.

The script processes raw participant data and generates categorized
Excel sheets along with demographic statistics.

---

## 🛠 Tools & Skills Used
- Python
- Pandas
- NumPy
- Excel (openpyxl)

---

## 📂 Input Data
The dataset includes:
- Participant ID
- Age (with missing values)
- Gender
- Country
- Disease
- Research Status (Active / Completed / Terminated)
- Study Group

---

## ⚙️ What This Script Does
- Removes duplicate records
- Handles missing age values using median
- Validates age range (0–120)
- Filters data by research status
- Generates demographic statistics:
  - Total participants
  - Average, median & standard deviation of age
  - Gender distribution
  - Country & disease counts

---

## 📊 Output
An Excel file with:
- Active Studies
- Completed Studies
- Terminated Studies
- Demographic Statistics

---

## ▶️ How to Run
```bash
python biomedical_analysis.py

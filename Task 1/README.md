# 🚢 Titanic Dataset - Data Cleaning & Preprocessing

This repository contains the complete process of data cleaning and preprocessing using the **Titanic dataset**. It serves as a practical learning task for interview preparation and machine learning workflows.

---

## 📌 Objectives

- Understand the ML life cycle from problem definition to deployment
- Practice data cleaning techniques
- Apply preprocessing methods like encoding, scaling, and outlier removal
- Prepare data for modeling
- Answer frequently asked ML interview questions

---

## 📂 Contents

1. `Titanic_Dataset.ipynb` – Jupyter Notebook with cleaning and preprocessing steps
2. `Titanic-Dataset.csv` – Raw dataset used for the task
3. `TASK1 (Learning & interview).pdf` – Theory, notes, and interview questions

---

## 🧠 Machine Learning Lifecycle (Covered)

1. Problem Definition
2. Data Collection
3. **Data Cleaning**
4. **Data Preprocessing**
5. Exploratory Data Analysis (EDA)
6. Model Selection
7. Model Training
8. Model Evaluation
9. Hyperparameter Tuning
10. Model Deployment
11. Monitoring & Maintenance

---

## 🧽 Data Cleaning

### ✔️ Tasks Performed:
- **Handling Missing Values**: Imputation using mean, median
- **Removing Duplicates**: Using `.drop_duplicates()`
- **Fixing Data Types**: Converted string to datetime, etc.
- **Handling Outliers**: Detected using IQR and Z-score
- **Standardizing Formats**: Gender/text columns
- **Filtering Irrelevant Data**

### 🔍 Tools:
- `pandas`, `numpy`, `matplotlib`, `seaborn`

---

## ⚙️ Data Preprocessing

### ✔️ Techniques Used:
- **Normalization / Standardization**: `MinMaxScaler`, `StandardScaler`
- **Encoding Categorical Variables**: Label and One-Hot Encoding
- **Feature Engineering**: Extracted new variables like Join_Year
- **Feature Selection**: Used correlation and importance-based techniques
- **Data Splitting**: Train/Validation/Test split

---

## 💡 Interview Questions Answered

1. Types of Missing Data (MCAR, MAR, MNAR)
2. Handling Categorical Variables (Label vs One-Hot Encoding)
3. Normalization vs Standardization
4. Outlier Detection (Z-score, IQR, Boxplots)
5. Importance of Preprocessing
6. One-Hot Encoding vs Label Encoding
7. Handling Data Imbalance (SMOTE, class weights, etc.)
8. Can Preprocessing Affect Model Accuracy?

> All examples are based on the Titanic dataset for clarity.

---

## ✅ Key Takeaways

- Data cleaning improves data quality by fixing errors and inconsistencies.
- Preprocessing ensures the dataset is ready for machine learning models.
- Each preprocessing decision (like scaling or encoding) directly affects model performance.
- Outliers, missing values, and categorical variables require special attention.

---

## 📎 Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn

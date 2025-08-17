# 🏬 Task 8: Clustering with K-Means

## 📌 Objective

This project demonstrates **Unsupervised Learning** using **K-Means Clustering**. The dataset used is *Mall Customers Dataset*, where customers are grouped based on their annual income and spending score.

The main goals are:

1. Load and visualize the dataset (with optional PCA for 2D view).
2. Fit K-Means and assign cluster labels.
3. Use the **Elbow Method** to determine the optimal number of clusters.
4. Visualize clusters with color coding.
5. Evaluate clustering performance using **Silhouette Score**.

---

## 📂 Project Structure

```
Task 8/
│── dataset/
│   └── Mall_Customers.csv          # Dataset used for clustering
│
│── interview preparation/
│   └── INTERVIEW QUESTIONS.pdf     # Theory Q&A for clustering concepts
│
│── notebook/
│   └── Mall_customers8.ipynb       # Jupyter notebook with implementation
│
│── README.md                       # Project documentation
```

---

## 🛠️ Tools & Libraries

* **Python 3**
* **Pandas** (Data handling)
* **Matplotlib / Seaborn** (Visualization)
* **Scikit-learn** (K-Means, PCA, Silhouette Score)

---

## 🚀 Steps Implemented

1. **Data Loading** – Load the *Mall\_Customers.csv* file.
2. **Data Exploration** – Check features like *Age, Gender, Annual Income, Spending Score*.
3. **K-Means Clustering** – Apply clustering to group customers.
4. **Elbow Method** – Find the optimal number of clusters (K).
5. **Visualization** – Use scatter plots with cluster coloring (and PCA for 2D).
6. **Evaluation** – Compute **Silhouette Score** to assess clustering quality.

---

## 📊 Results & Insights

* Customers can be segmented into distinct groups based on spending habits and income.
* The Elbow Method & Silhouette Score were used to justify the chosen number of clusters.
* Visualizations help understand customer segments for targeted marketing strategies.

---

## 🎯 Interview Preparation

The `interview preparation` folder contains **important clustering questions and answers**, including:

* How K-Means works
* Elbow Method
* Silhouette Score
* Inertia
* Limitations of K-Means
* Difference between **Clustering vs Classification**

---

## 📌 How to Run

1. Clone this repository

   ```bash
   git clone <repo_link>
   cd Task 8
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook

   ```bash
   jupyter notebook notebook/Mall_customers8.ipynb
   ```

---

## 📜 License

This project is for **educational purposes** only.

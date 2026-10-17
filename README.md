# 📊 Sales Data Analysis & Visualization

A Python-based **Sales Data Analysis and Visualization** project that demonstrates how to retrieve data from REST APIs, clean and transform datasets, combine multiple CSV files, perform Exploratory Data Analysis (EDA), and generate meaningful business visualizations.

---

## 🎯 Project Overview

The goal of this project is to analyze sales-related data collected from multiple REST APIs and transform raw data into meaningful insights.

The project covers the complete data analysis workflow:

**API Data Collection → Data Cleaning → Duplicate Removal → CSV Export → Data Merging → EDA → Data Visualization → Insights**

The project works with four main datasets:

- 👥 Customers
- 🛒 Orders
- 📦 Products
- 📅 Order Dates

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Data processing and analysis |
| 🔗 Requests | Retrieve data from REST APIs |
| 🐼 Pandas | Data cleaning, transformation, merging, and analysis |
| 📊 Matplotlib | Data visualization |
| 📈 Seaborn | Statistical visualization |
| 📄 CSV | Data storage and exchange |
| 📓 Jupyter Notebook / PyCharm | Development environment |

---

## 🔄 Project Workflow

### 1. Data Collection from REST APIs

Retrieved sales-related data from **4 REST API endpoints** using Python's `Requests` library.

The APIs provided information related to:

- Customers
- Orders
- Products
- Order Dates

```python
import requests

response = requests.get(api_url)
data = response.json()
```

---

### 2. Data Cleaning

The collected API data was processed using **Pandas** to prepare it for analysis.

The cleaning process included:

- Handling missing values
- Removing duplicate records
- Checking data types
- Standardizing column names
- Validating data consistency
- Preparing datasets for merging

---

### 3. CSV Export

After cleaning each API dataset, the processed data was exported into separate CSV files.

Example:

```text
customers.csv
orders.csv
products.csv
order_dates.csv
```

This made the cleaned datasets easier to store, reuse, and analyze.

---

### 4. Data Merging

The individual CSV files were loaded into Pandas and combined using appropriate keys.

The goal was to create a **consolidated sales dataset** containing customer, order, product, and date information.

Example:

```python
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
order_dates = pd.read_csv("order_dates.csv")

sales_data = orders.merge(customers, on="customer_id", how="left")
sales_data = sales_data.merge(products, on="product_id", how="left")
```

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed on the consolidated dataset to understand sales performance and identify meaningful patterns.

The analysis included:

- Descriptive statistics
- Sales performance analysis
- Product performance analysis
- Order analysis
- Customer analysis
- Date-based sales analysis
- Identification of trends and patterns
- Comparison of different product categories

---

## 📊 Data Visualization

**Matplotlib** and **Seaborn** were used to create visualizations that communicate important findings from the data.

Visualizations include:

- 📈 Sales trends over time
- 📊 Product-wise sales performance
- 🏆 Top-performing products
- 📦 Product/category analysis
- 👥 Customer-related sales analysis
- 📅 Order/date-based analysis

Example:

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(data=sales_data, x="product", y="sales")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
```

---

## 💡 Key Insights

The analysis was used to identify:

- Products contributing the highest sales
- Products with lower sales performance
- Sales trends across different dates
- Customer purchasing patterns
- Differences in product performance
- Overall sales distribution and trends

These insights demonstrate how raw sales data can be transformed into **data-driven business conclusions**.

---

## 📁 Project Structure

```text
Sales-Data-Analysis-Visualization/
│
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   └── order_dates.csv
│
├── src/
│   ├── api_data.py
│   ├── data_cleaning.py
│   ├── data_merge.py
│   └── visualization.py
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── requirements.txt
│
└── README.md
```

> The folder structure can be adjusted based on the actual organization of your project.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Sales-Data-Analysis-Visualization.git
```

### 2. Navigate to the Project Folder

```bash
cd Sales-Data-Analysis-Visualization
```

### 3. Install Required Libraries

```bash
pip install pandas requests matplotlib seaborn
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Project

Run the Python scripts or Jupyter Notebook to perform the complete analysis workflow.

---

## 📦 Requirements

The main Python libraries used in this project are:

```text
pandas
requests
matplotlib
seaborn
```

---

## 🚀 Skills Demonstrated

This project demonstrates practical experience in:

- Python Programming
- REST API Data Extraction
- API Data Processing
- Data Cleaning
- Duplicate Handling
- CSV Data Handling
- Data Integration
- Data Merging
- Exploratory Data Analysis
- Statistical Analysis
- Data Visualization
- Business Insight Generation

---

## 📌 Project Highlights

**Data Source:** REST APIs  
**Data Format:** JSON → CSV  
**Programming Language:** Python  
**Analysis:** Exploratory Data Analysis (EDA)  
**Visualization:** Matplotlib & Seaborn  
**Data Processing:** Pandas  
**API Handling:** Requests  

---

## 👨‍💻 Author

**Naveen**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Tableau

---

⭐ If you find this project useful, feel free to give the repository a star!

# Azure Retail Data Pipeline

An end-to-end retail analytics project built using Python, Azure SQL Database, SQL, and Power BI. This project demonstrates the complete data pipeline process from raw CSV files to an interactive business intelligence dashboard.

---

## Project Overview

This project simulates a retail company's analytics workflow by:

- Importing raw CSV datasets
- Cleaning and transforming data with Python (pandas)
- Loading data into Azure SQL Database
- Creating SQL views for reporting
- Building an interactive Power BI dashboard

The final dashboard provides insights into sales performance, customer behavior, and product performance.

---

## Technologies Used

- Python
- pandas
- SQLAlchemy
- Azure SQL Database
- SQL
- Power BI
- Git
- GitHub

---

## Project Architecture

```
CSV Files
     │
     ▼
Python ETL (pandas + SQLAlchemy)
     │
     ▼
Azure SQL Database
     │
     ▼
SQL Views
     │
     ▼
Power BI Dashboard
```

---

## Repository Structure

```
azure-retail-data-pipeline
│
├── data/
│   └── raw/
├── powerbi/
│   ├── Retail Sales Dashboard.pbix
│   └── screenshots/
├── python/
│   ├── load/
│   └── profile_data.py
├── sql/
│   └── views/
├── README.md
├── requirements.txt
└── .env.example
```

---

## ETL Process

The ETL pipeline performs the following steps:

1. Reads retail CSV datasets using pandas.
2. Cleans and validates the data.
3. Renames columns to match the SQL schema.
4. Connects securely to Azure SQL Database using environment variables.
5. Loads each dataset into normalized SQL tables.
6. Uses SQL views to prepare reporting datasets for Power BI.

---

## SQL Views

The project includes custom reporting views:

- **vw_SalesSummary**
- **vw_CustomerLifetimeValue**
- **vw_ProductPerformance**

These views simplify reporting and improve dashboard performance.

---

# Power BI Dashboard

## Executive Overview

![Executive Overview](powerbi/screenshots/executive-overview.png)

Displays:

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Monthly Revenue Trend
- Revenue by Category
- Revenue by City
- Top Products

---

## Customer Insights

![Customer Insights](powerbi/screenshots/customer-insights.png)

Displays:

- Average Order Value
- Orders per Customer
- Customer Lifetime Revenue
- Top Customers

---

## Product Performance

![Product Performance](powerbi/screenshots/product-performance.png)

Displays:

- Average Product Revenue
- Top Product Revenue
- Products Sold
- Revenue by Product
- Revenue by Category

---

## Running the Project

1. Clone the repository

```bash
git clone https://github.com/cad171uakron/azure-retail-data-pipeline.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file using `.env.example`

4. Update the Azure SQL credentials.

5. Run the ETL script.

---

## Future Improvements

- Azure Data Factory pipeline
- Azure Blob Storage integration
- Automated scheduled ETL
- Data quality validation
- Incremental data loading

---

## Author

**Carter Dockery**

Bachelor of Science – Computer Information Systems

University of Akron

GitHub:
https://github.com/cad171uakron

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Azure SQL](https://img.shields.io/badge/Azure-SQL-0078D4)
![Power BI](https://img.shields.io/badge/Power-BI-F2C811)
![License](https://img.shields.io/badge/License-MIT-green)
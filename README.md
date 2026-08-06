# Chocolate-Sales-Analytics-Python-Power-BI
End-to-end sales analytics project using Python (Pandas) for data cleaning and Power BI for interactive dashboard reporting.
Data source: Kaggle 
License: CC BY-SA 4.0
Website link: https://www.kaggle.com/datasets/saidaminsaidaxmadov/chocolate-sales/data
Icons8: https://icons8.com/icons/set/person

## Tool Used
- Python
- Pandas
- Power BI
- DAX

## Workflow
1. Data Cleaning (Python)
The raw CSV dataset was cleaned using Pandas, including:
- Renaming columns
- Removing leading/trailing spaces
- Standardising country names
- Converting dates
- Validating numeric fields
- Checking missing values
- Removing duplicate records
- Exporting a cleaned dataset

2. Data Modelling (Power BI)
Created measures including:
- Total Sales
- Total Boxes
- Average Unit Price
- Top Country
- Best Product
- Best Salesperson
- Year-over-Year Growth
- Product Ranking

3. Dashboard Design
The dashboard contains a summary page.

Interactive slicers allow filtering by:
- Year
- Country
- Product
- Salesperson

Key Insights:
- Australia generated the highest revenue.
- Smooth Silky Salty was the top-selling product.
- Ches Bonnell achieved the highest sales.
- Total sales increased compared with the previous year.

4. Skills Demonstrated
- Data Cleaning
- Exploratory Data Analysis
- Data Modelling
- DAX
- Power BI Dashboard Design
- KPI Development
- Business Intelligence Reporting

5. Repository Structure:
data/
python/
images/
Chocolate Sales Dashboard.pbix
README.md

6. Business Questions Answered:
This dashboard was designed to answer the following questions:
- Which country generated the highest revenue?
- Which products contributed the most sales?
- Who were the top-performing salespeople?
- How many boxes were shipped?
- How has sales performance changed compared with the previous year?

7. Future Improvements:
- Add drill-through pages
- Include profit and margin analysis
- Connect to a SQL database instead of CSV
- Implement automated refresh using Python

## Disclaimer
This is an independent portfolio project created using publicly available data.
It is not associated with or based on any work, data, systems or intellectual property from my employer.
This repo contains all Python code and CSV files for the ETL project 
3 data sources: 
  Kaggle API: I retrieved a database from Kaggle using the Kaggle API in Python to download the files (apicall.py)
  Local CSV: I used the downloaded CSVs to import most of the data in Python as pandas dataframes then into the SQLite3 database (pastryinvtable.py, 
    producttable2.py, productscleaning.py, receiptstable.py) 
    all CSVs are available in the Git repo in the datasets folder and from the Kaggle source dataset 
    https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113?rvi=1
  MySQL database: I used the Employees MySQL database (with some changes made) to connect with employees (joinedstaff.sql, employeesandlocations.py)
    also available from https://dev.mysql.com/doc/employee/en/employees-installation.html 

SQL Queries can be found in sqlqueries.py 

cafe_data.db is a SQLite3 database containing the tables employees, locations, pastry_inventory, products, and receipts, all connected by various IDs 

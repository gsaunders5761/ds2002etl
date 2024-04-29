# import receipts table (transaction records) from csv file
import pandas as pd
import sqlite3

# connect to SQLite database
conn = sqlite3.connect('cafe_data.db')

# create a cursor object
cursor = conn.cursor()
cursor.execute('''PRAGMA foreign_keys = ON''')

# create table
cursor.execute('''CREATE TABLE IF NOT EXISTS receipts (
                transaction_id INTEGER PRIMARY KEY,
                transaction_date DATE,
                sales_outlet_id	INTEGER,
                staff_id INTEGER, 
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER, 
                unit_price FLOAT,
                FOREIGN KEY (product_id) REFERENCES products(product_id),
                FOREIGN KEY (staff_id) REFERENCES Employees(staff_id)
                )''')

# select only desired columns from original table
selected_cols = ['transaction_id', 'transaction_date', 'sales_outlet_id', 'staff_id', 'customer_id', 'product_id', 'quantity', 'unit_price']

# process and insert data into the table while reading from the CSV file
filepath = '/Users/gracesaunders/PycharmProjects/ds2002etl/datasets/201904 sales reciepts.csv'
try:
    data = pd.read_csv(filepath, usecols = selected_cols)
    for index, row in data.iterrows():
        cursor.execute('''INSERT INTO receipts (transaction_id, transaction_date, 
        sales_outlet_id, staff_id, customer_id, product_id, quantity, unit_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        ('transaction_id', 'transaction_date', 'sales_outlet_id', 'staff_id',
         'customer_id', 'product_id', 'quantity', 'unit_price'))
except Exception as e:
    print(f"Error processing {filepath}: {e}")
# commit changes and close connection
conn.commit()
conn.close()

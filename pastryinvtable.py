# import pastry inventory table  from a csv file
import csv
import sqlite3

file_path = '/Users/gracesaunders/Desktop/kagglecafe/pastry inventory.csv'

#connect to sqlite db
conn = sqlite3.connect('cafe_data.db')

# create a cursor object
cursor = conn.cursor()

# define the table schema
cursor.execute('''CREATE TABLE IF NOT EXISTS pastry_inventory (
                        sales_outlet_id	INTEGER,
                        transaction_date DATE,
                        product_id INTEGER,
                        start_of_day INTEGER, 
                        quantity_sold INTEGER,
                        waste INTEGER, 
                        percent_waste INTEGER,
                        FOREIGN KEY (product_id) REFERENCES products(product_id)
                        )''')

# open the CSV file and iterate through its rows
with open(file_path, 'r') as pastry_inv:
        csv_reader = csv.reader(pastry_inv)
        # skip the header row
        next(csv_reader, None)
        # iterate through each row in the csv file
        for row in csv_reader:
                sales_outlet_id = row[0]
                transaction_date = row[1]
                product_id = row[2]
                start_of_day = row[3]
                quantity_sold = row[4]
                waste = row[5]
                percent_waste = row[6]

                # insert each row into the pastry_inventory table
                try:
                    cursor.execute('''INSERT INTO pastry_inventory (sales_outlet_id, transaction_date, product_id, start_of_day, quantity_sold, waste, percent_waste)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''', (sales_outlet_id, transaction_date, product_id, start_of_day, quantity_sold, waste, percent_waste))
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

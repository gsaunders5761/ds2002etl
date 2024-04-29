import pandas as pd
import sqlite3

# define the file path + columns for extraction
filepath = '/Users/gracesaunders/PycharmProjects/ds2002etl/datasets/product.csv'
selected_cols = ['product_id', 'product_group', 'product_category', 'product_type',
                 'product', 'product_description', 'unit_of_measure',
                 'current_wholesale_price', 'current_retail_price']

# connect to SQLite database
with sqlite3.connect('cafe_data.db') as conn:
    cursor = conn.cursor()

    # create table schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_group TEXT,
        product_category TEXT,
        product_type TEXT, 
        product TEXT,
        product_description TEXT, 
        unit_of_measure TEXT, 
        current_wholesale_price REAL,
        current_retail_price REAL
    )''')

    # read data from CSV using selected columns
    try:
        data = pd.read_csv(filepath, usecols=selected_cols)
        # Using pandas to_sql function
        data.to_sql('products', conn, if_exists='append', index=False)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")


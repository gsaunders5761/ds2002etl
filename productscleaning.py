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
    try:
        clean = pd.read_csv(filepath, usecols=selected_cols)
        clean['clean_retail_price'] = clean['current_retail_price'].replace('^\$', '', regex=True).astype(float)

        # Using pandas to_sql function to replace
        clean.to_sql('products', conn, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

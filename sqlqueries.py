import sqlite3
import pandas as pd

# connect to SQLite database
with sqlite3.connect('cafe_data.db') as conn:

    # create a cursor object
    cursor = conn.cursor()

    # query 1: average prices by product groups
    cursor.execute('''SELECT 
        product_group,
        AVG(clean_retail_price) AS average_retail_price
    FROM 
        products
    GROUP BY 
        product_group;''')



    # Print the results
    print("Average prices by product group: ")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # query 2: sort product quantities sold with product names
    cursor.execute('''SELECT 
    p.product_id,
    p.product,
    SUM(r.quantity) AS total_sold
FROM 
    receipts AS r
JOIN 
    products AS p ON r.product_id = p.product_id
GROUP BY 
    p.product_id, p.product
ORDER BY 
    total_sold DESC;
''')
    print("\nTotal sold for each product: ")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # count gender of employees
    cursor.execute('''SELECT gender , COUNT(gender) AS counts
    FROM employees
    GROUP BY gender''')

    print("\nGender ratio of employees: ")
    results = cursor.fetchall()
    for row in results:
        print(row)
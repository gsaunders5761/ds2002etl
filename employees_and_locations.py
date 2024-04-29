# convert SQL database to sqlite database
# the database I used is the MySQL Employees database https://dev.mysql.com/doc/employee/en/employees-introduction.html
import warnings
import pandas as pd
from sqlalchemy import text, create_engine
import sqlite3
warnings.filterwarnings('ignore')

# variables for SQL connection
host_name = "datatbase.ds2002.org"
port = "3306"
user_id = "wez6fg"
pwd = "wez6fg!"
db_name = "wez6fg"

# connnect to SQL database and convert to a pandas dataframe
def get_sqlalchemy_dataframe(user_id, pwd, host_name, db_name, sql_query):
    conn_str = f"mysql+pymysql://{user_id}:{pwd}@{host_name}/{db_name}"
    sqlEngine = create_engine(conn_str, pool_recycle=3600)
    connection = sqlEngine.connect()
    dframe = pd.read_sql(sql_query, connection)
    connection.close()
    return dframe

# sql query to retrieve employees table
sql_query = "SELECT staff_id, first_name, last_name, gender FROM employees"
employees = get_sqlalchemy_dataframe(user_id, pwd, host_name, db_name, text(sql_query))

# connect to sqlite database and insert employees table
conn = sqlite3.connect('/Users/gracesaunders/PycharmProjects/ds2002etl/cafe_data.db')
employees.to_sql('Employees', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
print(employees.head())

# SQL query to retrieve departments table
# note: I altered the data in the departments table to represent coffee chain locations rather than departments
sql_query_2 = "SELECT * FROM departments"
locations = get_sqlalchemy_dataframe(user_id, pwd, host_name, db_name, text(sql_query_2))

# connect to sqlite database and insert locations table
conn = sqlite3.connect('/Users/gracesaunders/PycharmProjects/ds2002etl/cafe_data.db')
locations.to_sql('locations', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
print(locations.head())
from mysql.connector import connection
import csv
import pandas as pd

# connect to DB server
cnx = connection.MySQLConnection(user='readonlyuser', password='Msis5193Fall2023',
                                 host='34.70.89.75',
                                 database='Northwind')

# initialize the cursor
cursor = cnx.cursor()

# select the data from a table to be exported
cursor.execute("select * from Category")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file Category.csv
with open('Category.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
        
# close DB connection
cnx.close()

#Task 2
#Use the exported CSV files to find the number of products in each category, and save the result into a new CSV file

product = pd.read_csv('Product.csv')
category = pd.read_csv('Category.csv')
df = pd.concat([product, category])
print(df.columns)
product_category = df.groupby(["categoryId"]).agg(products=("productId", "nunique"))
print(product_category)
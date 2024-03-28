"""
Description: Constants for sales analysis ETL.

@author : Satyajit Mohapatra
@date : 23-03-2024
"""

sales_query = 'select customer_id, sales_id from sales'
orders_query = 'select item_id, IFNULL(quantity,0) as quantity,sales_id from orders'     
customers_query = 'select customer_id , age from customers'
items_query = 'select item_id,item_name from items'

csv_path = 'C:/Users/Dell/sales_analysis_18_35.csv'
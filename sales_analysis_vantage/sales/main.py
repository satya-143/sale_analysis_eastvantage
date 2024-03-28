import os
from utils.utility import database_connection, read_data_from_db, write_as_csv
from utils.constant import sales_query, orders_query, customers_query, items_query, csv_path

if __name__ == '__main__':
    try:
        # reading credential from .env
        database_file = os.getenv("DATABASE_ENV").strip()
        # creating database connection
        conn = database_connection(database_file)
        cursor = conn.cursor()
        # reading sales data from db
        sales_df = read_data_from_db(conn, sales_query)
        # reading customer data from db
        customer_df = read_data_from_db(conn, customers_query)
        # reading orders data from db
        orders_df = read_data_from_db(conn, orders_query)
        # reading items data from db
        items_df = read_data_from_db(conn, items_query)

        # total quantities of each item bought per customer aged 18-35.
        customer_sales_df = sales_df.merge(customer_df, on='customer_id', how='left')

        order_items_df = orders_df.merge(items_df, on='item_id', how='left')
        order_items_df1 = order_items_df[['quantity', 'sales_id', 'item_name']]

        final_raw_output = order_items_df1.merge(customer_sales_df, on='sales_id', how='left')
        final_raw_output1 = final_raw_output[['quantity', 'item_name', 'customer_id', 'age']]

        final_result = final_raw_output1.groupby(['item_name', 'customer_id', 'age'])['quantity'].aggregate(
            'sum').reset_index()
        final_result = final_result.query('age >= 18 and age <= 35')
        final_result = final_result.query('quantity != 0')

        flag = write_as_csv(csv_path, ';', final_result)
        if flag:
            print("Output CSV file generated")
        else:
            print("Output CSV file not generated")
        conn.close()

    except Exception as error:
        print("Error Something went wrong - {}".format(error))

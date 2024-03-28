"""
Description: Utility for sales analysis ETL.

@author : Satyajit Mohapatra
@date : 23-03-2024
"""
import pandas as pd
import sqlite3


def database_connection(database_file: str) -> sqlite3.Connection:
    # Desc : Function for Database connection   
    # param database_file : sqlite3 datbase file
    # return: sqlite database connection
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except sqlite3.DatabaseError as err:
        print("While connecting to database someting went wrong {}".format(err))


def read_data_from_db(connection: sqlite3.Connection, query: str) -> pd.DataFrame:
    # Desc : Function for read data from database    
    # param connection : database connection
    # param query : query to fetch data
    # return: Pandas Dataframe
    try:
        df = pd.read_sql_query(query, connection)
        return df

    except Exception as err:
        print("Error while fetching data from query {}".format(err))


def write_as_csv(csv_path: str, delimiter: str, df) -> bool:
    # Desc : Function for write dataframe as csv    
    # param csv_path : database connection
    # param delimiter : csv file separator (, : ; ' "  etc.)
    # param df : dataframe to write as csv
    # return: Boolean
    try:
        df.to_csv(csv_path, sep=delimiter, header=True, index=False, index_label=None)
        return True
    except Exception as err:
        print("Error while write as csv".format(err))
        return False

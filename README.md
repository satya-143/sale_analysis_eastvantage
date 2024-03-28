# sale_analysis_eastvantage
### 
*<b> PREREQUISITE :<b>


Python project task ( folder: sales_analysis_vantage  )
-------------------------------------------------------
1) create the python virtual environment and activate it

         command :  python -m venv sales_env

              windows system : .\sales_env\Scripts\activate

              linux system: source /sales_env/bin/activate

2) install dependencies

         command : pip install -r requirements.txt

3) install any database management tool 

    (like DEeaver : https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe)

   then create a connection using shared .db file

4) mention the same .db file location in .env file which is resides inside sales_analysis_vantage folder and csv file path in utils/constant.py .

5) go to your terminal where you have activated the virtual environment and run below command.

        command :   python main.py

# SQL project task ( folder: sales_analysis_vantage_sql )
###

1) Open the folder sales_analysis_vantage_sql there will .sql file which contain the sql code to get the same result which is returned by python code.

2) copy the code into dbeaver sql workbench and run it and export the result as csv with delimeter ';'

Note: In both the folders output .csv files are attached.
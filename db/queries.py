
from db import sqlliteconnect as mydb
import pandas as pd
from db import mysqlconnector as odbc
from helpers import file_reader_writer as fr

#First team based results to show on screen
def filter_test_run_name(env):
    myfile = fr.readerWriter('variables.txt')
    connection_string = myfile.get_connection_string()
    dbconn = odbc.mysqlconnector(connection_string)
    conn = dbconn.sql_open_connection(connection_string)
    table = f'{env}_reports'
    query = f'select DISTINCT test_run_name FROM [QATestPerformance].[ADMINISTAFF\\fjdiaz].[{table}]'
    df = pd.read_sql_query(query, conn)
    dbconn.sql_close_connection(conn)
    return df

def filter_scenarios(env, test_run_name):
    myfile = fr.readerWriter('variables.txt')
    connection_string = myfile.get_connection_string()
    dbconn = odbc.mysqlconnector(connection_string)
    conn = dbconn.sql_open_connection(connection_string)
    table = f'{env}_reports'
    query = f'select DISTINCT scenario FROM [QATestPerformance].[ADMINISTAFF\\fjdiaz].[{table}] where test_run_name like \'{test_run_name}\''
    df = pd.read_sql_query(query, conn)
    dbconn.sql_close_connection(conn)
    return df

def filter_scenario_data(env, test_run_name, scenario):
    myfile = fr.readerWriter('variables.txt')
    connection_string = myfile.get_connection_string()
    dbconn = odbc.mysqlconnector(connection_string)
    conn = dbconn.sql_open_connection(connection_string)
    table = f'{env}_reports'
    query = f'select * FROM [QATestPerformance].[ADMINISTAFF\\fjdiaz].[{table}] where test_run_name like \'{test_run_name}\' and scenario like \'{scenario}\''
    df = pd.read_sql_query(query, conn)
    dbconn.sql_close_connection(conn)
    return df



from db import sqlliteconnect as mydb
import pandas as pd
from db import mysqlconnector as odbc
from helpers import file_reader_writer as fr

#First team based results to show on screen
def basequery(team):
    myfile = fr.readerWriter('variables.txt')
    connection_string = myfile.get_connection_string()
    dbconn = odbc.mysqlconnector(connection_string)
    conn = dbconn.sql_open_connection(connection_string)
    query = 'select test_run_name, count,min, average, max, percentile_95, std_deviation FROM [QATestPerformance].[ADMINISTAFF\\fjdiaz].[reports] order by end_time'
    df = pd.read_sql_query(query, conn)
    dbconn.sql_close_connection(conn)
    return df
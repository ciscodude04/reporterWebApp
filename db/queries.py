
from db import sqlliteconnect as mydb
import pandas as pd

#First team based results to show on screen
def basequery(team):
    dbconn = mydb.SQLiteConnect()
    connection = dbconn.sqlite_open_connection(mydb.SQLiteConnect.stagedb)
    df = pd.read_sql_query(f'''
                           select DISTINCT test_run_name, count,min, average,max, count, percentile_95, std_deviation FROM {team} order by end_time desc LIMIT 10;''', connection)
    connection.close()
    return df

def base_reports(team):
    dbconn = mydb.SQLiteConnect()
    connection = dbconn.sqlite_open_connection(mydb.SQLiteConnect.stagedb)
    df = pd.read_sql_query(f'''
    select DISTINCT
    ''')

#Second query to run for team screen

#basequery('testing')
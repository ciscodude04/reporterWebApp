from db import sqlliteconnect as db
import pandas as pd

#First team based results to show on screen
def basequery(team):
    dbconn = db.SQLConnect()
    connection = dbconn.sqlite_open_connection(db.SQLConnect.stagedb)
    df = pd.read_sql_query(f'''
                           SELECT DISTINCT test_run_name FROM {team} order by end_time desc;''', connection)
    connection.close()
    return df

#Second query to run for team screen

import sqlite3 as sqlite
from sqlite3 import Error

class SQLiteConnect:

    stagedb = 'mydbtesting.db'

    def __init__(self):
        pass

    def sqlite_stage_dbconnection(self):
        return self.stagedb
    
    def sqlite_open_connection(self, db):
        try:
            con = sqlite.connect(db)
            print('Connection established with ' + db)
            return con
        except Error:
            print (Error)

    def sqlite_cursor(self, con):
        cur = con.cursor()
        print ("Connected and ready to run query")
        return cur
    
    def sqlite_executemany(self, con, query, list):
        '''Execute a lot of sql statements'''
        cur = con.cursor()
        cur.executemany(query,list)
        print('Executing sql statement ' + query)
        con.commit()
        print('Execution commited.')
    
    def sqlite_queryall(self, con, q):
        cur = con.cursor()
        print('Executing sql statement: ' + q)
        for row in cur.execute(q):
            print(row)
        con.close()
        print('Connection closed')

    def sqlite_sql_execute(self, con, q):
        cur = con.cursor()
        cur.execute(q)
        print('Executing sql statement ' + q)
        con.commit()
        print('Execution commited.')

    def sqlite_connection_close(self, con):
        con.close()
        print('Connection closed')


def create_new_team_table(table_name):
    q = f'''
    CREATE TABLE IF NOT EXISTS {table_name}(
    project TEXT,
    test_run_name TEXT,
    scenario TEXT,
    step TEXT,
    count TEXT,
    min TEXT,
    average TEXT,
    max TEXT,
    percentile_90 TEXT,
    percentile_95 TEXT,
    percentile_99 TEXT,
    std_deviation TEXT,
    status TEXT,
    term_reason TEXT,
    duration TEXT,
    start_time TEXT,
    end_time TEXT,
    created_at DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP
    );'''

    return q

def create_premier_accounts_table():
    q = '''
    CREATE TABLE IF NOT EXISTS premier_accounts(
    id INT IDENTITY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    per_id INT,
    cpny_id INT,
    mdm_person_id INT,
    mdm_orgid INT,
    created at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'''

def drop_table(table_name):
    q = '''DROP TABLE {table_name};'''
    return q

def insert_data_to_team_table(table):
    q = '''INSERT INTO '''+ table + ''' VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)'''
    return q

def create_team_table(table):
#Example on how to add a new table. DO NOT RUN EVERYTIME
    mycon = SQLiteConnect()
    thecon = mycon.sqlite_open_connection(mycon.stagedb)
    mytable = create_new_team_table(table)
    mycon.sqlite_sql_execute(thecon, mytable)
    mycon.sqlite_connection_close(thecon)

#mydb = SQLiteConnect()
#thecon = mydb.sqlite_open_connection('stagedb.db')

#thecon.sqlite_connection_close(thecon)
import pypyodbc as odbc
import pandas as pd

class mysqlconnector():

    def __init__(self, _connection_string):
        self.connection_string = _connection_string

    def sql_open_connection(self, connection_string):
        try:
            conn = odbc.connect(connection_string)
            print('Connection established...')
            return conn
        except Exception as e:
            print(e)
            sql_close_connection(conn)

    def sql_execute_statement(self, conn, query):
        try:
            conn.cursor().execute(query)
            conn.commit()
            print('Executing statement: ', query)
        except Exception as e:
            print(e)
            sql_close_connection(conn)

    def sql_execute_many_statements(self, conn, query, list):
        try:
            conn.cursor().executemany(query, list)
            conn.commit()
            print('Executing query: ', query)
        except Exception as e:
            print(e)
            sql_close_connection(conn)

    def sql_close_connection(self, conn):
        try:
            conn.close()
            print('Connection successfully closed...')
        except Exception as e:
            print(e)

    def sql_statement_insert_data(self, table_name):
        # table = f'{env}_{table_name}'
        q = f'''INSERT INTO [QATestPerformance].[ADMINISTAFF\\fjdiaz].[{table_name}] VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)'''
        return q


    def sql_statement_create_new_team_table(self, team_name):
        q=f'''
        USE QATestPerformance

CREATE TABLE testing_reports(
    project VARCHAR(255),
    test_run_name VARCHAR(255),
    scenario VARCHAR(255),
    step VARCHAR(255),
    count NVARCHAR(255),
    error_count NVARCHAR(255),
    min DECIMAL(8,3),
    average DECIMAL(8,3),
    max DECIMAL(8,3),
    percentile_50 DECIMAL(8,3),
	percentile_90 DECIMAL(8,3),
    percentile_95 DECIMAL(8,3),
    percentile_99 DECIMAL(8,3),
    std_deviation VARCHAR(255),
    status VARCHAR(255),
    term_reason VARCHAR(255),
    duration VARCHAR(255),
    start_time VARCHAR(255),
    end_time VARCHAR(255),
    created_at DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP)
        '''
        return q

    def sql_statement_drop_table(self, team_name):
        q = '''DROP TABLE {team_name}'''
        return q

def create_a_table(team_name, connection_string):
    mysql = mysqlconnector(connection_string)
    conn = mysql.sql_open_connection(connection_string)
    query = mysql.sql_statement_create_new_team_table(team_name)
    mysql.sql_execute_statement(conn, query)
    mysql.sql_close_connection(conn)
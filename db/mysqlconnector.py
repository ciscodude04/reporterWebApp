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

    def sql_statement_insert_data(self, team_name):
        q = f'''INSERT INTO {team_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,CURRENT_TIMESTAMP)'''
        return q


    def sql_statement_create_new_team_table(self, team_name):
        q=f'''
        use QATestPerformance

CREATE TABLE {team_name}(
    project VARCHAR,
    test_run_name VARCHAR,
    scenario VARCHAR,
    step VARCHAR,
    count VARCHAR,
    error_count VARCHAR,
    min VARCHAR,
    average VARCHAR,
    max VARCHAR,
    percentile_50 VARCHAR,
    percentile_95 VARCHAR,
    percentile_99 VARCHAR,
    std_deviation VARCHAR,
    status VARCHAR,
    term_reason VARCHAR,
    duration VARCHAR,
    start_time VARCHAR,
    end_time VARCHAR,
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
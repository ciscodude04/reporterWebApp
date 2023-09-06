import xml.etree.ElementTree as ET
#from db import sqlliteconnect as db
from db import mysqlconnector as sql
from helpers import file_reader_writer as r


class xmlReader:
    def __init__(self) -> None:
        pass
        
        
    def fetchscenarioDatafromXML(self, root):
        #Project Name
        get_project = root[0][0]
        project = str(get_project.get('name'))

        #Conditions
        params = root[0][1]
        start_time = params.get('start')
        end_time = params.get('end')
        duration = params.get('duration')
        testrun_name = params.get('name')
        status = params.get('status')
        term_reason = params.get('terminationReason')
        total_users_location = root[0][2][7]
        total_users = total_users_location.get('value')


        #data
        data = []
        for vu in root.findall('virtual-users'):
            for statlayer1 in vu.findall('statistic-item'):
                for statlayer2 in statlayer1.findall('statistic-item'):
                    for statlayer3 in statlayer2.findall('statistic-item'):
                        sl3scenario = statlayer1.get('id')
                        sl3step = statlayer3.get('name')
                        sl3avg1 = statlayer3.get('avg')
                        sl3min = statlayer3.get('min')
                        sl3max = statlayer3.get('max')
                        sl3deviation = statlayer3.get('stddev')
                        sl3errorcount = statlayer3.get('errors')
                        sl3count = statlayer3.get('hits')
                        sl350percentile = statlayer3.get('percentile1')
                        sl395percentile = statlayer3.get('percentile2')
                        sl399percentile = statlayer3.get('percentile3')
                        #print(f'{sl3scenario}, {sl3step}, {sl3count}')

                        data.append((project, testrun_name, sl3scenario, sl3step, sl3count,sl3errorcount, sl3min, sl3avg1,sl3max, sl350percentile, sl395percentile, sl399percentile, sl3deviation,status, term_reason, duration, start_time, end_time))

        return data
    
def neoload_xml_reader(table_name, xml_file_location):
    tree = ET.parse(xml_file_location)
    root = tree.getroot()
    test_data = xmlReader()
    mydata = test_data.fetchscenarioDatafromXML(root)
    database = db.SQLiteConnect()
    myconstring = db.SQLiteConnect.stagedb
    connection = database.sqlite_open_connection(myconstring)
    database.sqlite_sql_execute(connection, db.create_new_team_table(table_name))
    database.sqlite_executemany(connection,db.insert_data_to_team_table(table_name),mydata)
    database.sqlite_connection_close(connection)

def neoload_sql_xml_reader(team_name, xml_file_location):
    tree = ET.parse(xml_file_location)
    root = tree.getroot()
    test_data = xmlReader()
    mydata = test_data.fetchscenarioDatafromXML(root)
    myfile = r.readerWriter('variables.txt')
    myfile.open_file()
    results = myfile.dictionary_reader()
    connection_string = results.get('connection_string')
    mysqlobj = sql.mysqlconnector(connection_string)
    conn = mysqlobj.sql_open_connection(connection_string)
    query = mysqlobj.sql_statement_insert_data(team_name)
    mysqlobj.sql_execute_many_statements(conn, query, mydata)
    mysqlobj.sql_close_connection(conn)
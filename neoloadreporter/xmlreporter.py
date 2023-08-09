import xml.etree.ElementTree as ET
from db import sqlliteconnect as db


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
                        sl3count = statlayer3.get('hits')
                        sl395percentile = statlayer3.get('percentile2')
                        print(f'{sl3scenario}, {sl3step}, {sl3count}')

                        data.append((project, testrun_name, sl3scenario, sl3step, sl3count,sl3min, sl3avg1,sl3max, sl395percentile, sl3deviation,status, term_reason, duration, start_time, end_time))

        return data
    
def neoload_xml_reader(table_name, xml_file_location):
    tree = ET.parse(xml_file_location)
    root = tree.getroot()
    test_data = xmlReader()
    mydata = test_data.fetchscenarioDatafromXML(root)
    database = db.SQLiteConnect()
    myconstring = db.SQLiteConnect.stagedb
    connection = database.sqlite_open_connection(myconstring)
    database.sqlite_executemany(connection,db.insert_data_to_team_table(table_name),mydata)
    connection.close(connection)

#reader = neoload_xml_reader('testing','C:\\Users\\Cisco\\Documents\\Python Projects\\webappdashboard\\reporterWebApp\\reportsample.xml')
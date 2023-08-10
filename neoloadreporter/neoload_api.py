import requests
import json
import time
import logging

header = {'content-type' : 'application/json'}

def generate_report(reportname, format):
    try:
        payload = {
            "d": {
                'TestResultName' : ''+ reportname + '',
                'Format' : 'XML'
            }
        }
        d = requests.post('', headers=header, data = json.dumps(payload))
        s = json.loads(d.text)
        ReportId = str(s['d']['ReportId'])
        return ReportId
    except:
        logging.info("Did not find test case")

def downloadReport(reportID):
    time.sleep(4)
    downloadReport = {
        "d" : {
            'ReportId' : '' + str(reportID) + '',
        }
    }
    reportdownload = requests.post('', headers=header)
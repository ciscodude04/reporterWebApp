from flask import Flask, render_template, request, flash, redirect, url_for
from os import environ
import os
from db import queries as q
from neoloadreporter import xmlreporter as x
import neoloadreporter as rep
from werkzeug.utils import secure_filename
from db import sqlliteconnect as team

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD EXTENSIONS'] = ['.xml']
app.config['UPLOAD PATH'] = 'reporterWebApp\\uploads'

@app.route("/")
def hello_world():
    return render_template('main.html')

# This is to show initial test run results
@app.route('/teamresults', methods =['GET', 'POST'])
def teampage():
        return render_template('teamresults.html')

@app.route('/testruns', methods = ['GET', 'POST'])
def testruns():
    if request.method == 'POST':
        _env = request.form['env']
        data = q.filter_test_run_name(_env)
        return render_template('testruns.html', testrun=data)

#Fetch Scenarios
@app.route('/getscenarios', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        _env = request.form['env']
        _testruns = request.form['test_runs']
        data = q.filter_scenarios(_env, _testruns)
        return render_template('scenariosupdate.html', scenario=data)

#Fetch the scenario data
@app.route('/scenariodata', methods =['GET', 'POST'])
def update_scenario():
    if request.method == 'POST':
        _env = request.form['env']
        _testruns = request.form['test_runs']
        _scenario = request.form['scenario']
        data = q.filter_scenario_data(_env, _testruns, _scenario)
        return render_template('scenariodatapage.html', scenedata=data)

#Sample Report
@app.route('/template1', methods=['GET'])
def sample1():
    mydata = q.filter_test_run_name()
    print(mydata)
    return render_template('mainreport1.html', thedata=mydata)

@app.route('/upload', methods=['GET','POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['upload_file']
        _env = request.form['env']
        table = f'{_env}_reports'
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_location = os.path.join(app.config['UPLOAD PATH'], filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD PATH'], filename))
            x.neoload_sql_xml_reader(table, file_location)
            return '<h1>File has been uploaded</h1>'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
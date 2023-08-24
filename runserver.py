from flask import Flask, render_template, request, flash, redirect, url_for
from os import environ
import os
from db import queries as que
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

@app.route('/teamportal/<team>', methods =['GET', 'POST'])
def teampage(team):
    data = que.basequery(team)
    return render_template('teamportal.html', team_name=team, testrun=data)

@app.route('/template1', methods=['GET'])
def sample1():
    mydata = que.basequery('fop')
    print(mydata)
    return render_template('mainreport1.html', thedata=mydata)

@app.route('/upload', methods=['GET','POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['upload_file']
        table_name = request.form['team_name']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_location = os.path.join(app.config['UPLOAD PATH'], filename)
            print(file_location)
            uploaded_file.save(os.path.join(app.config['UPLOAD PATH'], filename))
            x.neoload_xml_reader(table_name,file_location)
            return '<h1>File has been uploaded</h1>'
    else:
        return render_template('upload.html')





    # print('made it')
    # if request.method == 'POST':
    #     uploaded_file = request.files['files']
    #     if file.filename != '':
    #         uploaded_file.save(environ.PATH.join(app.config['UPLOAD PATH'], file.filename))
    #         return "<h1> Data has been uploaded</h1>"
    # else:
    #     return render_template('upload.html')

@app.route('/upload2', methods=['GET','POST'])
def uploadsecondfile():
    if request.method == 'POST':
        team_selection = request.form['team']
        environment = request.form['env']
        report_string = request.form['uploadtype']
        x.neoload_xml_reader(team_selection, report_string)
        print(f'here is the data: /n {report_string}')
        return "<h1>File has been upload</h1>"
        pass
    else:
        
        pass
    return render_template('uploadbackup.html')


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
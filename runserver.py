from flask import Flask, render_template, request, flash, redirect, url_for
from os import environ
from db import queries as que
from neoloadreporter import xmlreporter as x
import neoloadreporter as rep
from werkzeug.utils import secure_filename
from db import sqlliteconnect as team

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    #team.create_team_table('testing')
    #x.neoload_xml_reader('testing','reportsample.xml')
    return render_template('main.html')

@app.route('/teamportal/<team>', methods =['GET', 'POST'])
def teampage(team):
    data = que.basequery(team)
    return render_template('teamportal.html', team_name=team, testrun=data)

@app.route('/template1', methods=['GET'])
def sample1():
    mydata = que.basequery('testing')
    print(mydata)
    return render_template('mainreport1.html', thedata=mydata)

@app.route('/upload', methods=['GET','POST'])
def uploadfile():
     if request.method == 'POST':
        file = request.files['files']
        if file.filename == '':
            flash('No selected file')
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(environ.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
        # team_selection = request.form['team']
        # environment = request.form['env']
        # report_query_location = request.form['uploadtype']
        # x.neoload_xml_reader(team_selection,report_query_location)
        return "<h1> Data has been uploaded</h1>"
     else:
         return render_template('upload.html')

def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
from flask import Flask, render_template, request, flash, redirect, url_for
from os import environ
from db import queries as que
from neoloadreporter import xmlreporter as x
import neoloadreporter as rep
from werkzeug.utils import secure_filename
from db import sqlliteconnect as team

UPLOAD_FOLDER = 'uploads'
#ALLOWED_EXTENSIONS = {'.xml'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD EXTENSIONS'] = ['.xml']
app.config['UPLOAD PATH'] = 'uploads'

@app.route("/")
def hello_world():
    #team.create_team_table('fop')
    #x.neoload_xml_reader('fop','C:\\Users\\fjdiaz\\OneDrive - Insperity Inc\\Documents\\Python\\dashboard\\reporterWebApp\\reportsample.xml')
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
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = environ.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('upload.html'))





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
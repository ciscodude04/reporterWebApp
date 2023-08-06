from flask import Flask, render_template
from os import environ
from db import queries as que

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World</p>"

@app.route('/teamportal/<team>', methods =['GET', 'POST'])
def teampage(team):
    data = que.basequery(team)
    return render_template('teamportal.html', team_name=team, testrun=data)


@app.route('/template1', methods=['GET'])
def sample1():
    return render_template('mainreport1.html')





if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
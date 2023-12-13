from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
  return  render_template('index.html')

@app.route('/idontbelieve')
def index2():
  return  render_template('idontbelive.html')
@app.route('/ibelieve')
def index3():
  return  render_template('ibelive.html')
app.run(host='0.0.0.0', port=81)

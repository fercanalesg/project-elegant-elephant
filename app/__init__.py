import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import*

load_dotenv()
app = Flask(__name__)

mydb=MYSQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD"),
			host=os.getenv("MYSQL_HOST"),port=3306)
print(mydb)

@app.route('/')
def index():
    return render_template('index.html', title="Home", url=os.getenv("URL"))

@app.route('/professionalinfo')
def professionInfo():
    return render_template('prof.html', title="Education/Experience", url=os.getenv("URL"))

@app.route('/hobbies')
def portfolio():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

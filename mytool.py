from flask import Flask,render_template,url_for 
from config import config

mytoolApp = Flask(__name__)

@mytoolApp.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__' :
    mytoolApp.run(debug=True,port=3300)

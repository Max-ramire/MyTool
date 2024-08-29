from flask import Flask 

mytoolApp = Flask(__name__)

@mytoolApp.route('/')
def home():
    return '<h1>Hello</h1>'

if __name__ == '__main__' :
    mytoolApp.run(debug=True,port=3300)

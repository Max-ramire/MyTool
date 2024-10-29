from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
import datetime 
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

mytoolApp = Flask(__name__)
db        =MySQL(mytoolApp)
adminSession = LoginManager (mytoolApp)

@adminSession.user_loader
def agregarUsuario(ID):
    return ModelUser.get_by_id(db,id)

@mytoolApp.route('/')
def home():
    return render_template('usuarios.html')

@mytoolApp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'post':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg = datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario(nombre,correo,clave,fechareg) VALUES (%s,%s,%s,%s)",(nombre,correo,claveCifrada,fechareg)")
        db.connection.commit()
        return render_template("home.html")
    return render_template('signup.html')

@mytoolApp.route('/signin')
def signin():
    return render_template('signin.html')


if __name__ == '__main__' :
    mytoolApp.config.from_object(config['development'])
    mytoolApp.run(debug=True,port=3300)
00
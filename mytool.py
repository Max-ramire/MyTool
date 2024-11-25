from flask import Flask,render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
from datetime import datetime
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

mytoolApp = Flask(__name__)
#pythonanywhere
mytoolApp.config.from_object(config['development'])
#mytoolApp.config.from_object(config['mail'])
db        =MySQL(mytoolApp)
mail      =  Mail(mytoolApp)
adminSession = LoginManager (mytoolApp)

@adminSession.user_loader
def agregarUsuario(ID):
    return ModelUser.get_by_id(db,id)

@mytoolApp.route('/')
def home():
    return render_template('home.html')

@mytoolApp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'post':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg = datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario(nombre,correo,clave,fechareg) VALUES (%s,%s,%s,%s)",(nombre,correo,claveCifrada,fechareg))
        db.connection.commit()
        msg = Message(subject='Bienvenidos a mytools',recipients=[correo])
        msg.html = render_template('mail.html',nombre=nombre)
        mail.send(msg)
        return render_template("home.html")
    return render_template('signup.html')

@mytoolApp.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == "POST":
        usuario = User(0,None,request.form['correo'],request.form['clave'],)
        usuarioAutenticado = ModelUser.signin(db,usuario)
        if usuarioAutenticado is None:
            if usuarioAutenticado.clave:
                login_user(usuarioAutenticado)
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html') 
                else:
                    return render_template('user.html')
            else:
                    flash('Contraseña Incorrecta')
                    return redirect(request.url)
        else:
            Flask('Usuario Inexistente')
            return redirect(request.url)
        return render_template('signin.html')
@mytoolApp.route('/signout',methods = ['GET','POST'])
def signout():
    logout_user()
    return render_template('home.html')

@mytoolApp.route("/sUsuario" , methods=['GET','POST'])
def sUsuario():
    selUsuario = db.connection.cursor()
    selUsuario.excute("SELECT FROM usuario")
    u           =selUsuario.fetchall()
    selUsuario.close()
    return render_template('usuarios.html', usuarios = u)

@mytoolApp.route('/iUsuario', methods = ['GET','POST'])
def usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave = request.form['clave']
    claveCifrada = generate_password_hash(clave)
    fechareg = datetime.now()
    perfil = request.form['perfil']
    agregarUsuario = db.connection.cursor()
    agregarUsuario.excute("INSERT INTO usuario ( nombre, correo, clave, perfil, fechareg, perfil) VALUES (%s, %s , %s, %s, %s)",(nombre, correo, claveCifrada, fechareg, perfil))
    db.connection.commit()
    agregarUsuario.close()
    flash('Usuario agregado')
    return redirect(url_for('sUsuario'))

@mytoolApp.route('/uUsuario/<int:id>',methods=['GET','POST'])
def uUsuario(id):
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave = request.form['clave']
    claveCifrada = generate_password_hash(clave)
    fechareg = datetime.now()
    perfil = request.form['perfil']
    actUsuario = db.connection.cursor()
    actUsuario.excute("UPDATE usuario SET nombre = %s, correo=%s, clave=%s, fechareg=%s ,perfil = %s WHERE id =%s",(nombre,correo,claveCifrada,fechareg, perfil))
    db.connection.commit()
    actUsuario.close()
    flash('Usuario actualizado')
    return redirect(url_for('sUsuario'))

@mytoolApp.route('/dUsuario/<int:id>',methods=['GET','POST'])
def dUsuario(id):
    delUsuario = db.connection.cursor()
    delUsuario.excute("DELETE FROM usuario WHERE id = %s", (id,))
    db.connection.commit()
    delUsuario.close
    flash("Usuario eliminado")
    return redirect(url_for('sUsuario'))

if __name__ == '__main__' :
        mytoolApp.config.from_object(config['development'])
mytoolApp.run(debug=True,port=3300)

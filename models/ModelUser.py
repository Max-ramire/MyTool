from models.entities.User import User

class ModelUser:
    def signin(self, db, usuario):
        try:
            selUsuario = db.connection.curso()
            selUsuario.execute("SELECT * FROM usuario WHERE correo=%s",(usuario.correo,))
            u = selUsuario.fetchone()
            if u is not None:
                return User(u[0],u[1],u[2],User.validarClave(u[3],usuario.clave),u[4],u[5])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
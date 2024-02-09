from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):


    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    n_oficio = db.Column(db.String(100))
    fecha = db.Column(db.Date())
    recibido = db.Column(db.String(100))
    remitido = db.Column(db.String(100))
    finalidad = db.Column(db.String(100))
    asunto = db.Column(db.String(100))
    respuesta = db.Column(db.String(100))
    fecha_respuesta = db.Column(db.Date())
    observacion = db.Column(db.String(100))

    tipo_registro = db.Column(db.String(10), nullable=True)



    def __repr__(self):
        return '<Contacts %r>' % self.n_oficio

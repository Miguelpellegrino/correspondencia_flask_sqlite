from flask_wtf import FlaskForm
from wtforms import StringField,DateField, SelectField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    n_oficio = StringField('N°OFICIO', validators=[DataRequired(), Length(min=-1, max=80, message='N°OFICIO')])
    fecha = DateField('Fecha')
    recibido = StringField('Recibio', validators=[DataRequired(), Length(min=-1, max=80, message='Quien recibio')])
    remitido = StringField('Remitido', validators=[DataRequired(), Length(min=-1, max=80, message='Quien Envio')])
    finalidad = StringField('Finalidad', validators=[DataRequired(), Length(min=-1, max=80, message='Tipo de finalidad')])
    asunto = StringField('Asunto', validators=[DataRequired(), Length(min=-1, max=80, message='Asunto del oficio')])
    respuesta = StringField('Respuesta', validators=[DataRequired(), Length(min=-1, max=80, message='Respuesta')])
    fecha_respuesta = DateField('Fecha')
    observacion = StringField('Observacion', validators=[DataRequired(), Length(min=-1, max=80, message='Respuesta')])
    tipo_registro = SelectField('Tipo de registro', choices=[('enviado', 'Enviado'), ('recibido', 'Recibido')])

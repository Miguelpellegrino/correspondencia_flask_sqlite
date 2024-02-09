from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Contact
from forms import ContactForm

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = False

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('contacts'))


@app.route("/new_contact", methods=('GET', 'POST'))
def new_contact():
    '''
    Create new contact
    '''
    form = ContactForm()
    if form.validate_on_submit():
        my_contact = Contact()
        form.populate_obj(my_contact)
        db.session.add(my_contact)
        try:
            db.session.commit()
            # User info
            flash('Registro Creado Correctamente', 'success')
            return redirect(url_for('contacts'))
        except:
            db.session.rollback()
            flash('Error De Registro.', 'danger')

    return render_template('web/new_contact.html', form=form)


@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    '''
    Edit contact

    :param id: Id from contact
    '''
    my_contact = Contact.query.filter_by(id=id).first()
    form = ContactForm(obj=my_contact)
    if form.validate_on_submit():
        try:
            # Update contact
            form.populate_obj(my_contact)
            db.session.add(my_contact)
            db.session.commit()
            # User info
            flash('Registro Actualizado', 'success')
        except:
            db.session.rollback()
            flash('Error Al Actualizar.', 'danger')
    return render_template(
        'web/edit_contact.html',
        form=form)


@app.route("/contacts")
def contacts():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.order_by(Contact.n_oficio).all()
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/enviados")
def enviados():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.filter_by(tipo_registro='enviado')
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/recibidos")
def recibidos():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.filter_by(tipo_registro='recibido')
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/all")
def all():
    '''
    Show alls contacts
    '''
    contacts = Contact.query.order_by(Contact.n_oficio).all()
    return render_template('web/contacts.html', contacts=contacts)

@app.route("/search")
def search():
    '''
    Search
    '''
    n_oficio_search = request.args.get('n_oficio')
    all_contacts = Contact.query.filter(
            Contact.n_oficio.contains(n_oficio_search)
        ).order_by(Contact.n_oficio).all()

    if all_contacts == []:
        all_contacts = Contact.query.filter(
            Contact.fecha.contains(n_oficio_search)
        ).order_by(Contact.fecha).all()
    

    return render_template('web/contacts.html', contacts=all_contacts)


@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    '''
    Delete contact
    '''
    try:
        mi_contacto = Contact.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_contacto)
        db.session.commit()
        flash('Eliminado Correctamente.', 'danger')
    except:
        db.session.rollback()
        flash('Error Al Eliminar.', 'danger')

    return redirect(url_for('contacts'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")

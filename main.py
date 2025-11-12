# Importando liberías
from flask import Flask, render_template, request, redirect, session
# Conectar librería para trabajar con bases de datos
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Configurar la clave secreta para la sesión
app.secret_key = 'my_top_secret_123'
# Estableciendo la conexión con SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creando la Base de Datos
db = SQLAlchemy(app)
# Crando una tabla

class Card(db.Model):
    # Estableciendo campos de entrada
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(100), nullable=False)
    # Subtítulo
    subtitle = db.Column(db.String(300), nullable=False)
    # Texto
    text = db.Column(db.Text, nullable=False)
    # Correo electrónico del titular de la tarjeta
    user_email = db.Column(db.String(100), nullable=False)

    # Objeto de salida y su ID
    def __repr__(self):
        return f'<Card {self.id}>'
    

# Tarea #1. Crear la tabla de usuarios


# Página de atterizaje de contenido
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
            
        # Tarea #4. Implementar la verificación de usuario

     
    else:
        return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Tarea #3. Implementar grabación de usuario


        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# Página de contenido de lanzamiento
@app.route('/index')
def index():
    # Tarea #4. Asegúrate de que el usuario solo vea sus propias tarjetas.
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Lanzando la página de la tarjeta
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Abrir la página de creación de tarjetas
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formulario de la tarjeta
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Tarea #4. Realizar la creación de tarjetas en nombre del usuario
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)

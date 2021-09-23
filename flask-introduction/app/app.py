import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine

app = Flask(__name__)

# Parametros de configuracion a la base de datos

#--Base de datos SQLAlchemy
usuario = os.getenv('MYSQL_USER')
user_pass= os.getenv('MYSQL_PASSWORD')
basedatos= os.getenv('MYSQL_DATABASE')
uri= 'mysql://'+ usuario + ':'+ user_pass +'@database/'+basedatos
#uri='mysql://testuser:admin123@database/todobase'
app.config['SQLALCHEMY_DATABASE_URI']=uri
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Create an engine object.
#engine = create_engine(uri)

# Create database if it does not exist.
#conn = engine.connect()
#>>> engine.dialect.has_table(conn, table_name='departments')
#if not engine.dialect.has_table(conn, table_name='todo'):
    
    #db.create_all()
#--


# A continuacion se crea un modelo o esquema para la base de datos

class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #
    # Funcion que devuelve una cadena cada vez que se crea un nuevo elemento
    # Devuelve el 'id' de la tarea recien creada
    #
    def __repr__(self): 
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index(): 
    if request.method == 'POST': 
        if request.json and 'content' in request.json:
            task_content = request.json.get('content',"")
        else: 
            task_content = request.form['content'] 
        # 
        # Se crea un objeto conforme al modelo declarado 
        # 
        new_task = Todo(content = task_content) 
        try: 
            db.session.add(new_task) 
            db.session.commit() 
            if request.json:
                return 'Enviado'
            else: 
                return redirect('/') 
        except: 
            return 'There was an issue adding your task' 
    else: 
        try:
            tasks = Todo.query.order_by(Todo.date_created).all()
        except:
            db.create_all()
            tasks = Todo.query.order_by(Todo.date_created).all()

        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>', methods=['DELETE','GET'])
def delete(id): 
    task_to_delete = Todo.query.get_or_404(id) 
    try: 
        db.session.delete(task_to_delete) 
        db.session.commit() 
        return redirect('/') 
    except: 
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET', 'POST','PUT'])
def update(id):
    task = Todo.query.get_or_404(id) 
    if request.method == 'POST': 
        task.content = request.form['content']     
        try: 
            db.session.commit() 
            return redirect('/') 
        except: 
            return 'There was an issue updating your task' 
    if request.method == 'PUT': 
        task.content = request.json['content'] 
        try: 
            db.session.commit() 
            return redirect('/') 
        except: 
            return 'There was an issue updating your task' 
    else: 
        return render_template('update.html', task=task)


if __name__ == "__main__": 
    app.run(host='0.0.0.0',debug=True)

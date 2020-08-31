from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/LNV/Desktop/my_project/todo.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(80))
    complate=db.Column(db.Boolean)        
@app.route('/')
def index():
    todos=todo.query.all()
    return render_template("index.html",todos=todos)


@app.route("/add",methods=["POST"])
def add():
    title=request.form.get("title")

    newtodo=todo(title=title,complate=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/gun/<string:id>")
def detele(id):
    todos = todo.query.filter_by(id=id).first()
    
    if todos.complate == True:
        todos.complate=False
    else:
        todos.complate=True
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/det/<string:id>")
def det(id):
    todos =todo.query.filter_by(id=id).first()
    db.session.delete(todos)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
        
import re
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

aplication = app = Flask(__name__, static_url_path="/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ahoj.db' 
db = SQLAlchemy(app)


class item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable = False)
    sallary = db.Column(db.Integer())

    def __repr__(self):
        return f'Item {self.name}'
    
    
    
@app.route("/")
@app.route("/home")
def HELLO():
    return render_template('hello.html')

@app.route("/about")
def About():
    meno = "SALLARY:"
    zoznam = item.query.all()
    return render_template("about.html", zoznam=zoznam, meno=meno)



if __name__ == "__main__":
    app.run(debug=False,)

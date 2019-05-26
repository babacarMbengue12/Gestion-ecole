from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dda22ba3e6d12380acdc3c1238569588'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config.from_object('babacar.models')


from babacar import routes

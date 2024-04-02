from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cors import configure_cors

app = Flask(__name__)
app.config.from_object('config.Config')
configure_cors(app) 

db = SQLAlchemy(app)

from app import routes, models

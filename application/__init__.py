from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enbqqjku:3gHudZ0t9YUMAJos2sMZD7IcmxvDoXWA@trumpet.db.elephantsql.com/enbqqjku'
db = SQLAlchemy(app)

from application import routes
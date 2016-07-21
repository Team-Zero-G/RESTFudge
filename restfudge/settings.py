import os
from flask import Flask, url_for
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = 'restfudge/static/data/'

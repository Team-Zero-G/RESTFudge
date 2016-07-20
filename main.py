from flask import Flask
from flask_restful import Resource, Api
from restfudge.main import RestFudge

app = Flask(__name__)
api = Api(app)

api.add_resource(RestFudge, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

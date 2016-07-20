from flask import Flask
from flask_restful import Resource

class RestFudge(Resource):
    """ RESTful API for ImageFudge """

    def post(self):
        """ returns a fudged image as specified by request data """
        pass

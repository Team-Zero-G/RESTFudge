from flask import Flask
from flask_restful import Resource

class RestFudge(Resource):
    def get(self):
        result = dict()
        return result

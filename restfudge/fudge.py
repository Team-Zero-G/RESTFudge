import os
from flask import Flask, redirect, url_for, render_template, make_response
from flask_restful import Api, Resource
from restfudge.settings import app, api

class FudgeMeta(Resource):
    def get(self, guid):
        if is_valid(guid):
            files = os.listdir(app.config['UPLOAD_FOLDER'])
            filename = [filename for filename in files if guid in filename][0]
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template(
                'image.html',
                filepath='data/'+filename,
                filename=filename
            ), 200, headers)
        else:
            return redirect(url_for('index'))



def is_valid(guid):
    ''' Determines if a guid is valid.
    Length should be 32.
    Alpha chars should be all caps.
    File with that name should exist in upload folder.
    '''
    if len(guid) is not 32:
        return False
    if guid.upper() != guid:
        return False

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return True in list(True for filename in files if guid in filename)

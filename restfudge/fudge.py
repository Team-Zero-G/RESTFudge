import os
from flask import redirect, url_for, render_template, make_response
from flask_restful import Resource
from restfudge.settings import app

from imagefudge.image_fudge import Fudged


class FudgeMeta(Resource):
    """ Handles original images """
    def get(self, guid):
        if is_valid(guid):
            filename = get_file_from_guid(guid)
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template(
                'image.html',
                filepath='data/'+filename,
                filename=filename
            ), 200, headers)
        else:
            return redirect(url_for('index'))


class FudgeAPIMeta(Resource):
    def get(self, guid, effect):
        ''' Returns an image if the particular effect has been applied.
        Otherwise redirects to the index page.
        '''
        if is_valid(guid) and effect is not None:
            filename = get_file_from_guid(guid, effect)
            if filename is not None:
                headers = {'Content-Type': 'text/html'}
                return make_response(render_template(
                    'image.html',
                    filepath='data/{}'.format(filename),
                    filename=filename
                ), 200, headers)
        return redirect(url_for('index'))



def is_supported(effect):
    return effect in [
        "draw_relative_arcs",
    ]


def get_file_from_guid(guid, effect=None):
    ''' Returns a file based on its guid '''
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    if effect is None:
        search = guid
    else:
        search = "{}_{}".format(guid, effect)
    return next(filter(lambda x: search in x, files)) or None


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

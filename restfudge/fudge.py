import os
from flask import request, redirect, url_for, render_template, make_response
from flask_restful import Resource
from restfudge.settings import app
from restfudge.utils import switch

from imagefudge.image_fudge import Fudged, FudgeMaker


HTML_HEADERS = {'Content-Type': 'text/html'}


class FudgeMeta(Resource):
    """ Handles original images.
    Renders the image page if the image exists.
    Otherwise redirects back to the index.
    """
    def get(self, slug):
        ''' Checks to make sure a slug is valid.

        '''
        if is_valid(slug):
            filename = get_file_from_slug(slug)
            return render_image(filename)
        else:
            return redirect(url_for('index'))


class FudgeAPIMeta(Resource):
    def get(self, slug, effect):
        ''' Returns an image if the particular effect has been applied.
        Otherwise redirects to the index page.
        '''
        if is_valid(slug) and effect is not None:
            filename = get_file_from_slug(slug, effect)
            if filename is not None:
                return render_image(filename)
        return redirect(url_for('index'))

    def post(self, slug, effect):
        ''' Applies an effect on an image '''
        if is_valid(slug) and effect is not None:
            filename = get_file_from_slug(slug)
            ext = filename.split('.')[1]
            filename = "{}{}".format(app.config['UPLOAD_FOLDER'], filename)
            new_filename = '{slug}_{effect}.{ext}'
            new_filename = new_filename.format(slug=slug,
                                               effect=effect,
                                               ext=ext)
            args = { i:j for i,j in request.form.items() }
            fudged = self._fudge(filename, effect, args)
            fudged.save('{}{}'.format(app.config['UPLOAD_FOLDER'], new_filename))
            filename = new_filename
        return render_image(filename)

    def _fudge(self, filename, effect, kwargs):
        f = FudgeMaker(filename)
        for case in switch(effect):
            if case('draw_relative_arcs'):
                f.draw_relative_arcs(origins=kwargs['origins'],
                                     endpoints=kwargs['endpoints'],
                                     arclen=kwargs['arclen'])
                break
            elif case('fuzzy'):
                f.fuzzy(int(kwargs['magnitude']))
                break
        return f


def render_image(filename):
    ''' Renders the image in the html
    template using the given filename.
    '''
    return make_response(render_template(
        'image.html',
        filepath='data/{}'.format(filename),
        filename=filename
    ), 200, HTML_HEADERS)


def get_file_from_slug(slug, effect=None):
    ''' Returns a file based on its slug '''
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    if effect is None:
        search = slug
    else:
        search = "{}_{}".format(slug, effect)
    return next(filter(lambda x: search in x, files)) or None


def is_valid(slug):
    ''' Determines if a slug is valid.
    Length should be 32.
    Alpha chars should be all caps.
    File with that name should exist in upload folder.
    '''
    if len(slug) is not 32:
        return False
    if slug.upper() != slug:
        return False

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return True in list(True for filename in files if slug in filename)

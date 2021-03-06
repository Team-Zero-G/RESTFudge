import os
from flask import request, redirect, url_for, render_template, make_response
from werkzeug import secure_filename
from restfudge.utils import allowed_file, slug
from restfudge.settings import app, api
from restfudge.fudge import FudgeMeta, FudgeAPIMeta


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Handles file uploads and displays uploaded files '''
    # Handle file upload
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            extension = file.filename[file.filename.index('.'):]
            _slug = slug(file.filename)
            filename = secure_filename(_slug + extension)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

    headers = {'Content-Type': 'text/html'}
    # No file. Render index template.
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    data = zip(files, [file.split('.')[0] for file in files])
    return make_response(render_template(
        'index.html',
        data=data
    ), 200, headers)


api.add_resource(FudgeMeta, '/<string:slug>')
api.add_resource(FudgeAPIMeta, '/<string:slug>/<string:effect>')

def run(debug=False):
    app.run(host='0.0.0.0', debug=debug)


if __name__ == '__main__':
    run()

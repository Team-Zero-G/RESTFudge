import os
from flask import request, redirect, url_for, render_template, make_response
from werkzeug import secure_filename
from restfudge.utils import allowed_file, guid
from restfudge.settings import app, api
from restfudge.fudge import FudgeMeta


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Handles file uploads and displays uploaded files '''
    # Handle file upload
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            extension = file.filename[file.filename.index('.'):]
            _guid = guid(file.filename)
            filename = secure_filename(_guid + extension)
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


api.add_resource(FudgeMeta, '/<string:guid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

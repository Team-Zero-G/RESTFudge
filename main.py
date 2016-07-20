import os
import hashlib
from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api
from werkzeug import secure_filename

from imagefudge.image_fudge import Fudged

# Initialize Flask
app = Flask(__name__)
api = Api(app)

ALLOWED_EXTENSIONS = set(['jpg', 'png'])
app.config['UPLOAD_FOLDER'] = 'data/'


def allowed_file(filename):
    ''' Returns true if a file is one of the allowed types '''
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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

    # No file. Render index template.
    return render_template(
        'index.html',
        data=os.listdir(app.config['UPLOAD_FOLDER'])
    )


def guid(filename):
    ''' Returns an uppercase, 32 bit, hexidecimal guid. '''
    filename = filename.encode()
    return str(hashlib.md5(filename).hexdigest()).upper()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

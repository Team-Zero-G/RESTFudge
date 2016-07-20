import os
from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api
from werkzeug import secure_filename

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
    # Handle file upload
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

    # No file. Render index template.
    return render_template(
        'index.html',
        data=os.listdir(app.config['UPLOAD_FOLDER'])
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')

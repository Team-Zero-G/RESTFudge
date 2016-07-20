import os
from flask import Flask, request, redirect, url_for
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

ALLOWED_EXTENSIONS = set(['jpg','png'])
app.config['UPLOAD_FOLDER'] = 'data/'


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

    template = open('index.html', 'r').read()
    return str(template).join(os.listdir(app.config['UPLOAD_FOLDER']))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

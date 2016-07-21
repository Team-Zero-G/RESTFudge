import hashlib


ALLOWED_EXTENSIONS = set(['jpg', 'png'])


def allowed_file(filename):
    ''' Returns true if a file is one of the allowed types '''
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def guid(filename):
    ''' Returns an uppercase, 32 bit, hexidecimal guid. '''
    filename = filename.encode()
    return str(hashlib.md5(filename).hexdigest()).upper()

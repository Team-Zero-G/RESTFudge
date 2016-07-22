import hashlib


ALLOWED_EXTENSIONS = set(['jpg', 'png'])


def allowed_file(filename):
    ''' Returns true if a file is one of the allowed types '''
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def slug(filename):
    ''' Returns an uppercase, 32 bit, hexidecimal slug. '''
    filename = filename.encode()
    return str(hashlib.md5(filename).hexdigest()).upper()


class switch(object):
    ''' Switch statement class copied from
    http://code.activestate.com/recipes/410692/
    and adapted to fit this project.
    '''
    def __init__(self, value):
        self.value = value
        self.matched = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.matched or not args:
            return True
        elif self.value in args:
            self.matched = True
            return True
        else:
            return False

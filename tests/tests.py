import os
import signal
import subprocess
from flask import Flask
from flask import request, redirect, url_for, render_template, make_response
from flask_testing import TestCase
from restfudge.utils import allowed_file, slug
from restfudge.fudge import FudgeMeta, FudgeAPIMeta
from main import run, api


TEST_IMAGE = 'restfudge/static/data/15DE87EECEF79345239D20D4B0FB5D6C.png'


class TestFudgeMeta(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app 

    def setUp(self):
        self.image = TEST_IMAGE
        self.slug = self.image.replace('/','.').split('.')[-2]

    def test_slug(self):
        self.assertEqual(len(self.slug), 32)

    """
    def test_get(self):
        result = self.client.get('/{}'.format(self.slug))
        print(result.__dir__())
    """

if __name__ == '__main__':
    unittest.main()

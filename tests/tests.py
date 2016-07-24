import os
import signal
import subprocess
from unittest import TestCase
from flask import request, redirect, url_for, render_template, make_response
from restfudge.utils import allowed_file, slug
from restfudge.fudge import FudgeMeta, FudgeAPIMeta
from restfudge.settings import app
from main import run, api


TEST_IMAGE = 'restfudge/static/data/15DE87EECEF79345239D20D4B0FB5D6C.png'


class TestFudgeMeta(TestCase):
    def setUp(self):
        self.app = app
        self.image = TEST_IMAGE
        self.slug = self.image.replace('/','.').split('.')[-2]

    def test_slug(self):
        self.assertEqual(len(self.slug), 32)

if __name__ == '__main__':
    run(debug=True)
    unittest.main()

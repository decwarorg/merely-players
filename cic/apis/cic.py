import json
from flask_restx import Namespace, Resource
from cic.utils import pathroot
from flask import render_template, make_response

api = Namespace('cic')

@api.route('/')
class CIC(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('cic.html'), 200, headers)
    
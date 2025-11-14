import json
from flask_restx import Namespace, Resource
from cic.utils import pathroot

api = Namespace('galaxy')

@api.route('/')
class Galaxy(Resource):
    def get(self):
        path = pathroot() + '/data/galaxy.json'
        galaxy = json.load(open(path))
        return galaxy
    
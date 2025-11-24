import json
from flask_restx import Namespace, Resource
from cic.utils import pathroot

api = Namespace('robots')

@api.route('/start')
class GalaxyStart(Resource):
    def get(self):
        return 'started'
    
@api.route('/stop')
class GalaxyStop(Resource):
    def get(self):
        return 'stopped'
    
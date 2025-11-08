from flask_restx import Namespace, Resource

api = Namespace('hello')

@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
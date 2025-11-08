from flask_restx import Namespace, Resource

api = Namespace('cats')

@api.route('/')
class CatList(Resource):
    def get(self):
        return ['wow']
    
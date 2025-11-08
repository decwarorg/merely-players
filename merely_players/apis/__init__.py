from flask_restx import Api
from .namespace1 import api as ns1
from .namespace2 import api as ns2
api = Api()
api.add_namespace(ns1)
api.add_namespace(ns2)

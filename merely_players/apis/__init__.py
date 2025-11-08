from flask_restx import Api

api = Api()

from .galaxy import api as galaxy
api.add_namespace(galaxy)

# from .namespace2 import api as ns2
# api.add_namespace(ns2)

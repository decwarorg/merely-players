from flask_restx import Api

api = Api()

from cic.apis.galaxy import api as galaxy
api.add_namespace(galaxy)

from cic.apis.cic import api as cic
api.add_namespace(cic)

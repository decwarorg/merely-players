from flask import request
from flask_restx import Namespace, Resource
import cic.robot.runner as runner

api = Namespace('robots')

@api.route('/start')
class RobotsStart(Resource):
    def get(self):
        ipstr = request.args.get('ipstr', '').strip() or None
        runner.start(ipstr=ipstr)
        return 'started'
    
@api.route('/stop')
class RobotsStop(Resource):
    def get(self):
        runner.stop()
        return 'stopped'
    
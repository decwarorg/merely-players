from flask_restx import Namespace, Resource
import cic.robot.runner as runner

api = Namespace('robots')

@api.route('/start')
class RobotsStart(Resource):
    def get(self):
        runner.start()
        return 'started'
    
@api.route('/stop')
class RobotsStop(Resource):
    def get(self):
        runner.stop()
        return 'stopped'
    
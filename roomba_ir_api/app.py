import falcon

from . import control

api = application = falcon.API()
clean = control.Clean()

api.add_route('/control/clean', clean)
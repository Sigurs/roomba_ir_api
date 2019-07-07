import json
import os
import falcon
import time
import subprocess
import logging


class Clean(object):

    def on_get(self, req, resp):

        doc = {
            'status': 'ok',
        }

        resp.status = falcon.HTTP_200

        try:
            subprocess.check_output('irsend send_start iRobot_Roomba clean', shell=True, stderr=subprocess.STDOUT)

            time.sleep(1)

            subprocess.check_output('irsend send_stop iRobot_Roomba clean', shell=True, stderr=subprocess.STDOUT)
        except Exception as e:
            logging.exception(e)
            doc['status'] = 'error'
            resp.status = falcon.HTTP_500

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

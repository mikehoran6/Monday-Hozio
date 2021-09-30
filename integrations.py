import os
import json
import sys
import requests
from constants import apiUrl, headers
from flask import Flask, request, abort, make_response
app = Flask(__name__)

@app.route('/createtasksgroup', methods=['POST'])
def create_tasks_group():
    if request.method == 'POST':
        hook = request.json
        if 'challenge' in hook:
            resp_headers = {'Content-Type': 'application/json'}
            response = make_response(json.dumps(hook), 200, resp_headers)
            return response
        else:
            sys.stdout.write(str(hook))
            client_name = hook['event']['pulseName']
            query = 'mutation { create_group (board_id: 1673060240, group_name: ' + client_name + ') { id }}'
            data = {'query': query}
            requests.post(url=apiUrl, json=data, headers=headers)
            return 200, 'success'
    else:
        return 400, 'failed'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
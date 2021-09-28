import os
import json
from flask import Flask, request, abort, make_response
app = Flask(__name__)

@app.route('/createtasksgroup', methods=['POST'])
def create_tasks_group():
    dispatcher = {'1': function1()}
    logs = open('Logs.txt', 'a')
    if request.method == 'POST':
        hook = request.json
        if 'challenge' in hook:
            headers = {
                'Content-Type': 'application/json'
            }
            response = make_response(json.dumps(hook), 200, headers)
            return response
    else:
        abort(400)

def function1():
    print()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
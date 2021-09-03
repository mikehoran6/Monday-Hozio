import os
from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    dispatcher = {'1': create_tasks_group}
    logs = open('Logs.txt', 'a')
    if request.method == 'POST':
        hook = request.json
        logs.write('test' + '\n')
        logs.close()
        return 'success', 200
    else:
        abort(400)

def create_tasks_group(hook):
    print('create')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
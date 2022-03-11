from flask import Flask
import json

app = Flask(__name__)

@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def welcome(name):
    return json.dumps( {'name' : name }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8005)

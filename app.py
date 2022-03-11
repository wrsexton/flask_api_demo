from flask import Flask

app = Flask(__name__)

@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def welcome(name):
    return f"<h1>Hello, {name}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8005)

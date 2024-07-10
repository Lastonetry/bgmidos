from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from REX'


if __name__ == "__serverr__":
    app.run()

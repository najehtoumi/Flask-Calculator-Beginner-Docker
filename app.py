from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from logic import Add, Divide, Multiply, Subtract

app = Flask(__name__)
api = Api(app)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")


@app.route('/')
def hello_world():
    return "Hello DevOps it's NOW "


if __name__=="__main__":
    app.run(host="0.0.0.0")

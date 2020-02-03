from flask import Flask
from flask_restful import Api
from home.resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Categories, "/")
api.add_resource(Products, "/<category_id>")
api.add_resource(Price, "/price")



if __name__ == "__main__":
    app.run(debug=True)
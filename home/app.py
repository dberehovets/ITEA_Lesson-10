from flask import Flask, request, render_template
from flask_restful import Api
from home.resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Categories, "/")
api.add_resource(Products, "/<category>")


# @app.route("/")
# def index():
#     print(request.json)
#     return render_template("index.html")
#
#
# @app.route("/<category>")
# def products(category):
#     return category


if __name__ == "__main__":
    app.run(debug=True)
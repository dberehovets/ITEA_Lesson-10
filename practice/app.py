from flask import Flask
import practice.models
from flask_restful import Api
from practice.resources import PostResource, AuthorResource, TagResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PostResource, "/posts")
api.add_resource(AuthorResource, "/authors")
api.add_resource(TagResource, "/tags")

# @app.route("/")
# def hello_world():
#     return "Hello World"


if __name__ == "__main__":
    app.run()
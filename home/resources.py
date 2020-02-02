from flask_restful import Resource


class Categories(Resource):
    def get(self):
        print("get")

    def post(self):
        print("post")


class Products(Resource):
    def get(self):
        print("get")

    def post(self):
        print("post")
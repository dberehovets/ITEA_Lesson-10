from flask_restful import Resource
from practice.models import *
from practice.schema import *
from flask import request


class PostResource(Resource):

    def get(self, post_id=None):

        query = Post.objects if not post_id else Post.objects.get(id=post_id)
        many = not post_id

        return PostSchema().dump(
            query,
            many=many
        )

    def post(self):
        err = PostSchema().validate(request.json)

        if err:
            return err

        post = Post(**request.get_json()).save()

        post.reload()
        return PostSchema().dump(post)

    def put(self, post_id):
        posts = Post._get_collection()
        post = posts.find_one_and_update({"id": post_id}, {"$set": request.get_json()})

        post.reload()
        return PostSchema().dump(post)

    def delete(self, post_id):
        post = Post.objects(id=post_id)
        post.delete()
        return PostSchema().dump(post)


class TagResource(Resource):

    def get(self, tag_id):
        tag = Tag.objects(id=tag_id)
        query = Post.objects(tag=tag)
        many = True if query.count() > 1 else False

        return PostSchema().dump(
            query,
            many=many
        )

    def post(self):
        err = PostSchema().validate(request.json)

        if err:
            return err

        tag = Tag(**request.get_json()).save()

        tag.reload()
        return TagSchema().dump(tag)

    def put(self, tag_id):
        tags = Tag._get_collection()
        tag = tags.find_one_and_update({"id": tag_id}, {"$set": request.get_json()})

        tag.reload()
        return TagSchema().dump(tag)

    def delete(self, tag_id):
        tag = Tag.objects(id=tag_id)
        tag.delete()
        return PostSchema().dump(tag)


class AuthorResource(Resource):
    def get(self, autor_id):
        author = Author.objects(id=autor_id)
        query = Post.objects(author=author)
        many = True if query.count() > 1 else False

        return PostSchema().dump(
            query,
            many=many
        )

    def post(self):
        err = AuthorSchema().validate(request.json)

        if err:
            return err

        author = Author(**request.get_json()).save()

        author.reload()
        return AuthorSchema().dump(author)

    def put(self, author_id):
        authors = Author._get_collection()
        author = authors.find_one_and_update({"id": author_id}, {"$set": request.get_json()})

        author.reload()
        return AuthorSchema().dump(author)

    def delete(self, author_id):
        author = Author.objects(id=author_id)
        author.delete()
        return PostSchema().dump(author)
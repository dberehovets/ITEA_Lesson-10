from mongoengine import *

connect("blog")


class Tag(Document):
    title = StringField(max_length=128)

    def get_posts(self):
        """Getting posts of the current tag"""
        return Post.objects(tag=self)


class Author(Document):
    name = StringField(default="guest", max_length=256)
    surname = StringField(max_length=256)

    def get_posts_amount(self):
        return Post.objects(author=self).count()


class Post(Document):

    title = StringField(default="New Post", max_length=255)
    content = StringField()
    publication_date = DateField()
    author = ReferenceField(Author)
    views_amount = IntField(default=0)
    tag = ReferenceField(Tag)

    @staticmethod
    def get_post(title):
        post = Post.objects(title=title).get()
        post.views_amount += 1
        return post

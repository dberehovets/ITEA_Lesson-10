from mongoengine import *

connect("shop")


class Category(Document):

    title = StringField(required=True, max_length=256)
    description = StringField(max_length=4096)
    parent = ReferenceField("self")
    is_root = BooleanField(default=False)
    subcategories = ListField(ReferenceField("self"))

    @classmethod
    def create(cls, **kwargs):
        kwargs["subcategories"] = []
        if kwargs.get("parent"):
            kwargs["is_root"] = False
        return Category(**kwargs).save()

    def add_subcategory(self, cat_obj):
        cat_obj.parent = self
        cat_obj.save()

        self.subcategories.append(cat_obj)
        self.save()

    def is_parent(self):
        return bool(self.subcategories)

    def get_products(self):
        return Product.objects(category=self)


class Product(Document):
    title = StringField(default="New Product", max_length=256)
    description = StringField(max_length=4096)
    price = IntField(min_value=1)
    category = ReferenceField(Category)
    amount = IntField(required=True)
    views = IntField(default=0)

    @classmethod
    def get_product(cls, prod_id):
        product = Product.objects(id=prod_id).get()
        product.views += 1
        product.save()
        return product


if __name__ == "__main__":

    Category(title="Electronics", description="Computers, Smartphones, etc.").save()
    Category(title="Food", description="Everything you could eat.").save()
    Category(title="Cosmetics", description="Treat your body with love.").save()
    Category(title="Clothes", description="Wear the best").save()

    Product(title="IPhone",
            description="Good phone",
            price=20000,
            category=Category.objects(title="Electronics").get(),
            amount=40).save()

    Product(title="Shorts",
            description="Summer clothes",
            price=300,
            category=Category.objects(title="Clothes").get(),
            amount=20).save()

    Product(title="Pizza",
            description="Bad food",
            price=150,
            category=Category.objects(title="Food").get(),
            amount=5).save()

    Product(title="Water",
            description="Clean your face",
            price=50,
            category=Category.objects(title="Cosmetics").get(),
            amount=8).save()

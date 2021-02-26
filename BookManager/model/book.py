import peewee as pw
# from BookManager.model.base_model import BaseModel
from BookManager.model.author import Author
from BookManager.model.category import Category
from BookManager.utilities.orm import BaseModel
class Book(BaseModel):
    name = pw.CharField()
    author = pw.ForeignKeyField(Author)
    category = pw.ForeignKeyField(Category)
    count=pw.IntegerField(default=1)


    class Meta:
        # database = database
        db_table = 'books'
    # person = pw.ForeignKeyField(Contact)



# Books.create_table()
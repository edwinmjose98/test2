import peewee as pw
# from BookManager.model.base_model import BaseModel
from BookManager.utilities.orm import BaseModel

class Author(BaseModel):
    author_name = pw.CharField()

    class Meta:
        # database = database
        db_table = 'author'
    # person = pw.ForeignKeyField(Contact)

# Author.create_table()
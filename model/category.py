import peewee as pw
# from BookManager.model.base_model import BaseModel
from BookManager.utilities.orm import BaseModel


class Category(BaseModel):
    category_name = pw.CharField()
    cat_count=pw.IntegerField(default=1)

    class Meta:
        # database = database
        db_table = 'category'
    # person = pw.ForeignKeyField(Contact)

# Category.create_table()
import peewee as pw

database=pw.MySQLDatabase("books", host="localhost", port=3306, user="root" , passwd="edwin123!")

class BaseModel(pw.Model):
    class Meta:
        database = database
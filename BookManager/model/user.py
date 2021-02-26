from flask_login import UserMixin
# from BookManager.model.base_model import BaseModel
import peewee as pw
from BookManager.utilities.orm import BaseModel


# database=pw.MySQLDatabase("books", host="localhost", port=3306, user="root" , passwd="edwin123!")

class User(BaseModel, UserMixin):
    username=pw.CharField()
    password=pw.CharField()
    Role=pw.CharField()
    class Meta():
        db_table='User'


    # @classmethod
    # def check_username(cls,username):
    #     try:
    #         q=User.select().where(User.username==username).get()
    #         return 1
    #     except:
    #         return -1
    # @classmethod
    # def get_password(cls, username):
    #     password=User.select(User.password).where(User.username == username)
    #     return password
    #
    # @classmethod
    # def get_user(cls,username):
    #     user=User.select().where(User.username==username).get()
    #     return user
        # if user.exists():
        #     return user
        # else:
        #     return -1




# User.create_table()
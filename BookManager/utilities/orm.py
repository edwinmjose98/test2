import os

import peewee as pw
from playhouse.shortcuts import model_to_dict

proxy = pw.Proxy()
password = "edwin123!"
database = pw.MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
    user=os.getenv("MYSQL_USERNAME"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    thread_safe=True,
)

proxy.initialize(database)


class BaseModel(pw.Model):
    class Meta:
        database = proxy

    def to_dict(self, only=None, exclude=None, extra_attrs=None, **kwargs):
        return model_to_dict(
            self, only=only, exclude=exclude, extra_attrs=extra_attrs, **kwargs
        )
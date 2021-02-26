import pytest
from peewee import SqliteDatabase

# from test.dataaccess import orm
from BookManager.test.dataaccess.db_models import MODELS as models
from BookManager.test.dataaccess.mock_data import load_test_data


# https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm
from BookManager.utilities import orm


@pytest.fixture(scope="session")
def db():
    # A session scope test fixture for db operaions.
    test_db = SqliteDatabase(":memory:")
    try:
        # orm.proxy.initialize(test_db)

        print("Creating the database .")
        test_db.bind(models, bind_refs=False, bind_backrefs=False)

        print("Connect to database .")
        connect_status = test_db.connect()
        if connect_status is not True:
            print("Connection FAILED ", connect_status)
        else:
            print("Connection SUCCESS ", connect_status)

        print("Populate the tables from models.")
        test_db.create_tables(models)

        print("Load initial test data")
        load_test_data(test_db)

        yield test_db

        # revert all the changes once the test completes
        test_db.rollback()

    finally:
        print("Closing db connection.")
        test_db.close()

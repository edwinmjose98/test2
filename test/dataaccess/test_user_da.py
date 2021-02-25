# from dataaccess.user_da import UserDA
#
#
# def test_get_user_positive(db):
#     user_dict: dict = UserDA.get_user("defaultuser", "abcd")
#     assert user_dict is not None
#     assert user_dict["name"] == "defaultuser"
#
#
# def test_get_user_invalid_data(db):
#     user_dict: dict = UserDA.get_user("defaultuser", "wrongpassword")
#     assert user_dict is None
#
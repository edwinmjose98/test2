# from dataaccess.user_da import UserDA
# from service.user_service import UserService
#
#
# def test_authenticate(mocker):
#     mocker.patch.object(UserDA, "get_user",
#                         return_value={"id": 100, "username": "usernameval", "role": {"role": "role"}})
#     valid, user_vo = UserService.authenticate("name", "password")
#     assert valid
#     assert user_vo is not None
#     assert user_vo.username == "usernameval"
#
#
# def test_authenticate_failed(mocker):
#     mocker.patch.object(UserDA, "get_user", return_value=None)
#     valid, user_vo = UserService.authenticate("name", "password")
#     assert valid is False
#     assert user_vo is None

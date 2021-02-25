import functools
from flask_login import current_user

class AccessControl:
    @staticmethod
    def admin(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if current_user.Role == 'Admin':
                return func(*args, **kwargs)
            else:
                raise 403
        return _wrapper

# import functools
#
# from flask_login import current_user
#
# from utilities.constants import Role
# from utilities.custom_exception import ApiException
#
#
# class AccessControl:
#     @staticmethod
#     def admin(func):
#         @functools.wraps(func)
#         def _wrapper(*args, **kwargs):
#             if current_user.role != Role.ADMIN.value:
#                 raise ApiException.forbidden()
#             return func(*args, **kwargs)
#         return _wrapper

    # @staticmethod
    # def user(func):
    #     @functools.wraps(func)
    #     def _wrapper(*args, **kwargs):
    #         if current_user.role == Role.ADMIN.value or current_user.role == Role.USER.value:
    #             func(*args, **kwargs)
    #         else:
    #             raise ApiException.forbidden()
    #
    #     return _wrapper
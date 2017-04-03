# coding=utf-8
from functools import wraps
from flask_login import current_user
from flask import abort
from .models import Permit


def require_permit(permit):
    def decorator(func):
        @wraps(func)  # help返回真实的函数信息
        def inner(*args, **kwargs):
            if not current_user.check_permit(permit):
                abort(403)
            return func(*args, **kwargs)

        return inner

    return decorator


def require_admin_permit(func):
    return require_permit(Permit.admin)(func)
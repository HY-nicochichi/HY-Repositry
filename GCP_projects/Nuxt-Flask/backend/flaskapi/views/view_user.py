from flask import Blueprint
from extensions import auth_manager

bp_user = Blueprint('bp_user', __name__, url_prefix='/user')

@bp_user.get('/')
def user_get() -> tuple[dict, int]:
    return {'user_info': auth_manager.user_info()}, 200

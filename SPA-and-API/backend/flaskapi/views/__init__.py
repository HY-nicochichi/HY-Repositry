from flask import Blueprint
from .view_doc import bp_doc
from .view_jwt import bp_jwt
from .view_user import bp_user
from extensions import jwt_manager
from helpers import user_helper
from models import User

bps: list[Blueprint] = [
    bp_doc,
    bp_jwt,
    bp_user
]

@jwt_manager.user_lookup_loader
def lookup_user(header: dict, data: dict) -> User | None:
    return user_helper.search_by_id(data['sub'])

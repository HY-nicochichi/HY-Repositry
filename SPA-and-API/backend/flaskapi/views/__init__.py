from flask import Blueprint
from .view_jwt import bp_jwt
from .view_user import bp_user

bps: list[Blueprint] = [
    bp_jwt,
    bp_user
]

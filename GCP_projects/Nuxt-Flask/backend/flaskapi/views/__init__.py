from flask import Blueprint
from .view_doc import bp_doc
from .view_auth import bp_auth
from .view_user import bp_user

bps: list[Blueprint] = [
    bp_doc,
    bp_auth,
    bp_user
]

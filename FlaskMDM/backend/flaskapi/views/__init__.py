from .view_jwt import bp_jwt
from .view_manager import bp_manager
from .view_enterprise import bp_enterprise
from .view_policy import bp_policy

bps = [
    bp_jwt,
    bp_manager,
    bp_enterprise,
    bp_policy
]

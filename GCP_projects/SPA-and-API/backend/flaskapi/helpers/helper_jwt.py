from flask_jwt_extended import get_jwt_identity, create_access_token

class JWTHelper():

    def get_identity():
        identity = get_jwt_identity()
        return identity 

    def create(user_id):
        access_token = create_access_token(identity=user_id)
        return access_token

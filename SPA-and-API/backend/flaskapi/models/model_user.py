from extensions import db_orm, BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    user_id = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    mail = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    hashPASS = db_orm.Column(db_orm.String(255), nullable=False)
    username = db_orm.Column(db_orm.String(255), nullable=False)

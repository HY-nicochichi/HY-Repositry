from extensions import db_orm, BaseModel

class Policy(BaseModel):

    __tablename__ = 'policies'

    policy_name = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    enterprise_name = db_orm.Column(db_orm.String(255), nullable=False)

from extensions import db_orm, BaseModel

class Enterprise(BaseModel):

    __tablename__ = 'enterprises'

    enterprise_name = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    manager_id = db_orm.Column(db_orm.String(255), nullable=False)

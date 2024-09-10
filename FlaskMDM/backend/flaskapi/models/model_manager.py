from extensions import db_orm, BaseModel

class Manager(BaseModel):

    __tablename__ = 'managers'

    manager_id = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    hashPASS = db_orm.Column(db_orm.String(255), nullable=False)

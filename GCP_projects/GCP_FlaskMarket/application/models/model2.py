from application.extensions import db_orm, BaseModel

class Item(BaseModel):

    __tablename__ = 'items'

    item_id = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    itemname = db_orm.Column(db_orm.String(255), nullable=False)
    price = db_orm.Column(db_orm.Integer, nullable=False)
    stock = db_orm.Column(db_orm.Integer, nullable=False)
    tag = db_orm.Column(db_orm.String(255), nullable=False)
    seller = db_orm.Column(db_orm.String(255), nullable=False)

    __table_args__ = (
        db_orm.CheckConstraint(price >= 0, name='price_positive'),
        db_orm.CheckConstraint(stock >= 0, name='stock_positive'),
    )

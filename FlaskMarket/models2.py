from uuid import uuid4
from extensions import db_orm, BaseModel

class Item(BaseModel):

    __tablename__ = 'items'

    id = db_orm.Column(db_orm.String(255), primary_key=True, nullable=False)
    itemname = db_orm.Column(db_orm.String(255), nullable=False)
    price = db_orm.Column(db_orm.Integer, nullable=False)
    stock = db_orm.Column(db_orm.Integer, nullable=False)
    tag = db_orm.Column(db_orm.String(255), nullable=False)
    seller = db_orm.Column(db_orm.String(255), nullable=False)

    __table_args__ = (
        db_orm.CheckConstraint(price >= 0, name='price_positive'),
        db_orm.CheckConstraint(stock >= 0, name='stock_positive'),
    )

    def tag_search(tag='None'):
        if str(tag) == 'None':
            return Item.query.filter_by().all()
        return Item.query.filter_by(tag=str(tag)).all()

    def seller_search(seller):
        return Item.query.filter_by(seller=str(seller)).all()

    def search_by_id(id):
        return Item.query.filter_by(id=str(id)).first()

    def register(itemname, price, stock, tag, seller):
        id = str(uuid4())
        item = Item(id=id, itemname=str(itemname), price=int(price),
        stock=int(stock), tag=str(tag), seller=str(seller))
        db_orm.session.add(item)
        db_orm.session.commit()
        return

    def delete_by_id(id):
        db_orm.session.delete(Item.search_by_id(id))
        db_orm.session.commit()
        return
    
    def delete_by_seller(seller):
        items = Item.seller_search(seller)
        for item in items:
           db_orm.session.delete(item)
        db_orm.session.commit()
        return
    
    def update_stock(id, new_stock):
        Item.search_by_id(id).stock = int(new_stock)
        db_orm.session.commit()
        return

    def update_price(id, new_price):
        Item.search_by_id(id).price = int(new_price)
        db_orm.session.commit()
        return

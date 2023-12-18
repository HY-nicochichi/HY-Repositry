from uuid import uuid4
from extensions import db, BaseModel

class Item(BaseModel):

    __tablename__ = 'items'

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    itemname = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(255), nullable=False)
    seller = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        db.CheckConstraint(price >= 0, name='price_positive'),
        db.CheckConstraint(stock >= 0, name='stock_positive'),
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
        db.session.add(item)
        db.session.commit()
        return

    def delete_by_id(id):
        db.session.delete(Item.search_by_id(id))
        db.session.commit()
        return
    
    def delete_by_seller(seller):
        items = Item.seller_search(seller)
        for item in items:
           db.session.delete(item)
        db.session.commit()
        return
    
    def update_stock(id, new_stock):
        Item.search_by_id(id).stock = int(new_stock)
        db.session.commit()
        return

    def update_price(id, new_price):
        Item.search_by_id(id).price = int(new_price)
        db.session.commit()
        return

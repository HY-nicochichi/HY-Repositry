from uuid import uuid4
from extensions import db_orm, BaseModel

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

class ItemHelper():

    def tag_search(tag='None'):
        if str(tag) == 'None':
            return Item.query.filter_by().all()
        return Item.query.filter_by(tag=str(tag)).all()

    def seller_search(seller):
        return Item.query.filter_by(seller=str(seller)).all()

    def search_by_id(item_id):
        return Item.query.filter_by(item_id=str(item_id)).first()

    def register(itemname, price, stock, tag, seller):
        item_id = str(uuid4())
        item = Item(item_id=item_id, itemname=str(itemname), price=int(price),
        stock=int(stock), tag=str(tag), seller=str(seller))
        db_orm.session.add(item)
        db_orm.session.commit()
        return

    def delete_by_id(item_id):
        db_orm.session.delete(ItemHelper.search_by_id(item_id))
        db_orm.session.commit()
        return
    
    def delete_by_seller(seller):
        items = ItemHelper.seller_search(seller)
        for item in items:
           db_orm.session.delete(item)
        db_orm.session.commit()
        return
    
    def update_stock(item_id, new_stock):
        ItemHelper.search_by_id(item_id).stock = int(new_stock)
        db_orm.session.commit()
        return

    def update_price(item_id, new_price):
        ItemHelper.search_by_id(item_id).price = int(new_price)
        db_orm.session.commit()
        return

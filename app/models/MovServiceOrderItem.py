# mov_service_order_item.py
from one import db
from BaseApi import BaseAPI
from models.CatProduct import CatProduct
from models.MovServiceOrder import MovServiceOrder

class MovServiceOrderItem(db.Model):
    id_service_order_item     = db.Column(db.Integer, primary_key=True)
    id_service_order          = db.Column(db.Integer, db.ForeignKey('mov_service_order.id_service_order'))
    id_service_order_sequence = db.Column(db.Integer)
    product_code              = db.Column(db.String(255), db.ForeignKey('cat_product.product_code'))
    quantity                  = db.Column(db.Float)
    unit_price                = db.Column(db.Float)
    value                     = db.Column(db.Float)

    # Definir las relaciones con las tablas mov_service_order y cat_product
    service_order = db.relationship(MovServiceOrder, backref='items', foreign_keys=[id_service_order])
    product = db.relationship(CatProduct, backref='service_order_items', foreign_keys=[product_code])

    def to_dict(self):
        return {
            'id_service_order_item':     self.id_service_order_item,
            'id_service_order':          self.id_service_order,
            'id_service_order_sequence': self.id_service_order_sequence,
            'product_code':              self.product_code,
            'quantity':                  self.quantity,
            'unit_price':                self.unit_price,
            'value':                     self.value,
        }

    def __repr__(self):
        return '<MovServiceOrderItem {}>'.format(self.id_service_order_item)

    def __str__(self):
        return f'Service Order Item ID: {self.id_service_order_item}'


class MovServiceOrderItemAPI(BaseAPI):
    def __init__(self):
        super().__init__(MovServiceOrderItem)

mov_service_order_item_api = MovServiceOrderItemAPI()

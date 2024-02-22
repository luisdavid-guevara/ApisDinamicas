# CatProduct.py
from one import db
from BaseApi import BaseAPI

class CatProduct(db.Model):
    id_product         = db.Column(db.Integer, primary_key=True)
    product_group_code = db.Column(db.String(255))
    product_code       = db.Column(db.String(255))
    sku                = db.Column(db.String(255))
    uom                = db.Column(db.String(255))
    minimum_stock      = db.Column(db.Float)
    is_active          = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id_product':         self.id_product,
            'product_group_code': self.product_group_code,
            'product_code':       self.product_code,
            'sku':                self.sku,
            'uom':                self.uom,
            'minimum_stock':      self.minimum_stock,
            'is_active':          self.is_active,
        }

    def __repr__(self):
        return '<CatProduct {}>'.format(self.product_code)

    def __str__(self):
        return self.product_code


class CatProductAPI(BaseAPI):
    def __init__(self):
        super().__init__(CatProduct)

cat_product_api = CatProductAPI()

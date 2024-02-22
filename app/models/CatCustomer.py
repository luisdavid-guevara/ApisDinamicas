# CatCustomer.py
from one import db
from BaseApi import BaseAPI

class CatCustomer(db.Model):
    id_customer  = db.Column(db.Integer, primary_key=True)
    short_name   = db.Column(db.String(255))
    tax_id       = db.Column(db.String(255))
    tax_regime   = db.Column(db.String(255))
    customer_name = db.Column(db.String(255))
    legal_name   = db.Column(db.String(255))
    website      = db.Column(db.String(255))
    email        = db.Column(db.String(255))
    phone        = db.Column(db.String(255))
    is_active    = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id_customer':   self.id_customer,
            'short_name':    self.short_name,
            'tax_id':        self.tax_id,
            'tax_regime':    self.tax_regime,
            'customer_name': self.customer_name,
            'legal_name':    self.legal_name,
            'website':       self.website,
            'email':         self.email,
            'phone':         self.phone,
            'is_active':     self.is_active,
        }

    def __repr__(self):
        return '<CatCustomer {}>'.format(self.customer_name)

    def __str__(self):
        return self.customer_name


class CatCustomerAPI(BaseAPI):
    def __init__(self):
        super().__init__(CatCustomer)

cat_customer_api = CatCustomerAPI()

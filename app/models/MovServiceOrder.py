# mov_service_order.py
from one import db
from BaseApi import BaseAPI
from models.CatWorker import CatWorker

class MovServiceOrder(db.Model):
    id_service_order = db.Column(db.Integer, primary_key=True)
    cod_project      = db.Column(db.String(255))
    short_name       = db.Column(db.String(255), db.ForeignKey('mov_project.short_name'))
    date_assigned    = db.Column(db.TIMESTAMP)
    time_assigned    = db.Column(db.TIMESTAMP)
    id_worker        = db.Column(db.Integer, db.ForeignKey('cat_worker.id_worker'))
    map_latitude     = db.Column(db.String(255))
    map_longitude    = db.Column(db.String(255))
    url_signature    = db.Column(db.String(255))

    # Definir la relación con la tabla cat_worker
    worker = db.relationship(CatWorker, backref='service_orders', foreign_keys=[id_worker])

    def to_dict(self):
        return {
            'id_service_order': self.id_service_order,
            'cod_project':      self.cod_project,
            'short_name':       self.short_name,
            'date_assigned':    self.date_assigned,
            'time_assigned':    self.time_assigned,
            'id_worker':        self.id_worker,
            'map_latitude':     self.map_latitude,
            'map_longitude':    self.map_longitude,
            'url_signature':    self.url_signature,
        }

    def __repr__(self):
        return '<MovServiceOrder {}>'.format(self.cod_project)

    def __str__(self):
        return self.cod_project


class MovServiceOrderAPI(BaseAPI):
    def __init__(self):
        super().__init__(MovServiceOrder)

mov_service_order_api = MovServiceOrderAPI()

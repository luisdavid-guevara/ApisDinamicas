# mov_project.py
from one import db
from BaseApi import BaseAPI
from models.CatCustomer import CatCustomer

class MovProject(db.Model):
    id_project   = db.Column(db.Integer, primary_key=True)
    id_company   = db.Column(db.Integer)
    cod_project  = db.Column(db.String(255))
    name         = db.Column(db.String(255))
    short_name   = db.Column(db.String(255), db.ForeignKey('cat_customer.short_name'))
    created_at   = db.Column(db.TIMESTAMP)
    created_by   = db.Column(db.String(255))
    updated_at   = db.Column(db.TIMESTAMP)
    updated_by   = db.Column(db.String(255))

    # Definir la relación con la tabla cat_customer
    customer = db.relationship(CatCustomer, backref='projects', foreign_keys=[short_name])

    def to_dict(self):
        return {
            'id_project':  self.id_project,
            'id_company':  self.id_company,
            'cod_project': self.cod_project,
            'name':        self.name,
            'short_name':  self.short_name,
            'created_at':  self.created_at,
            'created_by':  self.created_by,
            'updated_at':  self.updated_at,
            'updated_by':  self.updated_by,
        }

    def __repr__(self):
        return '<MovProject {}>'.format(self.cod_project)

    def __str__(self):
        return self.cod_project


class MovProjectAPI(BaseAPI):
    def __init__(self):
        super().__init__(MovProject)

mov_project_api = MovProjectAPI()

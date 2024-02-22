# CatStatus.py
from one import db
from BaseApi import BaseAPI

class CatStatus(db.Model):
    id_status   = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id_status':   self.id_status,
            'description': self.description,
        }

    def __repr__(self):
        return '<CatStatus {}>'.format(self.description)

    def __str__(self):
        return self.description


class CatStatusAPI(BaseAPI):
    def __init__(self):
        super().__init__(CatStatus)

cat_status_api = CatStatusAPI()

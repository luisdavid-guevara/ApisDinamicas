from one import db
from BaseApi import BaseAPI

class CatWorker(db.Model):
    id_worker   = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    username    = db.Column(db.String(255))
    password    = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id_worker':  self.id_worker,
            'name'     :  self.name,
            'username' :  self.username,
            'password' :  self.password 
        }

    def __repr__(self):
        return '<CatWorker {}>'.format(self.username)

    def __str__(self):
        return self.username


class CatWorkerAPI(BaseAPI):
    def __init__(self):
        super().__init__(CatWorker)


cat_worker_api = CatWorkerAPI()





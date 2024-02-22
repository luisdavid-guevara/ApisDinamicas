# CatEquipment.py
from one import db
from BaseApi import BaseAPI

class CatEquipment(db.Model):
    id_equipment   = db.Column(db.Integer, primary_key=True)
    equipment_type = db.Column(db.String(255))
    serial_number  = db.Column(db.Integer)
    condition      = db.Column(db.String(255))
    

    def to_dict(self):
        return {
            'id_equipment':   self.id_equipment,
            'equipment_type': self.equipment_type,
            'serial_number':  self.serial_number,
            'condition':      self.condition,
        }

    def __repr__(self):
        return '<CatEquipment {}>'.format(self.equipment_type)

    def __str__(self):
        return self.equipment_type


class CatEquipmentAPI(BaseAPI):
    def __init__(self):
        super().__init__(CatEquipment)

cat_equipment_api = CatEquipmentAPI()

# models/base_conf_parameter.py
from one import db

class BaseConfParameter(db.Model):
    id_conf_parameter = db.Column(db.Integer, primary_key=True)
    cod_configuration = db.Column(db.String(255))
    cod_parameter = db.Column(db.String(255))
    description = db.Column(db.String(255))
    value = db.Column(db.String(255))
    is_active = db.Column(db.Boolean)

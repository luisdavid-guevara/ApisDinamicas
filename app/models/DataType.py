#DataType.py
from one import db
from BaseApi import BaseAPI

class DataType(db.Model):
    id_data    =   db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto      =   db.Column(db.String(255))
    entero     =   db.Column(db.Integer)
    decimal5   =   db.Column(db.Numeric(8, 5))
    logico     =   db.Column(db.Boolean)
    url        =   db.Column(db.String(255))
    fecha      =   db.Column(db.Date)
    fecha_hora =   db.Column(db.DateTime, default=db.func.now())


    def to_dict(self):
        return{
            'id_data':    self.id_data,
            'texto':      self.texto,
            'entero':     self.entero,
            'decimal5':   self.decimal5,
            'logico':     self.logico,
            'url':        self.url,
            'fecha':      self.fecha,
            'fecha_hora': self.fecha_hora,
        }
    def __repr__(self):
        return '<DataType {}>'.format(self.id_data)

    def __str__(self):
        return self.id_data
    

class DataTypeAPI(BaseAPI):
    def __init__(self):
        super().__init__(DataType)

data_type_api = DataTypeAPI()


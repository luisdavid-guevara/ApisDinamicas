# mov_service_order_task.py
from one import db
from BaseApi import BaseAPI
from models.MovServiceOrder import MovServiceOrder
from models.CatWorker import CatWorker
from models.CatEquipment import CatEquipment
from models.CatStatus import CatStatus

class MovServiceOrderTask(db.Model):
    id_service_order_task   = db.Column(db.Integer, primary_key=True)
    id_service_order        = db.Column(db.Integer, db.ForeignKey('mov_service_order.id_service_order'))
    id_worker               = db.Column(db.Integer, db.ForeignKey('cat_worker.id_worker'))
    id_equipment            = db.Column(db.Integer, db.ForeignKey('cat_equipment.id_equipment'))
    description             = db.Column(db.String(255))
    notes                   = db.Column(db.String(255))
    date_service            = db.Column(db.TIMESTAMP)
    time_spent              = db.Column(db.TIMESTAMP)
    id_status               = db.Column(db.Integer, db.ForeignKey('cat_status.id_status'))

    # Definir las relaciones con las tablas mov_service_order, cat_worker, cat_equipment y cat_status
    service_order = db.relationship(MovServiceOrder, backref='tasks', foreign_keys=[id_service_order])
    worker = db.relationship(CatWorker, backref='service_order_tasks', foreign_keys=[id_worker])
    equipment = db.relationship(CatEquipment, backref='service_order_tasks', foreign_keys=[id_equipment])
    status = db.relationship(CatStatus, backref='service_order_tasks', foreign_keys=[id_status])

    def to_dict(self):
        return {
            'id_service_order_task': self.id_service_order_task,
            'id_service_order': self.id_service_order,
            'id_worker': self.id_worker,
            'id_equipment': self.id_equipment,
            'description': self.description,
            'notes': self.notes,
            'date_service': self.date_service,
            'time_spent': self.time_spent,
            'id_status': self.id_status,
        }

    def __repr__(self):
        return '<MovServiceOrderTask {}>'.format(self.id_service_order_task)

    def __str__(self):
        return f'Service Order Task ID: {self.id_service_order_task}'


class MovServiceOrderTaskAPI(BaseAPI):
    def __init__(self):
        super().__init__(MovServiceOrderTask)

mov_service_order_task_api = MovServiceOrderTaskAPI()

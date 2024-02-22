#BaseApi.py
import logging
from flask import jsonify
from one import db

class BaseAPI:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        record = self.model.query.get(id)
        if record is None:
            return jsonify({'error': 'Record not found'}),   404
        return jsonify(record.to_dict())

    def get_all(self, page=1, per_page=10):
        pagination = self.model.query.paginate(page=page, per_page=per_page, error_out=False)
        result = {
            'success': True,
            'mensaje': 'Registros recuperados exitosamente.',
            'datos': [record.to_dict() for record in pagination.items],
            'pagina_seleccionada': page,
            'paginas_totales': pagination.pages,
            'registros_totales': pagination.total
        }
       
        logging.info(f"GET all result: {result}")
        return jsonify(result)

    def create(self, data):
        try:
            record = self.model(**data)
            db.session.add(record)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Registro creado exitosamente', 'datos agregados': record.to_dict()}), 201
        except Exception as e:
            logging.error(f"Error creating record: {e}")
            return jsonify({'success': False, 'error': f'Error al crear el registro: {e}'}), 500

    def update(self, id, data):
        record = self.model.query.get(id)
        if record is None:
            logging.error(f"Registro con el {id} no encontrado")
            return jsonify({'success': False, 'error': 'Registro no encontrado'}), 404

        try:
            for key, value in data.items():
                setattr(record, key, value)
            db.session.commit()
            return jsonify({'success': True, 'message': f'Registro con el id {id} actualizado exitosamente', 'datos actualizados': record.to_dict()})
        except Exception as e:
            logging.error(f"Error al actualizar el registro con el id {id}: {e}")
            return jsonify({'success': False, 'error': f'Error al actualizar registro {e}'}), 500

    def delete(self, id):
        record = self.model.query.get(id)
        if record is None:
            logging.error(f"Registro con el {id} no encontrado")
            return jsonify({'success': False, 'error': 'Registro no encontrado'}), 404

        try:
            db.session.delete(record)
            db.session.commit()
            return jsonify({'success': True, 'message': f'Registro con el ID {id} borrado exitosamente'})
        except Exception as e:
            logging.error(f"Error al eliminar el registro con el ID {id}: {e}")
            return jsonify({'success': False, 'error': f'Error al borrar un registro: {e}'}), 500
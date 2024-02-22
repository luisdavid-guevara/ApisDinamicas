# routes/api.py
from flask import Blueprint, jsonify, request
from BaseApi import BaseAPI
from models.DataType import DataType
from models.CatWorker import CatWorker
from models.CatStatus import CatStatus 
from models.CatProduct import CatProduct
from models.CatCustomer import CatCustomer
from models.CatEquipment import CatEquipment
from models.MovProject import MovProject    
from models.MovServiceOrder import MovServiceOrder  
from models.MovServiceOrderTask import MovServiceOrderTask   
from models.MovServiceOrderItem import MovServiceOrderItem
from models.BaseConfParameter import BaseConfParameter  


def register_route(app, route_config):
    print(f"Processing route configuration: {route_config}")
    blueprint_name = 'api_' + route_config['cod_configuration'].replace('/', '_')
    api_blueprint = Blueprint(blueprint_name, __name__)

    print(f"Registering route: {route_config['value']} with methods: ['GET', 'POST', 'PUT', 'DELETE']")

    @api_blueprint.route(route_config['value'], methods=['GET', 'POST', 'PUT', 'DELETE'])
    def dynamic_route():
        model = None
        if route_config['cod_parameter'] in ['get_workers', 'get_mov_service_orders', 'get_mov_service_tasks', 
                                             'get_data_type', 'get_status', 'get_products', 'get_customers', 
                                             'get_equipments', 'get_projects','get_mov_service_order_items']:
            if route_config['cod_parameter'] == 'get_workers':
                model = CatWorker
            elif route_config['cod_parameter'] == 'get_data_type':
                model = DataType
            elif route_config['cod_parameter'] == 'get_status':
                model = CatStatus
            elif route_config['cod_parameter'] == 'get_products':
                model = CatProduct
            elif route_config['cod_parameter'] == 'get_equipments':
                model = CatEquipment
            elif route_config['cod_parameter'] == 'get_customers':
                model = CatCustomer
            elif route_config['cod_parameter'] == 'get_projects':
                model = MovProject
            elif route_config['cod_parameter'] == 'get_mov_service_orders':
                model = MovServiceOrder
            elif route_config['cod_parameter'] == 'get_mov_service_tasks':
                model = MovServiceOrderTask
            elif route_config['cod_parameter'] == 'get_mov_service_order_items':
                model = MovServiceOrderItem
            
                   
        
        print(f"Model for route: {model}")


        if model is None:
            return jsonify({'error': 'Model not found'}),  404

        api = BaseAPI(model)

        if request.method == 'GET': 
            page = request.args.get('page',  1, type=int)
            per_page = request.args.get('per_page',  10, type=int)
            if 'id' in request.args:
                return api.get(request.args['id'])
            else:
                return api.get_all(page, per_page)
        elif request.method == 'POST':
            data = request.get_json()
            return api.create(data)
        elif request.method == 'PUT':
            data = request.get_json()
            return api.update(request.args['id_request'], data)
        elif request.method == 'DELETE':
            return api.delete(request.args['id_request'])

    app.register_blueprint(api_blueprint)

def register_all_routes(app):
    configurations = BaseConfParameter.query.filter_by(is_active=True).all()

    for config in configurations:
        register_route(app, config)

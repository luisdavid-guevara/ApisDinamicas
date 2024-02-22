# utils/dynamic_routes.py
from flask import Flask
from models.BaseConfParameter import BaseConfParameter
from routes.api import register_route

def register_routes(app):
    with app.app_context():
        configurations = BaseConfParameter.query.all()

        print(f"Found {len(configurations)} configurations")

        for config in configurations:
            if config.is_active:
                print(f"Processing active configuration: {config}")
                
                route_config = {
                    'value': config.value.split('?')[0],  
                    'cod_parameter': config.cod_parameter,
                    'cod_configuration': config.cod_configuration
                }
                
                register_route(app, route_config)




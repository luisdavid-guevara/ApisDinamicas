# app/run.py
from one import create_app
from utils.dynamic_routes import register_routes

app = create_app()

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)




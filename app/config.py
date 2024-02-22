#config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:informatica1934@localhost/Terian_BD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG = True

def get_config(config_name):
    configs = {
        'development': Config,
        'production': Config,
        'testing': Config
    }
    return configs[config_name]()


class BaseConfig:
    '''Base Configuration'''
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    '''DevelopmentConfig'''
    DEBUG = True

class TestingConfig(BaseConfig):
    '''Testing config'''
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False

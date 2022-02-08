class Config:
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'super-secret'

    API_TITLE = 'ResourceHub API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'

    SQLALCHEMY_DATABASE_URI = 'mysql://aaman007:password@db/resource_hub'


class DevelopmentConfig(Config):
    pass


class StagingConfig(Config):
    ENV = 'production'
    DEBUG = False


class ProductionConfig(Config):
    pass

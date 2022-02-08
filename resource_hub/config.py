class Config:
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'super-secret'

    API_TITLE = 'ResourceHub API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'

    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    pass


class StagingConfig(Config):
    ENV = 'production'
    DEBUG = False


class ProductionConfig(Config):
    pass

# coding=utf8


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'bible.db'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://root:root@localhost/amazing'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

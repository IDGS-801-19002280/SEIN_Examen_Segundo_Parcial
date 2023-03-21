class DevelopmentConfig() :
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mitomano5000@127.0.0.1/tiendita'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

config = {
    'development' : DevelopmentConfig
}
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    ENV = 'development'
    TESTING=True
    SECRET_KEY = 'dev'
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        r'postgresql://admin:25108-Alber8@192.168.178.27:5432/blading_catalogue'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 20

    UPLOAD_FOLDER = '\\uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

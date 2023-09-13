from flask import Flask, send_file
from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



app = Flask(__name__)

app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = Config.ALLOWED_EXTENSIONS
app.config['DEBUG'] = True
#db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
#migrate = Migrate(app, db)



SQLALCHEMY_DATABASE_URL = "sqlite:///./db_map.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



from app import routes, models


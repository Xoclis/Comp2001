import pathlib
import connexion
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine

# Define the base directory
basedir = pathlib.Path(__file__).parent.resolve()

# Create the Connexion app
connex_app = connexion.App(__name__, specification_dir=basedir)

# Flask app configuration
app = connex_app.app  
database = 'COMP2001_GSilcox'
username = 'GSilcox'
password = 'GxuQ785+'  
encoded_password = urllib.parse.quote_plus(password)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mssql+pyodbc://{username}:{encoded_password}@DIST-6-505.uopnet.plymouth.ac.uk/"
    f"{database}?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes&Encrypt=yes"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy()  
ma = Marshmallow()


# config.py
API_BASE_URL = "http://localhost:8000/api"

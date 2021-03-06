import os
from dotenv import load_dotenv
from datetime import timedelta 

load_dotenv()

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'


JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.environ['JWT_ACCESS_TOKEN_EXPIRES']))






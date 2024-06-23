import os

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

manufacturers = Table(
    'manufacturers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(60)),
    Column('nationality', String(20)),
)

database = Database(DATABASE_URI)
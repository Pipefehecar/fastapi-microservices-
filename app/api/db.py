from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:cars@localhost/postgres'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

cars = Table(
    'cars',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('year', Integer()),
    Column('manufacturer', String(30)),
    Column('description', String(250)),
    Column('categories', ARRAY(String)),
    Column('features', ARRAY(String))
)

database = Database(DATABASE_URL)
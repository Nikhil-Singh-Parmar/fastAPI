from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

users = Table (
    'users', meta ,
    Column('id',Integer,primary_key=true),
    Column('name',String(250)),
    Column('email',String(250)),
    Column('password',String(250)),
)
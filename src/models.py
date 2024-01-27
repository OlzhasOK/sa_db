from sqlalchemy import Table, Column, String, Integer, MetaData

metadata = MetaData()

students_table = Table(
    'students',
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),


)
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import insert
from sqlalchemy import select
engine = create_engine('sqlite:///example.db', echo=True)

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)

)

metadata.create_all(engine)

with engine.conenct() as connection:
    stmt = insert(users).values(name='Alice', age =25)
    connection.execute(stmt)
    connection.commit()

with engine.connect() as connection:
    stmt = select(users)
    result = connection.execute(stmt)
    for row in result:
        print(row)
        

from sqlalchemy import create_engine,Column,MetaData,Integer,String,Table
from sqlalchemy.orm import declarative_base
database_url = "postgresql+psycopg://postgres:Honey3156%24%40@localhost:5433/college"


engine = create_engine(database_url)

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key = True )
    Name = Column(String)
    Age = Column(Integer)

Base.metadata.create_all(engine)


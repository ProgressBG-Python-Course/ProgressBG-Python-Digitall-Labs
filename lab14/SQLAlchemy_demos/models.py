from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import  Column, Integer, String, Float, Boolean, Date, DateTime

# Declare a base using declarative_base
Base = declarative_base()

# Define the User class inheriting from Base
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    country = Column(String(20))
    town = Column(String(20))
    zip = Column(Integer)

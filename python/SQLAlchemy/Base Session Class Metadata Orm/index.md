# Alchemy-checkpoint.ipynb

## key words:

sqlalchemy.ext.declarative
declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float
Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)
from sqlalchemy.orm import Session
session = Session(bind=engine)

### All records to db

session.add(dog)
session.add(cat)
session.commit()

# Define a class

## Utilize python constructor to initialize the object

## create an instance of the class

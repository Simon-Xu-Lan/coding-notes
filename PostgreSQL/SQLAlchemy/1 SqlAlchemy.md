# SQLAlchemy
## connect to local database
```py
# import create_engine from sqlalchemy
from sqlalchemy import create_engine

# Database path - local
database_path = "../Resources/Census_Data.sqlite"

# Create an engine that can talk to the database
# // for absolute path, 
# /// for relative path
engine = create_engine(f"sqlite:///{database_path}")

# Query All Records in the the Database
data = engine.execute("SELECT * FROM Census_Data")
display(type(data))
for record in data:
    pprint(record)
```

## connect to remote database

## panda and sqlachemy
 Pandas
import pandas as pd
```py
# SQL Alchemy
from sqlalchemy import create_engine

database_path = "../Resources/Census_Data.sqlite"

# Create Engine
engine = create_engine(f"sqlite:///{database_path}")
conn = engine.connect()

# Query All Records in the the Database
data = pd.read_sql("SELECT * FROM Census_Data", conn)

# Data is a dataframe. Preview the Data
data.head()

# If not declare conn, put "engine", the pd.read_sql would automatically create run engine.connect()
data1 = pd.read_sql("SELECT * FROM Census_Data", engine)
data1.head()

```

## Class and Table
- example <a href="Classs and Table">Example</a>
```py
# ----------------------------------
# Dependencies
# Imports the method used for connecting to DBs
from sqlalchemy import create_engine

# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float 

# ----------------------------------
# Create Dog and Cat Classes

# Sets an object to utilize the default declarative base in SQL Alchemy
Base = declarative_base()

# Creates Classes which will serve as the anchor points for our Tables
class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)


class Cat(Base):
    __tablename__ = 'cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)

# ----------------------------------
# Create a Specific Instance of the Dog and Cat classes

# Calls the Pet Constructors to create "Dog" and "Cat" objects
dog = Dog(name='Rex', color='Brown', age=4)
cat = Cat(name="Felix", color="Gray", age=7)

# ----------------------------------
# Create Database Connection
# Creates a connection to our DB
engine = create_engine("sqlite:///pets.sqlite")
conn = engine.connect()

# ----------------------------------
# Create a "Metadata" Layer That Abstracts our SQL Database
# Create (if not already in existence) the tables associated with our classes.
Base = declarative_base()
Base.metadata.create_all(engine)

# ----------------------------------
# Use this to clear out the db
# Base.metadata.drop_all(engine)

# ----------------------------------
# Create a Session Object to Connect to DB
# Session is a temporary binding to our DB
from sqlalchemy.orm import Session
session = Session(bind=engine)

# ----------------------------------
# Add Records to the Appropriate DB
# Use the SQL ALchemy methods to run simple "INSERT" statements using the classes and objects  
session.add(dog)
session.add(cat)
session.commit()

# ----------------------------------
# Query the Tables
# Perform a simple query of the database
dog_list = session.query(Dog)
for doggy in dog_list:
    print(doggy.name)

cat_list = session.query(Cat)
for kitty in cat_list:
    print(kitty.name)
```

## connection error
### connect to heroku postgresql

- sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres
- https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
```py
# database url shoud be postgresql
'postgresql://lnsggibhegnuwr:82a4fbcaded5866b9cf551920730166d67b9d7bb2db2b0b2836603666f8c4576@ec2-52-1-115-6.compute-1.amazonaws.com:5432/d4or2bl8vpoan0'

# not prostgres
# sql alchemy not support the name postgres any more
```
### Install pycopg2 package
```shell
pip install psycopg2-binary
```
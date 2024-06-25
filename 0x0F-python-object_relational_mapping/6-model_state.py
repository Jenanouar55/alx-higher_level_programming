#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

connection_string = f'mysql+mysqldb://{username}:{password}@localhost/{database}'
engine = create_engine(connection_string, pool_pre_ping=True)
Base.metadata.create_all(engine)

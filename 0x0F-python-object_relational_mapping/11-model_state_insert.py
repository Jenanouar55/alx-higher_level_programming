#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()

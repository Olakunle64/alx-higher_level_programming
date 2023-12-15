#!/usr/bin/python3
"""Write a script that lists all State objects from the
    database hbtn_0e_6_usa using SQLAlchemy ORM

    Note: only print the state with the first state_id
    """

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id)[0]
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print()

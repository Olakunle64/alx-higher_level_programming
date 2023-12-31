#!/usr/bin/python3
"""Write a script that lists all State objects with
    the city associated to it from the
    database hbtn_0e_101_usa using SQLAlchemy ORM

    """

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import State, Base


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
    all_states = session.query(State).order_by(State.id).all()
    for s in all_states:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))
    session.commit()
    session.close()

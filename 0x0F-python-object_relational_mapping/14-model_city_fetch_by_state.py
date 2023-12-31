#!/usr/bin/python3
"""Write a script that lists all State objects from the
    database hbtn_0e_6_usa using SQLAlchemy ORM

    Note: change a particular state name to another one
    """

from model_state import Base, State
from model_city import City
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
    state_obj = session.query(City, State).filter(
                City.state_id == State.id).all()
    for obj_tuple in state_obj:
        print("{}: ({}) {}".format(
                obj_tuple[1].name, obj_tuple[0].id, obj_tuple[0].name))

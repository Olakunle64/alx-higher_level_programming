#!/usr/bin/python3
"""Write a script that lists all State objects from the
    database hbtn_0e_6_usa using SQLAlchemy ORM

    Note: add an object to the database
    """

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City
from relationship_state import Base, State


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
    city_obj = City(name='San Francisco')
    state_obj = State(name='California')
    state_obj.cities.append(city_obj)
    session.add(state_obj)
    session.commit()
    session.close()

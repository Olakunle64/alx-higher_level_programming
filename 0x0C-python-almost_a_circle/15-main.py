#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([{'width': 47, 'height': 51, 'x': 93, 'y': 41, 'id': 1}, {"id": 4, "name": "kunle"}])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

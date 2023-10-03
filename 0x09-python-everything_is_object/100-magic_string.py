#!/usr/bin/python3

def magic_string():
    magic_string.track = getattr(magic_string, "track", 0) + 1
    return ", ".join(["BestSchool"] * magic_string.track)

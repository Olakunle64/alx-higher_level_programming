#!/usr/bin/python3

def f():
    f.counter = getattr(f, "counter", 0) + 1 
    return ", ".join(["Monty Python"] * f.counter)
for i in range(10):
    print(f())
print(f.counter)

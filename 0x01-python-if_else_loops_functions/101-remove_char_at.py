#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    ret = ""
    for ch in str:
        if i != n:
            ret += ch
        i += 1
    return ret

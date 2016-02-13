#!/usr/bin/python
# -*- coding: utf-8 -*-
from stack import Stack

def par_check(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    return False


if __name__ == '__main__':
    print(par_check('(((())))'))
    print(par_check('((())'))

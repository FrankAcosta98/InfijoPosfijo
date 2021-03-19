#!/usr/bin/env python

__author__ = "Frank Acosta"

"""
    codigo que recibe formula matematica
    y la devuelve en forma posfijo
    para tareas de programacion
    Ps: la raiz es R y no acepta letras
"""

from Stack import Stack
from Queue import Queue

# importa pila y fila


inf = list(input('inserte string: '))
ops = {'R': 3, '^': 3, '/': 2, '*': 2, '+': 1, '-': 1, ')': 4}

que = Queue()
stk = Stack()
indx = 0

for item in inf:
    if item.isnumeric():
        que._Push(item)

    elif item in ops:
        if ops.get(item) == 4:
            for i in range(stk._getLen()):
                que._Push(stk._Pop())

        elif stk._getLast() == None:
            stk._Push(item)
        else:
            if ops.get(item) > ops.get(stk._getLast()):
                stk._Push(item)

            elif ops.get(item) < ops.get(stk._getLast()):
                for i in range(stk._getLen()):
                    que._Push(stk._Pop())
                stk._Push(item)

            elif ops.get(item) == ops.get(stk._getLast()):
                que._Push(stk._Pop())
                stk._Push(item)

for item in range(stk._getLen()):
    que._Push(stk._Pop())

print('posfijo: ')
que._Print()
res = Stack()

for i in range(que._getLen()):
    item = que._Pop()
    if item.isnumeric():
        res._Push(item)
    elif item in ops:
        b = int(res._Pop())
        a = int(res._Pop())
        if item == '^':
            res._Push(pow(a, b))
        elif item == 'R':
            res._Push(pow(a, 1/b))
        elif item == '*':
            res._Push(a * b)
        elif item == '/':
            res._Push(a / b)
        elif item == '+':
            res._Push(a + b)
        if item == '-':
            res._Push(a-b)
print('resultado: ')
res._Print()

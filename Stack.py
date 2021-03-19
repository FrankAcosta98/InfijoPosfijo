#!/usr/bin/env python
class Stack:
"""clase pila"""
    def __init__(self, ls=None):
        if(ls != None):
            self.ls = ls
        else:
            self.ls = list()

    def _Pop(self):
    """lifo"""
        if len(self.ls) == 1:
            temp=self.ls[0]
            self.ls = list()
            return temp
        else:
            return self.ls.pop()

    def _Push(self, item):
        self.ls.append(item)

    def _Print(self):
        print(self.ls)
    
    def _getLast(self):
        if len(self.ls)>=1:
            return self.ls[-1]
        else:
            return None

    def _getLen(self):
        return len(self.ls)

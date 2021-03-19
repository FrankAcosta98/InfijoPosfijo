#!/usr/bin/env python
class Queue:
"""clase fila"""

    def __init__(self, ls=None):
    """inicia lista"""
        if(ls != None):
            self.ls = ls
        else:
            self.ls = list()

    def _Pop(self):
    """fifo"""
        if len(self.ls) == 1:
            temp = self.ls[0]
            self.ls = list()
            return temp
        else:
            temp = self.ls.pop(0)
            tls = []
            for i in self.ls:
                if i != None:
                    tls.append(i)
            self.ls = tls
            return temp

    def _Push(self, item):
        self.ls.append(item)

    def _Print(self):
        print(*self.ls)

    def _getLen(self):
        return len(self.ls)

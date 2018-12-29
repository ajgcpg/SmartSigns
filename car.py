#each car has a queue positon (pos) based on when it arrived relative to other cars at the intersection
class Car:
    def __init__(self, sign):
        self.sign = sign
        self.pos = 0

    def __repr__(self):
        return f"[Sign: {self.sign}, Queue position: {self.pos}]"

    def setPos(self, index):
        self.pos = index

    def advance(self):
        self.pos -= 1

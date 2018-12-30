#each car has a queue positon (pos) based on when it arrived relative to other cars at the intersection
import threading

class Car:
    def __init__(self, sign):
        self.sign = sign
        self.pos = 0
        self.stp_3_sec = False

    def __repr__(self):
        return f"[Sign: {self.sign}, Queue position: {self.pos}]"

    def setPos(self, index):
        self.pos = index

    def wait(self):
        def change():
            self.stp_3_sec = True
            print(f"Car at sign {self.sign} time is up")
        threading.Timer(3, change).start()

    def advance(self):
        self.pos -= 1

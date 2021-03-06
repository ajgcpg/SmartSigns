#Each sign has an indicator which shows drivers the status of each other sign in an intersection. The larger the number,
#the farther it is from the rightmost sign. For example, if there is a car at the rightmost sign, the "0" indicator will be set to true,

class stopSign():
    def __init__(self, numsigns):
        self.signs = [None] * numsigns
        for i, sign in enumerate(self.signs):
            self.signs[i] = False
        self.car = None

    def __repr__(self):
        ret = []
        for i, sign in enumerate(self.signs):
            ret.append(f"{i}={sign} ")
        retstr = "".join(x for x in ret)
        return f"Car: {self.car is not None} | Indicators: {retstr}"

    #updates sign's indicators to reflect positions of other cars
    def set_state(self, side, state):
        for i, sign in enumerate(self.signs):
            if i == side:
                self.signs[i] = state


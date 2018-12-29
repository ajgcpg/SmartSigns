#Each sign has an indicator which shows drivers the status of each other sign in an intersection. The larger the number,
#the farther it is from the rightmost sign. For example, if there is a car at the rightmost sign, the "0" indicator will be set to true,

class stopSign():
    def __init__(self, numsigns):
        self.signs = [None] * numsigns
        for i, sign in enumerate(self.signs):
            self.signs[i] = False
        self.car_present = False
        self.car = None

    def __repr__(self):
        ret = []
        for i, sign in enumerate(self.signs):
            ret.append(f"{i}={sign} ")
        retstr = "".join(x for x in ret)
        return(f"Car: {self.car_present} | Indicators: {retstr}")

    #updates to reflect presence of a car at this sign
    def set_car_state(self, state):
        self.car_present = state

    #updates sign's indicators to reflect positions of other cars
    def set_state(self, side, state):
        for i, sign in enumerate(self.signs):
            if i == side:
                self.signs[i] = state

    #check if it is safe for car at this sign to go (WIP)
    def check_safety(self):
        if self.car.pos != 0:
            print("not safe to go")
            return False
        print("safe to go")
        return True


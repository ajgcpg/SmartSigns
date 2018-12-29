from stopsign import stopSign
from car import Car

class Controller:
    def __init__(self, numsigns):
        self.signs = [None] * numsigns
        for i, sign in enumerate(self.signs):
            self.signs[i] = stopSign(numsigns)
        self.queue = []

    def __repr__(self):
        ret = []
        for i, sign in enumerate(self.signs):
            ret.append([str(sign)])
        return "\n".join(str(x) for x in ret)

    #given a sign, checks status of other signs, starting with rightmost sign
    def check_others(self, index):
        ret = []

        for sign in self.signs[index+1:]:
            ret.append(sign.car_present)
        for sign in self.signs[:index]:
            ret.append(sign.car_present)

        #for each sign that returned true for car_present, update the respective indicator
        for i, status in enumerate(ret):
                self.signs[index].set_state(i, status)
        #print("Sign", index+1, "Status:\n", ret)

    #updates status of all signs
    def update_all_signs(self):
        for i, sign in enumerate(self.signs):
            self.check_others(i)

    #adds car to queue, and updates the correct sign to reflect that a car is present
    def new_car(self, sign):
        if(self.signs[sign].car_present):
            print("Car already at this sign")
            return
        car = Car(sign)
        car.setPos(len(self.queue))
        self.queue.append(car)
        self.signs[sign].set_car_state(True)
        self.update_all_signs()

    #removes car from queue and advances the remaining cars
    def remove_car(self):
        sign = self.queue[0].sign
        self.queue.pop(0)
        for i, car in enumerate(self.queue):
            self.queue[i].advance()
        self.signs[sign].set_car_state(False)
        self.update_all_signs()

    #check if it is safe for car at current sign to go (WIP)
    def check_safety(self, sign):
        return self.signs[sign].check_safety()

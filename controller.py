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
            ret.append(sign.car is not None)
        for sign in self.signs[:index]:
            ret.append(sign.car is not None)

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
        if self.signs[sign].car is not None:
            print("Car already at this sign")
            return
        print(f"Car arrived at sign {sign}")
        car = Car(sign)
        car.setPos(len(self.queue))
        self.queue.append(car)
        self.signs[sign].car = car
        self.update_all_signs()
        self.signs[sign].car.wait()

    #removes car from queue and advances the remaining cars
    def remove_car(self):
        sign = self.queue[0].sign
        self.queue.pop(0)
        for i, car in enumerate(self.queue):
            self.queue[i].advance()
        self.signs[sign].car = None
        self.update_all_signs()

    #check if it is safe for car at current sign to go
    def check_safety(self, sign):
        if not self.signs[sign].car:
            print("No car")
        elif self.signs[sign].car.pos != 0:
            print("Not safe - not first in queue")
        elif not self.signs[sign].car.stp_3_sec:
            print("Not safe - hasn't waited 3 sec")
        else:
            print("Safe to go")

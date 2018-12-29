from stopsign import stopSign

class Controller:
    def __init__(self, numsigns):
        self.signs = [None] * numsigns
        for i, sign in enumerate(self.signs):
            self.signs[i] = stopSign(numsigns)

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
            if status:
                self.signs[index].switch_state(i)
        print("Sign", index+1, "Status:\n", ret)

    #updates status of all signs
    def update_all(self):
        for i, sign in enumerate(self.signs):
            self.check_others(i)

    def add_car(self, index):
        self.signs[index].switch_car_state()



x = Controller(4)

print("Default State:")
print(x)

print("\nPut car at stop sign 3")

x.add_car(2)

print(x)

print("\nCheck and update signs")

x.update_all()

print(x)


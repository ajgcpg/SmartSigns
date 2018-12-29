from stopsign import stopSign

class Controller:
    def __init__(self, numsigns):
        self.signs = [None] * numsigns
        for i, sign in enumerate(self.signs):
            self.signs[i] = stopSign()

    def __repr__(self):
        ret = []
        for i, sign in enumerate(self.signs):
            ret.append([{"car": sign.car_present}, {"top": sign.top}, {"bot": sign.bot},
                        {"left": sign.left}, {"right": sign.right}])
        return "\n".join(str(x) for x in ret)

    #given a sign, checks status of other signs, starting with rightmost sign
    def check_others(self, index):
        ret = []

        for sign in self.signs[index+1:]:
            ret.append(sign.car_present)
        for sign in self.signs[:index]:
            ret.append(sign.car_present)

        print(ret)



x = Controller(3)

x.signs[2].switch_car_state()

print(x)

print(x.check_others(1))


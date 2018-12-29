#Each sign has an indicator (right, top, left, bot) which shows drivers
#the status of each other sign in an intersection. For example, if there is a car at the rightmost sign,
#the "right" indicator will be set to true.

class stopSign():
    def __init__(self):
        self.right = False
        self.top = False
        self.left = False
        self.bot = False
        self.car_present = False

    def __repr__(self):
        return(f"Car: {self.car_present} Top: {self.top}\nLeft: {self.left}\nBot: {self.bot}\nRight: {self.right}")

    def switch_car_state(self):
        self.car_present = not self.car_present

    def switch_state(self, side):
        if(side == 'T'):
            self.top = not self.top
        elif(side == 'B'):
             self.bot = not self.bot
        elif(side == 'L'):
             self.left = not self.left
        elif(side == 'R'):
             self.right = not self.right
        else:
            print("Invalid argument, please enter side (T, B, L, R)")


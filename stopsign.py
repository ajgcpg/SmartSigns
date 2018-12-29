#Each sign has an indicator (right, top, left, bot) which shows drivers
#the status of each other sign in an intersection. For example, if there is a car at the rightmost sign,
#the "right" indicator will be set to true.

class stopSign():
    def __init__(self):
        self.right = False
        self.top = False
        self.left = False
        self.car_present = False

    def __repr__(self):
        return(f"Car: {self.car_present} Top: {self.top}\nLeft: {self.left}\nBot: {self.bot}\nRight: {self.right}")

    def switch_car_state(self):
        self.car_present = not self.car_present

    #this is bad logic rn i'm working on it rn
    def switch_state(self, side):
        if(side == 0):
            self.right = not self.right
        elif(side == 1):
             self.top = not self.top
        elif(side == 2):
             self.left = not self.left
        else:
            print("Invalid argument")


class stopSign():
    def __init__(self):
        self.left = False
        self.right = False
        self.top = False
        self.bot = False

    def __repr__(self):
        return(f"Top: {self.top}\nLeft: {self.left}\nBot: {self.bot}\nRight: {self.right}")

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


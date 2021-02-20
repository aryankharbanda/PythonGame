import gbvar as gb
import config

class Paddle:
    def __init__(self, y, x):
        self._y = y
        self._x = x
        self._length = 9

    def moveleft(self, ball):
        if(self._x > 1):
            self._x -= 2
            if(ball._flag==0):
                ball._x -= 2

    def moveright(self, ball):
        if(self._x + self._length < config.columns-3): #set
            self._x += 2
            if(ball._flag==0):
                ball._x += 2

    def setlength(self,len):
        self._length = len

import gbvar as gb
import config

class Powerup:
    def __init__(self, y, x):
        self._y = y
        self._x = x
        self._vely = 2
        self._state = 0
        # 0 -> moves down
        # 1 -> collected/active
        # 2 -> ended
        # 3 -> not collected
        self._starttime = 0

    def move(self):
        if(self._state == 0):
            self._y += self._vely

    

class Expand(Powerup):
    def __init__(self, y, x):
        self._power = 'E'
        super().__init__(y,x)

    def activate(self,paddle):
        # expand paddle
        paddle.setlength(11)
        paddle._x -= 1

    def deactivate(self,paddle):
        paddle.setlength(9)
        paddle._x += 1
        
class Contract(Powerup):
    def __init__(self, y, x):
        self._power = 'C'
        super().__init__(y,x)

    def activate(self,paddle):
        # contract paddle
        paddle.setlength(7)
        paddle._x += 1

    def deactivate(self,paddle):
        paddle.setlength(9)
        paddle._x -= 1

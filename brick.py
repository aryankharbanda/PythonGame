import gbvar as gb
import config

class Brick:
    def __init__(self, y, x, power):
        self._y = y
        self._x = x
        self._hits = 0
        self._vanish = 0
        self._power = power

class Brick1(Brick):
    def __init__(self, y, x, power):
        self._level = '1'
        self._maxhits = 1
        super().__init__(y,x, power)

class Brick2(Brick):
    def __init__(self, y, x, power):
        self._level = '2'
        self._maxhits = 2
        super().__init__(y,x, power)

class Brick3(Brick):
    def __init__(self, y, x, power):
        self._level = '3'
        self._maxhits = 3
        super().__init__(y,x, power)

class Brick4(Brick):
    def __init__(self,y,x, power):
        self._level = '4'
        self._maxhits = -1
        super().__init__(y,x, power)

class ExBrick(Brick):
    def __init__(self, y, x, power,c):
        self._level = '5'
        self._maxhits = 1
        self._cluster = c
        super().__init__(y,x,power)
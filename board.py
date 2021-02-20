import gbvar as gb
import config
import colorama
import numpy as np


class Board:
    def __init__(self):
        self._rows = config.rows
        self._cols = config.columns
        self._grid = np.array([[' ' for col in range(self._cols)]
                       for row in range(self._rows)])

    def renderPaddle(self,p):
        x = 0
        while x < p._length:
            self._grid[p._y][p._x + x] = 'p'
            x += 1
    def clearPaddle(self,p):
        x = 0
        while x < p._length:
            self._grid[p._y][p._x + x] = ' '
            x += 1

    def renderBall(self,b):
        self._grid[b._y][b._x] = 'b'
    def clearBall(self,b):
        self._grid[b._y][b._x] = ' '
        
    def renderBricks(self, arr):
        for brick in arr:
            if(brick._vanish == 0):
                x = 0
                while x < 7:
                    self._grid[brick._y][brick._x + x] = brick._level
                    x += 1
    def clearBricks(self, arr):
        for brick in arr:
            x = 0
            while x < 7:
                self._grid[brick._y][brick._x + x] = ' '
                x += 1

    def renderPowers(self, arr):
        for power in arr:
            if(power._state == 0):
                self._grid[power._y][power._x] = power._power
    def clearPowers(self, arr):
        for power in arr:
            self._grid[power._y][power._x] = ' '

    def renderGrid(self):
        if(gb.gameover == 0):
            print("\033[2;1H" + colorama.Fore.WHITE + colorama.Back.BLUE + colorama.Style.BRIGHT + ("SCORE: "+str(gb.score)+"   |  LIVES: "+str(gb.lives)+"   |  TIME: "+str(gb.times)) .center(config.columns+2))
            print(colorama.Style.RESET_ALL)
            for ix in range(0, config.columns + 2):
                print("_", end='')
            print(' ')
            for y in range(0, config.rows):
                x = 0
                print("|", end='')
                while x < config.columns:
                    if self._grid[y][x] == ' ':
                        print(' ', end='')
                        x += 1
                    
                    elif self._grid[y][x] == 'p':
                        print(colorama.Back.LIGHTWHITE_EX+'^', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        # print(' ', end='')
                        x += 1
                    elif self._grid[y][x] == 'b':
                        # print('\U0001F923', end='')
                        print(colorama.Fore.RED+'*', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1

                    elif self._grid[y][x] == '1':
                        print(colorama.Back.YELLOW+'_', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    elif self._grid[y][x] == '2':
                        print(colorama.Back.GREEN+'_', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    elif self._grid[y][x] == '3':
                        print(colorama.Back.CYAN+'_', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    elif self._grid[y][x] == '4':
                        print(colorama.Back.BLUE+'_', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    elif self._grid[y][x] == '5':
                        print(colorama.Back.WHITE+colorama.Fore.BLACK+'X', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1

                    elif self._grid[y][x] == 'E':
                        print('\U0001F923', end='')
                        x += 2
                    elif self._grid[y][x] == 'C':
                        print('\U0001F923', end='')
                        x += 2

                
                print('|\n', end='')
            
        if(gb.gameover == 1):
            # print("GAME OVER, SCORE = " + str(gb.score)", TIME = ''")
            print("\033[2;1H" + colorama.Fore.WHITE + colorama.Back.RED + colorama.Style.BRIGHT + ("GAME OVER !!! SCORE: "+str(gb.score)+" TIME: "+str(gb.overtime)) .center(config.columns+2))
            print(colorama.Style.RESET_ALL)
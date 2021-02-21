import gbvar as gb
import config
import powerup
import random

class Ball:
    def __init__(self, y, x):
        self._y = y
        self._x = x
        self._flag = 0
        self._velx = 1
        self._vely = -1


    def shoot(self):
        if(self._flag == 0):
            self._flag = 1
            if(random.randint(0,1)):
                self._velx = -1

    # def moveleft(self):
    #     if(self._flag == 0):
    #         if(self._x > 1): #set this value
    #             self._x -= 2

    # def moveright(self):
    #         if(self._x < config.columns-2):
    #     if(self._flag == 0):
    #             self._x += 2

    def move(self):
        if(self._flag == 1):
            self._x += self._velx
            self._y += self._vely

    def checkcolwall(self, paddle, powers):
        if(self._flag == 1):
            if(self._x + self._velx < 0):
                self._velx = -self._velx
            elif(self._x + self._velx > config.columns-1):
                self._velx = -self._velx

            if(self._y + self._vely < 0):
                self._vely = -self._vely
            elif(self._y + self._vely > config.rows-1):
                # life lost
                gb.lives -= 1
                if(gb.lives == 0):
                    gb.gameover = 1
                    gb.overtime = gb.times

                # disable all powerups
                gb.disablepowers(powers, paddle)           

                # reset position of paddle and ball
                self._flag = 0
                self._y = 33
                self._x = 57+random.randint(0,6)
                self._velx = 1
                self._vely = -1
                paddle._y = 34
                paddle._x = 57
                

    def checkcolbricks(self, arr):
        if(self._flag == 1):
            for brick in arr:
                if(brick._vanish == 0):
                    if(self._y + self._vely == brick._y):
                        if((self._x + self._velx >= brick._x) and (self._x + self._velx < brick._x + 7)):
                            # collision
                            if(brick._level == '5'):
                                # explosion
                                gb.explosion(brick,gb.explodingarr)
                                if(gb.thruflag==0):
                                    self._vely = -self._vely

                            else:
                                if(gb.thruflag==0):
                                    # gb.score += 1
                                    self._vely = -self._vely
                                    brick._hits += 1
                                    # maxhits
                                    if(brick._hits == brick._maxhits):
                                        brick._vanish = 1
                                        gb.score += 1

                                        # powerups
                                        if(random.randint(0,100)>50):
                                            a = random.randint(1,3)
                                            if a==1:
                                                pow = powerup.Expand(brick._y,brick._x+3)
                                                gb.poweruparr.append(pow)
                                            if a==2:
                                                pow = powerup.Contract(brick._y,brick._x+3)
                                                gb.poweruparr.append(pow)
                                            if a==3:
                                                pow = powerup.Thru(brick._y,brick._x+3)
                                                gb.poweruparr.append(pow)

                                    if(brick._level == '2'):
                                        brick._level = '1'
                                    if(brick._level == '3'):
                                        brick._level = '2'
                                else:
                                    brick._vanish = 1
                                    gb.score += 1

                            
    def checkcolpaddle(self, paddle):
        if(self._flag == 1):
            if(self._y == 33 and self._vely > 0):
                dist = self._x - paddle._x
                if(dist>=0 and dist<paddle._length):
                    # collision
                    self._vely = -self._vely
                    
                    if(paddle._length == 9):
                        if(dist==0 or dist==1):
                            self._velx += -2
                        if(dist==2 or dist==3):
                            self._velx += -1
                        # if(dist==4):
                        if(dist==5 or dist==6):
                            self._velx += 1
                        if(dist==7 or dist==8):
                            self._velx += 2
                    
                    if(paddle._length == 11):
                        if(dist==0 or dist==1):
                            self._velx += -2
                        if(dist==2 or dist==3):
                            self._velx += -1
                        # if(dist==4/5/6):
                        if(dist==7 or dist==8):
                            self._velx += 1
                        if(dist==9 or dist==10):
                            self._velx += 2
                    
                    if(paddle._length == 7):
                        if(dist==0):
                            self._velx += -2
                        if(dist==1 or dist==2):
                            self._velx += -1
                        # if(dist==3):
                        if(dist==4 or dist==5):
                            self._velx += 1
                        if(dist==6):
                            self._velx += 2


                            
            

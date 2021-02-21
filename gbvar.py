import config
import paddle
import board
import ball 
import brick 
import time
import random

# rows, columns = 36, 122
lives = 3
score = 0
times = 0
gameover = 0
overtime = 0

thruflag = 0

time_start = time.time()

def timeUpdate(ctime):
    return round(ctime - time_start)

board = board.Board()


paddle = paddle.Paddle(34,57)
ball = ball.Ball(33,57+random.randint(0,6))

brickarr = []

brickarr.append(brick.Brick2(21, 61))
brickarr.append(brick.Brick1(21, 68))
brickarr.append(brick.Brick3(21, 75))
brickarr.append(brick.Brick1(20, 63))
brickarr.append(brick.Brick1(19, 65))
brickarr.append(brick.Brick2(18, 67))

brickarr.append(brick.Brick4(17, 69))
brickarr.append(brick.Brick4(17, 62))
brickarr.append(brick.Brick1(16, 71))
brickarr.append(brick.Brick1(15, 73))
brickarr.append(brick.Brick1(14, 75))
brickarr.append(brick.Brick2(14, 82))
brickarr.append(brick.Brick3(14, 89))

brickarr.append(brick.Brick1(21, 82))
brickarr.append(brick.Brick1(20, 84))
brickarr.append(brick.Brick1(19, 86))
brickarr.append(brick.Brick1(18, 88))
brickarr.append(brick.Brick1(17, 90))
brickarr.append(brick.Brick1(16, 92))
brickarr.append(brick.Brick1(15, 94))
brickarr.append(brick.Brick1(14, 96))


explodingarr = []
e1 = brick.ExBrick(20,70,0)
brickarr.append(brick.Brick2(20, 77))
brickarr.append(e1)
explodingarr.append(e1)
e2 = brick.ExBrick(19,72,0)
brickarr.append(brick.Brick2(19, 79))
brickarr.append(e2)
explodingarr.append(e2)
e3 = brick.ExBrick(18,74,0)
brickarr.append(brick.Brick2(18, 81))
brickarr.append(e3)
explodingarr.append(e3)
e4 = brick.ExBrick(17,76,0)
brickarr.append(brick.Brick2(17, 83))
brickarr.append(e4)
explodingarr.append(e4)
e5 = brick.ExBrick(16,78,0)
brickarr.append(brick.Brick2(16, 85))
brickarr.append(e5)
explodingarr.append(e5)
e6 = brick.ExBrick(15,80,0)
brickarr.append(brick.Brick2(15, 87))
brickarr.append(e6)
explodingarr.append(e6)

brickarr.append(brick.Brick2(21, 54))
brickarr.append(brick.Brick1(21, 47))
brickarr.append(brick.Brick3(21, 40))
brickarr.append(brick.Brick1(20, 52))
brickarr.append(brick.Brick1(19, 50))
brickarr.append(brick.Brick2(18, 48))

brickarr.append(brick.Brick4(17, 46))
brickarr.append(brick.Brick4(17, 53))
brickarr.append(brick.Brick1(16, 44))
brickarr.append(brick.Brick1(15, 42))
brickarr.append(brick.Brick1(14, 40))
brickarr.append(brick.Brick2(14, 33))
brickarr.append(brick.Brick3(14, 26))

brickarr.append(brick.Brick1(21, 33))
brickarr.append(brick.Brick1(20, 31))
brickarr.append(brick.Brick1(19, 29))
brickarr.append(brick.Brick1(18, 27))
brickarr.append(brick.Brick1(17, 25))
brickarr.append(brick.Brick1(16, 23))
brickarr.append(brick.Brick1(15, 21))
brickarr.append(brick.Brick1(14, 19))

e7 = brick.ExBrick(20,45,1)
brickarr.append(brick.Brick2(20, 38))
brickarr.append(e7)
explodingarr.append(e7)
e2 = brick.ExBrick(19,43,1)
brickarr.append(brick.Brick2(19, 36))
brickarr.append(e2)
explodingarr.append(e2)
e3 = brick.ExBrick(18,41,1)
brickarr.append(brick.Brick2(18, 34))
brickarr.append(e3)
explodingarr.append(e3)
e4 = brick.ExBrick(17,39,1)
brickarr.append(brick.Brick2(17, 32))
brickarr.append(e4)
explodingarr.append(e4)
e5 = brick.ExBrick(16,37,1)
brickarr.append(brick.Brick2(16, 30))
brickarr.append(e5)
explodingarr.append(e5)
e6 = brick.ExBrick(15,35,1)
brickarr.append(brick.Brick2(15, 28))
brickarr.append(e6)
explodingarr.append(e6)

poweruparr = []


def checkpowercol(power, paddle):
    if(power._state == 0):
        if(power._y == 32 or power._y == 33):
            dist = power._x - paddle._x
            if(dist>=0 and dist<paddle._length + 1):
                # collect powerup 
                power._state = 1
                power.activate(paddle)
                power._starttime = time.time()
            else:
                power._state = 3

def checkpowertime(power, paddle):
    if(power._state == 1):
        if(time.time() - power._starttime > 10.0):
            power.deactivate(paddle)
            power._state = 2
            
def disablepowers(powers, paddle):
    for power in powers:
        if(power._state == 1):
            power.deactivate(paddle)
            power._state = 2

def explosion(ogbrick, explodingarr):
    global score
    for exbrick in explodingarr:
        if(exbrick._cluster == ogbrick._cluster):
            exbrick._vanish = 1
            score += 1
            
            # looping through each neighborring point
            for x in range(exbrick._x-1,exbrick._x+8):
                y = exbrick._y-1
                for brick in brickarr:
                    if(brick._vanish == 0 and brick._level != '5'):
                        if(brick._y == y):
                            if(x>=brick._x and x<brick._x + 7):
                                # explode normal brick
                                brick._vanish = 1
                                score += 1
            for x in range(exbrick._x-1,exbrick._x+8):
                y = exbrick._y+1
                for brick in brickarr:
                    if(brick._vanish == 0 and brick._level != '5'):
                        if(brick._y == y):
                            if(x>=brick._x and x<brick._x + 7):
                                # explode normal brick
                                brick._vanish = 1
                                score += 1

            x = exbrick._x-1
            y = exbrick._y
            for brick in brickarr:
                if(brick._vanish == 0 and brick._level != '5'):
                    if(brick._y == y):
                        if(x>=brick._x and x<brick._x + 7):
                            # explode normal brick
                            brick._vanish = 1
                            score += 1   

            x = exbrick._x+7
            y = exbrick._y
            for brick in brickarr:
                if(brick._vanish == 0 and brick._level != '5'):
                    if(brick._y == y):
                        if(x>=brick._x and x<brick._x + 7):
                            # explode normal brick
                            brick._vanish = 1
                            score += 1       
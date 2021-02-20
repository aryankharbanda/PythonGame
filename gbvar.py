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

time_start = time.time()

def timeUpdate(ctime):
    return round(ctime - time_start)

board = board.Board()


paddle = paddle.Paddle(34,57)
ball = ball.Ball(33,57+random.randint(0,6))


# flag = 0

brickarr = []
brickarr.append(brick.Brick1(10, 80, 2))
brickarr.append(brick.Brick1(10, 1, 0))
brickarr.append(brick.Brick1(14, 90, 0))
brickarr.append(brick.Brick1(18, 50, 0))
brickarr.append(brick.Brick1(16, 70, 0))
brickarr.append(brick.Brick2(10, 24, 0))
brickarr.append(brick.Brick3(14, 60, 0))
# brickarr.append(brick.Brick4(14, 11, 0))
brickarr.append(brick.Brick1(21, 61, 0))
brickarr.append(brick.Brick1(20, 63, 0))
brickarr.append(brick.Brick1(19, 65, 0))
brickarr.append(brick.Brick2(18, 67, 0))
brickarr.append(brick.Brick4(17, 69, 0))
brickarr.append(brick.Brick4(17, 62, 0))

explodingarr = []
e1 = brick.ExBrick(20,70,0,0)
brickarr.append(e1)
explodingarr.append(e1)
e2 = brick.ExBrick(19,72,0,0)
brickarr.append(e2)
explodingarr.append(e2)
e3 = brick.ExBrick(18,74,0,0)
brickarr.append(e3)
explodingarr.append(e3)
e4 = brick.ExBrick(10,74,0,1)
brickarr.append(e4)
explodingarr.append(e4)

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
import input
import config
import gbvar as gb
# import paddle
# import board
import subprocess
import time
import sys

if __name__ == "__main__":

    while(1):
        # clear screen
        gb.board.clearPaddle(gb.paddle)
        gb.board.clearBall(gb.ball)
        gb.board.clearBricks(gb.brickarr)
        gb.board.clearPowers(gb.poweruparr)

        # input
        obj = input.Get()
        inp = input.input_to(obj)

        if(inp=='q' or inp=='Q'):
            break

        if(inp=='a' or inp=='A'):
            gb.paddle.moveleft(gb.ball)
            # gb.ball.moveleft()

        if(inp=='d' or inp=='D'):
            gb.paddle.moveright(gb.ball)
            # gb.ball.moveright()

        if(inp=='w' or inp=='W'):
            gb.ball.shoot()


        # time update
        gb.times = gb.timeUpdate(time.time())

        # update screen
        gb.ball.move()
        gb.ball.checkcolwall(gb.paddle,gb.poweruparr)
        gb.ball.checkcolbricks(gb.brickarr)
        gb.ball.checkcolpaddle(gb.paddle)
        for power in gb.poweruparr:
            power.move()
            gb.checkpowercol(power,gb.paddle)
            gb.checkpowertime(power,gb.paddle)

        # print screen
        subprocess.call("clear")
        
        gb.board.renderPowers(gb.poweruparr)
        gb.board.renderBricks(gb.brickarr)
        gb.board.renderPaddle(gb.paddle)
        gb.board.renderBall(gb.ball)
        gb.board.renderGrid()
        
        time.sleep(.1)
        print(gb.thruflag)

        
        
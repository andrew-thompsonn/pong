from pong_window import*
from random import randrange


class PongEngine:


    def __init__(self, pongWindow):
        self.paddleMoveDist = CURSOR_SIZE
        self.ballXVelocity = 10*self.getStartDirection()
        self.ballYVelocity = randrange(4)*self.getStartDirection()
        self.window = pongWindow
        self.window.screen.listen()
        self.window.screen.onkeypress(self.movePlayerPaddleUp, "Up")
        self.window.screen.onkeypress(self.movePlayerPaddleDown, "Down")
        self.playerScore = 0
        self.computerScore = 0
        self.run()



    def getStartDirection(self):
        number = randrange(10)
        if number > 4.5:
            direction = -1
        else:
            direction = 1
        return direction



    def run(self):
        while True:
            self.moveBall()
            if self.ballXVelocity > 0:
                self.moveComputerPaddle()
            self.window.screen.update()
            self.checkPoint()



    def moveComputerPaddle(self):
        paddleY = self.window.getComputePaddleCoordinates()
        paddleTop = paddleY + 3*CURSOR_SIZE + 5
        paddleBot = paddleY - 3*CURSOR_SIZE - 5
        xCoord, yCoord = self.window.getBallCoordinates()
        if yCoord > paddleTop:
            self.window.moveComputerPaddle(self.paddleMoveDist)
        elif yCoord < paddleBot:
            self.window.moveComputerPaddle(-self.paddleMoveDist)



    def movePlayerPaddleUp(self):
        deltaY = self.paddleMoveDist
        if self.paddleMoveValid(deltaY):
            self.window.movePlayerPaddle(deltaY)



    def movePlayerPaddleDown(self):
        deltaY = -self.paddleMoveDist
        if self.paddleMoveValid(deltaY):
            self.window.movePlayerPaddle(deltaY)



    def paddleMoveValid(self, deltaY):
        currentYCoord = self.window.getPlayerPaddleCoordinates()
        maxCoordinate = SCREEN_HEIGHT/2 if deltaY > 0 else -SCREEN_HEIGHT/2
        if deltaY < 0:
            deltaY -= 3*CURSOR_SIZE - 10
            return True if currentYCoord + deltaY > maxCoordinate else False
        elif deltaY > 0:
            deltaY += 3*CURSOR_SIZE - 10
            return True if currentYCoord + deltaY < maxCoordinate else False


    def moveBall(self):
        xCoord, yCoord = self.window.getBallCoordinates()
        self.window.ball.goto(xCoord + self.ballXVelocity, yCoord + self.ballYVelocity)
        collisionOccurred, deltaYVelocity = self.checkPaddleCollision()
        self.ballYVelocity += deltaYVelocity
        if collisionOccurred:
            self.ballXVelocity *= -1
        elif self.checkBoundaryCollision():
            self.ballYVelocity *= -1



    def checkPaddleCollision(self):
        if self.ballXVelocity < 0:
            paddleY = self.window.getPlayerPaddleCoordinates()
        else:
            paddleY = self.window.getComputePaddleCoordinates()
        paddleTop = paddleY + 3*CURSOR_SIZE + 10
        paddleBot = paddleY - 3*CURSOR_SIZE - 10
        xCoord, yCoord = self.window.getBallCoordinates()
        inFront = paddleBot < yCoord < paddleTop
        touching = 400 - CURSOR_SIZE < abs(xCoord) < 400
        collisionOccurred = True if touching and inFront else False
        if collisionOccurred:
            ballPadPosition = yCoord - paddleY
            english = int(ballPadPosition/10)
        else:
            english = 0
        return collisionOccurred, english


    def checkBoundaryCollision(self):
        xCoord, yCoord = self.window.getBallCoordinates()
        if SCREEN_HEIGHT/2 - abs(yCoord) <= CURSOR_SIZE + 10:
            return True
        else:
            return False



    def checkPoint(self):
        score = False
        xCoord, yCoord = self.window.getBallCoordinates()
        if xCoord < -450:
            self.computerScore += 1
            score = True
            # self.window.showMessage()
        elif xCoord > 450:
            self.playerScore += 1
            score = True
        if score:
            self.updateScoreBoard()
            self.resetBall()



    def updateScoreBoard(self):
        self.window.scoreBoard.clear()
        self.window.scoreBoard.write("{}\t{}".format(self.playerScore, self.computerScore),
                                     align="center", font=("Courier", 38))


    def resetBall(self):
        self.window.ball.color("black")
        self.window.ball.goto(0, 0)
        self.window.ball.color("white")
        self.ballXVelocity = -8
        self.ballYVelocity = randrange(6)



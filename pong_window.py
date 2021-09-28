import turtle
import time

CURSOR_SIZE     = (20)
SCREEN_WIDTH    = (1000)
SCREEN_HEIGHT   = (600)


class PongWindow:

    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 600
        self.initScreen()
        self.initPaddles()
        self.initBall()
        self.initScoreBoard()
        self.drawSquare()
        self.drawTitle()


    def initScreen(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=self.WIDTH, height=self.HEIGHT)


    def initPaddles(self):
        self.playerPaddle = turtle.Turtle()
        self.computerPaddle = turtle.Turtle()
        self.initPaddle(self.playerPaddle, -400, 0)
        self.initPaddle(self.computerPaddle, 400, 0)


    def initPaddle(self, paddle, xCoord, yCoord):
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=6, stretch_len=1)
        paddle.penup()
        paddle.goto(xCoord, yCoord)


    def initBall(self):
        self.ball = turtle.Turtle()
        self.ball.speed(4)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)


    def initScoreBoard(self):
        self.scoreBoard = turtle.Turtle()
        self.scoreBoard.speed(0)
        self.scoreBoard.color("white")
        self.scoreBoard.penup()
        self.scoreBoard.hideturtle()
        self.scoreBoard.goto(0, 220)
        self.scoreBoard.write("0\t0", align="center", font=("Courier", 38))


    def getBallCoordinates(self):
        currentYCoord = self.ball.ycor()
        currentXCoord = self.ball.xcor()
        return currentXCoord, currentYCoord


    def getPlayerPaddleCoordinates(self):
        currentYCoord = self.playerPaddle.ycor()
        return currentYCoord


    def getComputePaddleCoordinates(self):
        currentYCoord = self.computerPaddle.ycor()
        return currentYCoord


    def movePlayerPaddle(self, distance):
        currentYCoord = self.playerPaddle.ycor()
        updatedYCoord = currentYCoord + distance
        self.playerPaddle.sety(updatedYCoord)


    def moveComputerPaddle(self, distance):
        currentYCoord = self.computerPaddle.ycor()
        updatedYCoord = currentYCoord + distance
        self.computerPaddle.sety(updatedYCoord)


    def drawSquare(self):
        square = turtle.Turtle()
        square.hideturtle()
        square.speed("fast")
        square.color("white")
        square.left(90)
        square.forward(SCREEN_HEIGHT/2 - CURSOR_SIZE/2)
        square.backward(SCREEN_HEIGHT - CURSOR_SIZE - 10)
        square.left(90)
        square.forward(450)
        square.right(90)
        square.forward(SCREEN_HEIGHT - CURSOR_SIZE - 10)
        square.right(90)
        square.forward(900)
        square.right(90)
        square.forward(SCREEN_HEIGHT - CURSOR_SIZE - 10)
        square.right(90)
        square.forward(450)


    def drawTitle(self):
        self.title = turtle.Turtle()
        self.title.speed(0)
        self.title.color("white")
        self.title.penup()
        self.title.hideturtle()
        self.title.goto(-280, -280)
        self.title.write("P  O  N  G", font=("Courier", 24))


    def showMessage(self):
        self.message = turtle.Turtle()
        self.message.speed(0)
        self.message.color("white")
        self.message.penup()
        self.message.hideturtle()
        self.message.goto(280, -150)
        self.message.write("Get fkn rekt", font=("Courier", 8))

        self.message.write("", font=("Courier", 8))

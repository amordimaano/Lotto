# File: lotto_chee_dimaano_envase.py
# References: Python (Zelle)
# Programmers: Rosalie Chee; Amor Dimaano; Jonathan Envase
# Special thanks to Emerson Escolar for his invaluable help in
# debugging the program.

from random import*
from graphics import*
from math import*
from time import sleep
from string import*

class Button:
    def __init__(self, win, center, width, height, label):
        w = width/2.0
        h = height/2.0
        x = center.getX()
        y = center.getY()
        self.xmax = x+w
        self.xmin = x-w
        self.ymax = y+h
        self.ymin = y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(16)
        self.label.draw(win)
        self.deactivate()
    def clicked(self, p):
        return self.active and \
            self.xmin <= p.getX() <= self.xmax and \
            self.ymin <= p.getY() <= self.ymax
    def getLabel(self):
        return self.label.getText()
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
    def undraw(self):
        self.label.undraw()
        self.rect.undraw()


class ball:
    def __init__(self,win,center,radius,label,size,style,color):
        self.ball = Circle(center,radius)
        self.ball.setFill(color)
        self.number = Text(center,label)
        self.number.setSize(size)
        self.number.setStyle(style)
        self.ball.draw(win)
        self.number.draw(win)
        self.dx = 1
        self.dy = 0
        self.state = 0
    def ballmove(self,ballList,winList):
        center = self.ball.getCenter()
        x = center.getX()
        y = center.getY()
        if 355<x<415 and y<=455:
            self.ballremove(ballList,winList)
        if x==65:
            self.dy = randrange(1,5,1)
        if x<65:
          self.dx = 1
        if y<=455:
            self.dy = randrange(1,5,1)
        if y>=685:
            self.dy = -(randrange(1,4,1))
        if x>65:
            if x==65:
                self.dx = 1
            if y==455:
                self.dy = 1
            if x==705:
                self.dx = -(randrange(1,6,1))
            if y==685:
                self.dy = -(randrange(1,4,1))
        self.ball.move(self.dx,self.dy)
        self.number.move(self.dx,self.dy)
    def ballremove(self,ballList,winList):
        center = self.ball.getCenter()
        x = center.getX()
        y = center.getY()
        if x==385 and y>367:
            self.dx = 0
            self.dy = 367 - y
        if x<385 and y>367:
            self.dx = 385 - x
            self.dy = 367 - y
        if x>385 and y>367:
            self.dx = 385 - x
            self.dy = 367 - y
        self.ball.move(self.dx,self.dy)
        self.number.move(self.dx,self.dy)
        center = self.ball.getCenter()
        x = center.getX()
        y = center.getY()
        if x==385 and y==367:
            if len(ballList)==42:
                self.dx = -73
            if len(ballList)==41:
                self.dx = -43
            if len(ballList)==40:
                self.dx = -15
            if len(ballList)==39:
                self.dx = 17
            if len(ballList)==38:
                self.dx = 47
            if len(ballList)<=37:
                self.dx = 77
            self.dy = 0
        self.ball.move(self.dx,self.dy)
        self.number.move(self.dx,self.dy)
        ballList.remove(self)
        winList.append(self.number.getText())
        return ballList,winList

def drawWin(win):
    # Draw Window Separator
    vertical = Line(Point(770,0),Point(770,738))
    vertical.draw(win)
    combinations = Rectangle(Point(770,300),Point(1275,733))
    combinations.draw(win)
    winnings = Rectangle(Point(770,0),Point(1275,300))
    winnings.draw(win)
    # Draw Title
    lottowinners = Image(Point(385,230),'LottoWinners.gif')
    lottowinners.draw(win)
    # Draw Lotto Part
    ballcontainerdown = Line(Point(0,650),Point(50,650))
    ballcontainerdown.draw(win)
    boxtop = Line(Point(0,700),Point(720,700))
    boxtop.draw(win)
    boxleft = Line(Point(50,440),Point(50,650))
    boxleft.draw(win)
    boxright = Line(Point(720,440),Point(720,700))
    boxright.draw(win)
    boxdownleft = Line(Point(50,440),Point(355,440))
    boxdownleft.draw(win)
    boxdownright = Line(Point(415,440),Point(720,440))
    boxdownright.draw(win)
    balldropleft = Line(Point(355,390),Point(355,440))
    balldropleft.draw(win)
    balldropright = Line(Point(415,390),Point(415,440))
    balldropright.draw(win)
    combinationupleft = Line(Point(205,390),Point(355,390))
    combinationupleft.draw(win)
    combinationupright = Line(Point(415,390),Point(565,390))
    combinationupright.draw(win)
    combinationleft = Line(Point(205,345),Point(205,390))
    combinationleft.draw(win)
    combinationright = Line(Point(565,345),Point(565,390))
    combinationright.draw(win)
    combinationdown = Line(Point(205,345),Point(565,345))
    combinationdown.draw(win)    
    # Draw Winnings Part
    won = Text(Point(1085,250),'You WON')
    won.setStyle('bold')
    won.setSize(36)
    won.setFace('courier')
    won.draw(win)
    hollywoodlotto = Image(Point(850,225),'hollywoodlotto.gif')
    hollywoodlotto.draw(win)
    withnums = Text(Point(1022.5,135),"with the numbers")
    withnums.setStyle('bold')
    withnums.setSize(25)
    withnums.setFace('courier')
    withnums.draw(win)
    # Draw Numver Combination Part
    jackpot = Image(Point(900,595),'hitting the jackpot.gif')
    jackpot.draw(win)
    php = Text(Point(1100,625),"Php")
    php.setSize(30)
    php.setStyle('bold')
    php.setTextColor('blue')
    php.draw(win)
    prize = Text(Point(1100,553),"25,000,000")
    prize.setStyle('bold')
    prize.setSize(30)
    prize.draw(win)
    wcombination = Text(Point(1022.5,445),"winning combination")
    wcombination.setStyle('bold')
    wcombination.setSize(25)
    wcombination.setFace('courier')
    wcombination.draw(win)

def main():
    # Draw Window
    win = GraphWin("Lotto 6/42",1260,730)
    win.setCoords(0,0,1260,730)
    win.setBackground('white')
    # Draw Close Button
    close = Button(win,Point(50,20),75,30,"exit")
    close.activate()
    # Draw 1st Window View
    islandsspill = Image(Point(630,365),'islandsspill.gif')
    islandsspill.draw(win)
    playhere = Button(win,Point(630,100),100,50,"Play Here")
    playhere.activate()
    p = win.getMouse()
    if close.clicked(p):
        win.close()
    if playhere.clicked(p):
        islandsspill.undraw()
        playhere.undraw()
        # Draw Window Components
        drawWin(win)
        # Draw Start Simulation Button
        startdraw = Button(win,Point(385,35),135,33,"Start Draw")
        # Draw User Number Entry
        numbers = Entry(Point(385,80),20)
        numbers.setText("")
        numbers.draw(win)
        # Draw Balls
        ballList = []
        for i in range(42):
            ballList.append(ball(win,Point(25,675),15,i+1,16,"bold","orange"))
        if close.clicked(win.getMouse()):
            win.close()
        # Get User Number Input
        t = 0
        while t==0:
            if numbers.getText()!="":
                startdraw.activate()
                pt = win.getMouse()
                while startdraw.clicked(pt):
                    numberuserball = []
                    for i in split(numbers.getText(),','):
                        numberuserball.append(i)
                    if len(numberuserball)==6:
                        t = 1
                    else:
                        t = 0
                    break
        # Draw Numbers Chosen to Box
        while t==1:
            if len(numberuserball)==6:
                userball = []
                ballcheck = []
                x = 864
                y = 74
                for i in split(numbers.getText(),','):
                    userball.append(ball(win,Point(x,y),31,i,32,"bold","white"))
                    ballcheck.append(eval(i))
                    x = x + 62
                t = 2
        # Start Simulation
        winList = []
        winNum = []
        x = 864
        y = 395
        while t==2:
            for i in ballList:
                i.ballmove(ballList,winList)
                # Draw Winning Combination to Conbination Box
                if ballList.count(i)==0:
                    winNum.append(ball(win,Point(x,y),31,i.number.getText(),32,"bold","yellow"))
                    x = x + 62
                if len(ballList)<=36:
                    t = 3
                else :
                    t = 2
        # Calculate Winnings
        num = 0
        for i in ballcheck:
            if winList.count(i)==1:
                num = num + 1
            else:
                num = num
        if num==6:
            jackpot = Text(Point(1085,200),"THE JACKPOT PRIZE OF")
            jackpot.setSize(20)
            jackpot.draw(win)
            jackpot2 = Text(Point(1085,175),"25,000,000")
            jackpot2.setStyle('bold')
            jackpot2.setTextColor('red')
            jackpot2.setSize(25)
            jackpot2.draw(win)
        elif num==5:
            num5 = Text(Point(1085,200),'20,000')
            num5.setSize(20)
            num5.setStyle('bold')
            num5.setTextColor('red')
            num5.draw(win)
        elif num==4:
            num4 = Text(Point(1085,200),'600')
            num4.setSize(20)
            num4.setStyle('bold')
            num4.setTextColor('red')
            num4.draw(win)
        elif num==3:
            num3 = Text(Point(1085,200),'20')
            num3.setSize(20)
            num3.setStyle('bold')
            num3.setTextColor('red')
            num3.draw(win)
        else:
            nothing = Text(Point(1085,200),'0 Php')
            nothing.setSize(20)
            nothing.setStyle('bold')
            nothing.setTextColor('red')
            nothing.draw(win)
        if close.clicked(win.getMouse()):
            win.close()
            
main()


# Works Cited:
#   Islandsspil [Magician's hat with Lotto text]. Digital image. Betware. Certus. 30 Sept. 2008 <http://www.betware.com/clients-and-partners/clients/>.
#   Loh, Christopher. Hitting the Jackpot [Man in front of slot machine]. Digital image. I've been thinking...:Newton TAB Blog. 30 Mar. 2007. Wicked Local TM. 30 Sept. 2008 <http://blogs.townonline.com/newton/?p=3362>.
#   Lotto Logo [Lottery balls with LOTTO text]. Digital image. Image Library. 30 Sept. 2008 <http://www.mylotto.co.nz/wps/wcm/myconnect/lotteries2/nzlotteries/global/news/mediakit/imagelibrary/>.
#   Mike. Hollywood Lotto [Hand with cash]. Digital image. Mike's Lookout. 31 Jan. 2007. 30 Sept. 2008 <http://www.belshe.com/2007/01/>.

import pygame
from network import Network
# from testPlayer import Player
from Player import Player
import mySQLconnect
import math
import mysql.connector
pygame.init()


screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Bubble Poppers")

#  test variables for how big I want the screen, character movement, proj speed
clock = pygame.time.Clock()
x_p = 100
yP = 100
widthP = 50
heightP = 50
starttime = pygame.time.get_ticks()
pSpeed = 3
aSpeed = 6
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
timer = 120


class Player(object):
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.radius = rad
        self.color = color
        self.speed = pSpeed
        self.hitbox = (self.x - 15, self.y - 15, 25, 25)
        self.health = 100
        self.win = False

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 1)

    def drawHitbox(self, screen):
        pygame.draw.rect(screen, blue, self.hitbox)


character1 = Player(100, 100, 25, blue)
character2 = Player(400, 400, 25, red)




def connectdb():
    mydb = mysql.connector.connect(host="localhost", user="root", password='', database="mydb")
    UserID = 1
    Wins = 1
    mycursor1 = mydb.cursor()

    mycursor2 = mydb.cursor()

    mycursor1.execute("SELECT Wins FROM Account WHERE UserID = '1'")

    myresult = mycursor1.fetchall()

    for x in myresult:
        Wins = x[0]

    Wins += 1
    Wins = str(Wins)
    sql = "UPDATE account SET Wins = " + Wins + "WHERE UserID = '1'"

    mycursor2.execute(sql)

    mydb.commit()


class Bubble:
    def __init__(self, x, y):
        self.pos = (x, y)
        bx, by = pygame.mouse.get_pos()
        self.d = (bx - x, by - y)
        length = math.hypot(*self.d)
        if length == 0.0:
            self.d = (0, -1)
        else:
            self.d = (self.d[0]/length, self.d[1]/length)
        angle = math.degrees(math.atan2(-self.d[1], self.d[0]))

        self.bubble = pygame.Surface((7, 2)).convert_alpha()
        self.bubble.fill(white)
        self.bubble = pygame.transform.rotate(self.bubble, angle)
        self.speed = aSpeed
        self.radius = 7

    def update(self):
        self.pos = (self.pos[0]+self.d[0]*self.speed, self.pos[1]+self.d[1]*self.speed)

    def draw(self, surf):
        bubble = self.bubble.get_rect(center=self.pos)
        surf.blit(self.bubble, bubble)


bubbles1 = []
bubbles2 = []


def win_check():
    if character1.win:
        return print("Character One Wins! (RED)")
    if character2.win:
        return print("Character Two Wins! (BLUE)")


def redrawWindow(screen, character1, character2, bubbles1, bubbles2):

    linePos1 = pygame.mouse.get_pos()
    line1 = [(character1.x, character1.y), linePos1]
    screen.fill(black)
    character1.draw(screen)
    character2.draw(screen)

    for bubble in bubbles1:
        bubble.draw(screen)
    for bubble in bubbles2:
        bubble.draw(screen)
    pygame.draw.line(screen, white, line1[0], line1[1])
    pygame.display.flip()
    pygame.display.update()
    character2.drawHitbox(screen)




class Game:
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    reloadSecond = 0.0
    reload_timer = 0.0
    reload = False


    while run:
        clock.tick(60)
        p2 = n.send(p)
        clock.tick(60)
        seconds = (pygame.time.get_ticks() - starttime) / 1000

        linePos1 = pygame.mouse.get_pos()
      #  line1 = [(character1.x, character1.y), linePos1]

        p.move()
        character1.pos = (character1.x, character1.y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bubble in bubbles1[:]:
            bubble.update()
            if not screen.get_rect().collidepoint(bubble.pos):
                bubbles1.remove(bubble)
            # hitbox check
            if bubble.pos[1] - bubble.radius < character2.hitbox[1] \
                    + character2.hitbox[3] and bubble.pos[1] + bubble.radius > character2.hitbox[1]:

                if bubble.pos[0] + bubble.radius > character2.hitbox[0] and bubble.pos[0] \
                        - bubble.radius < character2.hitbox[0] + character2.hitbox[2]:
                    character2.health -= 50
                    bubbles1.pop(bubbles1.index(bubble))
                    if character2.health <= 0:
                        run = False
                        character1.win = True
                        print("Winner!")

        for bubble in bubbles2[:]:
            bubble.update()
            if not screen.get_rect().collidepoint(bubble.pos):
                bubbles2.remove(bubble)
            # hitbox check
            if bubble.pos[1] - bubble.radius < character1.hitbox[1] \
                    + character1.hitbox[3] and bubble.pos[1] + bubble.radius > character1.hitbox[1]:

                if bubble.pos[0] + bubble.radius > character1.hitbox[0] and bubble.pos[0] \
                        - bubble.radius < character1.hitbox[0] + character1.hitbox[2]:
                    character1.health -= 50
                    bubbles1.pop(bubbles1.index(bubble))
                    if character1.health <= 0:
                        run = False
                        character2.win = True
                        print("Winner!")



        linePos1 = pygame.mouse.get_pos()
        line1 = [(character1.x, character1.y), linePos1]
        pos = (character1.x, character1.y)



        if event.type == pygame.MOUSEBUTTONDOWN and reload is False:
            bubbles1.append(Bubble(*pos))





            reload = True

            reload_timer = seconds + 0.2

        action = pygame.key.get_pressed()
        if action[pygame.K_d] and character1.x + character1.speed < 500:
            character1.x += character1.speed

        if action[pygame.K_a] and character1.x - character1.speed > 0:
            character1.x -= character1.speed

        if action[pygame.K_w] and character1.y - character1.speed > 0:
            character1.y -= character1.speed

        if action[pygame.K_s] and character1.y + character1.speed < 500:
            character1.y += character1.speed

        if event.type == pygame.MOUSEBUTTONDOWN and reload is True:
            if seconds <= reload_timer:
                # nothing happens
                nothing = 1

            elif reload_timer - seconds <= 0:
                reload = False
        for bubble in bubbles1:
            if bubble.pos == (character2.x, character2.y):
                run = False
        for bubble in bubbles2:
            if bubble.pos == (character1.x, character1.y):
                run = False

        redrawWindow(screen, p, p2, bubbles1, bubbles2)
    pygame.quit()
    win_check()
    tDatabaseConnect = True
    asdf = 1

    while tDatabaseConnect and asdf > 0:
        try:
            connectdb()
            if asdf == 1:
                asdf = asdf - 1



        except:
            break


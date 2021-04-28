import pygame
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
assignedColor = 0


class Player(object):
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.pos = 0, 0
        self.radius = rad
        self.color = color
        self.speed = pSpeed
        self.hitbox = (self.x - 15, self.y - 15, 25, 25)
        self.health = 100
        self.win = False
        self.circle = (x, y, rad, color)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 1)

    def drawHitbox(self, screen):
        pygame.draw.rect(screen, blue, self.hitbox)

    def move(self):
            action = pygame.key.get_pressed()

            if action[pygame.K_d] and self.x + self.speed < 500:
                self.x += self.speed

            if action[pygame.K_a] and self.x - self.speed > 0:
                self.x -= self.speed

            if action[pygame.K_w] and self.y - self.speed > 0:
                self.y -= self.speed

            if action[pygame.K_s] and self.y + self.speed < 500:
                self.y += self.speed
            self.update()

    def update(self):
        self.circle = (self.x, self.y, self.radius, blue)
        self.pos = (self.x, self.y)










import pygame
import pygame.display
import random
import pygame.draw
import pygame.event


WIDTH = 800
HEIGHT = 600

class Snake():
    def __init__(self):
        self.width = 30
        self.height = 30
        self.headPosX = WIDTH/2
        self.headPosY = HEIGHT/2
        self.bodies = []
        self.dir = ""
        self.speed = 0.2
    def draw(self,surface):
        pygame.draw.rect(surface,"green",(self.headPosX,self.headPosY,self.width,self.height))
        if len(self.bodies)>0:
            for body in self.bodies:
                body.draw(surface)
    def moveHead(self):
        if self.dir == "UP":
            self.headPosY -= self.speed
        if self.dir == "DOWN":
            self.headPosY += self.speed
        if self.dir == "LEFT":
            self.headPosX -= self.speed
        if self.dir == "RIGHT":
            self.headPosX += self.speed
    def moveBody(self):
        if len(self.bodies)>0:
            for i in range(len(self.bodies)-1,-1,-1):
                if i == 0:
                    self.bodies[0].posX = self.headPosX
                    self.bodies[0].posY = self.headPosY
                else:
                    self.bodies[i].posX = self.bodies[i-1].posX
                    self.bodies[i].posY = self.bodies[i-1].posY
    def addBody(self):
        body = Body(self.headPosX,self.headPosY)
        self.bodies.append(body)



class Body():
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.width = 30
        self.height = 30
    def draw(self,surface):
        pygame.draw.rect(surface,"green",(self.posX,self.posY,self.width,self.height))



class Food():
    def __init__(self):
        self.width = 20
        self.height = 20
        self.posX = random.randint(0,WIDTH-self.width)
        self.posY = random.randint(0,HEIGHT-self.height)
    def draw(self,surface):
        pygame.draw.rect(surface,"red",(self.posX,self.posY,self.width,self.height))




def main():
    pygame.init()
    run = True
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    snake = Snake()
    food = Food()
    

    while run == True:
        snake.draw(window)
        food.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if snake.dir != "DOWN":
                        snake.dir = "UP"
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if snake.dir != "UP":
                        snake.dir = "DOWN"
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if snake.dir != "RIGHT":
                        snake.dir = "LEFT"
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if snake.dir != "LEFT":
                        snake.dir = "RIGHT"

        if snake.headPosX <=0 or snake.headPosX >= WIDTH-snake.width:
            run = False
        if snake.headPosY <=0 or snake.headPosY >= HEIGHT-snake.height:
            run = False

        snakeRect = pygame.Rect(snake.headPosX,snake.headPosY,snake.width,snake.height)
        foodRect = pygame.Rect(food.posX,food.posY,food.width,food.height)

        if pygame.Rect.colliderect(snakeRect,foodRect):
            food.posX = random.randint(0,WIDTH-food.width)
            food.posY = random.randint(0,HEIGHT-food.height)

        snake.moveBody()
        snake.moveHead()

        pygame.display.update()
        window.fill("black")



main()
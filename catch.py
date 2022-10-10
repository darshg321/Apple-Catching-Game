import random, pygame, os
from tkinter import CENTER
from tokenize import Triple
from turtle import screensize
pygame.init()

fps = pygame.time.Clock()

pygame.display.set_caption('Catch!')
screen = pygame.display.set_mode([1280, 720])

WHITE = (255, 255, 255)

score = 0

class Plate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('catch\images', 'plate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 640
        self.y = 600

        
    def collision(self):
        collided = pygame.sprite.spritecollide(plate, apples, False)
        print(apple.rect.y)
        print(self.rect.x)
        if collided:
            global score
            score += 1
            apple.y = 50
            apple.x = random.randrange(0, 1220)
            
            collided = None
            
            
    def handling(self):
        self.rect.y = self.y
        self.rect.x = self.x
        
        key = pygame.key.get_pressed()
        dist = 15
        if key[pygame.K_RIGHT] and self.x < 1185:
            self.x += dist
        elif key[pygame.K_LEFT] and self.x > 0:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

plate = Plate()

apple_x = 640
apple_y = 50

class Apple(pygame.sprite.Sprite):
    def __init__(self, vel):
        super().__init__()
        self.image = pygame.image.load(os.path.join('catch\images', 'apple.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = apple_x
        self.y = apple_y
        self.vel = vel
        
    def update(self):
        if start == True:
            self.y += self.vel
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

fall_speed = 6
apple = Apple(fall_speed)

all_sprites = pygame.sprite.Group()
all_sprites.add(plate)
all_sprites.add(apple)

apples = pygame.sprite.Group()
apples.add(apple)

start_button = pygame.image.load(os.path.join('catch\images', 'start.png')).convert_alpha()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft =  (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        position = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
start_btn = Button(500, 360, start_button, 2)

pygame.font.init()
font = pygame.font.SysFont('Futura', 75)


start = False

while True:
    screen.fill((21, 128, 209))
    
    plate.handling()
    plate.draw(screen)

    
    plate.collision()
    
    apples.draw(screen)
    
    apples.update()
    
    
    score_text = font.render("Score {0}".format(score), 1, WHITE)
    screen.blit(score_text, (5, 10))
    
    
    if start == False:
        if start_btn.draw():
            start = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    fps.tick(60)

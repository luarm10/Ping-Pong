from pygame import *
init()

SW, SH = 800, 600
FPS = 120

screen = display.set_mode((SW, SH))
display.set_caption('Ping Pong')
PALETAZUL = ('pingazul.png')
PALETAROJA = ('pingrojo3.png')
BACKGROUND_IMG = 'cancha.jpg'
PELOTA = ('pelota.png')
font = font.Font(None, 50)

background = image.load(BACKGROUND_IMG)
background = transform.scale(background, (SW, SH))

class Character(sprite.Sprite):

    def __init__(self, img, cor_x, cor_y, width, height, speed=0):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed
        
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Character):
    def updateP1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SW - 80:
            self.rect.y += self.speed

    def updateP2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < SW - 80:
            self.rect.y += self.speed

# class Pelota(Character):
#     def __init__(self, img, cor_x, cor_y, width, height, speed_x, speed_y):
#         super().__init__(img, cor_x, cor_y, width, height, speed)
#         self.speed_x = speed_x
#         self.speed_y = speed_y
    
screen.blit(background, (0, 0))
p1 = Player('pingazul.png', 5, 110, 60, 100, 5)
p2 = Player('pingrojo3.png', SW-123, 135, 135, 135, 5)
ball = Character('pelota.png',100, 50, 50, 50, 3)

speed_x = 5
speed_y = 5

clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    screen.fill((100, 30 , 30))
    screen.blit(background, (0, 0))
    p1.reset()
    p1.updateP1()
    p2.reset()
    p2.updateP2()
    ball.reset()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y <= 0:
        speed_y *= -1
    if ball.rect.y >= SH - 50:
        speed_y *= -1
    if sprite.collide_rect(ball , p1):
        speed_x *= -1
    if sprite.collide_rect(ball , p2):
        speed_x *= -1

    if ball.rect.x <= 0:
        screen.fill((0, 0, 0))
        p2_win = font.render('Jugador 2 has ganado!', 1, ((0, 0, 0)))

    
    display.update()
    clock.tick(FPS)

quit()





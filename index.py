import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
fps = pygame.time.Clock()
running = True
dt = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("mario.png")
        self.image = pygame.transform.scale(self.image, (200,250))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 720:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 1280:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)      
P1 = Player()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    P1.update()
    P1.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = fps.tick(60) / 1000 #FPS

pygame.quit()
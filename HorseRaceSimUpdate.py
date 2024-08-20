import pygame
import sys
import random

pygame.init()
pygame.font.init()

width = 1000
height = 800
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Font settings
font = pygame.font.SysFont('Times New Roman', 36)
text_color = (255, 255, 255)

horses = pygame.sprite.Group()

class Horse(pygame.sprite.Sprite):
    def __init__(self, horsename, x, y, color):
        super().__init__()
        self.horsename = horsename
        self.image = pygame.image.load(f"img\\{self.horsename}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.w)
        self.color = color
        horses.add(self)
        self.finished = False
        
    def update(self):
        global game, run, finish_order

        if game:
            if not self.finished:
                if self.rect.x < 900:
                    self.rect.x += random.randrange(0, 5)
                else:
                    self.finished = True
                    finish_order.append(self.horsename)
                    print(f"{self.horsename} finished!")
                    
            if len(finish_order) == len(horses):
                game = 0
                print("Race finished!")
                print("Order of finish:", finish_order)
        
game = 1
finish_order = []

# Create horse instances
horse1 = Horse("horse1", 10, 100, "white")
horse2 = Horse("horse2", 10, 200, "blue")
horse3 = Horse("horse3", 10, 300, "red")
horse4 = Horse("horse4", 10, 400, "yellow")
horse5 = Horse("horse5", 10, 500, "green")

run = 1
while run:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    horses.update()
    horses.draw(screen)
    
    if not game:  # After the race has ended
        for i, horsename in enumerate(finish_order):
            text = font.render(f"{i+1}. {horsename}", True, text_color)
            screen.blit(text, (10, 600 + i * 30))  # Display the order on the screen
    
    pygame.display.flip()
    clock.tick(25)
    
pygame.quit()
sys.exit()

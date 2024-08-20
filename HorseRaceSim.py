# this is my horse racing simulator

import pygame
import sys
import random

pygame.init()
pygame.font.init()  # Ensure font is initialized

width = 1000
height = 800
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Use Pygame's default font with a smaller size
font = pygame.font.Font(None, 24)
text_color = (255, 255, 255)
background_color = (0, 0, 0)  # Black background
horse_color = (0, 255, 0)

horses = pygame.sprite.Group()

class Horse(pygame.sprite.Sprite):
    def __init__(self, horsename, x, y, color):
        super().__init__()
        self.horsename = horsename
        self.image = pygame.image.load(f"img\\{self.horsename}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
                
        #text = font.render(self.horsename, True, text_color)
       # screen.blit(text, (self.rect.x, self.rect.y - 30))
       
        # Render text above the horse
        text = font.render(self.horsename, True, text_color)
        text_rect = text.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y - 20))
        
        # Draw background rectangle behind the text
        pygame.draw.rect(screen, background_color, text_rect)
        
        # Blit the text on top of the rectangle
        screen.blit(text, text_rect)

game = 1
finish_order = []

# Create horse instances
pablo = Horse("horse1", 10, 100, "white")
horse2 = Horse("horse2", 10, 200, "blue")
horse3 = Horse("horse3", 10, 300, "red")
horse4 = Horse("horse4", 10, 400, "yellow")
horse5 = Horse("horse5", 10, 500, "green")

run = 1
result_display_time = 5000  # Time in milliseconds to display the results before quitting
result_timer_started = False

while run:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    horses.update()
    horses.draw(screen)
    
    if not game:  # After the race has ended
        if not result_timer_started:
            pygame.time.set_timer(pygame.USEREVENT, result_display_time)
            result_timer_started = True
    
        pygame.draw.rect(screen, background_color, (10, 590, 300, 200))
        
        for i, horsename in enumerate(finish_order):
            text = font.render(f"{i+1}. {horsename}", True, text_color)
            screen.blit(text, (20, 600 + i * 30))  # Display the order on the screen

    pygame.display.flip()
    clock.tick(25)
    
    if result_timer_started:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                run = 0
    
pygame.quit()
sys.exit()
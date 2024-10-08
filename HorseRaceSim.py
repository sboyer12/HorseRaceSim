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
        self.speed = random.uniform(0.2, 1)  # Variable speed
        self.max_speed = random.uniform(2, 4)  # Maximum speed
        self.acceleration = random.uniform(0.1, 0.3)  # Acceleration rate
        self.deceleration = random.uniform(0.1, 0.3)  # Deceleration rate
        self.current_speed = self.speed
        
    def update(self):
        global game, run, finish_order

        if game:
            if not self.finished:
                if self.rect.x < 900:
                   # self.rect.x += random.randrange(0, 5)
                    self.current_speed += self.acceleration
                    if self.current_speed > self.max_speed:
                        self.current_speed = self.max_speed
                    
                    # Move the horse with some variability
                    movement = random.uniform(self.current_speed - 1, self.current_speed + 1)
                    self.rect.x += max(0, movement)   
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
horse1 = Horse("Natey", 10, 50, "red")
horse2 = Horse("MrKaplan", 10, 130, "red")
horse3 = Horse("Seba", 10, 210, "red")
horse4 = Horse("Raffy", 10, 290, "red")
horse5 = Horse("Seany", 10, 370, "red")
horse6 = Horse("MrFlack", 10, 450, "red")
horse7 = Horse("Mish", 10, 530, "red")
horse8 = Horse("Larko", 10, 610, "red")
horse9 = Horse("Griffy", 10, 690, "red")
horse10 = Horse("Kodjak", 10, 770, "red")

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
            result_text = font.render(f"{i+1}. {horsename}", True, text_color, background_color)
            screen.blit(result_text, (20, 50 + i * 30))
            #text = font.render(f"{i+1}. {horsename}", True, text_color)
            #screen.blit(text, (20, 50 + i * 30))  # Display the order on the screen

    pygame.display.flip()
    clock.tick(25)
    
    if result_timer_started:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                run = 0
    
pygame.quit()
sys.exit()
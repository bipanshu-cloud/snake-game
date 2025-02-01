import pygame
from settings import *

class Snake:
    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0][:]
        if self.direction == "UP":
            head[1] -= SNAKE_SIZE
        elif self.direction == "DOWN":
            head[1] += SNAKE_SIZE
        elif self.direction == "LEFT":
            head[0] -= SNAKE_SIZE
        elif self.direction == "RIGHT":
            head[0] += SNAKE_SIZE
        
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        # Draw the snake with a highlight on the head
        for idx, segment in enumerate(self.body):
            color = YELLOW if idx == 0 else GREEN
            pygame.draw.rect(screen, color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

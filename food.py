# food.py - No need to import Food from itself
import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.position = [random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))

    def respawn(self):
        self.position = [random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE]

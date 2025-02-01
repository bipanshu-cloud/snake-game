import pygame
import sys
from snake import Snake
from food import Food
from settings import *

pygame.init()

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Initialize game objects
snake = Snake()
food = Food()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    snake.move()

    # Collision with food
    if snake.body[0] == food.position:
        snake.grow()
        food.respawn()

    # Collision with walls
    head_x, head_y = snake.body[0]
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        running = False

    # Collision with itself
    if snake.body[0] in snake.body[1:]:
        running = False

    # Draw objects
    snake.draw(screen)
    food.draw(screen)

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)

pygame.quit()
sys.exit()

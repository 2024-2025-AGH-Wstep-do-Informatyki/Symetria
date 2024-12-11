import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
player_speed = 20
running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra")
clock = pygame.time.Clock()

player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - 100
good_food_list = []
bad_food_list = []
protection_yellow_list = []
platform_y = HEIGHT - 80
score = 0
player_protected = False
protection_timer = 0
protection_duration = 5000

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_good_food():
    for food in good_food_list:
        pygame.draw.rect(screen, GREEN, food)

def draw_bad_food():
    for food in bad_food_list:
        pygame.draw.rect(screen, RED, food)

def draw_yellow_protection():
    for food in protection_yellow_list:
        pygame.draw.rect(screen, YELLOW, food)

def draw_platform():
    pygame.draw.line(screen, BLACK, (0, platform_y), (WIDTH, platform_y), 5)

def check_good_collision(x, y, foods):
    return any(pygame.Rect(x, y, player_width, player_height).colliderect(food) for food in foods)

def check_bad_collision(x, y, foods):
    return any(pygame.Rect(x, y, player_width, player_height).colliderect(food) for food in foods)

def check_yellow_collision(x, y, foods):
    return any(pygame.Rect(x, y, player_width, player_height).colliderect(food) for food in foods)

def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 10))

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < WIDTH // 2:
                player_x -= player_speed
            else:
                player_x += player_speed

    if random.randint(0, 50) == 0:
        good_food_list.append(pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20))
    if random.randint(0, 70) == 0:
        bad_food_list.append(pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20))
    if random.randint(0, 100) == 0:
        protection_yellow_list.append(pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20))

    for food in good_food_list:
        food.y += 5
    for food in bad_food_list:
        food.y += 7
    for food in protection_yellow_list:
        food.y += 5

    good_food_list = [food for food in good_food_list if food.y < HEIGHT]
    bad_food_list = [food for food in bad_food_list if food.y < HEIGHT]
    protection_yellow_list = [food for food in protection_yellow_list if food.y < HEIGHT]

    if check_bad_collision(player_x, player_y, bad_food_list):
        if not player_protected:
            print("Zginąłeś! Wynik:", score)
            running = False
        else:
            bad_food_list = [food for food in bad_food_list if not check_bad_collision(player_x, player_y, [food])]

    if check_good_collision(player_x, player_y, good_food_list):
        score += 10
        good_food_list = [food for food in good_food_list if not check_good_collision(player_x, player_y, [food])]

    if check_yellow_collision(player_x, player_y, protection_yellow_list):
        player_protected = True
        protection_timer = pygame.time.get_ticks()
        protection_yellow_list = [yellow for yellow in protection_yellow_list if not check_yellow_collision(player_x, player_y, [yellow])]

    if player_protected:
        current_time = pygame.time.get_ticks()
        if current_time - protection_timer > protection_duration:
            player_protected = False

    draw_good_food()
    draw_bad_food()
    draw_yellow_protection()
    draw_player(player_x, player_y)
    draw_platform()
    draw_score(score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

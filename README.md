# pingpong
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7

# Настройки мяча
BALL_SIZE = 15
ball_speed_x, ball_speed_y = 5, 5

# Начальные позиции
paddle_a = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Счет
score_a = 0
score_b = 0
font = pygame.font.Font(None, 74)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Управление ракетками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= paddle_speed
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += paddle_speed
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += paddle_speed

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Отскок мяча от верхней и нижней границ
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Отскок мяча от ракеток
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Проверка на гол
    if ball.left <= 0:
        score_b += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score_a += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= -1

    # Отрисовка
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Отображение счета
    score_text_a = font.render(str(score_a), True, WHITE)
    score_text_b = font.render(str(score_b), True, WHITE)
    screen.blit(score_text_a, (WIDTH // 4, 20))
    screen.blit(score_text_b, (WIDTH * 3 // 4 - score_text_b.get_width(), 20))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение работы
pygame.quit()
sys.exit()

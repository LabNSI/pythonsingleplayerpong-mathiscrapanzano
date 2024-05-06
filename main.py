import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen.fill(BLACK)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 50)


for i in range(3, 0, -1):
    screen.fill(BLACK)
    countdown_text = myfont.render(str(i), False, RED)
    screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2 - countdown_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)

radius = 10
x = WIDTH // 2
y = HEIGHT // 2

pygame.draw.circle(screen, WHITE, (x, y), radius)

paddle = {
    "width": 100,
    "height": 10,
    "color": YELLOW,
    "x": WIDTH // 2 - 20,
    "y": HEIGHT - 15
}

pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 1
x_sens = 1
y_sens = -1
pause = False
score = 0

end = False
while not end:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = not pause

    if key[pygame.K_RETURN]:
        pause = False

    if key[pygame.K_m]:
        pause = False

    if not pause:
        if key[pygame.K_LEFT]:
            paddle["x"] -= speed

        if key[pygame.K_RIGHT]:
            paddle["x"] += speed

        if x + radius >= WIDTH or x - radius <= 0:
            x_sens = -x_sens

        if y - radius <= 0:
            y_sens = -y_sens

        if y + radius >= paddle["y"] and paddle["x"] <= x <= paddle["x"] + paddle["width"]:
            y_sens = -y_sens
            score = score + 1
            if score %1 == 0 :
                speed += 1
                #paddle["width"] = paddle["width"] - 10

        if y + radius >= HEIGHT:
            end = True

        x = x + x_sens * speed
        y = y + y_sens * speed

    pygame.draw.circle(screen, WHITE, (x, y), radius)
    pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    score_text = myfont.render(str(score), False, RED)
    screen.blit(score_text, (10 , countdown_text.get_height()))

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
print(score)
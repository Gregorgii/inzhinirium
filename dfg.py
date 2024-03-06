import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if (x > 400 or x < 100) or (y < 100 or y > 400):
        speed = 1
    else:
        speed = 3

    if (x > 400 or x < 100) or (y < 100 or y > 400):
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    else:
        x = y = 250



    win.fill((0, 155, 45))

    pygame.draw.circle(win, color, (x, y), radius=10)
    pygame.display.update()
    pygame.time.delay(10)
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
win.fill((0, 187, 97))


class Circle:
    def __init__(self, surface, color, x, y, radius, dir):
        self.surface = surface
        self.color = color
        self.radius = radius
        self.y = y
        self.x = x
        self.dir = dir

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += 2 * self.dir
        if self.x > 500:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1



circles = []
for i in range(100):
    circles.append(Circle(win, (i*2.5, 255, i*2.5), i*25, i*25, 30, 1))



bob = Circle(win, (100, 120, 50), 250, 250, 30, 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 187, 97))
    bob.move()
    bob.draw()
    for i in circles:
        i.move()
        i.draw()

    pygame.time.delay(10)
    pygame.display.update()

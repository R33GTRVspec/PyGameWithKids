import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))  # , flags=pygame.NOFRAME)
pygame.display.set_caption("PygameBeginning")
icon = pygame.image.load('images/game_icon.png')
pygame.display.set_icon(icon)

running = True
while running:

    pygame.display.update()

    #screen.fill((110, 120, 220))

    for event in pygame.event.get():
        if event.type == pygame.event.get():
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((100, 50, 100))

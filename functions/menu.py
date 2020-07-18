import pygame
pygame.init()
font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial", 20)
def write(text, screen, x, y, color="Coral",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=((screen.w * 2 + screen.w //2) // 2, y))
    screen.screen.blit(text, text_rect)
    return text


def menu(Puzzle, start):
    "The menu to choose among different games"
    
    global game, randomstage
    
    
    Puzzle.screen.fill((0, 0, 0))
    write("PuzzleMania", Puzzle, 200, 50, color="yellow")
    write("A Game by Giovanni Gatto", Puzzle, 200, 120, color="red")
    write("Follow me on youtube", Puzzle, 200, 140)
    write("and pythonprogramming.altervista.org", Puzzle, 200, 160)
    write("CHOOSE YOUR PUZZLE", Puzzle, 200, 300, color="green")
    write("1 - Avengers", Puzzle, 150, 340)
    write("2 - Captain America", Puzzle, 150, 360)
    write("3 - Girl", Puzzle, 150, 380)
    write("4 - Night landscape", Puzzle, 150, 400)
    write("5 - Coffee", Puzzle, 150, 420)
    # write("4 - Arkanoid tiny 2", 150, 400)
    write("July 2020", Puzzle, 150, 480, color="gray")
    loop = 1
    while loop:
        # screen.blit(background, (0, 0))
        # keys = pygame.key.get_pressed()
        #ui = pygame.event.wait()
        # show_particles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start()
                if event.key == pygame.K_1:
                    game = 1
                    restart1()
                elif event.key == pygame.K_2:
                    game = 2
                    restart2()
                elif event.key == pygame.K_3:
                    game = 3
                    restart3()
                elif event.key == pygame.K_4:
                    game = 4
                    restart4()
                elif event.key == pygame.K_5:
                    randomstage = 1
                    game = 5
                    game2 = randrange(1, 5)
                    if game2 == 1:
                        restart1()
                    if game2 == 2:
                        restart2()
                    if game2 == 3:
                        restart3()
                    if game2 == 4:
                        restart4()
                # Next game
                # elif event.key == pygame.K_6:
                #     game = 6
                #     restart6()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                    screen.fill((0, 0, 0))
                    mainloop()
                if event.key == pygame.K_ESCAPE:
                    loop = 0
            # Put this in line with for event ...
            pygame.display.update()
    pygame.quit()
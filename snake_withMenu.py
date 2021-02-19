import pygame, random

pygame.init()
sw=800
sh=600
screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("SNAKE GAME")
font_32=pygame.font.SysFont("Arial",48)
font_64=pygame.font.SysFont("Arial",64)
font = pygame.font.SysFont("Arial",32)
score_print=pygame.font.SysFont("Arial",32)
clock= pygame.time.Clock()


def snake_game(sp):
    t=sp
    snake_pos = [[300, 300], [320, 300], [340, 300], [360, 300]]
    step = 20
    up = (0, -step)
    down = (0, step)
    right = (step, 0)
    left = (-step, 0)

    direction = left
    timer = 0
    game_over = False


    def gameover():
        over_text = font_64.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (250, 230))
        scr_text = font_64.render("FINAL SCORE: " + str(score), True, (255, 255, 255))
        screen.blit(scr_text, (250, 330))


    def pause():
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pause = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            screen.fill((0,0,0))
            pause_text = font_64.render("Game Paused", True, (255, 255, 255))
            screen.blit(pause_text, (250, 230))
            pauseText = font_32.render("Press c to continue or q to Quit", True, (255,255,255))
            screen.blit(pauseText, (150, 330))
            clock.tick(5)
            pygame.display.update()


    score = 0
    # apple position
    game_over=False
    apple_pos = [260, 300]
    mainmenu=False
    pauseTxt= True
    running = True
    while running:
        screen.fill((180, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("UP")
                    direction = up
                if event.key == pygame.K_DOWN:
                    print("DOWN")
                    direction = down
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                    direction = left
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    direction = right
                if event.key == pygame.K_p:
                    pause()

        timer += 1
        if timer == 5:
            snake_pos = [[snake_pos[0][0] + direction[0], snake_pos[0][1] + direction[1]]] + snake_pos[:-1]
            timer = 0

        if snake_pos[0] == apple_pos:
            x = (random.randint(100, 700) // 20) * 20
            y = (random.randint(100, 500) // 20) * 20
            apple_pos = [x, y]
            score += 1
            snake_pos.append(snake_pos[-1])

        # boundary Conditions
        for i in range (len(snake_pos)):
            if snake_pos[i][0] == 800:
                snake_pos[i][0] = 0
            elif snake_pos[i][0] == 0:
                snake_pos[i][0] = 800
            if snake_pos[i][1] == 600:
                snake_pos[i][1] = 0
            elif snake_pos[i][1] == 0:
                snake_pos[i][1] = 600

        for i in range(1, len(snake_pos)):
            if snake_pos[i] == snake_pos[0]:
                game_over = True

        if pauseTxt:
            p_text = font.render("Press p to Pause", True, (255, 255, 255))
            screen.blit(p_text, (320, 10))


        if game_over:
            screen.fill((100,200,100))
            for i in range(len(snake_pos)):
                snake_pos[i][0]=2000
            apple_pos=[2000,2000]
            pauseTxt=False
            gameover()
            print(score)



        for x, y in snake_pos:
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)

        pygame.draw.circle(screen, (255, 0, 0), apple_pos, 10)
        text = score_print.render("SCORE: " + str(score), True, (255, 255, 255))
        screen.blit(text, (0, 0))


        clock.tick(t)
        pygame.display.update()


mode=0
state=0
clicked=False

Mainrunning=True
while Mainrunning:
    screen.fill((100,200,100))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Mainrunning=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("spave")
                state=1
        if event.type==pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                clicked=True
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button ==1:
                clicked=False

    mx,my=pygame.mouse.get_pos()

    if clicked and state==0:
        if 250 < mx < 500 and 130 < my < 220:
            mode = 1
            print(mode)
        if 250 < mx < 500 and 230 < my < 290:
            mode = 2
            print(mode)
        if 250 < mx < 600 and 310 < my < 500:
            mode = 3
            print(mode)

    if mode==1:
        red_rect=pygame.Rect(285, 160, 200, 60)
        pygame.draw.rect(screen, (255,0,0), red_rect,2)

    if mode==2:
        red_rect=pygame.Rect(285, 230, 200, 60)
        pygame.draw.rect(screen, (255,0,0), red_rect,2)

    if mode==3:
        red_rect=pygame.Rect(285, 300, 200, 60)
        pygame.draw.rect(screen, (255,0,0), red_rect,2)
    if state==1:
        if mode==1:
            Mainrunning=False
            speed=20
            snake_game(speed)
        if mode == 2:
            Mainrunning = False
            speed = 40
            snake_game(speed)
        if mode==3:
            Mainrunning=False
            speed=60
            snake_game(speed)


    titlemsg= font_64.render("SNAKE GAME", True, (0,0,255))
    screen.blit(titlemsg, (230,20))

    selectMode = font_32.render("Select Level: ", True, (0, 0, 255))
    screen.blit(selectMode, (30, 120))

    easy = font_32.render("Easy", True, (0, 0, 255))
    screen.blit(easy, (300, 160))

    Medium = font_32.render("Medium", True, (0, 0, 255))
    screen.blit(Medium, (300, 230))

    Hard = font_32.render("Hard", True, (0, 0, 255))
    screen.blit(Hard, (300, 300))

    start = font_32.render("Press SPACE BAR to start the game!!", True, (0,0,255))
    screen.blit(start, (30,400))




    pygame.display.update()
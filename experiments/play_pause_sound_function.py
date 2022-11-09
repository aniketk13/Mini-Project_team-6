def paused():

    largeText = pygame.font.SysFont("Checker",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

       #Now, all you need to do is add a check if the P key is pressed in the KEYDOWN event if-statement

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_p:
                pause = True
                paused()


        # Next up, we want to cover the game over sequence, which is triggered when we crash.

        def crash():

            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("You Crashed", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)

            while True:
                for event in pygame.event.get():
                    # print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                # gameDisplay.fill(white)

                button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
                button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

                pygame.display.update()
                clock.tick(15)

            #Now you want to edit the bottom of the game_loop function to look like:
            if x > display_width - car_width or x < 0:
                crash()

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                dodged += 1
                thing_speed += 1
                thing_width += (dodged * 1.2)

            if y < thing_starty + thing_height:
                print('y crossover')

                if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                    print('x crossover')
                    crash()
#Basically, you want to replace the game_over = True with crash().

#To start, let's make a sound:

crash_sound = pygame.mixer.Sound("crash.wav")
#Now that we know how to call sounds, how can we do music?

pygame.mixer.music.load('jazz.wav')
pygame.mixer.music.play(-1)

#Now, we want the music to play, and it is, then we need the crash sound to play when crashed. Also, we'd like to stop the music if this is the case.
def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
#Now, the only other thing we may want to do is learn how to pause/unpause music when the player pauses the game. This is easy enough.


    def paused():
        ############
        pygame.mixer.music.pause()
        #############


#And then of course we must unpause it:


    def unpause():
        global pause
        #################
        pygame.mixer.music.unpause()
        #################
        pause = False
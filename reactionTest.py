# Example file showing a circle moving on screen
import pygame
import random
import time


def handleTime():
    global initialTime
    global finalTime
    global averageTime
    global times
    global totalAttempts

    finalTime = pygame.time.get_ticks() / 1000
    print('your time is: ', round(finalTime - initialTime, 2))
    times.append(finalTime - initialTime)
    time.sleep(3)

    averageTime = sum(times) / totalAttempts
    initialTime = pygame.time.get_ticks() / 1000


def increaseScore():
    global randomNumber
    global player_pos
    global initialTime
    global scored
    global score
    global totalAttempts
    global finalTime
    global averageTime

    scored = True
    score += 1
    totalAttempts += 1

    handleTime()

    # show the results
    print('your score is: ', score)
    print('your total attempts are: ', totalAttempts)
    print('your average time is: ', round(averageTime, 2))

    # convert to two decimal places
    print('your hit rate is: ', round(score * 100 / totalAttempts), '%')

    # handle next circle
    randomNumber = generateRandomNumber()
    player_pos = generateRandomPosition()
    scored = False


def handleWrongKey():
    global hitPoints
    global totalAttempts
    global randomNumber
    global player_pos

    totalAttempts += 1
    hitPoints -= 1
    print('you lost a hit point')

    handleTime()

    # handle next circle
    randomNumber = generateRandomNumber()
    player_pos = generateRandomPosition()


def generateRandomPosition():
    randomX = random.randint(0, screen.get_width())
    randomY = random.randint(0, screen.get_height())
    return pygame.Vector2(randomX, randomY)


def generateRandomNumber():
    randomNumber = random.randint(0, 3)
    return randomNumber

# function to render a cicle on screen


def renderCircle():
    global randomNumber

    if randomNumber == 0:
        pygame.draw.circle(screen, "red", player_pos, 40)
    elif randomNumber == 1:
        pygame.draw.circle(screen, "blue", player_pos, 40)
    elif randomNumber == 2:
        pygame.draw.circle(screen, "yellow", player_pos, 40)
    elif randomNumber == 3:
        pygame.draw.circle(screen, "green", player_pos, 40)


# function to check if the player pressed the right key
def checkKey():
    global randomNumber

    if randomNumber == 0:
        if keys[pygame.K_r]:
            increaseScore()
        else:
            if keys[pygame.K_b] or keys[pygame.K_y] or keys[pygame.K_g]:
                handleWrongKey()
    elif randomNumber == 1:
        if keys[pygame.K_b]:
            increaseScore()
        else:
            if keys[pygame.K_r] or keys[pygame.K_y] or keys[pygame.K_g]:
                handleWrongKey()
    elif randomNumber == 2:
        if keys[pygame.K_y]:
            increaseScore()
        else:
            if keys[pygame.K_r] or keys[pygame.K_b] or keys[pygame.K_g]:
                handleWrongKey()
    elif randomNumber == 3:
        if keys[pygame.K_g]:
            increaseScore()
        else:
            if keys[pygame.K_r] or keys[pygame.K_b] or keys[pygame.K_y]:
                handleWrongKey()


# setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = generateRandomPosition()

randomNumber = generateRandomNumber()

scored = False

initialTime = pygame.time.get_ticks() / 1000

score = 0

totalAttempts = 0

currentTime = 0

hitPoints = 3

times = []
averageTime = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # get the current time
    currentTime = (pygame.time.get_ticks() / 1000) - initialTime

    if currentTime > 3:
        print('you lost')
        running = False

    if hitPoints < 1:
        print('you lost')
        running = False

    keys = pygame.key.get_pressed()

    renderCircle()

    checkKey()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

import sys
from colour import Colour
from screen import Screen
from player import Player
from compPlayer import CompPlayer
from game import Game
from obstacle import Obstacle
from startAndEndPoints import StartAndEndPoints
from enemy import Enemy
import pygame

pygame.init()


def playGame():
    """ Simulate the game """
    # Variables
    SCREENWIDTH = 1350
    SCREENHEIGHT = 770
    font = pygame.font.Font('freesansbold.ttf', 20)
    startPointSize = 100
    startPoint = [0, SCREENHEIGHT/2 - startPointSize/2]
    startPointColour = Colour.GREEN
    endPointSize = 100
    endPoint = [SCREENWIDTH - endPointSize, SCREENHEIGHT/2 - endPointSize/2]
    playerSize = 40
    playerStartingPosition = [i + startPointSize /
                              2 - playerSize/2 for i in startPoint.copy()]
    playerColour = Colour.BLUE
    playerOutlineColour = Colour.BLACK
    playerOutlineWidth = 1
    compPlayerMutationRate = 0.12
    compPlayerTime = 175
    compPlayerColour = Colour.RED
    compPlayerPopulationSize = 750
    obstacleColour = Colour.BLACK
    obstacleWidth = 1
    endPointColour = Colour.GREEN
    finishBlit = [False]
    enemyColour = Colour.BLUE
    enemyVelocity = 6
    enemySize = 30
    previousEvent = (0, 0)
    gameTickFrequency = 60
    # Setting up enemy
    enemy = Enemy(enemyColour, enemyVelocity, enemySize)
    # Setting up obstacles
    obstacle = Obstacle(obstacleColour, obstacleWidth)
    # Setting up the game
    game = Game(gameTickFrequency)
    # Setting up the screen
    screen = Screen(SCREENWIDTH, SCREENHEIGHT, font,
                    backgroundColour=Colour.LIGHTPURPLE)
    screen.reset()
    # Setting up the player
    player = Player(startingPosition=(playerStartingPosition),
                    size=playerSize, colour=playerColour, outlineColour=playerOutlineColour, outlineWidth=playerOutlineWidth)
    screen.drawPlayer(player)
    # Setting up the start and end points
    startAndEndPoints = StartAndEndPoints(
        startPoint, startPointSize, startPointColour, endPoint, endPointSize, endPointColour)
    screen.drawStartAndEndPoints(startAndEndPoints)
    # Setting up the computer players
    compPlayer = CompPlayer(compPlayerMutationRate,
                            compPlayerTime, gameTickFrequency, compPlayerPopulationSize, startAndEndPoints, startingPosition=(playerStartingPosition), size=playerSize, colour=compPlayerColour, outlineColour=playerOutlineColour, outlineWidth=playerOutlineWidth)
    # Updating the screen
    screen.update()
    # Main loop
    keepGoing = True
    while keepGoing:
        # Looping through all the events that happen
        for event in pygame.event.get():
            # Store previous event
            previousEvent = game.eventStore(event, previousEvent)
            tempEvent = event
            # Quit game
            if event.type == pygame.QUIT:
                sys.exit()
                break
            # Taking obstacle points
            obstacle.recordObstacle(event)
            # Taking enemy points
            enemy.recordEnemy(event, previousEvent)
            # Taking player movement input
            player.takeMoveInput(event)
            # If the spacebar is pressed intialise the computer generated population
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Setting up initial population for compPlayer
                    compPlayer.initialisePopulation(enemy, finishBlit)
            # If r is pressed then remove the genetic algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Setting up initial population for compPlayer
                    compPlayer.populationReset()
        # See whether number of moves have gone past limit
        compPlayer.timeLimitDetection(enemy, finishBlit)
        # Checking if player and obstacles collide, taking player movement input
        player.playerObstacleCollision(obstacle)
        player.takeMoveInput(tempEvent)
        # Checking if the player and enemies collide, taking compPlayer movement input
        compPlayer.compPlayerObstacleCollision(obstacle)
        compPlayer.takeMoveInput()
        # Checking if player and screen boundaries collide
        player.playerEdgeCollision(SCREENWIDTH, SCREENHEIGHT)
        # Checking if compPlayer and screen boundaries collide
        compPlayer.compPlayerEdgeCollision(SCREENWIDTH, SCREENHEIGHT)
        # Checking if player and end point collide
        player.playerEndPointCollision(startAndEndPoints)
        # Checking if compPlayer and end point collide
        compPlayer.compPlayerEndPointCollision(screen, game, finishBlit)
        # Checking if the player and enemies collide
        player.playerEnemyCollision(enemy)
        # Checking if the compPlayer and enemies collide
        compPlayer.compPlayerEnemyCollision(enemy)
        # Resetting the screen
        screen.reset()
        # Updating all enemy position
        enemy.move()
        # Updating player position in player class
        player.move()
        # Updating comPlayer position in player class
        compPlayer.move(finishBlit)
        # Setting up the start and end points
        screen.drawStartAndEndPoints(startAndEndPoints)
        # Updating player position in screen
        screen.drawPlayer(player)
        # Updating compPlayer position in screen
        screen.drawCompPlayer(compPlayer)
        # Drawing obstacles in screen
        screen.drawObstacles(obstacle)
        # Drawing enemies in screen
        screen.drawEnemies(enemy)
        # Allowing the average fitness, highest fitness and current generation to be displayed onto the screen if the genetic algorithm has started
        text, textRect = screen.initialiseText(
            compPlayer, game, "averageFitness")
        screen.displayText(text, textRect, compPlayer)
        text, textRect = screen.initialiseText(
            compPlayer, game, "highestFitness")
        screen.displayText(text, textRect, compPlayer)
        text, textRect = screen.initialiseText(compPlayer, game, "generation")
        screen.displayText(text, textRect, compPlayer)
        # Checking if compPlayer and end point collide. Updating screen if they do
        compPlayer.compPlayerEndPointCollision(screen, game, finishBlit)
        # Finalising screen for this moment
        screen.update()
        game.tick()


# Run the main file
playGame()

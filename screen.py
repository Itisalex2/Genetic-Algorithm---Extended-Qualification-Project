from colour import Colour
import pygame


class Screen:
    def __init__(self, SCREENWIDTH, SCREENHEIGHT, font, backgroundColour=Colour.LIGHTPURPLE):
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT
        self.font = font
        self.backgroundColour = backgroundColour
        self.screen = pygame.display.set_mode(
            (self.SCREENWIDTH, self.SCREENHEIGHT))

    def drawPlayer(self, player):
        """ Draw the actual player """
        # startingPosition is a tuple, where [0] is the x value and [1] is the y value
        pygame.draw.rect(
            self.screen, player.colour, (player.position[0], player.position[1], player.size, player.size))
        pygame.draw.rect(
            self.screen, player.outlineColour, (player.position[0], player.position[1], player.size, player.size), width=player.outlineWidth)

    def drawCompPlayer(self, compPlayer):
        """ Draw the compPlayer """
        # startingPosition is a tuple, where [0] is the x value and [1] is the y value
        for pos, value in enumerate(compPlayer.populationArray):
            pygame.draw.rect(
                self.screen, compPlayer.colour, (value[1][0], value[1][1], compPlayer.size, compPlayer.size))
            pygame.draw.rect(
                self.screen, compPlayer.outlineColour, (value[1][0], value[1][1], compPlayer.size, compPlayer.size), width=compPlayer.outlineWidth)

    def drawObstacles(self, obstacles):
        """ Draw all the obstacles """
        for obstacle in obstacles.obstacleArray:
            pygame.draw.line(self.screen, obstacles.colour, (
                obstacle[0][0], obstacle[0][1]), (obstacle[1][0], obstacle[1][1]), width=obstacles.width)

    def drawStartAndEndPoints(self, startAndEndPoints):
        pygame.draw.rect(
            self.screen, startAndEndPoints.startPointColour, (startAndEndPoints.startPoint[0], startAndEndPoints.startPoint[1], startAndEndPoints.startPointSize, startAndEndPoints.startPointSize))
        pygame.draw.rect(
            self.screen, startAndEndPoints.endPointColour, (startAndEndPoints.endPoint[0], startAndEndPoints.endPoint[1], startAndEndPoints.endPointSize, startAndEndPoints.endPointSize))

    def drawEnemies(self, enemies):
        """ Draw all the enemies """
        for enemy in enemies.enemyArray:
            # enemy[2] is the position of the enemy
            pygame.draw.rect(self.screen, enemies.colour,
                             (enemy[2][0], enemy[2][1], enemies.size, enemies.size))

    def update(self):
        """ Updates the screen """
        pygame.display.update()

    def reset(self):
        self.screen.fill(self.backgroundColour)

    def initialiseText(self, compPlayer, game, variable):
        if variable == "averageFitness":
            text = self.font.render(
                f"Average fitness: {str(compPlayer.tempTotalFitness / compPlayer.populationSize)}", True,
                Colour.BLACK)
            textRect = text.get_rect()
            textRect.center = (self.SCREENWIDTH - 205, self.SCREENHEIGHT - 30)
        elif variable == "highestFitness":
            text = self.font.render(
                f"Highest fitness: {str(compPlayer.tempHighestFitnessPlayer[4])}", True,
                Colour.BLACK)
            textRect = text.get_rect()
            textRect.center = (self.SCREENWIDTH - 205, self.SCREENHEIGHT - 12)
        elif variable == "Finish":
            text = self.font.render(
                f"END POINT REACHED! Time taken: {compPlayer.finalMoveCount / game.tickFrequency} seconds", True,
                Colour.BLACK)
            textRect = text.get_rect()
            textRect.center = (self.SCREENWIDTH // 2, self.SCREENHEIGHT // 2)
        else:
            text = self.font.render(
                f"Current generation: {str(compPlayer.generation)}", True,
                Colour.BLACK)
            textRect = text.get_rect()
            textRect.center = (self.SCREENWIDTH - 205, self.SCREENHEIGHT - 48)
        return text, textRect

    def displayText(self, text, textRect, compPlayer):
        if len(compPlayer.populationArray) != 0:
            self.screen.blit(text, textRect)

    def displayFinishText(self, text, textRect):
        self.screen.blit(text, textRect)

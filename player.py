from colour import Colour
import sys
import pygame


class Player:
    def __init__(self, startingPosition=[50, 50], size=50, colour=Colour.BLUE, outlineColour=Colour.BLACK, outlineWidth=3):
        self.size = size
        self.colour = colour
        self.velocityLeft = 0
        self.velocityRight = 0
        self.velocityUp = 0
        self.velocityDown = 0
        self.startingPosition = startingPosition.copy()
        self.position = startingPosition.copy()
        self.outlineColour = outlineColour
        self.outlineWidth = outlineWidth
        self.directionArray = []

    def playerObstacleCollision(self, obstacles):
        for obstacle in obstacles.obstacleArray:
            # If the line is horizontal
            if obstacle[2] == "horizontal":
                # If the player's x position is between the line endpoints
                if self.position[0] >= obstacle[0][0] - self.size and self.position[0] <= obstacle[1][0]:
                    # If the player's y position is the same as the endpoints. The +sth stuff is just to adjust the collision detection
                    if obstacle[0][1] - self.position[1] < self.size and obstacle[0][1] - self.position[1] > 0:
                        if self.position[0] + self.size - 3 <= obstacle[0][0]:
                            self.directionArray.append("Left")
                        elif self.position[0] + 3 >= obstacle[1][0]:
                            self.directionArray.append("Right")
                        elif self.position[1] + self.size - 5 >= obstacle[0][1]:
                            self.directionArray.append("Down")
                        elif self.position[1] - 3 <= obstacle[0][1]:
                            self.directionArray.append("Up")
            else:
                # If the player's y position is between the line endpoints
                if self.position[1] >= obstacle[0][1] - self.size and self.position[1] <= obstacle[1][1]:
                    # If the player's x position is the same as the endpoints. The +sth stuff is just to adjust the collision detection
                    if obstacle[0][0] - self.position[0] < self.size and obstacle[0][0] - self.position[0] > 0:
                        if self.position[1] + self.size - 3 <= obstacle[0][1]:
                            self.directionArray.append("Up")
                        elif self.position[1] + 3 >= obstacle[1][1]:
                            self.directionArray.append("Down")
                        elif self.position[0] + self.size - 5 <= obstacle[0][0]:
                            self.directionArray.append("Left")
                        elif self.position[0] + 5 >= obstacle[0][0]:
                            self.directionArray.append("Right")

    def playerEndPointCollision(self, startAndEndPoints):
        """ Detect whether the player has entered the end point """
        # Checking if the player x value is within the end point
        if self.position[0] >= startAndEndPoints.endPoint[0] and self.position[0] + self.size <= startAndEndPoints.endPoint[0] + startAndEndPoints.endPointSize:
            # Checking if y value is within the end point
            if self.position[1] >= startAndEndPoints.endPoint[1] and self.position[1] + self.size <= startAndEndPoints.endPoint[1] + startAndEndPoints.endPointSize:
                self.position = self.startingPosition.copy()

    def playerEdgeCollision(self, SCREENWIDTH, SCREENHEIGHT):
        """ Ensure that player does not go outside of screen """
        if self.position[0] <= 0:
            self.velocityLeft = 0
            self.position[0] = 0
        if self.position[0] >= SCREENWIDTH - self.size:
            self.velocityRight = 0
            self.position[0] = SCREENWIDTH - self.size
        if self.position[1] <= 0:
            self.velocityUp = 0
            self.position[1] = 0
        if self.position[1] >= SCREENHEIGHT - self.size:
            self.velocityDown = 0
            self.position[1] = SCREENHEIGHT - self.size

    def playerEnemyCollision(self, enemies):
        for enemy in enemies.enemyArray:
            # If player approaching enemy from the left
            if enemy[2][0] + enemies.size > self.position[0] and enemy[2][0] + enemies.size < self.position[0] + self.size:
                if enemy[2][1] > self.position[1] and enemy[2][1] < self.position[1] + self.size:
                    self.position = self.startingPosition.copy()
            # If player approaching enemy from the right
            if enemy[2][0] < self.position[0] + self.size and enemy[2][0] > self.position[0]:
                if enemy[2][1] > self.position[1] and enemy[2][1] < self.position[1] + self.size:
                    self.position = self.startingPosition.copy()
            # If player approaching enemy from the top
            if enemy[2][0] > self.position[0] and enemy[2][0] < self.position[0] + self.size:
                if enemy[2][1] + self.size > self.position[1] and enemy[2][1] + self.size < self.position[1] + self.size:
                    self.position = self.startingPosition.copy()
            # If player approaching enemy from the bottom
            if enemy[2][0] > self.position[0] and enemy[2][0] < self.position[0] + self.size:
                if enemy[2][1] > self.position[1] and enemy[2][1] < self.position[1] + self.size:
                    self.position = self.startingPosition.copy()

    def takeMoveInput(self, event):
        """ Decides player veloicty """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocityLeft = -4
            if event.key == pygame.K_RIGHT:
                self.velocityRight = 4
            if event.key == pygame.K_UP:
                self.velocityUp = -4
            if event.key == pygame.K_DOWN:
                self.velocityDown = 4
        if "Left" in self.directionArray:
            self.velocityRight = 0
        if "Right" in self.directionArray:
            self.velocityLeft = 0
        if "Up" in self.directionArray:
            self.velocityDown = 0
        if "Down" in self.directionArray:
            self.velocityUp = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.velocityLeft = 0
            if event.key == pygame.K_RIGHT:
                self.velocityRight = 0
            if event.key == pygame.K_UP:
                self.velocityUp = 0
            if event.key == pygame.K_DOWN:
                self.velocityDown = 0

    def move(self):
        """ Moves the player """
        self.position[0] += self.velocityLeft + self.velocityRight
        self.position[1] += self.velocityUp + self.velocityDown
        self.directionArray = []

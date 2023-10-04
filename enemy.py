import math
import pygame
import copy


class Enemy:
    def __init__(self, colour, velocity, size):
        self.enemyArray = []
        self.colour = colour
        self.firstPosition = [None, None]
        self.secondPosition = [None, None]
        self.velocity = velocity
        self.size = size
        self.copyEnemyArray = []

    def recordEnemy(self, event, recordEnemyEvent):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                self.firstPosition[0] = recordEnemyEvent[0]
                self.firstPosition[1] = recordEnemyEvent[1]
            if event.key == pygame.K_RSHIFT:
                self.secondPosition[0] = recordEnemyEvent[0]
                self.secondPosition[1] = recordEnemyEvent[1]
                if (self.secondPosition[0] - self.firstPosition[0] == 0) or (self.secondPosition[1] - self.firstPosition[1] == 0):
                    return None
                # Making sure that the x position of the first position is less
                if self.firstPosition[0] > self.secondPosition[0]:
                    self.firstPosition, self.secondPosition = self.secondPosition, self.firstPosition
                # If the line is going upwards
                if self.secondPosition[1] < self.firstPosition[1]:
                    # Find angle
                    angle = math.atan((self.firstPosition[1] - self.secondPosition[1]) / (
                        self.secondPosition[0] - self.firstPosition[0]))
                    verticalVelocity = -self.velocity * math.sin(angle)
                    horizontalVelocity = self.velocity * math.cos(angle)
                # If the line is going downwards
                else:
                    # Find angle
                    angle = math.atan((self.secondPosition[0] - self.firstPosition[0]) / (
                        self.secondPosition[1] - self.firstPosition[1]))
                    verticalVelocity = self.velocity * math.cos(angle)
                    horizontalVelocity = self.velocity * math.sin(angle)
                firstTime = True
                self.enemyArray.append(
                    [self.firstPosition.copy(), self.secondPosition.copy(), self.firstPosition.copy(), horizontalVelocity, verticalVelocity, firstTime])
                self.copyEnemyArray.append([self.firstPosition.copy(), self.secondPosition.copy(
                ), self.firstPosition.copy(), horizontalVelocity, verticalVelocity, firstTime])

    def move(self):
        """ Moves the enemy"""
        for pos, enemy in enumerate(self.enemyArray):
            # If it is the enemy's first time moving
            if enemy[5]:
                self.enemyArray[pos][2][0] += enemy[3] * 1.2
                self.enemyArray[pos][2][1] += enemy[4] * 1.2
                self.enemyArray[pos][5] = False
            # If the enemy is close to the start point
            elif abs(enemy[2][0] - enemy[0][0]) < abs(enemy[3]):
                self.enemyArray[pos][2] = enemy[0].copy()
                self.enemyArray[pos][3] = -enemy[3]
                self.enemyArray[pos][4] = -enemy[4]
                self.enemyArray[pos][2][0] += enemy[3] * 1.2
                self.enemyArray[pos][2][1] += enemy[4] * 1.2
            # If the enemy is close to the end point
            elif abs(enemy[2][0] - enemy[1][0]) < abs(enemy[3]):
                self.enemyArray[pos][2] = enemy[1].copy()
                self.enemyArray[pos][3] = -enemy[3]
                self.enemyArray[pos][4] = -enemy[4]
                self.enemyArray[pos][2][0] += enemy[3] * 1.2
                self.enemyArray[pos][2][1] += enemy[4] * 1.2
            else:
                self.enemyArray[pos][2][0] += enemy[3]
                self.enemyArray[pos][2][1] += enemy[4]

    def resetPosition(self):
        self.enemyArray = copy.deepcopy(self.copyEnemyArray)

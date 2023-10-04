import pygame


class Obstacle:
    def __init__(self, colour, width):
        self.obstacleArray = []
        self.obstacleFirstPoint = None
        self.obstacleSecondPoint = None
        self.colour = colour
        self.width = width

    def recordObstacle(self, event):
        """ Intake obstacle point information and record it into array """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.obstacleFirstPoint = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            self.obstacleSecondPoint = event.pos
            # If obstacle is horizontal
            if abs(self.obstacleFirstPoint[0] - self.obstacleSecondPoint[0]) >= abs(self.obstacleFirstPoint[1] - self.obstacleSecondPoint[1]):
                # Sorting obstacle by having the samllet x value as the first point
                if self.obstacleFirstPoint[0] > self.obstacleSecondPoint[0]:
                    self.obstacleFirstPoint, self.obstacleSecondPoint = self.obstacleSecondPoint, self.obstacleFirstPoint
                # Adding obstacle to array
                if self.obstacleFirstPoint[0] < self.obstacleSecondPoint[0]:
                    self.obstacleArray.append(
                        ((self.obstacleFirstPoint[0], self.obstacleFirstPoint[1]), (self.obstacleSecondPoint[0], self.obstacleFirstPoint[1]), ("horizontal")))
            else:
                # Sorting obstacle by having the samllet y value as the first point
                if self.obstacleFirstPoint[1] > self.obstacleSecondPoint[1]:
                    self.obstacleFirstPoint, self.obstacleSecondPoint = self.obstacleSecondPoint, self.obstacleFirstPoint
                # obstacle is vertical
                self.obstacleArray.append(
                    ((self.obstacleFirstPoint[0], self.obstacleFirstPoint[1]),
                     (self.obstacleFirstPoint[0], self.obstacleSecondPoint[1]), ("vertical")))

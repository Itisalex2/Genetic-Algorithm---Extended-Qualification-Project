from colour import Colour
import random


class CompPlayer():
    def __init__(self, mutationRate, time, gameTickFrequency, populationSize, startAndEndPoints, startingPosition=[50, 50], size=50, colour=Colour.RED, outlineColour=Colour.BLACK, outlineWidth=3):
        self.size = size
        self.colour = colour
        self.startingPosition = startingPosition.copy()
        self.outlineColour = outlineColour
        self.outlineWidth = outlineWidth
        self.mutationRate = mutationRate
        self.movesLimit = 4 * gameTickFrequency
        self.moveCount = 0
        self.finalMoveCount = 0
        self.populationSize = populationSize
        self.startAndEndPoints = startAndEndPoints
        self.populationArray = []
        self.parents = []
        self.tempHighestFitnessPlayer = [None, None, None, None, 0]
        self.tempTotalFitness = 0
        self.generation = 0
        self.timeCount = 0
        self.time = time
        self.gameTickFrequency = gameTickFrequency

    # Genetic algorithm section

    def populationReset(self):
        self.populationArray = []
        self.tempTotalFitness = 0
        self.tempHighestFitnessPlayer = [None, None, None, None, 0]
        self.generation = 0
        self.moveCount = 0

    def initialisePopulation(self, enemy, finishBlit):
        """ Creating the population """
        # Resetting everything for new generation
        finishBlit[0] = False
        self.populationReset()
        for i in range(self.populationSize):
            # Randomly selecting the frist 100 moves of the player
            moveChoices = ["Up", "Down", "Left", "Right"]
            first100MoveList = random.choices(
                moveChoices, weights=[1, 1, 1, 1], k=self.time * self.gameTickFrequency)
            # Appending each compPlayer into the popluationArray
            self.populationArray.append(
                [first100MoveList, self.startingPosition.copy(), [0, 0, 0, 0], [], None])
        enemy.resetPosition()

    def fitnessScore(self):
        """ Calculate the fitness score for each compPlayer and update it. Also update the tempTotalFitness """
        for pos, value in enumerate(self.populationArray):
            # Find distance between the current position of the compPlayer and the end point
            endPointCentre = [(i + self.startAndEndPoints.endPointSize/2)
                              for i in self.startAndEndPoints.endPoint.copy()]
            currentPosition = value[1]
            currentFitnessScore = ((currentPosition[0] - endPointCentre[0]) ** 2 + (
                currentPosition[1] - endPointCentre[1]) ** 2) ** (1/2)
            self.populationArray[pos][4] = currentFitnessScore ** -1
            self.tempTotalFitness += value[4]

    def selection(self):
        # Checking if the highest of the fitness score of the new population is higher than the old and updating the tempHighestFitness
        self.populationArray = sorted(
            self.populationArray, key=lambda x: x[4], reverse=True)
        if self.tempHighestFitnessPlayer[4] <= self.populationArray[0][4]:
            self.tempHighestFitnessPlayer = self.populationArray[0].copy()
        # Roulett wheel algorithm, ranking system
        parentsSelected = False
        while not parentsSelected:
            for pos, value in enumerate(self.populationArray):
                randomProbability = random.random()
                selectionProbability = (1 / (pos + 2)) ** 1/2
                # Decide whether to accept compPlayer as new parent
                if randomProbability <= selectionProbability:
                    self.parents.append(value)
                    # Check if there are already 2 parents
                    if len(self.parents) == 2:
                        parentsSelected = True
                        break

    def crossover(self):
        """ One point crossover """
        parent1 = self.parents[0]
        parent2 = self.parents[1]
        for i in range(0, self.populationSize, 2):
            randomSlice = random.randint(1, self.moveCount - 1)
            self.populationArray[i] = [parent1[0][0:randomSlice] + parent2[0][randomSlice:],
                                       self.startingPosition.copy(), [0, 0, 0, 0], [], None]
            self.populationArray[i + 1] = [parent2[0][0:randomSlice] + parent1[0][randomSlice:],
                                           self.startingPosition.copy(), [0, 0, 0, 0], [], None]
        self.parents = []

    def mutation(self):
        """ Mutatation of the population """
        meanNumberOfMutations = self.mutationRate * \
            self.moveCount * self.populationSize
        randomNumberOfMutations = random.randint(
            int(1/2 * meanNumberOfMutations), int(3/2 * meanNumberOfMutations))
        for i in range(randomNumberOfMutations):
            randomCompPlayer = random.randint(0, self.populationSize - 1)
            randomMoveIndex = random.randint(0, self.moveCount - 1)
            moveChoices = ["Up", "Down", "Left", "Right"]
            sameMove = True
            while sameMove:
                newMove = random.choices(
                    moveChoices, weights=[1, 1, 1, 1], k=1)[0]
                if newMove != self.populationArray[randomCompPlayer][0][randomMoveIndex]:
                    self.populationArray[randomCompPlayer][0][randomMoveIndex] = newMove
                    sameMove = False
        # Elitism. Replace a random compPlayer by the highest fitness player
        randomCompPlayerReplacedByTempHighestFitnessPlayer = random.randint(
            0, self.populationSize - 1)
        self.populationArray[randomCompPlayerReplacedByTempHighestFitnessPlayer] = [
            self.tempHighestFitnessPlayer[0], self.startingPosition.copy(), [0, 0, 0, 0], [], None]

    def timeLimitDetection(self, enemy, finishBlit):
        """ Determines whether the time that the user has inputed has been reached """
        if self.moveCount == self.movesLimit and not finishBlit[0]:
            self.tempTotalFitness = 0
            # The rest of the genetic algorithm functions
            self.fitnessScore()
            self.selection()
            self.crossover()
            self.mutation()
            self.moveCount = 0
            self.generation += 1
            if self.movesLimit + int(0.01 * self.movesLimit) <= self.time * self.gameTickFrequency:
                self.movesLimit += int(0.01 * self.movesLimit)
            # Reset position of enemies
            enemy.resetPosition()
        # If whole thing done, reset position of player and keep looping
        if self.moveCount == self.movesLimit and finishBlit[0]:
            for pos, value in enumerate(self.populationArray):
                self.populationArray[pos][1] = self.startingPosition.copy()
                self.moveCount = 0
            enemy.resetPosition()

    # Game section

    def takeMoveInput(self):
        """ Decides compPlayer veloicty """
        for pos, value in enumerate(self.populationArray):
            # Directions - [0] is left, [1] is right, [2] is up, [3] is down
            if value[0][self.moveCount] == "Left":
                value[2][0] = -4
            else:
                value[2][0] = 0
            if value[0][self.moveCount] == "Right":
                value[2][1] = 4
            else:
                value[2][1] = 0
            if value[0][self.moveCount] == "Up":
                value[2][2] = -4
            else:
                value[2][2] = 0
            if value[0][self.moveCount] == "Down":
                value[2][3] = 4
            else:
                value[2][3] = 0
            if "Left" in value[3]:
                value[2][1] = 0
            if "Right" in value[3]:
                value[2][0] = 0
            if "Up" in value[3]:
                value[2][3] = 0
            if "Down" in value[3]:
                value[2][2] = 0

    def move(self, finishBlit):
        """ Moves the compPlayer """
        for pos, value in enumerate(self.populationArray):
            if finishBlit[0] and self.moveCount > self.finalMoveCount:
                pass
            else:
                value[1][0] += value[2][0] + value[2][1]
                value[1][1] += value[2][2] + value[2][3]
                value[3] = []
        if len(self.populationArray) != 0:
            self.moveCount += 1

    def compPlayerEdgeCollision(self, SCREENWIDTH, SCREENHEIGHT):
        """ Ensure that player does not go outside of screen """
        for pos, value in enumerate(self.populationArray):
            if value[1][0] <= 0:
                self.populationArray[pos][2][0] = 0
                self.populationArray[pos][1][0] = 0
            if value[1][0] >= SCREENWIDTH - self.size:
                self.populationArray[pos][2][1] = 0
                self.populationArray[pos][1][0] = SCREENWIDTH - self.size
            if value[1][1] <= 0:
                self.populationArray[pos][2][2] = 0
                self.populationArray[pos][1][1] = 0
            if value[1][1] >= SCREENHEIGHT - self.size:
                self.populationArray[pos][2][3] = 0
                self.populationArray[pos][1][1] = SCREENHEIGHT - self.size

    def compPlayerObstacleCollision(self, obstacles):
        for pos, value in enumerate(self.populationArray):
            for obstacle in obstacles.obstacleArray:
                # If the line is horizontal
                if obstacle[2] == "horizontal":
                    # If the compPlayer's x position is between the line endpoints
                    if value[1][0] >= obstacle[0][0] - self.size and value[1][0] <= obstacle[1][0]:
                        # If the compPlayer's y position is the same as the endpoints. The +sth stuff is just to adjust the collision detection
                        if obstacle[0][1] - value[1][1] < self.size and obstacle[0][1] - value[1][1] > 0:
                            if value[1][0] + self.size - 3 <= obstacle[0][0]:
                                self.populationArray[pos][3].append("Left")
                            elif value[1][0] + 3 >= obstacle[1][0]:
                                self.populationArray[pos][3].append("Right")
                            elif value[1][1] + self.size - 5 >= obstacle[0][1]:
                                self.populationArray[pos][3].append("Down")
                            elif value[1][1] - 3 <= obstacle[0][1]:
                                self.populationArray[pos][3].append("Up")
                else:
                    # If the compPlayer's y position is between the line endpoints
                    if value[1][1] >= obstacle[0][1] - self.size and value[1][1] <= obstacle[1][1]:
                        # If the compPlayer's x position is the same as the endpoints. The +sth stuff is just to adjust the collision detection
                        if obstacle[0][0] - value[1][0] < self.size and obstacle[0][0] - value[1][0] > 0:
                            if value[1][1] + self.size - 3 <= obstacle[0][1]:
                                self.populationArray[pos][3].append("Up")
                            elif value[1][1] + 3 >= obstacle[1][1]:
                                self.populationArray[pos][3].append("Down")
                            elif value[1][0] + self.size - 5 <= obstacle[0][0]:
                                self.populationArray[pos][3].append("Left")
                            elif value[1][0] + 5 >= obstacle[0][0]:
                                self.populationArray[pos][3].append("Right")

    def compPlayerEnemyCollision(self, enemies):
        for pos, value in enumerate(self.populationArray):
            for enemy in enemies.enemyArray:
                # If compPlayer approaching enemy from the left
                if enemy[2][0] + enemies.size > value[1][0] and enemy[2][0] + enemies.size < value[1][0] + self.size:
                    if enemy[2][1] > value[1][1] and enemy[2][1] < value[1][1] + self.size:
                        self.populationArray[pos][1] = self.startingPosition.copy(
                        )
                # If comPlayer approaching enemy from the right
                if enemy[2][0] < value[1][0] + self.size and enemy[2][0] > value[1][0]:
                    if enemy[2][1] > value[1][1] and enemy[2][1] < value[1][1] + self.size:
                        self.populationArray[pos][1] = self.startingPosition.copy(
                        )
                # If compPlayer approaching enemy from the top
                if enemy[2][0] > value[1][0] and enemy[2][0] < value[1][0] + self.size:
                    if enemy[2][1] + self.size > value[1][1] and enemy[2][1] + self.size < value[1][1] + self.size:
                        self.populationArray[pos][1] = self.startingPosition.copy(
                        )
                # If compPlayer approaching enemy from the bottom
                if enemy[2][0] > value[1][0] and enemy[2][0] < value[1][0] + self.size:
                    if enemy[2][1] > value[1][1] and enemy[2][1] < value[1][1] + self.size:
                        self.populationArray[pos][1] = self.startingPosition.copy(
                        )

    def compPlayerEndPointCollision(self, screen, game, finishBlit):
        """ Detect whether the compPlayer has entered the end point """
        if not finishBlit[0]:
            for pos, value in enumerate(self.populationArray):
                # Checking if the player x value is within the end point
                if value[1][0] >= self.startAndEndPoints.endPoint[0] and value[1][0] + self.size <= self.startAndEndPoints.endPoint[0] + self.startAndEndPoints.endPointSize:
                    # Checking if y value is within the end point
                    if value[1][1] >= self.startAndEndPoints.endPoint[1] and value[1][1] + self.size <= self.startAndEndPoints.endPoint[1] + self.startAndEndPoints.endPointSize:
                        self.populationArray = [value]
                        finishBlit[0] = True
                        self.finalMoveCount = self.moveCount
        else:
            text, textRect = screen.initialiseText(
                self, game, "Finish")
            screen.displayFinishText(text, textRect)

import pygame


class Game:
    def __init__(self, tickFrequency):
        self.tickFrequency = tickFrequency
        self.clock = pygame.time.Clock()

    def tick(self):
        """ Ticks time """
        self.clock.tick(self.tickFrequency)

    def eventStore(self, event, previousEvent):
        try:
            return event.pos
        except:
            return previousEvent

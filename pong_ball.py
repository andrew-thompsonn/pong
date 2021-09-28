#!/usr/bin/env python

import pygame

WHITE = (255, 255, 255)
BLUE  = (0,   255,   0)


class PongBall(pygame.sprite.Sprite):

    def __init__(self, coordinates, direction, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.startCoordinates = coordinates
        self.startDirection = direction

        self.__xVelocity = 5
        self.__yVelocity = 0

        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLUE, (25, 25), 25, 0)
        self.rect = self.image.get_rect()


class PongPaddle(pygame.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


FRAME_SIZE = (1000, 600)


class PongEngine:

    def __init__(self):
        self.gameClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(FRAME_SIZE)
        self.fps = 30

        self.ball = PongBall((0, 0), 1)

        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.ball)
        print("Initializing engine")
        self.runGame()


    def runGame(self):
        running = True
        while running:
            self.gameClock.tick(self.fps)
            for event in pygame.event.get():
                running = False if event.type == pygame.QUIT else True

            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()



def main():
    print("In main")
    engine = PongEngine()



if __name__ == "__main__":
    main()

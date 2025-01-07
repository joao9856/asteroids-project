import pygame
import pygame.freetype
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    text_display = pygame.freetype.Font(None, 24)
    scores = Score()
    


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                scores.set_highscore()
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.collision(shot):
                    scores.score_add()
                    asteroid.split()
                    shot.kill()
                    
        
        

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)
        
        
        text_display.render_to(screen, (20,20), f"Score: {str(scores.score)}", "white")
        text_display.render_to(screen, (SCREEN_WIDTH - 200,20), f"Highscore: {str(scores.highscore)}", "white")
        pygame.display.flip()


        #framerate set to 60
        dt = clock.tick(60) / 1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    


if __name__ == "__main__":
    main()
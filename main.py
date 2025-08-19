import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import os

def load_high_score(filename="highscore.txt"):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r") as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def save_high_score(score, filename="highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(score))

def main():
    while True:
        pygame.init()
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0

        pygame.font.init()
        font = pygame.font.SysFont(None, 48)
        small_font = pygame.font.SysFont(None, 36)

        updateable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Player.containers = (updateable, drawable)
        Asteroid.containers = (asteroids, updateable, drawable)
        AsteroidField.containers = (updateable,)
        Shot.containers = (shots, updateable, drawable)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        a_field = AsteroidField()

        score = 0
        high_score = load_high_score()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_high_score(high_score)
                    return

            screen.fill(color="black")
            updateable.update(dt)

            # Check for player collision with asteroids
            player_dead = False
            for a in asteroids:
                if player.check_collision(a):
                    print("Game Over!")
                    player_dead = True

            # Check for shot collision with asteroids and award points
            for a in asteroids:
                for s in shots:
                    if a.check_collision(s):
                        if a.radius == ASTEROID_MAX_RADIUS:
                            score += 10
                        elif a.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS:
                            score += 20
                        elif a.radius == ASTEROID_MIN_RADIUS:
                            score += 30
                        else:
                            score += 10  # fallback

                        a.split()
                        s.kill()

            # Handle game over and high score
            if player_dead:
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

                # Display Game Over and summary
                game_over_text = font.render("Game Over!", True, (255, 0, 0))
                score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
                high_score_text = small_font.render(f"High Score: {high_score}", True, (255, 255, 0))
                restart_text = small_font.render("Press Enter to restart", True, (200, 200, 200))

                screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 80))
                screen.blit(score_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
                screen.blit(high_score_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 20))
                screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 80))
                pygame.display.flip()

                # Wait for Enter key to restart or quit
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            save_high_score(high_score)
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                waiting = False
                    pygame.time.wait(50)

                running = False  # Break inner game loop to restart

            else:
                for i in drawable:
                    i.draw(screen)

                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 0))
                screen.blit(score_text, (20, 10))
                screen.blit(high_score_text, (SCREEN_WIDTH - 300, 10))

                pygame.display.flip()
                dt = clock.tick(144) / 1000

if __name__ == "__main__":
    main()

# pyright: basic
from Assets.assets import Assets
from player import Player
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    pygame.mixer.init()
    assets = Assets()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable]
    Shot.containers = [shots, updatable, drawable]

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        draw_ui(screen, player)

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            for shot in shots:
                if ast.is_colliding(shot):
                    ast.split(player)
                    shot.kill()

            if ast.is_colliding(player):
                player.die()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        pygame.display.set_caption(f"Asteroids, Score: {player.score}")

def draw_ui(screen, player):
    mainfont = Assets.get_instance().fonts.fonts.get("inter")

    lives_text = f"Lives: {player.lives}"
    score_text = f"Score: {player.score}"

    rightoffset = 40 * SCALE_FACTOR
    leftoffset = 40 * SCALE_FACTOR

    lives_surface = mainfont.render(lives_text, True, (255, 255, 255))
    lives_x = SCREEN_WIDTH - lives_surface.get_width() - rightoffset
    lives_y = 10 * SCALE_FACTOR
    screen.blit(lives_surface, (lives_x, lives_y))

    score_color = (255, 255, 255) if player.score < 50 else (255, 215, 0) if player.score < 100 else (255, 0, 0)
    score_surface = mainfont.render(score_text, True, score_color)
    score_y = lives_y + lives_surface.get_height() + 5
    screen.blit(score_surface, (lives_x, score_y))

    heart_image = Assets.get_instance().textures.images.get("heart")
    if heart_image:
        scaled_heart = pygame.transform.scale(heart_image, (int(20 * SCALE_FACTOR), int(20 * SCALE_FACTOR)))
        heart_width = scaled_heart.get_width()
        heart_height = scaled_heart.get_height()

        heart_x = leftoffset
        heart_y = 30 * SCALE_FACTOR

        for i in range(player.lives):
            screen.blit(scaled_heart, (heart_x + i * (heart_width + 5), heart_y))


if __name__ == "__main__":
    main()

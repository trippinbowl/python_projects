import pygame
import random
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scrum Master Selection")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 105, 180), (255, 255, 0), (0, 255, 255), (173, 216, 230), (0, 128, 0), (255, 165, 0), (128, 0, 128)]
CONFETTI_COUNT = 1000
MAX_FALL_SPEED = 5
SWAY_RANGE = 3

drum_sound = pygame.mixer.Sound('drum_roll.wav')  # Ensure you have a drum_roll.wav file


def play_drum_roll():
    pygame.mixer.Sound.play(drum_sound)
    start_time = time.time()
    while time.time() - start_time < 5:
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 48)
        text = font.render('Drum rolling...', True, WHITE)
        text_rect = text.get_rect(center=(width / 2, height / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
    pygame.mixer.Sound.stop(drum_sound)


def throw_confetti():
    confetti = [{
        'x': random.randint(0, width),
        'y': 0,
        'color': random.choice(COLORS),
        'size': random.randint(3, 8),
        'fall_speed': random.random() * MAX_FALL_SPEED + 1,
        'sway': random.random() * SWAY_RANGE - SWAY_RANGE / 2,
        'sway_speed': random.random() * 0.1 + 0.05
    } for _ in range(CONFETTI_COUNT)]

    while min(c['y'] for c in confetti) < height:
        screen.fill(BLACK)

        for piece in confetti:
            piece['x'] += piece['sway']
            piece['y'] += piece['fall_speed']
            piece['sway'] += piece['sway_speed']

            if abs(piece['sway']) > SWAY_RANGE / 2:
                piece['sway_speed'] *= -1

            pygame.draw.circle(screen, piece['color'], (int(piece['x']), int(piece['y'])), piece['size'])

        font = pygame.font.SysFont(None, 48)
        text = font.render(f'{next_scrum_master} is the new Scrum Master!', True, WHITE)
        text_rect = text.get_rect(center=(width / 2, height - 50))
        screen.blit(text, text_rect)

        pygame.display.flip()
        time.sleep(0.01)  # Adjust for smoother or faster animation


def main():
    global next_scrum_master
    running = True
    master = ["Rudhvik", "Shubham", "Divya"]
    next_scrum_master = random.choice(master)

    play_drum_roll()
    throw_confetti()

    # Wait for a key press or window close to exit
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()

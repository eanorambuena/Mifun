from engine.body import         *
from engine.core import         *
from engine.math_utils import   *
from engine.render import       *

def load2screen(screen, file_name = "result.png"):
    import  pygame
    bg = pygame.image.load(file_name).convert()
    screen.blit(bg, (0, 0))
    pygame.display.flip()

import pygame

BLACK = (0, 0, 0)

def render(game):
    pre_render(game)
    render_pixels(game)
    post_render(game)

def pre_render(game):
    game.screen.fill(BLACK)

def post_render(game):
    pygame.display.flip()
    game.clock.tick(60)

def render_pixels(game):
    for coords, pix in game.state.get_pixels().items():
        game.screen.set_at(coords, pix.color)


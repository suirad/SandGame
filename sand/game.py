import os
import pygame
from sand import events, logic, render
from sand.stype import sandbit, water, fire, stone


class Game(object):
    def __init__(self, config):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.state, self.screen = GameState(config), None
        self.size = self.width, self.height = 640, 480
        self.clock = pygame.time.Clock()
    def quit(self):
        pygame.quit()
    def init(self):
        self.refresh_title()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    def events(self):
        events.events(self)
    def logic(self):
        logic.logic(self)
    def render(self):
        render.render(self)
    def is_running(self):
        return self.state.is_running()
    def refresh_title(self):
        title = "Sand Game - Element: {} | Pen size: {} | Sources: {}".format(
            self.state.meta['current'].capitalize(),
            self.state.meta['pen'],
            self.state.meta['source_flow']
        )
        if self.state.meta['pause']:
            title += " | PAUSED"
        pygame.display.set_caption(title)

class GameState(object):
    def __init__(self, config):
        self.meta = dict()
        self.meta["running"] = True
        self.meta['pause'] = False
        self.meta['pix'] = dict()
        self.meta['pen'] = config['initial_pen']
        self.meta['bounds'] = config['bounds']
        self.meta['current'] = config['starting_element']
        self.meta['types'] = config['elements']
        self.meta['source_flow'] = config['sources_enabled']
        self.meta['sources'] = config['element_sources']
    def is_running(self):
        return self.meta["running"]
    def set_running(self, run):
        self.meta["running"] = run
    def get_pixels(self):
        return self.meta['pix']
    def change_type(self, dir):
        if dir is True:
            keys = list(self.meta['types'].keys())
            nexttype = keys[keys.index(self.meta['current'])-1]
            self.meta['current'] = nexttype
        else:
            keys = list(self.meta['types'].keys())
            nexttype = keys[(keys.index(self.meta['current'])+1) % len(keys)] # % len(keys) resets access to 0 once we bust index
            self.meta['current'] = nexttype



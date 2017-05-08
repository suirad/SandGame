import pygame
import random

def logic(game):
    if game.state.meta['pause']:
        return
    allpix = game.state.meta['pix']
    tick_pix(game, allpix)
    tick_sources(game, allpix)

def tick_pix(game, allpix):
    for coords in list(allpix.keys()):
        pix = allpix[coords]
        newcoords = pix.tick(coords, allpix)
        if newcoords == (-1, -1):
            del allpix[coords]
            continue
        elif newcoords == coords:
            continue
        elif (newcoords[0] < 0 or newcoords[0] > game.width-1) or \
                (newcoords[1] < 0 or newcoords[1] > game.height-1):
            if not game.state.meta['bounds']:
                del allpix[coords]
            continue
        neighbor = allpix.get(newcoords)
        if neighbor is None:
            allpix[newcoords] = pix
            del allpix[coords]
            continue
        if pix.interact(coords, newcoords, neighbor, allpix) is True:
            allpix[newcoords] = pix
            del allpix[coords]

def tick_sources(game, allpix):
    if not game.state.meta['source_flow']:
        return
    for cord, source in game.state.meta['sources'].items():
        coord = random.randint(cord[0], cord[0] + 10), cord[1]
        if allpix.get(coord) is None:
            allpix[coord] = game.state.meta['types'][source].clone()

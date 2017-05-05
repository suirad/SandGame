import pygame as pg
from sand.stype import sandbit

def events(game):
    game_events(game)
    mouse_events(game)

def game_events(game):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.state.set_running(False)
            break
        config_event(game, event)

def config_event(game, event):
    if event.type == pg.KEYUP and event.key == pg.K_c:
        game.state.get_pixels().clear()
    elif event.type == pg.KEYUP and event.key == pg.K_b:
        game.state.meta['bounds'] = not game.state.meta['bounds']
    elif event.type == pg.KEYUP and event.key == pg.K_1:
        game.state.meta['pen'] = 1
        game.refresh_title()
    elif event.type == pg.KEYUP and event.key == pg.K_2:
        game.state.meta['pen'] = 2
        game.refresh_title()
    elif event.type == pg.KEYUP and event.key == pg.K_3:
        game.state.meta['pen'] = 3
        game.refresh_title()
    elif event.type == pg.KEYUP and event.key == pg.K_s:
        game.state.meta['source_flow'] = not game.state.meta['source_flow']
        game.refresh_title()
    elif event.type == pg.KEYUP and event.key == pg.K_p:
        game.state.meta['pause'] = not game.state.meta['pause']
        game.refresh_title()
    elif event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 4:
            game.state.change_type(True)
            game.refresh_title()
        elif event.button == 5:
            game.state.change_type(False)
            game.refresh_title()

def mouse_events(game):
    if pg.mouse.get_pressed()[0] == 1: #left click
        mpos = pg.mouse.get_pos()
        pix = game.state.meta['types'][game.state.meta['current']]
        if game.state.meta['pen'] is 1:
            game.state.get_pixels()[mpos] = pix.clone()
        elif game.state.meta['pen'] is 2:
            points = [
                (mpos[0]-1, mpos[1]-1), (mpos[0], mpos[1]-1), (mpos[0]+1, mpos[1]-1),
                (mpos[0]-1, mpos[1]), (mpos[0], mpos[1]), (mpos[0]+1, mpos[1]),
                (mpos[0]-1, mpos[1]+1), (mpos[0], mpos[1]+1), (mpos[0]+1, mpos[1]+1),
            ]
            for point in points:
                if point[0] >= 0 and point[0] < game.width and \
                        point[1] >= 0 and point[1] < game.height:
                    game.state.get_pixels()[point] = pix.clone()
        elif game.state.meta['pen'] is 3:
            points = [
                (mpos[0]-2, mpos[1]-2), (mpos[0]-1, mpos[1]-2), (mpos[0], mpos[1]-2), (mpos[0]+1, mpos[1]-2), (mpos[0]+2, mpos[1]-2),
                (mpos[0]-2, mpos[1]-1), (mpos[0]-1, mpos[1]-1), (mpos[0], mpos[1]-1), (mpos[0]+1, mpos[1]-1), (mpos[0]+2, mpos[1]-1),
                (mpos[0]-2, mpos[1]), (mpos[0]-1, mpos[1]), (mpos[0], mpos[1]), (mpos[0]+1, mpos[1]), (mpos[0]+2, mpos[1]),
                (mpos[0]-2, mpos[1]+1), (mpos[0]-1, mpos[1]+1), (mpos[0], mpos[1]+1), (mpos[0]+1, mpos[1]+1), (mpos[0]+2, mpos[1]+1),
                (mpos[0]-2, mpos[1]+2), (mpos[0]-1, mpos[1]+2), (mpos[0], mpos[1]+2), (mpos[0]+1, mpos[1]+2), (mpos[0]+2, mpos[1]+2),
            ]
            for point in points:
                if point[0] >= 0 and point[0] < game.width and \
                        point[1] >= 0 and point[1] < game.height:
                    game.state.get_pixels()[point] = pix.clone()
    elif pg.mouse.get_pressed()[2] == 1:
        allpix = game.state.get_pixels()
        mpos = pg.mouse.get_pos()
        if game.state.meta['pen'] is 1:
            if allpix.get(mpos) is not None:
                del allpix[mpos]
        elif game.state.meta['pen'] is 2:
            points = [
                (mpos[0]-1, mpos[1]-1), (mpos[0], mpos[1]-1), (mpos[0]+1, mpos[1]-1),
                (mpos[0]-1, mpos[1]), (mpos[0], mpos[1]), (mpos[0]+1, mpos[1]),
                (mpos[0]-1, mpos[1]+1), (mpos[0], mpos[1]+1), (mpos[0]+1, mpos[1]+1),
            ]
            for point in points:
                if allpix.get(point) is not None:
                    del allpix[point]
        elif game.state.meta['pen'] is 3:
            points = [
                (mpos[0]-2, mpos[1]-2), (mpos[0]-1, mpos[1]-2), (mpos[0], mpos[1]-2), (mpos[0]+1, mpos[1]-2), (mpos[0]+2, mpos[1]-2),
                (mpos[0]-2, mpos[1]-1), (mpos[0]-1, mpos[1]-1), (mpos[0], mpos[1]-1), (mpos[0]+1, mpos[1]-1), (mpos[0]+2, mpos[1]-1),
                (mpos[0]-2, mpos[1]), (mpos[0]-1, mpos[1]), (mpos[0], mpos[1]), (mpos[0]+1, mpos[1]), (mpos[0]+2, mpos[1]),
                (mpos[0]-2, mpos[1]+1), (mpos[0]-1, mpos[1]+1), (mpos[0], mpos[1]+1), (mpos[0]+1, mpos[1]+1), (mpos[0]+2, mpos[1]+1),
                (mpos[0]-2, mpos[1]+2), (mpos[0]-1, mpos[1]+2), (mpos[0], mpos[1]+2), (mpos[0]+1, mpos[1]+2), (mpos[0]+2, mpos[1]+2),
            ]
            for point in points:
                if allpix.get(point) is not None:
                    del allpix[point]


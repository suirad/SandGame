from sand import game
import config

def main():
    thisgame = game.Game(config.GAMECONFIG)
    try:
        thisgame.init()
        while thisgame.is_running():
            thisgame.events()
            thisgame.logic()
            thisgame.render()
    finally:
        thisgame.quit()

if __name__ == "__main__":
    main()
    exit()

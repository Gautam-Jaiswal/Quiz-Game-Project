from game_window import Game

if __name__ == '__main__':
    #Checking if the file is already present or not
    try:
        with open('highscore.txt', 'r') as file:
            file.readline()
    except FileNotFoundError:
        with open('highscore.txt', 'w') as file:
            file.write(str(0))
    Game()

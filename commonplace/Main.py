from commonplace.Generate import generate_all
from commonplace.Game import PoemGame

def main():
    "Generates and runs the game."
    game_map, game_player = generate_all()
    name = "The Commonplace"
    with open('./commonplace/description.txt') as description_file:
        description = description_file.readlines()
    game = PoemGame(name, description, game_map, game_player)
    game.play_game()

if __name__ == '__main__':
    main()

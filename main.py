from game import Game
from engine import Engine
from board import Board

import berserk
from tokens import API_TOKEN, PUZZLE_ID

def main():
    game = Game()

    # FIXME Fix this code up a bit! (class Game methods should not be accessed like this)
    fen = load_puzzle_FEN()
    game.board_history = [fen]
    game.board.load_FEN(fen)
    game.start_new_turn()
    
    game.run()

def load_puzzle_FEN():
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)

    #breakpoint()

    puzzle = client.puzzles.get(PUZZLE_ID)
    return puzzle["puzzle"]["fen"]

if __name__ == "__main__":
    main()

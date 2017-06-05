# Game here...
from board import Board, AlreadyFilledException, BadBoardPositionException

print("Hello! It's Tic Tac Toe!")
game = Board()

while True:
    # Computer
    b = game.choose_pos()
    game._board = b

    if Board.check_status(game._board) is not None:
        if Board.check_status(game._board) == "X":
            print("WIN COMPUTER")
        else:
            print("WIN PLAYER")
        break

    print(game)

    # Player
    if game.is_free_cell():
        while True:
            posx = input("Enter x position(1, 2, 3): ")
            posy = input("Enter y position(1, 2, 3): ")

            try:
                game.put([int(posx) - 1, int(posy) - 1], Board.USER_MARK)
                break

            except BadBoardPositionException:
                print("Bad Position")
            except AlreadyFilledException:
                print("Already Filled")

            if Board.check_status(game._board) is not None:
                if Board.check_status(game._board) == "X":
                    print("WIN COMPUTER")
                else:
                    print("WIN PLAYER")
                break

    else:
        print("50% 50%)))")


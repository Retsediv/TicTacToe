# Game here...
from board import Board, AlreadyFilledException, BadBoardPositionException

print("Hello! It's Tic Tac Toe!")
game = Board()

while True:
    # Computer
    b = game.choose_pos()
    game._board = b

    print(game)

    # Player
    if game.is_free_cell():
        while True:
            posx = input("Enter x position")
            posy = input("Enter y position")

            try:
                game.put([int(posx), int(posy)], Board.USER_MARK)
                break

            except BadBoardPositionException:
                print("Bad Position")
            except AlreadyFilledException:
                print("Already Filled")

            if Board.check_status(game._board) is not None:
                print(Board.check_status(game._board))
    else:
        # 50 50
        print("50% 50%)))")


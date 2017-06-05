class Board:
    def __init__(self):
        """
        Create new instance of Board for playing tic-tac-toe game
        """
        self._board = [[None, None, None], [None, None, None], [None, None, None]]
        self.lastPosition = [None, None]
        self.lastMark = None

    def __str__(self):
        for line in self._board:
            for i in line:
                if i is None:
                    print(" ", end="")
                else:
                    print(i, end=" ")

            print()

    def check_status(self):
        for i in range(3):
            # horizontal
            if self._board[i][0] == self._board[i][1] == self._board[i][2] and self._board[i][0] is not None:
                return self._board[i][0]

            # vertical
            if self._board[0][i] == self._board[1][i] == self._board[2][i] and self._board[0][i] is not None:
                return self._board[0][i]

        # cross
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[2][2] is not None:
            return self._board[2][2]

        # cross
        if self._board[2][0] == self._board[1][1] == self._board[0][2] and self._board[0][2] is not None:
            return self._board[0][2]

    def put(self, position, mark):
        if 0 > position[0] > 2 or 0 > position[1] > 2:
            raise BadBoardPositionException("Bad position of mark")

        if self._board[position[0]][position[1]] is not None:
            raise AlreadyFilledException("This position is already filled")

        self._board[position[0]][position[1]] = mark

    def build_tree(self):
        pass

    def choose_pos(self):
        pass


class BadBoardPositionException(Exception):
    pass


class AlreadyFilledException(Exception):
    pass

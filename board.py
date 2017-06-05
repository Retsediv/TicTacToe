import copy
from btnode import BSTNode
from btree import LinkedBST
import random
import sys

sys.setrecursionlimit(100000)


class Board:
    """
    Class represents a board for playing
    Tic Tac Toe Game
    Here we have basic computer intelligence based on binary tree from variants
    """

    USER_MARK = "O"
    COMPUTER_MARK = "X"

    def __init__(self):
        """
        Create new instance of Board for playing tic-tac-toe game
        """
        self._board = [[None, None, None], [None, None, None], [None, None, None]]
        self.lastPosition = [None, None]
        self.lastMark = None

    def __str__(self):
        """
        String representation of board

        :return str:
        """
        s = ""
        for line in self._board:
            for i in line:
                if i is None:
                    s += " "
                else:
                    s += i + " "
            s += "\n"

        return s

    @staticmethod
    def check_status(board):
        """
        Check status of board. Are there winner or no?

        :param list[list] board:
        :return str: mark of winner
        """
        for i in range(3):
            # horizontal
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return [i][0]

            # vertical
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]

        # cross
        if board[0][0] == board[1][1] == board[2][2] and board[2][2] is not None:
            return board[2][2]

        # cross
        if board[2][0] == board[1][1] == board[0][2] and board[0][2] is not None:
            return board[0][2]

        return None

    def put(self, position, mark):
        """
        Check conditionals and put mark on the board

        :param list[int, int] position:
        :param str mark: str
        :return None:
        """
        if 0 > position[0] > 2 or 0 > position[1] > 2:
            raise BadBoardPositionException("Bad position of mark")

        if self._board[position[0]][position[1]] is not None:
            raise AlreadyFilledException("This position is already filled")

        self._board[position[0]][position[1]] = mark

    def build_tree(self, board):
        """
        Build binary game tree

        :param board:
        :return: BinaryTree
        """
        tree = LinkedBST()
        tree.add(board)

        playComputer = False
        if self.lastMark == Board.USER_MARK or self.lastMark is None:
            playComputer = True

        def process(node, playComputer):
            is_free = bool(max([cell is None for line in node.data for cell in line]))
            if not is_free:
                return

            # LEFT
            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if 0 > position[0] > 2 or 0 > position[1] > 2 or node.data[position[0]][position[1]] is not None:
                    continue
                else:
                    break

            if Board.check_status(node.data) is not None:
                return

            new_board = copy.deepcopy(node.data)
            new_board[position[0]][position[1]] = Board.COMPUTER_MARK if playComputer else Board.USER_MARK

            node.left = BSTNode(new_board)

            # RIGHT
            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if 0 > position[0] > 2 or 0 > position[1] > 2 or node.data[position[0]][position[1]] is not None:
                    continue
                else:
                    break

            if Board.check_status(node.data) is not None:
                return

            new_board = copy.deepcopy(node.data)
            new_board[position[0]][position[1]] = Board.COMPUTER_MARK if playComputer else Board.USER_MARK

            node.right = BSTNode(new_board)

            playComputer = not playComputer

            process(node.left, playComputer)
            process(node.right, playComputer)

        process(tree._root, playComputer)

        return tree

    def choose_pos(self):
        """
        Choose next step by computer based on binary tree

        :return list:
        """
        tree = self.build_tree(self._board)

        def count(node):
            if node.right is None and node.left is None:
                if Board.check_status(node.data) == Board.COMPUTER_MARK:
                    return 1
                elif Board.check_status(node.data) == Board.USER_MARK:
                    return -1
                else:
                    return 0

            return count(node.left) + count(node.right)

        count_left = count(tree._root.left)
        count_right = count(tree._root.right)

        if count_right > count_left:
            return tree._root.right.data
        else:
            return tree._root.left.data

    def is_free_cell(self):
        is_free = bool(max([cell is None for line in self._board for cell in line]))
        return is_free


class BadBoardPositionException(Exception):
    pass


class AlreadyFilledException(Exception):
    pass


board = Board()
board._board = [["O", "O", "O"], [None, None, None], [None, None, None]]
print(Board.check_status(board._board))
# print(board.choose_pos())
# print(tree._root.data)
# print(tree._root.left.data)
# print(tree._root.right.data)

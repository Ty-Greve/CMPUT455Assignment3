#!/usr/bin/python3
# Set the path to your python3 above

"""
Go0 random Go player
Cmput 455 sample code
Written by Cmput 455 TA and Martin Mueller

--- A3 ---
V1
Added FlatMonteCarloPlayer class
imported form board_base
change state.toPlay to state.current_player
FlatMonteCarlo Moved
Part 1 done
---
V2 (Part2)
finished part 2
---
V3 
Fixed edge case mentioned in assignment 3 update for the class
Should be Completed
---
"""

from gtp_connection import GtpConnection
from board_base import DEFAULT_SIZE, GO_POINT, GO_COLOR
from board import GoBoard
from board_util import GoBoardUtil
from engine import GoEngine
from board_base import EMPTY, BLACK, WHITE


class Go0(GoEngine):
    def __init__(self) -> None:
        """
        Go player that selects moves randomly from the set of legal moves.
        Does not use the fill-eye filter.
        Passes only if there is no other legal move.
        """
        GoEngine.__init__(self, "Go0", 1.0)

    def get_move(self, board: GoBoard, color: GO_COLOR) -> GO_POINT:
        return GoBoardUtil.generate_random_move(board, color, 
                                                use_eye_filter=False)
    
    def solve(self, board: GoBoard):
        """
        A2: Implement your search algorithm to solve a board
        Change if deemed necessary
        """
        pass


def run() -> None:
    """
    start the gtp connection and wait for commands.
    """
    board: GoBoard = GoBoard(DEFAULT_SIZE) #DEFAULT_SIZE
    con: GtpConnection = GtpConnection(Go0(), board)
    con.start_connection()


if __name__ == "__main__":
    run()

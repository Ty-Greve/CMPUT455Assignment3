#!/usr/bin/python3
# Set the path to your python3 above

"""
Go0 random Go player
Cmput 455 sample code
Written by Cmput 455 TA and Martin Mueller
"""
from gtp_connection import GtpConnection
from board_base import DEFAULT_SIZE, GO_POINT, GO_COLOR
from board import GoBoard
from board_util import GoBoardUtil
from engine import GoEngine
#from game_basics import EMPTY, BLACK, WHITE

class FlatMonteCarloPlayer(object):
    def __init__(self, numSimulations):
        self.numSimulations = numSimulations

    def name(self):
        return "Flat Monte Carlo Player ({0} sim.)".format(self.numSimulations)

    def genmove(self, state): #this should not be state, all instancesneed to be change
        assert not state.end_of_game()
        moves = state.legalMoves()
        numMoves = len(moves)
        score = [0] * numMoves
        for i in range(numMoves):
            move = moves[i]
            score[i] = self.simulate(state, move)
        bestIndex = score.index(max(score))
        best = moves[bestIndex]
        assert best in state.legalMoves()
        return best

    def simulate(self, state, move):
        stats = [0] * 3
        state.play(move)
        moveNr = state.moveNumber()
        for _ in range(self.numSimulations):
            winner, _ = state.simulate()
            stats[winner] += 1
            state.resetToMoveNumber(moveNr)
        assert sum(stats) == self.numSimulations
        assert moveNr == state.moveNumber()
        state.undoMove()
        eval = (stats[BLACK] + 0.5 * stats[EMPTY]) / self.numSimulations
        if state.toPlay == WHITE:
            eval = 1 - eval
        return eval

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
    board: GoBoard = GoBoard(DEFAULT_SIZE)
    con: GtpConnection = GtpConnection(Go0(), board)
    con.start_connection()


if __name__ == "__main__":
    run()

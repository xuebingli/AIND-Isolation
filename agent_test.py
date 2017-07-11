"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
from importlib import reload

import isolation
import game_agent
import sample_players


def play_game(player1, player2, logging=False):
    """Play a game and return the winner with optional logging
    """
    game = isolation.Board(player1, player2)
    # place player 1 on the board at row 2, column 3, then place player 2 on
    # the board at row 0, column 5; display the resulting board state
    game.apply_move((2, 3))
    game.apply_move((0, 5))
    if logging:
        print(game.to_string())
    # players take turns moving on the board, so player1 should be next to move
    assert player1 == game.active_player
    # get a list of the legal moves available to the active player
    if logging:
        print(game.get_legal_moves())
    # get a successor of the current state by making a copy of the board and
    # applying a move.
    new_game = game.forecast_move((1, 1))
    assert new_game.to_string() != game.to_string()
    if logging:
        print("\nOld state:\n{}".format(game.to_string()))
        print("\nNew state:\n{}".format(new_game.to_string()))
    # play the remainder of the game automatically -- outcome can be "illegal
    # move", "timeout", or "forfeit"
    winner, history, outcome = game.play()
    if logging:
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))
    return winner

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

    def test_minimax_against_greedy_1(self):
        """Minimax player as player 1 and greedy player as player 2
        """
        greedy_player = sample_players.GreedyPlayer(score_fn=sample_players.open_move_score)
        minimax_player = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        winner = play_game(player1=minimax_player, player2=greedy_player)
        self.assertEqual(winner, minimax_player)

    def test_minimax_against_greedy_2(self):
        """Greedy player as player 1 and minimax player as player 2
        """
        greedy_player = sample_players.GreedyPlayer(score_fn=sample_players.open_move_score)
        minimax_player = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        winner = play_game(player1=greedy_player, player2=minimax_player)
        self.assertEqual(winner, minimax_player)

    def test_alphabeta_against_greedy_1(self):
        """Alphabeta player as player 1 and greedy player as player 2
        """
        greedy_player = sample_players.GreedyPlayer(score_fn=sample_players.center_score)
        alphabeta_player = game_agent.AlphaBetaPlayer(score_fn=sample_players.center_score)
        winner = play_game(player1=alphabeta_player, player2=greedy_player)
        self.assertEqual(winner, alphabeta_player)

    def test_alphabeta_against_greedy_2(self):
        """Greedy player as player 1 and alphabeta player as player 2
        """
        greedy_player = sample_players.GreedyPlayer(score_fn=sample_players.center_score)
        alphabeta_player = game_agent.AlphaBetaPlayer(score_fn=sample_players.center_score)
        winner = play_game(player1=greedy_player, player2=alphabeta_player)
        self.assertEqual(winner, alphabeta_player)

if __name__ == '__main__':
    unittest.main()

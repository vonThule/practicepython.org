#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/17/2018
    Date last modified: 8/3/2018
    Python version: 3.6.5
    Description:
        Problem #26: Check Tic Tac Toe from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Check game results
def check_result(game):
    if game[1][1] != 0:
        first_diagonal = set([game[0][0], game[1][1], game[2][2]])
        second_diagonal = set([game[0][2], game[1][1], game[2][0]])
        if len(first_diagonal) == 1 or len(second_diagonal) == 1:
            return game[1][1]
    transposed = zip(*game)
    for row in transposed:
        game.append(row)
    for row in game:
        row_set = set(row)
        if len(row_set) == 1 and row[0] != 0:
            return row[0]
    return 0


# Main function
def main(games):
    i = 1
    for game in games:
        result = check_result(game)
        print("Game no.{}: {}".format(i, game))
        if result == 1 or result == 2:
            print("Result: Player {} wins!".format(result))
        else:
            print("Result: It's a draw.")
        i += 1


# Run program
if __name__ == "__main__":
    # Create several game results to check
    # Winner is 1
    game1 = [[1, 2, 0],
             [2, 1, 0], 
             [2, 1, 1]]

    # Winner is 2
    game2 = [[2, 2, 0],
             [2, 1, 0], 
             [2, 1, 1]]

    # Winner is 1
    game3 = [[0, 1, 0],
             [2, 1, 0], 
             [2, 1, 1]]

    # No winner
    game4 = [[1, 2, 0],
             [2, 1, 0], 
             [2, 1, 2]]

    # No winner
    game5 = [[1, 2, 0],
             [2, 1, 0], 
             [2, 1, 0]]

    games = [game1, game2, game3, game4, game5]
    main(games)


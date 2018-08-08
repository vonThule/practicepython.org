#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/13/2018
    Date last modified: 8/8/2018
    Python version: 3.6.5
    Description:
        Problem #8: Rock Paper Scissors from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user choice function
def player_choice(player):
    print("\n[{}]:".format(player))
    print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
    while True:
        try:
            player_input = int(input("Your choice >>> "))
            # player_input must be a number between 1 and 4
            if player_input >= 1 and player_input <= 4:
                break
            # If not, inform the player and ask for another input
            else:
                print("You must enter a number between 1 and 4.\nPlease try again...")
        # If player_input not an integer, catch exception and inform player
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
    return player_input


# Check result of game and display the result string
def check_result(pl1choice, pl2choice):
    if (pl1choice == 1 and pl2choice == 2 or
        pl1choice == 2 and pl2choice == 3 or
        pl1choice == 3 and pl2choice == 1):
        print("\nPlayer 2 wins!\n")
    elif (pl1choice == 1 and pl2choice == 3 or
          pl1choice == 2 and pl2choice == 1 or
          pl1choice == 3 and pl2choice == 2):
        print("\nPlayer 1 wins!\n")
    else:
        print("\nIt's a tie!\n")


# Ask if players want another game and return the answer
def another_game():
    while True:
        new = input("New game? (y/n) >> ")
        # If input is not 'y' or 'n' inform players and ask for another input
        if new.lower() != "y" and new.lower() != "n":
            print("You didn't input the right choice.\nPlease try again...")
        else:
            break
    return new


# Main function
def main():
    print("\n=========================================")
    print("||        ROCK, PAPER, SCISSORS        ||")
    print("=========================================")
    while True:
        pl1 = player_choice("Player 1")
        if pl1 == 4:
            break
        pl2 = player_choice("Player 2")
        if pl2 == 4:
            break
        result = check_result(pl1, pl2)
        again = another_game()
        if again == "n":
            break


# Run program
if __name__ == "__main__":
    main()


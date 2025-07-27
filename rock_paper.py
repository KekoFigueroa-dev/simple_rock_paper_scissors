"""
Rock, Paper, Scissors Game

A console-based implementation of the classic Rock, Paper, Scissors game.
Players compete against computer AI over multiple rounds with score tracking
and win/loss determination based on traditional game rules.

Author: KekoFigueroa-Dev
"""
import random


#Welcome message
print("Welcome to a game of Rock, Paper, Scissors")

#get rounds variable
while True:
    try:
        rounds = int(input("\nHow many rounds would you like to play?: "))
        if rounds > 0:
            break
        else:
            print("Please enter a whole positive number")
    except ValueError as e:
        print("Please enter a whole positive number")

# Initialize game variables
moves = ['rock','paper','scissors']
p_score = 0
c_score = 0

#Main game loop
for game_round in range(rounds):
    #Print main game screen/get user input
    print(f"\nRound {game_round + 1}")
    print(f"\nPlayer {p_score} \tComputer {c_score}")
    
    #Computer move
    c_index = random.randint(0,2)
    c_choice = moves[c_index]

    #Player move
    p_choice = input("Time to pick...rock, paper, scissors: ").strip().lower()

    #If player makes a valid move check
    if p_choice in moves:
        print(f"\tComputer: {c_choice}")
        print(f"\tPlayer: {p_choice}")
        # computer chooses rock
        if p_choice == "rock" and c_choice == "rock":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif p_choice == "paper" and c_choice == "rock":
            winner = "player"
            phrase = "Paper covers rock!"
        elif p_choice == "scissors" and c_choice == "rock":
            winner = "computer"
            phrase = "Rock smashes scissors!"

        #Computer chooses paper
        elif p_choice == "rock" and c_choice == "paper":
            winner = "computer"
            phrase = "Paper covers rock!"
        elif p_choice == "paper" and c_choice == "paper":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif p_choice == "scissors" and c_choice == "paper":
            winner = "player"
            phrase = "Scissors cut paper!"

        #Computer chooses Scissors
        elif p_choice == "rock" and c_choice == "scissors":
            winner = "player"
            phrase = "Rock smashes scissors!"
        elif p_choice == "paper" and c_choice == "scissors":
            winner = "computer"
            phrase = "Scissors cut paper!"
        elif p_choice == "scissors" and c_choice == "scissors":
            winner = "tie"
            phrase = "It is a tie, how boring!"

        #Catch for other conditions
        else:
            print("Round Winner can't be determined")
            winner = "tie"
            phrase = "It is a tie, how boring!"


        #Display round results
        print(f"\t{phrase}")
        if winner == 'player':
            print(f"\tYou win round {game_round + 1}")
            p_score += 1
        elif winner == 'computer':
            print(f"\tComputer wins round {game_round + 1}")
            c_score += 1
        else:
            print("\tThis round was a tie.")
    
    #Else the player did not make valid move
    else:
        print("That is not a valid option")
        print("Computer gets the point")
        c_score += 1

#Game has ended, print results
print("\nFinal Game Results")
print(f"\tRounds Played {rounds}")
print(f"\tPlayer Score: {p_score}")
print(f"\tComputer Score: {c_score}")

if p_score > c_score:
    print("\tWinner: PLAYER!")
    print("\tCongratulations! You are the champion of Rock, Paper, Scissors!")
elif c_score > p_score:
    print("\tWinner: Computer :'c")
    print("\tThe computer has defeated you in Rock, Paper, Scissors.  AI is TAKING OVER!")
else:
    print(f"Incredible! After {rounds} rounds the result is a TIE!!!")
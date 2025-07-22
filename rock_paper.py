import random
#Rock Paper Scissors

#Welcome message
print("Welcome to a game of Rock, Paper, Scissors")

#get rounds variable
rounds = int(input("\nHow many rounds would you like to play?: "))

#Initializing variables
moves = ['rock','paper','scissors']
p_score = 0
c_score = 0

#Main game loop
for game_round in range(rounds):
    #Print main game screen/get user input
    print("\nRound " + str(game_round + 1))
    print("\nPlayer: " + str(p_score) + "\tComputer " + str(c_score))
    
    #Computer move
    c_index = random.randint(0,2)
    c_choice = moves[c_index]

    #Player move
    p_choice = input("Time to pick...rock, paper, scissors: ".lower().strip())

    #If player makes a valid move check
    if p_choice in moves:
        print("\tComputer: " + c_choice)
        print("\tPlayer: " + p_choice)
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
        if p_choice == "rock" and c_choice == "paper":
            winner = "computer"
            phrase = "Paper covers rock!"
        elif p_choice == "paper" and c_choice == "paper":
            winner = "tie"
            phrase = "It is a tie, how boring!"
        elif p_choice == "scissors" and c_choice == "paper":
            winner = "player"
            phrase = "Scissors cut paper!"

        #Computer chooses Scissors
        if p_choice == "rock" and c_choice == "scissors":
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
        print("\t" + phrase)
        if winner == 'player':
            print('\tYou win round ' + str(game_round + 1) + ".")
            p_score += 1
        elif winner == 'computer':
            print('\tComputer wins round ' + str(game_round + 1) + ".")
            c_score += 1
        else:
            print("\tThis round was a tie.")
    
    #Else the player did not make valid move
    else:
        print("That is not a valid option")
        print("Computer gets the point")
        c_score += 1

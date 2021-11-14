def score(playerLives, computerLives):
    result = 2

    if playerLives == computerLives:
            print("Tie! Try again")

    elif playerLives == "rock":
        if computerLives == "paper":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0

    elif playerLives == "paper":
        if computerLives == "scissors":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0
    
    elif playerLives == "scissors":
        if computerLives == "rock":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0

    return result
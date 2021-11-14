from random import randint 
from gameComponents import winLose, gameVars, comparision

while gameVars.player is False:
    print("=========== ( ͡• ͜ʖ ͡•) : Bet I will win!===========")
    gameVars.player = input("Choose your weapon: rock, paper or scissors: " )
    gameVars.computer = gameVars.choices[randint(0,2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    round = comparision.score(gameVars.player, gameVars.computer)
    
    if round == 0:
        gameVars.computerLives = gameVars.computerLives - 1

    elif round == 1:
        gameVars.playerLives = gameVars.playerLives - 1

    print("------------( ͡~ ͜ʖ ͡°)Let's see the score ------------")
    print("Player lives: " + str(gameVars.playerLives))
    print("Computer lives: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lose, lol")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won! Let's try agian!")

    gameVars.player = False
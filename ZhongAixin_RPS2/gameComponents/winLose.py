from gameComponents import gameVars

def winorlose(status):
    print ("You " + status)

    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("===== (╥﹏╥) No.. Don't leave me alone =====")
        exit ()
    elif choice == "y":
        gameVars.playerLives = 2
        gameVars.computerLives = 2
        gameVars.player = False

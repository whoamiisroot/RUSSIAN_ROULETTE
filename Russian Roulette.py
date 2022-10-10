from random import *

while True:
    print("                                                     RUSSIAN ROULETTE                         ")
    x = randint(1, 6)
    repeat = []
    players = []

    num = int(input("HOW MANY BRAVE FELLAS ARE PLAYING TODAY ? "))
    while num != 2 and num != 3 and num != 6:
        print("for even chances of winning (survive) this game can be played by 2,3 or 6 players ")
        num = int(input("HOW MANY BRAVE FELLAS ARE PLAYING TODAY ? "))

    for i in range(1, num + 1):
        user = input(f"user {i}:")
        players.append(user)

    i = 0
    y = 0
    while y != x:
        if i < len(players):
            player = players[i]
        else:
            i = 0
            player = players[i]
        y = int(input(f"Hey {player} it's your turn now : "))
        if y == x:
            print(
                f"##################################-RIP- GAME OVER FOR {player} -RIP-##################################")
        else:
            if y in repeat:
                print("already typed")
                i -= 1
            else:
                print(f"YOU SURVIVED THIS TIME {player} ")
                repeat.append(y)
        i += 1
    print("--------------------------WHAT A LUCKY DAY FOR YOU LOL----------------------------------------")
    r = input("do you want to play again ? (press n to exit or press any other button to play again)")
    if r == "n":
        break
    print("____________________________________________________________________________________________")

#State: condition of what users input
#Input: Users type in conditions
#Rule: #1: Rock > Scissors
       #2: Rock < Paper
       #3: Rock == Rock
#Stop: Program stops when message is printed out

def main() : 
    while True:
        user1_input = input("Player 0: ")
        user2_input = input("Player 2: ")
        result = comparison(user1_input, user2_input)
        print(result)
        again = input("Play again? (y/n) ")
        if again.lower() != "y" :
            break

def comparison(player1, player2) :
    mapping = {"rock" : 0, "paper" : 1, "scissors" : 2}
    player1 = mapping[player1]
    player2 = mapping[player2]
    result = (player1 - player2) % 3 
    if result == 0 :
        return "Tie"
    elif result == 1 :
        return "player1 Won"
    else:
        return "player2 Won"
main()
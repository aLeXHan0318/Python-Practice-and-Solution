# State: Program determines whether the ineger is even or odd
# Input: An ieteger enterd by the user
# Rule:
#           - Input must be an integer
#           - If number % 2 equals 0, the number is even
#           - Otherwise, the number is odd
# Stop:  Program stops after displaying the result

def main() : 
    user_input = int(input("Enter a number: "))
    output = even_or_odd(user_input) 
    print(f"{user_input} is an {output} number")

def even_or_odd(number) :
    if number % 2 == 0:
        return "even" 

    else: 
        return "odd"

main() 

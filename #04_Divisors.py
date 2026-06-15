#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

#State: List contains all divisors of user input number
#Input: An integer
#Rule: #1: User input has to be an integer
       #2: List can only contain divisors of input number
#Stop: Program stops when divisor list is printed

def main() : 
    user_input = int(input("Enter a number: "))
    list_of_divisors = calculate(user_input)
    print(list_of_divisors)

def calculate(input_number):
    result = []
    for number in range(1,input_number + 1):
        if input_number % number ==0:
            result.append(number)
    return result

main() 

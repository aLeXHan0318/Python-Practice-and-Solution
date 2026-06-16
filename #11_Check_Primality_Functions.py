"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, 
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""

#State: the boolean value that indicate wether the input number is prime or not
#Input: An integer enterd by user
#Rule: Check the number is a prime or not a prime number
#Stop: Program ends when boolean value is succussfully printed out on terminal

def main() :
    user_input = int(input("Enter an integer: "))
    result = determine(user_input)
    print(f"{user_input} is {result}")

def determine(number) :
    if number < 2 :
        return "not a prime number"

    for divisors in range(2, number):
        if number % divisors == 0 :
            return "not a prime number"

    return "a prime number"
main()

#State: List contains required Fibonacci number
#Input: Integer enterd by user, representing how many Fibonacci number will be genereated in the list
#Rule: input has to be an integer
#Stop:Program ends when required Fibonacci number is genereated and printed out

def main() :
    user_input = int(input("Enter an integer:"))
    fibonacci_list = generated(user_input)
    print(fibonacci_list)

def generated(required_number) :
    fibonacci_list = []
    number_0 = 0 
    number_1 = 1
    for _ in range(required_number) :
        fibonacci_list.append(number_0)
        number_0, number_1 = number_1, number_0+number_1
    return fibonacci_list

main() 
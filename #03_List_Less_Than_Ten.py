#ake a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#Extras:Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


#State: List of numbers that smaller than the number user input
#Input: An integer enterd by the user 
#Rule:  #1: User input has to be an integer
        #2: List can only contain numbers under than user input
        #3: program output should be in list form
#Stop: program stops when a list has been created 

def main() :
    a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
    user_input = int(input("Enter an integer"))
    list_b = select(user_input, a)
    print(list_b)

def select(number, list_numbers) :
    result = []
    for item in list_numbers: 
        if item < number:
            result.append(item)
            
    return result

main()


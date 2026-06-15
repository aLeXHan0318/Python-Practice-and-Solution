#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python 
#that takes this list a and makes a new list that has only the even elements of this list in it

#State: There is no state
#Input: List saved in a variables
#Rule: New list can only contain even elements from the original list 
#Stop: Program ends after a new list contains even elemtents is printed out

def main() :
    list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    list_b = is_even(list_a)
    print(list_b)

def is_even(list_01) :
    return [number for number in list_01 if number % 2 == 0]

main()

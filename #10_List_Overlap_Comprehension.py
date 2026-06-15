#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way. Take two lists, say for example these two: 
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

#State: \
#Input: \
#Rule: New list must no contain duplicates
#Stop: Porgram ends when new list is printed out

def main() :
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list = select(list_a, list_b)
    print(list) 

def select(list01, list02) :
    return [number for number in set(list01) if number in set(list02)] 


main()

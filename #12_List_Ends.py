#State:None
#Input:None
#Rule: List only contains the first and last elements from the given list
#Stop: Program ends when new list is printed out

def main() :
    list_a = [5, 10, 15, 20, 25]
    result_list = select(list_a)
    print(result_list)

def select(list_1) :
    return [list_1[0], list_1[-1]]

main() 

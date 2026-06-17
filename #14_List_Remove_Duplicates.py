"""
State: \
Input: \
Rule: New list should have to duplicates from the orginal list
Stop: Program ends after new list is printed out
"""

def main() :
    list_a = [1, 2, 3, 4, 5, 5, 7, 8, 123, 123, 23,] 
    list_b = remove_duplicate(list_a) 
    print(list_b)

def remove_duplicate(orginal_list) :
    return list(set(orginal_list))
 
main()

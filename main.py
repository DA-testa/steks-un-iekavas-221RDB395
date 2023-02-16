# python3
# Anastasija Bondare, 221RDB395, 13.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
<<<<<<< HEAD
=======
            # Process opening bracket, write your code here
>>>>>>> b2b0c1f1f5df3480aa8508e71a4bb303a664f33f
            opening_brackets_stack.append(Bracket(next,i+1)) # pievieno klāt nākamo vērtību (tikai vienu)
            pass

        if next in ")]}":
<<<<<<< HEAD
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next): # iet pa vienu vienību pa kreisi
                return i+1
            opening_brackets_stack.pop()   
            pass

    if not opening_brackets_stack:
            print("Success")
        else:
            print(opening_brackets_stack[0].position)

=======
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next): # iet pa vienu vienību pa kreisi
                return i+1
            opening_brackets_stack.pop()     
            pass
        
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[0].position)
>>>>>>> b2b0c1f1f5df3480aa8508e71a4bb303a664f33f

def main():
    text = input()
    mismatch = find_mismatch(text)
<<<<<<< HEAD
=======
    # Printing answer, write your code here
>>>>>>> b2b0c1f1f5df3480aa8508e71a4bb303a664f33f
    print(mismatch) #izvade 


if __name__ == "__main__":
    main()

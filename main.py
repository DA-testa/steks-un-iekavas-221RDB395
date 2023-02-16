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
            opening_brackets_stack.append(Bracket(next,i+1)) # pievieno klāt nākamo vērtību (tikai vienu)
            pass

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next): # iet pa vienu vienību pa kreisi
                return i+1
            opening_brackets_stack.pop()   
            pass

    if not opening_brackets_stack:
            print("Success")
        else:
            print(opening_brackets_stack[0].position)

            
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next): # iet pa vienu vienību pa kreisi
                return i+1
            opening_brackets_stack.pop()     
            pass
        
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[0].position)


def main():
    text = input()
    if i in text:
        mismatch = find_mismatch(text)
        print(mismatch) #izvade 


if __name__ == "__main__":
    main()

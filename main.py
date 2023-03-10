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
            opening_brackets_stack.append(Bracket(next,i + 1)) # Pievieno klāt nākamo 1 vērtību 
            

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next): # Iet pa vienu vienību pa kreisi
                return i + 1 
            opening_brackets_stack.pop()   # Izdzēš pēdējo vērtību, kas tika pievienota
            


    if opening_brackets_stack: # Ja ir kāda no neaizvērtām iekavām, tad
        return opening_brackets_stack[0].position # nosaka, kurā pozīcijā/vietā tā atrodas un izvada numuru
    else:
        return "Success" # Pretējā gadījumā izvada Success, ja ir aizvērtas visas iekavas



def main():
    text = input() # Pirmā ievade
    if "I" or "F" in text: # Pārbauda, vai ievadītais teksts satur burtu "I" vai "F"
        text = input() # Otrā ievade
        mismatch = find_mismatch(text)
        print(mismatch) # Izvada rezultātu 


if __name__ == "__main__":
    main() 

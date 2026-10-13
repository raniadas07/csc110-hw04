# ------------------------------------------------------
#        Name: Rania Das
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
   """ Repeatedly asks the user for a sentence until it contains
    the secret word, or the word 'dog' or 'Dog'.
    Prints the appropriate success message when a match is found. """
   
   while True:
    a = str(input("Give me a sentence: "))
    if secret_word in a:
        print("You used the secret word!")
        break
    elif "dog" in a:
        print("You used the word \"dog\" or the word \"Dog\"!")
        break
    elif "Dog" in a:
        print("You used the word \"dog\" or the word \"Dog\"!")
        break
    else:
        print("Try again!")
    continue


# Task 2
def check_greater():
    """ Repeatedly asks the user for two integers until they are
    different, then prints which integer is greater or lesser. """
    
    while True:
        first = int(input("Give me an integer: "))
        second = int(input("Give me another integer: "))
        if first > second:
            print("First is Greater")
            print("Done")
            break
        elif second > first:
            print("Second is Greater")
            print("Done")
            break
        else:
            print("Try again!")
        continue



# Task 3
def get_special_numbers():
    """ Print odd multiples of 3 between 1 and 40, excluding multiples of 5. """
    
    for x in range(1, 41):
        if x%2 == 0:
            continue
        elif x%3 != 0:
            continue
        elif x%5 == 0:
            continue
        else:
            print(x)

# Task 4.a
def my_for_loop():
    """ Asks the user for a string. Returns if its length is not
    between 2 and 5 inclusive or if it contains a space.
    Otherwise, identifies each letter as a vowel or consonant. """
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = input("Give me a string: ")
    
    if len(string) not in range(2, 6) or " " in string:
        print("bad word")
        return

    for letter in string:
        if letter.lower() in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")


# Task 4.b
def my_while_loop():
    """ Repeatedly displays a menu with choices a, b, and c.
    Choice a repeats the menu, b returns from the function,
    and c exits the program. Invalid choices prompt a retry. """
    while True:
        option = input("Choose a, b, or c: ")
        if option == "a":
            continue
        elif option == "b":
            print("Goodbye")
            return
        elif option == "c":
            sys.exit()
        else:
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

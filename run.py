def introduction():
    print("Welcome to the Chronicles of Valor!")
    print("Chronicles of Valor is a text based adventure game where YOU decide your destiny! You will venture forth into Cydoia, a flourishing continent with all kinds of adventures waiting for you.")
    name = input("But first, go ahead and input your name: ")
    return name

def choose_class(name):
    print(f"Hello, {name}!")
    print("In Chronicles of Valor you will be playing as one of the following classes: a Fighter, a Rogue or a Wizard. Each class has a unique story to tell and for you to shape, so go ahead and choose your favorite!")
    print("1. Fighter")
    print("2. Rogue")
    print("3. Wizard")
    while True:
        choice = input("Input a number between 1 and 3: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


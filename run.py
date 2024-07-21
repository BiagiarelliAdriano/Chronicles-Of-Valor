def introduction():
    print('Welcome to the Chronicles of Valor!')
    print('Chronicles of Valor is a text based adventure game where YOU decide your destiny! \nYou will venture forth into Cydoia, a flourishing continent with all kinds of adventures waiting for you.')
    name = input('But first, go ahead and input your name: ')
    return name

def choose_class(name):
    print(f'Hello, {name}!')
    print('In Chronicles of Valor you will be playing as one of the following classes: a Fighter, a Rogue or a Wizard. \nEach class has a unique story to tell and for you to shape, so go ahead and choose your favorite!')
    print('1. Fighter')
    print('2. Rogue')
    print('3. Wizard')
    while True:
        choice = input('Input a number between 1 and 3: ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            print('Invalid choice. Please choose 1, 2, or 3.')

def start_story(name, player_class):
    if player_class == "1":
        current_story = 'fighter_start'
    elif player_class == "2":
        current_story = 'rogue_start'
    elif player_class == "3":
        current_story = 'wizard_start'

    while current_story:
        current_story = story_segments[current_story](name)

def story_fighter_start(name):
    print(f'You are {name}, a proud warrior that just got to Stillhollow, a small village in the continent of Cydoia. \nAfter reaching a small plaza, you can see a couple of people walking around and talking to each other. \nBefore you can do anything, you suddenly hear a man shouting: "Help! Please, we need help from a hero!" You see a young man with rough and dirty clothes running towards you. \n"Please, are you a hero? Can you help this poor village?"')
    print('What would you like to do?')
    print('1. You like to be called a hero, you can certainly help this poor man.')
    print('2. Ask first what it is about')
    print('3. Try to ignore the man and leave the village')
    choice = input('Enter the number of your choice: ')
    if choice == '1':
        return 'fighter_help_poor_man'
    elif choice == '2':
        return 'fighter_ask_first'
    elif choice == '3':
        return 'fighter_try_to_ignore_the_man'
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return 'fighter_start'

def story_fighter_help_poor_man(name):
    return None

def story_fighter_ask_first(name):
    return None

def story_fighter_try_to_ignore_the_man(name):
    return None

story_segments = {
    'fighter_start': story_fighter_start,
    'fighter_help_poor_man': story_fighter_help_poor_man,
    'fighter_ask_first': story_fighter_ask_first,
    'fighter_try_to_ignore_the_man': story_fighter_try_to_ignore_the_man

}

def main():
    name = introduction()
    player_class = choose_class(name)
    start_story(name, player_class)



if __name__ == '__main__':
    main()
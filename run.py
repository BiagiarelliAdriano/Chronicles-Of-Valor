def introduction():
    print('Welcome to the Chronicles of Valor!')
    print('Chronicles of Valor is a text based adventure game where YOU decide your destiny!')
    print('You will venture forth into Cydoia, a flourishing continent with all kinds of adventures waiting for you.')
    name = input('But first, go ahead and input your name: ')
    return name

def choose_class(name):
    print(f'Hello, {name}!')
    print('In Chronicles of Valor you will be playing as one of the following classes: a Fighter, a Rogue or a Wizard.')
    print('Each class has a unique story to tell and for you to shape, so go ahead and choose your favorite!')
    print('1. Fighter')
    print('2. Rogue')
    print('3. Wizard')
    while True:
        choice = int(input('Input a number between 1 and 3: '))
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
    print(f'You are {name}, a proud warrior that just got to Stillhollow, a small village in the continent of Cydoia.')
    print('After reaching a small plaza, you can see a couple of people walking around and talking to each other.')
    print('Before you can do anything, you suddenly hear a man shouting: "Help! Please, we need help from a hero!"')
    print('You see a young man with rough and dirty clothes running towards you. "Please, are you a hero? Can you help this poor village?"')
    print('What would you like to do?')
    print('1. You like to be called a hero, you can certainly help this poor man.')
    print('2. Ask first what it is about')
    print('3. Try to ignore the man and leave the village')
    choice = int(input('Enter the number of your choice: '))
    if choice == '1':
        return 'fighter_help_poor_man'
    elif choice == '2':
        return 'fighter_ask_first'
    elif choice == '3':
        return 'fighter_try_to_ignore_the_man'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')
        return 'fighter_start'

def story_fighter_help_poor_man(name):
    print('"Oh, thank goodness for your kind soul. My poor daughter was captured by the giants living in the giant beanstalk over there."')
    print('The man points towards what you now realize is a giant beanstalk that you didn’t notice before on the horizon.')
    print('The plant is so tall that you can’t see the end of it, being hidden in between the clouds.')
    print('"Please, I’m too poor and weak to do anything about it. Can you go and save her?"')
    print('What would you like to do?')
    print('1. Accept the quest and go towards the giant beanstalk.')
    print('2. Too dangerous. Walk away.')
    choice = int(input('Enter the number of your choice: '))
    if choice == '1':
        return 'fighter_accept_quest'
    elif choice == '2':
        return 'fighter_walk_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')
        return 'fighter_help_poor_man'

def story_fighter_ask_first(name):
    print('"Oh, thank goodness for your kind soul. My poor daughter was captured by the giants living in the giant beanstalk over there."')
    print('The man points towards what you now realize is a giant beanstalk that you didn’t notice before on the horizon.')
    print('The plant is so tall that you can’t see the end of it, being hidden in between the clouds.')
    print('"Please, I’m too poor and weak to do anything about it. Can you go and save her?"')
    print('What would you like to do?')
    print('1. Accept the quest and go towards the giant beanstalk.')
    print('2. Too dangerous. Walk away.')
    choice = int(input('Enter the number of your choice: '))
    if choice == '1':
        return 'fighter_accept_quest'
    elif choice == '2':
        return 'fighter_walk_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')
        return 'fighter_help_poor_man'

def story_fighter_try_to_ignore_the_man(name):
    print('You look at the man disgusted and you try to ignore them. The man continues to follow you until you reach the end of the village, ')
    print('at which point they decided to walk away. You leave the village, trying to find a better place for adventures')
    print('END OF GAME')
    return None

def story_fighter_accept_quest(name):
    print('You accept the quest of the poor man and assure them you will recover their daughter. You start your journey towards the giant beanstalk.')
    print('It is not that far, so it just takes you about half a day to get at the base of it. Looking up towards the sky, it looks like it will be a very long climb.')
    print('What would you like to do?')
    print('1. Rest and wait for the day after.')
    print('2. Climb the giant beanstalk right away.')
    choice = int(input('Enter the number of your choice: '))
    if choice == '1':
        return 'fighter_rest_and_wait'
    elif choice == '2':
        return 'fighter_climb_right_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')
        return 'fighter_accept_quest'

def story_fighter_walk_away(name):
    print('You tell the man you are not ready for such a dangerous task. The man, saddened, walks away and keeps shouting out for help.')
    print('Without much more reason to be in this village, you decide to leave and find more suitable adventures for you elsewhere.')
    print('END OF GAME')
    return None

def story_fighter_rest_and_wait(name):
    print('You decide you are too tired to start the climb right now. You build a small campfire and set up your travelling tent.')
    print('The night is uneventful and you take a good night sleep. The following morning, you are full of energy and ready to take on the climb.')
    print('You start going up, easily inserting your fingers in the plant to grab on to and climb. After a while, you reach the clouds.')
    print('It gets harder to climb while you cannot see all around you, but you manage to continue on. Finally, the clouds clear up and you get to the end of the beanstalk.')
    print('You get up to a giant platform built in what appears to be smooth stone. You can now see two sets of stone stairs that go even above the clouds.')
    print('One has steps of your size, the other has giant steps.')
    print('What would you like to do?')
    print('1. Take the stairs of your size.')
    print('2. Take the giant stairs.')
    choice = int(input('Enter the number of your choice'))
    if choice == '1':
        return 'fighter_climb_normal_stairs'
    elif choice == '2':
        return 'fighter_climb_giant_stairs'
    else:
        print('Invalid choice. Please choose 1 or 2.')
        return 'fighter_rest_and_wait'

def story_fighter_climb_right_away(name):
    print('You decide you can still continue your journey and take on this climb right away. The climb is difficult and tiring.')
    print('You have to stop multiple times on top of one of the branches to recover your breath.')
    print('The night comes and it gets harder and harder to actually see where you are going. You finally reach the clouds and now you cannot see anything.')
    print('What would you like to do?')
    print('1. Continue the climb.')
    print('2. Wait for the following morning.')
    choice = int(input('Enter the number of your choice'))
    if choice == '1':
        return 'story_continue_climb'
    elif choice == '2':
        return 'story_wait_for_morning'
    else:
        print('Invalid choice. Please choose 1 or 2.')
        return 'fighter_climb_right_away'

def story_fighter_climb_normal_stairs(name):
    return None

def story_fighter_climb_giant_stairs(name):
    return None

def story_continue_climb(name):
    return None

def story_wait_for_morning(name):
    return None

story_segments = {
    'fighter_start': story_fighter_start,
    'fighter_help_poor_man': story_fighter_help_poor_man,
    'fighter_ask_first': story_fighter_ask_first,
    'fighter_try_to_ignore_the_man': story_fighter_try_to_ignore_the_man,
    'fighter_accept_quest': story_fighter_accept_quest,
    'fighter_walk_away': story_fighter_walk_away,
    'fighter_rest_and_wait': story_fighter_rest_and_wait,
    'fighter_climb_right_away': story_fighter_climb_right_away,
    'fighter_climb_normal_stairs': story_fighter_climb_normal_stairs,
    'fighter_climb_giant_stairs': story_fighter_climb_giant_stairs,
    'story_continue_climb': story_continue_climb,
    'story_wait_for_morning': story_wait_for_morning

}

def main():
    name = introduction()
    player_class = choose_class(name)
    start_story(name, player_class)



if __name__ == '__main__':
    main()
import os

def clear_console():
    """ 
    Clears the console screen to ensure the new part of the story replaces the previous one.
    Works for both Windows (using 'cls') and Unix-based systems (using 'clear').
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def introduction():
    """ 
    Introduces the player to the game and prompts them to input their name.
    Returns the player's name.
    """
    print('Welcome to the Chronicles of Valor!')
    print('Chronicles of Valor is a text based adventure game where YOU decide your destiny!')
    print('You will venture forth into Cydoia, a flourishing continent with all kinds of adventures waiting for you.')
    name = input('But first, go ahead and input your name:\n')
    return name

def choose_class(name):
    """ 
    Greets the player by name and prompts them to choose a class (Fighter, Rogue, or Wizard).
    Returns the player's class choice.
    """
    clear_console()
    print(f'Hello, {name}!')
    print('In Chronicles of Valor you will be playing as one of the following classes: a Fighter, a Rogue or a Wizard.')
    print('Each class has unique choices for you to shape the story as you wish, so go ahead and choose your favorite!')
    print('1. Fighter')
    print('2. Rogue')
    print('3. Wizard')
    while True:
        choice = input('Input a number between 1 and 3:\n')
        if choice in ['1', '2', '3']:
            return choice
        else:
            print('Invalid choice. Please choose 1, 2, or 3.')

def story_start(name, player_class):
    """ 
    Starts the story based on the player's chosen class and sets up the initial description.
    Prompts the player with a choice to proceed in the story.
    Returns the next segment of the story based on the player's choice.
    """

    class_descriptions = {
        '1': 'a proud warrior',
        '2': 'a cunning thief',
        '3': 'a studious mage'
    }

    class_description = class_descriptions[player_class]

    clear_console()
    print(f'You are {name}, {class_description} that just got to Stillhollow, a small village in the continent of Cydoia.')
    print('After reaching a small plaza, you can see a couple of people walking around and talking to each other.')
    print('Before you can do anything, you suddenly hear a man shouting: "Help! Please, we need help from a hero!"')
    print('You see a young man with rough and dirty clothes running towards you. "Please, are you a hero? Can you help this poor village?"')
    print('What would you like to do?')
    print('1. You like to be called a hero, you can certainly help this poor man.')
    print('2. Ask first what it is about')
    print('3. Try to ignore the man and leave the village')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_help_poor_man'
    elif choice == '2':
        return 'story_ask_first'
    elif choice == '3':
        return 'story_try_to_ignore_the_man'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')

def story_help_poor_man(name):
    """ 
    Continues the story for a player who chose to help the man.
    Prompts the player with further choices and returns the next segment of the story.
    """
    clear_console()
    print('"Oh, thank goodness for your kind soul. My poor daughter was captured by the giants living in the giant beanstalk over there."')
    print('The man points towards what you now realize is a giant beanstalk that you didn’t notice before on the horizon.')
    print('The plant is so tall that you can’t see the end of it, being hidden in between the clouds.')
    print('"Please, I’m too poor and weak to do anything about it. Can you go and save her?"')
    print('What would you like to do?')
    print('1. Accept the quest and go towards the giant beanstalk.')
    print('2. Too dangerous. Walk away.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_accept_quest'
    elif choice == '2':
        return 'story_walk_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_ask_first(name):
    """ 
    Continues the story for a player who chose to ask about the situation first.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('"Oh, thank goodness for your kind soul. My poor daughter was captured by the giants living in the giant beanstalk over there."')
    print('The man points towards what you now realize is a giant beanstalk that you didn’t notice before on the horizon.')
    print('The plant is so tall that you can’t see the end of it, being hidden in between the clouds.')
    print('"Please, I’m too poor and weak to do anything about it. Can you go and save her?"')
    print('What would you like to do?')
    print('1. Accept the quest and go towards the giant beanstalk.')
    print('2. Too dangerous. Walk away.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_accept_quest'
    elif choice == '2':
        return 'story_walk_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_try_to_ignore_the_man(name):
    """ 
    Ends the story for a player who chose to ignore the man.
    """

    clear_console()
    print('You look at the man disgusted and you try to ignore them. The man continues to follow you until you reach the end of the village, ')
    print('at which point they decided to walk away. You leave the village, trying to find a better place for adventures')
    print('END OF GAME')
    return None

def story_accept_quest(name):
    """ 
    Continues the story for a player who chose to accept the man's quest.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You accept the quest of the poor man and assure them you will recover their daughter. You start your journey towards the giant beanstalk.')
    print('It is not that far, so it just takes you about half a day to get at the base of it. Looking up towards the sky, it looks like it will be a very long climb.')
    print('What would you like to do?')
    print('1. Rest and wait for the day after.')
    print('2. Climb the giant beanstalk right away.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_rest_and_wait'
    elif choice == '2':
        return 'story_climb_right_away'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_walk_away(name):
    """ 
    Ends the game for the player who chose to walk away from the man after hearing their request.
    """

    clear_console()
    print('You tell the man you are not ready for such a dangerous task. The man, saddened, walks away and keeps shouting out for help.')
    print('Without much more reason to be in this village, you decide to leave and find more suitable adventures for you elsewhere.')
    print('END OF GAME')
    return None

def story_rest_and_wait(name):
    """ 
    Continues the story for a player who chose to rest before climbing the giant beanstalk.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You decide you are too tired to start the climb right now. You build a small campfire and set up your travelling tent.')
    print('The night is uneventful and you take a good night sleep. The following morning, you are full of energy and ready to take on the climb.')
    print('You start going up, easily inserting your fingers in the plant to grab on to and climb. After a while, you reach the clouds.')
    print('It gets harder to climb while you cannot see all around you, but you manage to continue on. Finally, the clouds clear up and you get to the end of the beanstalk.')
    print('You get up to a giant platform built in what appears to be smooth stone. You can now see two sets of stone stairs that go even above the clouds.')
    print('One has steps of your size, the other has giant steps.')
    print('What would you like to do?')
    print('1. Take the stairs of your size.')
    print('2. Take the giant stairs.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_climb_normal_stairs'
    elif choice == '2':
        return 'story_climb_giant_stairs'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_climb_right_away(name):
    """ 
    Continues the story for a player who chose to climb the giant beanstalk right away.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You decide you can still continue your journey and take on this climb right away. The climb is difficult and tiring.')
    print('You have to stop multiple times on top of one of the branches to recover your breath.')
    print('The night comes and it gets harder and harder to actually see where you are going. You finally reach the clouds and now you cannot see anything.')
    print('What would you like to do?')
    print('1. Continue the climb.')
    print('2. Wait for the following morning.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_continue_climb'
    elif choice == '2':
        return 'story_wait_for_morning'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_continue_climb(name):
    """ 
    Ends the story for a player who chose to continue the climb of the giant beanstalk during the night.
    """

    clear_console()
    print('You persist on. You are not scared of some clouds and the darkness of the night. You continue with the same strategy to climb.')
    print('Suddenly, you do not notice a change in direction of a branch. You almost lose your grip, when a quick, strong current of wind picks up and pushes you away.')
    print('You lose your grip and fall 1000ft to the ground.')
    print('END OF GAME')
    return None

def story_wait_for_morning(name):
    """ 
    Continues the story for a player who chose to rest and wait for the following morning the continue the climb.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You decide it is too dark to continue. You find a good place to lay down and rest a bit. It is not too long before the morning comes.')
    print('Because of the high altitude, it was very cold and there were a lot of strong currents of cold wind all night.')
    print('You for sure made the right choice of not continuing the climb during the night, but you are still very tired. Now with the sunlight, you can continue climbing.')
    print('After a while, you finally get past the clouds and reach the end of the beanstalk. On top of the plant you find a giant platform built in smooth stone.')
    print('You can see two sets of stairs going up the clouds. One has your size of steps, the other one has giant steps.')
    print('What would you like to do?')
    print('1. Take the stairs of your size.')
    print('2. Take the giant stairs.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_climb_normal_stairs'
    elif choice == '2':
        return 'story_climb_giant_stairs'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_climb_normal_stairs(name):
    """ 
    Continues the story for a player who chose to climb the normal sized stairs.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You start going up using normal stairs. While you go up, you can still see to your right the giant steps that quickly pick up and go even higher.')
    print('After a long time passes, you finally reach the end of the stairs. You can see a giant gate of stone in front of you floating on a cloud.')
    print('You look to your right and you can see that even the giant stairs end right here.')
    print('You carefully step on the cloud, but you notice that is is basically like stepping on solid ground. You manage to get up to the gate.')
    print('What would you like to do?')
    print('1. Try and open the gate.')
    print('2. Call out for someone to open the gate.')
    print('3. Try and climb the gate.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_open_gate'
    elif choice == '2':
        return 'story_call_out'
    elif choice == '3':
        return 'story_climb_gate'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')

def story_climb_giant_stairs(name):
    """ 
    Continues the story for a player who chose to climb the giant stairs.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You get up to the giant steps.')
    print('You can figure out a way to jump and climb each step on the way. The climb is long and hard.')
    print('You manage to get around half way, when the night comes around. You persist on because even in the darkness of the night, you can still see a bit from this altitude.')
    print('So after a couple of hours, you finally manage to get up tha lst giant step. You are very tired. You can see a giant gate of stone in front of you floating on a cloud.')
    print('You look to your left and you can see that also the stairs of your size end right here.')
    print('You carefully step on the cloud, but you notice that it is basically like stepping on solid ground. You manage to get up to the gate.')
    print('What would you like to do?')
    print('1. Rest before doing anything with the gate.')
    print('2. Try and open the gate.')
    print('3. Call out for someone to open the gate.')
    print('4. Try and climb the gate.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_rest_before_gate'
    elif choice == '2':
        return 'story_open_gate'
    elif choice == '3':
        return 'story_call_out'
    elif choice == '4':
        return 'story_climb_gate'
    else:
        print('Invalid choice. Please choose 1, 2, 3, or 4.')

def story_open_gate(name):
    """ 
    Continues the story for a player who chose to push the gate open.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You start pushing one side of the gate. It is very big and it takes out all your strength to push.')
    print('After around 30 seconds, you hear a slight sound of the gate actually moving. You push even harder and you do manage to start opening this side of the gate.')
    print('After making enough room for you to squeeze in, you stop pushing and get to the other side of the gate. You see more stairs going up.')
    print('Taking a sigh, you start your climb on these stairs. After a while, you manage to get to the end of the stairs and your drop to another cloud.')
    print('You can now see a single, wooden, giant house, with green window, a red door and roof, and a chimney.')
    print('What would you like to do?')
    print('1. Knock on the front door.')
    print('2. Climb the house.')
    print('3. Find another way to get in from behind the house.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_knock_on_door'
    elif choice == '2':
        return 'story_climb_house'
    elif choice == '3':
        return 'story_check_behind_house'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')

def story_call_out(name):
    """ 
    Continues the story for a player who chose to call out for someone to open the gate.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You call out. There is no response.')
    print('What would you like to do?')
    print('1. Try and open the gate.')
    print('2. Try and climb the gate.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_open_gate'
    elif choice == '2':
        return 'story_climb_gate'
    else:
        print('Invalid choice. Please choose 1 or 2.')


def story_climb_gate(name):
    """ 
    Continues the story for a player who chose to climb the gate.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You look around. You notice, on one side of the gate, there are a couple of bumps that you could use to climb. You do so.')
    print('You follow the bumps up one side of the gate.')
    print('After reaching the top, you can see that behind the gate there is another set of stairs that go up even further towards another cloud.')
    print('On top of there, you can see a small house. You climb the down to the other side of the gate. You take a sigh and start climbing the stairs.')
    print('After a while, you manage to get to the end of these stairs, and what seemed like a small house from afar, you now see a giant house in front of you, ')
    print('with green windows, red door and roof, and a chimney.')
    print('What would you like to do?')
    print('1. Knock on the front door.')
    print('2. Climb the house.')
    print('3. Find another way to get in from behind the house.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_knock_on_door'
    elif choice == '2':
        return 'story_climb_house'
    elif choice == '3':
        return 'story_check_behind_house'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')

def story_rest_before_gate(name):
    """ 
    Continues the story for a player who chose to rest before doing anything with the gate.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You set up a small campfire and your travelling tent on the cloud. It feels weird, but yet interesting that you are standing on an actual cloud.')
    print('Focused on your mission, you rest for the night. The following morning, with new determination, you think of what to do with the gate.')
    print('What would you like to do?')
    print('1. Knock on the front door.')
    print('2. Climb the house.')
    print('3. Find another way to get in from behind the house.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_knock_on_door'
    elif choice == '2':
        return 'story_climb_house'
    elif choice == '3':
        return 'story_check_behind_house'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')
    

def story_knock_on_door(name):
    """ 
    Continues the story for a player who chose to knock on the front door of the house.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You knock. You wait for a bit. You knock again.')
    print('You start hearing the ground underneath your feet start to shake, as you hear stomping coming towards the door.')
    print('What would you like to do?')
    print('1. Hide next to the door.')
    print('2. Wait until the door opens.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_hide_next_to_door'
    elif choice == '2':
        return 'story_wait_for_door_open'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_climb_house(name):
    """ 
    Continues the story for a player who chose to climb a side of the house.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You find small openings in between the wooden beams so you can climb up. You reach one of the windows. You look inside.')
    print('Without being noticed, you can see a giant, cozy living room and kitchen. It looks like a normal house, very similar to the one you grew up in.')
    print('You see a giant man sleeping on an armchair in front of a fireplace. You see another figure on the ground in front of the gaint.')
    print('You squint your eyes. A child. A little girl, who is blocked inside a cage, looking sad.')
    print('What would you like to do?')
    print('1. Silently open the window and climb inside.')
    print('2. Find another way.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_climb_inside_window'
    elif choice == '2':
        return 'story_find_another_way'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_check_behind_house(name):
    """ 
    Continues the story for a player who chose to check behind the house.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You go around the house. You can see there is another, slightly smaller door.')
    print('What would you like to do?')
    print('1. Open the door.')
    print('2. Go back to the front.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_open_back_door'
    elif choice == '2':
        return 'story_go_back_to_front'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_hide_next_to_door(name):
    """ 
    Continues the story for a player who chose to hide next to the door when the giant opens it.
    Prompts the player with further choices and returns the next segment of the story.
    """

    clear_console()
    print('You quickly escape and put your back to the side of the wall, right next to the door. You wait. The giant steps get nearer. The door starts to open.')
    print('You look up. You see a giant man standing right next to you, and he starts to look around.')
    print('The giant says: "Mmh, stupid kids, always playing pranks on me."')
    print('What would you like to do?')
    print('1. Enter the house without being noticed.')
    print('2. Confront the giant.')
    choice = input('Enter the number of your choice:\n')
    if choice == '1':
        return 'story_enter_house_without_notice'
    elif choice == '2':
        return 'story_confront_giant'
    else:
        print('Invalid choice. Please choose 1 or 2.')

def story_wait_for_door_open(name):
    return None

def story_climb_inside_window(name):
    return None

def story_find_another_way(name):
    return None

def story_open_back_door(name):
    return None

def story_go_back_to_front(name):
    return None

def story_enter_house_without_notice(name):
    return None

def story_confront_giant(name):
    return None

story_segments = {
    'story_start': story_start,
    'story_help_poor_man': story_help_poor_man,
    'story_ask_first': story_ask_first,
    'story_try_to_ignore_the_man': story_try_to_ignore_the_man,
    'story_accept_quest': story_accept_quest,
    'story_walk_away': story_walk_away,
    'story_rest_and_wait': story_rest_and_wait,
    'story_climb_right_away': story_climb_right_away,
    'story_climb_normal_stairs': story_climb_normal_stairs,
    'story_climb_giant_stairs': story_climb_giant_stairs,
    'story_continue_climb': story_continue_climb,
    'story_wait_for_morning': story_wait_for_morning,
    'story_open_gate': story_open_gate,
    'story_call_out': story_call_out,
    'story_climb_gate': story_climb_gate,
    'story_rest_before_gate': story_rest_before_gate,
    'story_knock_on_door': story_knock_on_door,
    'story_climb_house': story_climb_house,
    'story_check_behind_house': story_check_behind_house,
    'story_hide_next_to_door': story_hide_next_to_door,
    'story_wait_for_door_open': story_wait_for_door_open,
    'story_climb_inside_window': story_climb_inside_window,
    'story_find_another_way': story_find_another_way,
    'story_open_back_door': story_open_back_door,
    'story_go_back_to_front': story_go_back_to_front,
    'story_enter_house_without_notice': story_enter_house_without_notice,
    'story_confront_giant': story_confront_giant

}

def main():
    name = introduction()
    player_class = choose_class(name)
    current_story = story_start(name, player_class)
    while current_story:
        current_story = story_segments[current_story](name)



if __name__ == '__main__':
    main()
# Import statements
import os
import random


# Global variables
PROMPT = 'Enter the number of your choice:\n'

conditional_choices = []

# Define global state dictionary to keep track of user choices and conditions
game_state = {
    'fighter_class_chosen': False,
    'rogue_class_chosen': False,
    'wizard_class_chosen': False,
    'grabbed_keys': False
}


def clear_console():
    '''
    Clears the console screen to ensure the new part of the story replaces
    the previous one. Works for both Windows (using 'cls') and Unix-based
         systems (using 'clear').
    '''
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def get_valid_choice(prompt, valid_choices):
    '''
    Prompt the user for input and validate the choice.
    Continuosly prompts until the user enters a valid choice
    (non-blank, numeric, and within valid_choices). Display
    error messages for invalid inputs.
    '''

    if conditional_choices:
        # Add conditional choices if their conditions are met
        for condition, choice in conditional_choices:
            if condition:
                valid_choices.append(choice)

    while True:
        choice = input(prompt)
        if not choice.strip():
            print('Please input a number.')
        elif not choice.isdigit():
            print('Please input a number.')
        elif int(choice) not in valid_choices:
            print(f'Invalid choice. Please choose '
                  f'{", ".join(map(str, valid_choices))}.')
        else:
            return int(choice)


def random_outcome(player_class, game_state, situation,
                   default_negative_range=(1, 9),
                   default_positive_range=(10, 20)):
    '''
    Generates a random outcome based on the player's class and situation.
    Returns negative or positive outcome based on the random number.
    Introduces different ranges for negative and positive outcomes based on the
    situations and player class.
    '''

    negative_range = default_negative_range
    positive_range = default_positive_range

    # Generate a random number
    random_number = random.randint(1, 20)

    # Customize ranges based on class and situation
    if player_class == 'rogue' and situation == 'hiding':
        negative_range = (1, 5)
        positive_range = (6, 20)
    elif player_class == 'fighter' and situation == 'climbing':
        negative_range = (1, 6)
        positive_range = (7, 20)
    elif situation == 'charming':
        if game_state.get('wizard_class_chosen', False):
            negative_range = (1, 12)
            positive_range = (13, 20)
        else:
            return 'negative'
        negative_range == (1, 13)
        positive_range == (14, 20)
    elif situation == 'breaking':
        if game_state.get('fighter_class_chosen', False):
            negative_range == (1, 5)
            positive_range == (6, 20)
        else:
            return 'negative'
    elif situation == 'lock picking':
        if game_state.get('rogue_class_chosen', False):
            negative_range = (1, 3)
            positive_range = (4, 20)
        else:
            return 'negative'
    elif situation == 'inspecting':
        if game_state.get('wizard_class_chosen', False):
            negative_range = (1, 7)
            positive_range = (8, 20)
        else:
            return 'negative'
    elif player_class == 'rogue' and situation == 'stealth':
        negative_range = (1, 5)
        positive_range = (6, 20)

    # Determine outcome based on random number
    if negative_range[0] <= random_number <= negative_range[1]:
        return 'negative'
    else:
        return 'positive'


def introduction():
    '''
    Introduces the player to the game and prompts them to input their name.
    Returns the player's name.
    '''
    print('''Welcome to the Chronicles of Valor!
Chronicles of Valor is a text based adventure game where YOU decide
your destiny! You will venture forth into Cydoia, a flourishing continent
with all kinds of adventures waiting for you.''')
    while True:
        name = input('But first, go ahead and input your name:\n').strip()
        if not name:
            print('Invalid. Please input at least one character.')
        elif any(char.isdigit() for char in name):
            print('Invalid. Name should not contain numbers.')
        else:
            return name


def choose_class(name):
    '''
    Greets the player by name and prompts them to choose a class
    (Fighter, Rogue, or Wizard). Returns the player's class choice.
    '''
    clear_console()
    print(f'''Hello, {name}!
In Chronicles of Valor you will be playing as one of the following
classes: a Fighter, a Rogue or a Wizard. Each class has unique choices for
you to shape the story as you wish, so go ahead and choose your favorite!
1. Fighter
2. Rogue
3. Wizard''')
    while True:
        choice = input('Input a number between 1 and 3:\n')
        if choice in ['1', '2', '3']:
            if choice == '1':
                game_state['fighter_class_chosen'] = True
            elif choice == '2':
                game_state['rogue_class_chosen'] = True
            elif choice == '3':
                game_state['wizard_class_chosen'] = True
            return choice
        else:
            print('Invalid choice. Please choose 1, 2, or 3.')


def story_start(name, player_class, game_state):
    '''
    Starts the story based on the player's chosen class and sets up
    the initial description. Prompts the player with a choice to proceed
    in the story. Returns the next segment of the story based on
    the player's choice.
    '''

    class_descriptions = {
        '1': 'a proud warrior',
        '2': 'a cunning thief',
        '3': 'a studious mage'
    }

    class_description = class_descriptions[player_class]

    clear_console()
    print(f'''You are {name}, {class_description} that just got to Stillhollow,
a small village in the continent of Cydoia. After reaching a small plaza,
you can see a couple of people walking around and talking to each other.
Before you can do anything, you suddenly hear a man shouting: "Help!
Please, we need help from a hero!" You see a young man with rough and
dirty clothes running towards you. "Please, are you a hero? Can you help
this poor village?"
What would you like to do?
1. You like to be called a hero, you can certainly help this poor man.
2. Ask first what it is about.
3. Try to ignore the man and leave the village.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_help_poor_man'
    elif choice == 2:
        return 'story_ask_first'
    elif choice == 3:
        return 'story_try_to_ignore_the_man'


def story_help_poor_man(name, player_class, game_state):
    '''
    Continues the story for a player who chose to help the man.
    Prompts the player with further choices and returns the next segment
    of the story.
    '''
    clear_console()
    print('''"Oh, thank goodness for your kind soul. My poor daughter was
captured by the giants living in the giant beanstalk over there."
The man points towards what you now realize is a giant beanstalk
that you didn’t notice before on the horizon. The plant is
so tall that you can’t see the end of it, being hidden in
between the clouds. "Please, I’m too poor and weak to do anything
about it. Can you go and save her?"
What would you like to do?
1. Accept the quest and go towards the giant beanstalk.
2. Too dangerous. Walk away.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_accept_quest'
    elif choice == 2:
        return 'story_walk_away'


def story_ask_first(name, player_class, game_state):
    '''
    Continues the story for a player who chose to ask about the situation
    first. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''"Oh, thank goodness for your kind soul. My poor daughter was
captured by the giants living in the giant beanstalk over there." The man
points towards what you now realize is a giant beanstalk that you didn’t
notice before on the horizon. The plant is so tall that you can’t see
the end of it, being hidden in between the clouds. "Please, I’m too poor
and weak to do anything about it. Can you go and save her?"
What would you like to do?
1. Accept the quest and go towards the giant beanstalk.
2. Too dangerous. Walk away.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_accept_quest'
    elif choice == 2:
        return 'story_walk_away'


def story_try_to_ignore_the_man(name, player_class, game_state):
    '''
    Ends the story for a player who chose to ignore the man.
    '''

    clear_console()
    print('''You look at the man disgusted and you try to ignore them. The man
continues to follow you until you reach the end of the village,
at which point they decided to walk away. You leave the village, trying
to find a better place for adventures.
END OF GAME''')
    return None


def story_accept_quest(name, player_class, game_state):
    '''
    Continues the story for a player who chose to accept the man's quest.
    Prompts the player with further choices and returns the next segment
    of the story.
    '''

    clear_console()
    print('''You accept the quest of the poor man and assure them you will
recover their daughter. You start your journey towards the giant
beanstalk. It is not that far, so it just takes you about half a day
to get at the base of it. Looking up towards the sky, it looks like it
will be a very long climb.
What would you like to do?
1. Rest and wait for the day after.
2. Climb the giant beanstalk right away.''')

    valid_choices = [1, 2]

    if game_state.get('wizard_class_chosen', False):
        print('3. Rest and cast Leomund Tiny Hut to be safe during the night.')
        valid_choices.append(3)

    choice = get_valid_choice(PROMPT, valid_choices)
    if choice == 1:
        return 'story_rest_and_wait'
    elif choice == 2:
        return 'story_climb_right_away'
    elif choice == 3:
        return 'story_wizard_tiny_hut'


def story_wizard_tiny_hut(name, player_class, game_state):
    '''
    Continues the story for a player who chose the wizard class and now can
    cast Leomund's Tiny Hut to take shelter. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You prepare a good place to cast the spell. It takes about
1 minute, but then a 10-foot-radius immobile dome of force springs into
existence around and above you and remains stationary. It immediately gets to
a cool temperature around you and you know that now nothing can see you from
outside and nothing magical can even pass through. You set up your tent and
rest easily for the night. The following morning you wake up to the low light
of the sun rising from the horizon, you dispell the Tiny Hut and you are
readier than ever to take on the climb. You start going up, easily inserting
your fingers in the plant to grab on to and climb. After a while, you reach
the clouds. It gets harder to climb while you cannot see all around you, but
you manage to continue on. Finally, the clouds clear up and you get to the end
of the beanstalk. You get up to a giant platform built in what appears to be
smooth stone. You can now see two sets of stone stairs that go even above the
clouds. One has steps of your size, the other has giant steps.
What would you like to do?
1. Take the stairs of your size.
2. Take the giant stairs.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_normal_stairs'
    elif choice == 2:
        return 'story_climb_giant_stairs'


def story_walk_away(name, player_class, game_state):
    '''
    Ends the game for the player who chose to walk away from the man after
    hearing their request.
    '''

    clear_console()
    print('''You tell the man you are not ready for such a dangerous task.
The man, saddened, walks away and keeps shouting out for help.
Without much more reason to be in this village, you decide to leave and
find more suitable adventures for you elsewhere.
END OF GAME''')
    return None


def story_rest_and_wait(name, player_class, game_state):
    '''
    Continues the story for a player who chose to rest before climbing
    the giant beanstalk. Prompts the player with further choices and returns
    the next segment of the story.
    '''

    clear_console()
    print('''You decide you are too tired to start the climb right now.
You build a small campfire and set up your travelling tent. The night is
uneventful and you take a good night sleep. The following morning,
you are full of energy and ready to take on the climb. You start going up,
easily inserting your fingers in the plant to grab on to and climb.
After a while, you reach the clouds. It gets harder to climb while you
cannot see all around you, but you manage to continue on. Finally,
the clouds clear up and you get to the end of the beanstalk. You get up
to a giant platform built in what appears to be smooth stone. You can now
see two sets of stone stairs that go even above the clouds. One has steps
of your size, the other has giant steps.
What would you like to do?
1. Take the stairs of your size.
2. Take the giant stairs.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_normal_stairs'
    elif choice == 2:
        return 'story_climb_giant_stairs'


def story_climb_right_away(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb the giant beanstalk
    right away. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You decide you can still continue your journey and take on this
climb right away. The climb is difficult and tiring. You have to stop
multiple times on top of one of the branches to recover your breath.
The night comes and it gets harder and harder to actually see where
you are going. You finally reach the clouds and now you cannot see
anything.
What would you like to do?
1. Continue the climb.
2. Wait for the following morning.''')

    outcome = random_outcome(player_class, 'climbing', game_state)

    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        if outcome == 'negative':
            return 'story_failed_continue_climb'
        else:
            return 'story_success_continue_climb'
    elif choice == 2:
        return 'story_wait_for_morning'


def story_failed_continue_climb(name, player_class, game_state):
    '''
    Ends the story for a player who chose to continue the climb and failed
    to resist the strong currents of wind.
    '''

    clear_console()
    print('''You persist on. You are not scared of some clouds and the darkness
of the night. You continue with the same strategy to climb. Suddenly,
you do not notice a change in direction of a branch. You almost lose your
grip, when a quick, strong current of wind picks up and pushes you away.
You lose your grip and fall 1000ft to the ground.
END OF GAME''')
    return None


def story_success_continue_climb(name, player_class, game_state):
    '''
    Continues the story for a player who chose to continue the climb and
    succeeded to resist the strong currents of wind. Prompts the player
    with futher choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You persist on. You are not scared of some clouds and the darkness
of the night. You continue with the same strategy to climb. Suddenly,
you do not notice a change in direction of a branch. You almost lose your
grip, when a quick, strong current of wind picks up and pushes you. You tighten
your grip and dig your fingers deeper, tense up all your muscles to resist
the cold. Fortunately, the current does not last that long, so thanks to your
strength you managed to hold on and not fall. You continue climbing. Finally
you reach the top of the beanstalk. You are very tired and should probably
rest for a while. You do not see the sun of the morning yet, but what you can
see is where you are now. You are on a big platform built in smooth stone on
top of the beanstalk. You can see two sets of stairs going up the clouds.
One has your size of steps, the other one has giant steps.
What would you like to do?
1. Take the stairs of your size.
2. Take the giant stairs.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_normal_stairs'
    elif choice == 2:
        return 'story_climb_giant_stairs'


def story_wait_for_morning(name, player_class, game_state):
    '''
    Continues the story for a player who chose to rest and wait for the
    following morning the continue the climb. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You decide it is too dark to continue. You find a good place to
lay down and rest a bit. It is not too long before the morning comes.
Because of the high altitude, it was very cold and there were a lot of
strong currents of cold wind all night. You for sure made the right choice
of not continuing the climb during the night, but you are still very tired.
Now with the sunlight, you can continue climbing. After a while,
you finally get past the clouds and reach the end of the beanstalk.
On top of the plant you find a giant platform built in smooth stone.
You can see two sets of stairs going up the clouds. One has your size of
steps, the other one has giant steps.
What would you like to do?
1. Take the stairs of your size.
2. Take the giant stairs.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_normal_stairs'
    elif choice == 2:
        return 'story_climb_giant_stairs'


def story_climb_normal_stairs(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb the normal sized
    stairs. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You start going up using normal stairs. While you go up, you can
still see to your right the giant steps that quickly pick up and go even
higher. After a long time passes, you finally reach the end of the stairs.
You can see a giant gate of stone in front of you floating on a cloud.
You look to your right and you can see that even the giant stairs end
right here. You carefully step on the cloud, but you notice that is
basically like stepping on solid ground. You manage to get up to the gate.
What would you like to do?
1. Try and open the gate.
2. Call out for someone to open the gate.
3. Try and climb the gate.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_open_gate'
    elif choice == 2:
        return 'story_call_out'
    elif choice == 3:
        return 'story_climb_gate'


def story_climb_giant_stairs(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb the giant stairs.
    Prompts the player with further choices and returns the next segment of
    the story.
    '''

    clear_console()
    print('''You get up to the giant steps. You can figure out a way to jump
and climb each step on the way. The climb is long and hard. You manage to
get around half way, when the night comes around. You persist on because
even in the darkness of the night, you can still see a bit from this
altitude. So after a couple of hours, you finally manage to get up
the last giant step. You are very tired. You can see a giant gate of stone
in front of you floating on a cloud. You look to your left and you can see
that also the stairs of your size end right here. You carefully step on
the cloud, but you notice that it is basically like stepping on solid
ground. You manage to get up to the gate.
What would you like to do?
1. Rest before doing anything with the gate.
2. Try and open the gate.
3. Call out for someone to open the gate.
4. Try and climb the gate.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3, 4])
    if choice == 1:
        return 'story_rest_before_gate'
    elif choice == 2:
        return 'story_open_gate'
    elif choice == 3:
        return 'story_call_out'
    elif choice == 4:
        return 'story_climb_gate'


def story_open_gate(name, player_class, game_state):
    '''
    Continues the story for a player who chose to push the gate open.
    Prompts the player with further choices and returns the next segment of
    the story.
    '''

    clear_console()
    print('''You start pushing one side of the gate. It is very big and it
takes out all your strength to push. After around 30 seconds, you hear a slight
sound of the gate actually moving. You push even harder and you do manage
to start opening this side of the gate. After making enough room for you to
squeeze in, you stop pushing and get to the other side of the gate.
You see more stairs going up. Taking a sigh, you start your climb on these
stairs. After a while, you manage to get to the end of the stairs and your
drop to another cloud. You can now see a single, wooden, giant house,
with green window, a red door and roof, and a chimney.
What would you like to do?
1. Knock on the front door.
2. Climb the house.
3. Find another way to get in from behind the house.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_knock_on_door'
    elif choice == 2:
        return 'story_climb_house'
    elif choice == 3:
        return 'story_check_behind_house'


def story_call_out(name, player_class, game_state):
    '''
    Continues the story for a player who chose to call out for someone to open
    the gate. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You call out. There is no response.
What would you like to do?
1. Try and open the gate.
2. Try and climb the gate.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_open_gate'
    elif choice == 2:
        return 'story_climb_gate'


def story_climb_gate(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb the gate.
    Prompts the player with further choices and returns the next segment of
    the story.
    '''

    clear_console()
    print('''You look around. You notice, on one side of the gate, there are a
couple of bumps that you could use to climb. You do so. You follow the
bumps up one side of the gate. After reaching the top, you can see that
behind the gate there is another set of stairs that go up even further
towards another cloud. On top of there, you can see a small house.
You climb the down to the other side of the gate. You take a sigh and start
climbing the stairs. After a while, you manage to get to the end of these
stairs, and what seemed like a small house from afar, you now see a giant
house in front of you, with green windows, red door and roof,
and a chimney.
What would you like to do?
1. Knock on the front door.
2. Climb the house.
3. Find another way to get in from behind the house.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_knock_on_door'
    elif choice == 2:
        return 'story_climb_house'
    elif choice == 3:
        return 'story_check_behind_house'


def story_rest_before_gate(name, player_class, game_state):
    '''
    Continues the story for a player who chose to rest before doing anything
    with the gate. Prompts the player with further choices and returns the
    next segment of the story.
    '''

    clear_console()
    print('''You set up a small campfire and your travelling tent on the cloud.
It feels weird, but yet interesting that you are standing on an actual
cloud. Focused on your mission, you rest for the night. The following
morning, with new determination, you think of what to do with the gate.
What would you like to do?
1. Knock on the front door.
2. Climb the house.
3. Find another way to get in from behind the house.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_knock_on_door'
    elif choice == 2:
        return 'story_climb_house'
    elif choice == 3:
        return 'story_check_behind_house'


def story_knock_on_door(name, player_class, game_state):
    '''
    Continues the story for a player who chose to knock on the front door of
    the house. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You knock. You wait for a bit. You knock again. You start hearing
the ground underneath your feet start to shake, as you hear stomping coming
towards the door.
What would you like to do?
1. Hide next to the door.
2. Wait until the door opens.''')

    outcome = random_outcome(player_class, 'hiding', game_state)

    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        if outcome == 'negative':
            return 'story_failed_to_hide'
        else:
            return 'story_successfully_hidden'
    elif choice == 2:
        return 'story_wait_for_door_open'


def story_climb_house(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb a side of the house.
    Prompts the player with further choices and returns the next segment of
    the story.
    '''

    clear_console()
    print('''You find small openings in between the wooden beams so you can
climb up. You reach one of the windows. You look inside. Without being
noticed, you can see a giant, cozy living room and kitchen. It looks like
a normal house, very similar to the one you grew up in. You see a giant man
sleeping on an armchair in front of a fireplace. You see another figure on
the ground in front of the gaint. You squint your eyes. A child.
A little girl, who is blocked inside a cage, looking sad.
What would you like to do?
1. Silently open the window and climb inside.
2. Find another way.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_inside_window'
    elif choice == 2:
        return 'story_find_another_way'


def story_check_behind_house(name, player_class, game_state):
    '''
    Continues the story for a player who chose to check behind the house.
    Prompts the player with further choices and returns the next segment of
    the story.
    '''

    clear_console()
    print('''You go around the house. You can see there is another, slightly
smaller door.
What would you like to do?
1. Open the door.
2. Go back to the front.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_open_back_door'
    elif choice == 2:
        return 'story_go_back_to_front'


def story_failed_to_hide(name, player_class, game_state):
    '''
    Ends the game for the player who failed to hide next to the door from
    the giant.
    '''

    clear_console()
    print('''You quickly escape and put your back to the side of the wall,
right next to the door. You wait. The giant steps get nearer. The door
starts to open, and you wait with your eyes close and holding your breath,
hoping the giant will not see you or hear you. You wait for a bit, and when
you open your eyes and look up, a see a giant angry face staring at you.
The giant man then proceeds to stomp on you.
END OF GAME''')
    return None


def story_successfully_hidden(name, player_class, game_state):
    '''
    Continues the story for a player who chose to hide next to the door when
    the giant opens it. Prompts the player with further choices and returns
    the next segment of the story.
    '''

    clear_console()
    print('''You quickly escape and put your back to the side of the wall,
right next to the door. You wait. The giant steps get nearer. The door
starts to open. You look up. You see a giant man standing right next
to you, and he starts to look around. The giant says: "Mmh, stupid kids,
always playing pranks on me."
What would you like to do?
1. Enter the house without being noticed.
2. Confront the giant.''')

    outcome = random_outcome(player_class, game_state, 'charming')

    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_enter_house_without_notice'
    elif choice == 2:
        if outcome == 'negative':
            return 'story_confront_giant'
        else:
            return 'story_charm_giant'


def story_wait_for_door_open(name, player_class, game_state):
    '''
    Continues the story for a player who chose to wait for the front door
    to open. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You run away from the door. You stop where you can confidently say
you are far enough so when the door opens, you can still see who opened it.
You wait.
The giant steps get nearer and nearer. Finally, the door starts to slowly
open. Standing behind it is a giant man, wearing what appear to be normal
leather attire. The man looks around, but does not seem to notice you.
What would you like to do?
1. Stare at the giant without saying a word.
2. Confront the giant.
3. Enter the house without being noticed.''')

    outcome = random_outcome(player_class, game_state, 'charming')

    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_stare_at_giant'
    elif choice == 2:
        if outcome == 'negative':
            return 'story_confront_giant'
        else:
            return 'story_charm_giant'
    elif choice == 3:
        return 'story_enter_house_without_notice'


def story_climb_inside_window(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb inside the
    window. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print(''' You try to push a sided of the window. The window is open.
You manage to push it just far enough so you can squeeze in. You plop to
the other side. You slowly close the window without making noise.
You are now inside. You can hear the giant man snoring loudly.
What would you like to do?
1. Climb down.
2. Exit through the window.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_climb_down'
    elif choice == 2:
        return 'story_exit_window'


def story_find_another_way(name, player_class, game_state):
    '''
    Continues the story for a player who chose to find another way.
    Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print(''' You decide it is too risky to enter the house this way. You climb
down the side of the house where you came from. You are now standing in front
of the house.
What would you like to do?
1. Knock on the front door.
2. Find another way to get in from behind the house.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_knock_on_door'
    elif choice == 2:
        return 'story_check_behind_house'


def story_open_back_door(name, player_class, game_state):
    '''
    Continues the story for a player who chose to open the back door.
    Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You run towards the smaller door. It is still giant for you.
You push, and you manage to open it far enough for you enter. When you get
inside, the door automatically closes behind you, without making noise. You are
now standing in a giant hallway, next to two pair of giant doors in each side,
and what appears to be a giant room all the way to the other side of the
hallway. You can see the other side of the front door.
What would you like to do?
1. Search the left door.
2. Search the right door.
3. Go down the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_search_left_door'
    elif choice == 2:
        return 'story_search_right_door'
    elif choice == 3:
        return 'story_go_down_hallway'


def story_go_back_to_front(name, player_class, game_state):
    '''
    Continues the story for a player who chose to go back to the front
    after checking behind the house. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You decide it is better to find another way.
You go back to the front of the house.
What would you like to do?
1. Knock on the front door.
2. Climb the house.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_knock_on_door'
    elif choice == 2:
        return 'story_climb_house'


def story_enter_house_without_notice(name, player_class, game_state):
    '''
    Continues the story for a player who chose to enter the house trying
    not to be noticed. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''You quickly get inside before the giant can close the door again.
You run, hugging the side wall, when you reach a giant piece of wood,
big enough for you to hide. You look up, and it looks like a giant table.
You should be safe here. You hear the giant front door closing, and again
footsteps. You look around. You are now in what appears to be a giant, cozy
living room, next to a kitchen. The giant man sits down on a giant armchair
and seems to be falling asleep. Looking at his feet, you can see another
person. A small girl, locked inside what appears to be an iron cage. You can
see to the side of the room that a hallway opens up to the rest of the house.
What would you like to do?
1. Get closer to the little girl.
2. Run towards the cage.
3. Run towards the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_get_closer_to_girl'
    elif choice == 2:
        return 'story_run_towards_cage'
    elif choice == 3:
        return 'story_run_towards_hallway'


def story_confront_giant(name, player_class, game_state):
    '''
    Ends the game for the user that tried to confront the giant.
    '''

    clear_console()
    print(f'''You yell out to the giant: "Hey, you giant! My name is {name},
and I am here to get back the little girl you kidnapped from the village
nearby." The giant angrily looks down towards you. He brings up his giant
foot and stomps on you.
END OF GAME''')
    return None


def story_charm_giant(name, player_class, game_state):
    '''
    Continues the story for a player who chose to, being a Wizard, try
    and cast Charm Person on the giant man. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print(f'''You calmly confront the giant: "Hello there, Mr. Giant.
I am {name}, an adventurer that came to know the request of a poor man."
While you talk, you get closer to the giant. The giant does not seem to be
much interested in what you have to say, but for now he does not do anything
aggressive towards you. You continue "Now, you see, this poor man asked me to
come visit you, because it appears you decided to take his only daughter as
hostage. Now, I do not know the motivations behind your choice, but you appear
to be a valorous giant warrior, but I have to say. Kidnapping is not that
valorous." After you finish saying this, you get to the giant man foot and you
touch it. A small, pink cloud of energy generates from your hand as you cast
Charm Person. You start backing up, waiting for the effect of the spell to
take place. The giant man expression seems to change. He says: "You know what?
You are right. Hold on." He then closes the door. You hear footsteps, clinging
of iron, a little girl scream, and then more footsteps. The door opens up
again. The giant man, holding something now, places in front of you a small
girl. He then says: "I am very sorry. Yesterday night I was just wandering
about the base of the beanstal and I saw that man looking very suspicious
around this girl, so I wanted to take her and maybe save her. You know, it is
been a while, but I too had a daughter."
What would you like to do?
1. Sympathize with the giant and let the little girl go.
2. Take the girl, excuse yourself, and leave.
3. Take the girl and run.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_sympathize_with_giant'
    elif choice == 2:
        return 'story_take_girl_excuse_leave'
    elif choice == 3:
        return 'story_take_girl_leave'


def story_sympathize_with_giant(name, player_class, game_state):
    '''
    Ends the game for the user who chose to sympathize with the giant
    after knowing the truth.
    '''

    clear_console()
    print('''Hearing the giant man story, you look towards the little girl
She seems confused and a bit scared. You ask her: "Is that the truth? Back to
the village, a man, who I thought was your father, asked me to rescue you."
The little girl points to her mouth, opens it without making a sound, and
shakes her head. The giant responds: "She is mute." Finding this interesting,
you are able to cast Detect Thoughts on the girl to know what she is thinking,
and maybe get an answer for you. You immediately hear the feeble voice of the
girl saying: "I do not know my father. I never met him." Understanding the
situation, you ask the little girl: "Would you like to stay with Mr. Giant?"
The little girl nods. You turn to the giant: "You are not going to eat her,
right?" "No, giants do not actually eat humans, you guys have too few calories,
it is not worth it." Knowing their not lying and thinking back to the man that
asked for you help, you decide to leave the little girl with the giant. After
saying goodbye to both and reassuring the girl to be safe, you decide it is
also not worth going back to the village to talk to that weird man, thinking
they were the father of the girl. After travelling back down the giant
beanstalk, you continue your adventures in the continent of Cydoia.
YOU WON.

Run the application again to play more.''')
    return None


def story_take_girl_excuse_leave(name, player_class, game_state):
    '''
    Ends the story for a player who chose to not trust the words of the giant
    and excuse themselves to save the little girl.
    '''

    clear_console()
    print('''You decide to not trust the words of the giant. You tell him:
"I am very sorry to hear that. Still, it is not a good excuse to kidnapp this
poor little girl from her father back to the village. Now, if you will excuse
us, have a good day." You start walking away, as the giant man waves goodbye
to the girl. You descend down the giant beanstalk. After around a day of
travel, you find your way back to Stillhollow and you reunite the little girl
with her father. The man starts crying with happiness. He gives you a bag of
gold to thank you for saving his daughter. Content with having done a good
deed and surviving visiting the house of a giant, you venture off for more
adventures. And they all lived happily ever after.
YOU WON

Run the application again to play more.''')
    return None


def story_take_girl_leave(name, player_class, game_state):
    '''
    Ends the story for a player who chose to not trust the words of the giant
    and run away with the little girl.
    '''

    clear_console()
    print('''You decide to not trust the words of the giant. You look at the
giant man. He now looks sad. You decide to book it, and you start running,
holding the girl with a hand. You descend down the giant beanstalk. After
around a day of travel, you find your way back to Stillhollow and you reunite
the little girl with her father. The man starts crying with happiness. He gives
you a bag of gold to thank you for saving his daughter. Content with having
done a good deed and surviving visiting the house of a giant, you venture off
for more adventures. And they all lived happily ever after.
YOU WON

Run the application again to play more.''')
    return None


def story_stare_at_giant(name, player_class, game_state):
    '''
    Continues the story for a player who chose to stare at the giant
    that opened the door. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''The giant man stands before you. He looks around confused and
angry, before saying: "Mmmh, stupid kids, always playing pranks on us."
He goes to close the door again.
What would you like to do?
1. Confront the giant.
2. Enter the house without being noticed.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_confront_giant'
    elif choice == 2:
        return 'story_enter_house_without_notice'


def story_climb_down(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb down
    after entering the house through a window. Prompts the player
    with further choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You are able to slide down a piece of wood to land on a giant
dinner table. You are able to slide down the table and get at its feet. You are
now hiding behind one of the legs. You look around. The giant man is still
soundly sleeping on the armchair. The girl does not seem to notice your
presence. You can now see that a hallway opens up on the other side of the
room to the rest of the house.
What would you like to do?
1. Get closer to the little girl.
2. Run towards the cage.
3. Run towards the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_get_closer_to_girl'
    elif choice == 2:
        return 'story_run_towards_cage'
    elif choice == 3:
        return 'story_run_towards_hallway'


def story_exit_window(name, player_class, game_state):
    '''
    Continues the story for a player who chose to get out of the house
    the window they climbed to enter the house. Prompts the player
    with further choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You decide it is not a good idea to enter the house this way,
the giant might notice you if you get down. You exit through the window.
You climb down the side of the house and you are back in front of the
entry door.
What would you like to do?
1. Knock on the front door.
2. Find another way to get in from behind the house.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choicee == 1:
        return 'story_kock_on_door'
    elif choice == 2:
        return 'story_check_behind_house'


def story_search_left_door(name, player_class, game_state):
    '''
    Continues the story for a player who chose to check the left door
    of the hallway. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''You run towards the left door. You push it open. You find yourself
inside what appears to be a bedroom. There's a giant bed right in front of you,
to its right you can see a bedside table and to the left of the room
you can see a giant wardrobe.
What would you like to do?
1. Climb the bed.
2. Climb the bedside table.
3. Open the wardrobe.
4. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3, 4])
    if choice == 1:
        return 'story_climb_bed'
    elif choice == 2:
        return 'story_climb_bedside_table'
    elif choice == 3:
        return 'story_open_wardrobe'
    elif choice == 4:
        return 'story_go_back_to_hallway'


def story_search_right_door(name, player_class, game_state):
    '''
    Continues the story for a player who chose to check the right door
    of the hallway. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''You run towards the right door. You push it open. You find
yourself inside what appears to be a library. There are giant bookshelves all
around the room, with a single side window on the wall in front of you.
What would you like to do?
1. Search for anything useful.
2. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_search_anything_useful'
    elif choice == 2:
        return 'story_go_back_to_hallway'


def story_go_down_hallway(name, player_class, game_state):
    '''
    Continues the story for a player who chose to ignore the doors
    and go straight to the end of the hallway. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print('''You run hugging the right wall towards the end of the hallway.
As soon as you reach the end, you can now hear someone snoring very loudly.
You look around. You see what appears to be a giant, cozy living room beside a
kitchen. There is a giant man sleeping on an armchair in front of a fireplace.
You look just around the corner. You can see an iron cage with someone inside.
A little girl.
What would you like to do?
1. Get closer to the little girl.
2. Run towards the cage.
3. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_get_closer_to_girl'
    elif choice == 2:
        return 'story_run_towards_cage'
    elif choice == 3:
        return 'story_go_back_to_hallway'


def story_get_closer_to_girl(name, player_class, game_state):
    '''
    Continues the story for a player who chose to get closer to the girl.
    Prompts the player with further choices and returns the next segment
    of the story.
    '''

    clear_console()
    print('''You quietly make your way towards the iron cage, carefully looking
towards the giant man to see if he wakes up. You manage to get right next to
the cage. You whisper to the little girl. She turns around and starts smiling
very happily. You gesture to stay silent and go towards the door of the cage.
There is a big lock on it.
What would you like to do?
1. Try to force the lock open.
2. Inspect the giant man for the keys.
3. Run towards the hallway.''')

    valid_choices = [1, 2, 3]

    # Check if the player has grabbed the keys
    if game_state.get('grabbed_keys', False):
        print('4. Open the cage with the keys.')
        valid_choices.append(4)

    if game_state.get('rogue_class_chosen', False):
        print('5. Try to pick the lock open.')
        valid_choices.append(5)

    outcome = random_outcome(player_class, game_state, 'breaking')
    lock_pick_outcome = random_outcome(player_class, game_state, 'lock picking')

    choice = get_valid_choice(PROMPT, valid_choices)
    if choice == 1:
        if outcome == 'negative':
            return 'story_try_force_lock'
        else:
            return 'story_break_lock'
    elif choice == 2:
        return 'story_inspect_giant_for_keys'
    elif choice == 3:
        return 'story_run_towards_hallway'
    elif choice == 4:
        return 'story_open_cage_with_keys'
    elif choice == 5:
        if lock_pick_outcome == 'negative':
            return 'story_failed_lock_pick'
        else:
            return 'story_successful_lock_pick'


def story_failed_lock_pick(name, player_class, game_state):
    return None


def story_successful_lock_pick(name, player_class, game_state):
    return None


def story_break_lock(name, player_class, game_state):
    '''
    Continues the story for a player who chose to destroy the lock of the
    iron cage where the little girl is kept. Prompts the player with further
    choices and returns the next segment of the story.
    '''

    clear_console()
    print('''Thanks to your herculean strenght, you are able to grab onto the
lock, pull it open and completely break it. After that, you can simply open the
cage. You get closer to the girl, who just looks at you with a worried
expression. You reassure her, but you notice that she is also being kept with
some shackles on her hands. They also have a place for a key in them.
What would you like to do?
1. Break the shackles.
2. Inspect the giant man for keys.
3. Run towards the hallway.''')

    outcome = random_outcome(player_class, game_state, 'breaking')

    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        if outcome == 'negative':
            return 'story_fail_to_break_shackles'
        else:
            return 'story_break_shackles'
    elif choise == 2:
        return 'story_inspect_giant_for_keys'
    elif choice == 3:
        return 'story_run_towards_hallway'


def story_fail_to_break_shackles(name, player_class, game_state):
    '''
    Continues the story for a player who chose to destroy the shackles
    entrapping the little girl. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''You try with all your strength to pull the shackles. The little
girl squicks in pain and you stop. This is not working.
What would you like to do?
1. Inspect the giant man for keys.
2. Run towards the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_inspect_giant_for_keys'
    elif choice == 2:
        return 'story_run_towards_hallway'


def story_break_shackles(name, player_class, game_state):
    '''
    Ends the game for the user that tried to break the shackles of the little
    girl inside the iron cage.
    '''

    clear_console()
    print('''Nothing can stop you and your strength. You manage to destroy the
shackles entrapping the little girl without harming her. You take her by
a hand, and you escape the giant house together. After around a day of travel,
you find your way back to Stillhollow and you reunite the little girl with her
father. The man starts crying with happiness. He gives you a bag of gold to
thank you for saving his daughter. Content with having done a good deed and
surviving visiting the house of a giant, you venture off for more adventures.
And they all lived happily ever after.
YOU WON

Run the application again to play more.''')
    return None


def story_run_towards_cage(name, player_class, game_state):
    '''
    Ends the game for the user that tried to run recklessly towards the cage.
    '''

    clear_console()
    print('''You run, but you make a little bit too much sound. Suddenly, while
you are running, everything gets darker, like if a giant foot just got on top
of you. You look up. A giant foot stomps on you.
END OF GAME''')
    return None


def story_run_towards_hallway(name, player_class, game_state):
    '''
    Continues the story for a player who chose to run towards the hallway.
    Prompts the player with further choices and returns the next segment
    of the story.
    '''

    clear_console()
    print('''You get to the hallway. You can see that there are three more
doors. One to your right, one to your left, and one directly towards the end
of the hallway.
What would you like to do?
1. Search the left door.
2. Search the right door.
3. Search the door at the end of the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_search_left_door'
    elif choice == 2:
        return 'story_search_right_door'
    elif choice == 3:
        return 'story_search_middle_door'


def story_climb_bed(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb on the giant bed.
    Prompts the player with further choices and returns the next segment
    of the story.
    '''

    clear_console()
    print('''You manage to get on top of the bed. It's not that soft, so it's
not difficult for you to walk on. You look around. There is something shining
on top of the bedside table. You get closer to take a better look. You can see
a small pair of keys.
What would you like to do?
1. Climb the bedside table.
2. Open the wardrobe.
3. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_climb_bedside_table'
    elif choice == 2:
        return 'story_open_wardrobe'
    elif choice == 3:
        return 'story_go_back_to_hallway'


def story_climb_bedside_table(name, player_class, game_state):
    '''
    Continues the story for a player who chose to climb on the giant bedside
    table. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You manage to get on top of the bedside table. There is not much
on top of it, only a giant lamp, a giant glass of water, and a small pair of
keys. They look like they would be able to open an iron cage.
What would you like to do?
1. Grab the keys and climb down.
2. Open the wardrobe.
3. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        game_state['grabbed_keys'] = True
        return 'story_grab_keys'
    elif choice == 2:
        return 'story_open_wardrobe'
    elif choice == 3:
        return 'story_go_back_to_hallway'


def story_open_wardrobe(name, player_class, game_state):
    '''
    Ends the story for users who tried to open the wardrobe in the
    giant bedroom.
    '''

    clear_console()
    print('''You grab one of the wardrobe doors. You pull towards you and you
manage to open it up. Inside is very dark, but after opening it a bit more,
you can now see a lot of dirty clothes hanging on a wooden stick. Before you
can close the door again, a giant pair of hands grab onto you and takes you
inside the wardrobe. You are then immediately squished to death.
END OF GAME''')
    return None


def story_go_back_to_hallway(name, player_class, game_state):
    '''
    Continues the story for a player who chose to go back to the hallway,
    either after exploring one of the two rooms, or checking out the main room
    in front of the house. Prompts the player with further choices and returns
    the next segment of the story.
    '''

    clear_console()
    print('''You are back at the hallway.
What would you like to do?
1. Search the left door.
2. Search the right door.
3. Search the door at the end of the hallway.
4. Go down the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3, 4])
    if choice == 1:
        return 'story_search_left_door'
    elif choice == 2:
        return 'story_search_right_door'
    elif choice == 3:
        return 'story_search_middle_door'
    elif choice == 4:
        return 'story_go_down_hallway'


def story_search_anything_useful(name, player_class, game_state):
    '''
    Continues the story for a player who chose to search the right room for
    anything useful. Prompts the player with further choices and returns the
    next segment of the story.
    '''

    clear_console()
    print('''You walk around, looking at the different books here and there.
After searching for a couple of minutes, you notice something shining
in between two books. You get closer. You move away the two books to make some
space and you reveal what appears to be some kind of potion with a weird,
almost transparent liquid in it.
What would you like to do?
1. Drink it.
2. Leave it.
3. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_drink_potion'
    elif choice == 2:
        return 'story_leave_potion'
    elif choice == 3:
        return 'story_go_back_to_hallway'


def story_try_force_lock(name, player_class, game_state):
    '''
    Continues the story for a player who chose to try to force and destroy the
    lock of the cage. Prompts the player with further choices and returns the
    next segment of the story.
    '''

    clear_console()
    print('''You try pulling the lock. You give it some solid punches and pull
it from the sides, but unfortunately, you are not strong enough to pry it open
with your bare hands.
What would you like to do?
1. Inspect the giant man for the keys.
2. Run towards the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_inspect_giant_for_keys'
    elif choice == 2:
        return 'story_run_towards_hallway'


def story_inspect_giant_for_keys(name, player_class, game_state):
    '''
    Continues the story for a player who chose to search the giant man hoping
    to find the keys to the iron cage. Prompts the player with further choices
    and returns the next segment of the story.
    '''

    clear_console()
    print('''You get close to the giant and quietly get on one of the arms of
the armchair. The giant man is now sleeping right in front of you. You look
around its body. It is wearing a normal white shirt with leathery shorts.
There are no pockets on his clothes. You can not see any key on him.
What would you like to do?
1. Jump on the giant man to look further.
2. Try to force the lock open.
3. Run towards the hallway.''')

    outcome = random_outcome(player_class, game_state, 'breaking')

    choice = get_valid_choice(PROMPT, [1, 2, 3])
    if choice == 1:
        return 'story_jump_on_giant'
    elif choice == 2:
        if outcome == 'negative':
            return 'story_try_force_lock'
        else:
            return 'story_break_lock'
    elif choice == 3:
        return 'story_run_towards_hallway'


def story_search_middle_door(name, player_class, game_state):
    '''
    Continues the story for a player who chose to search the door down the
    hallway. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You run at the end of the hallway, skipping the two rooms on the
side. You pull with all your forces and you manage to squeeze out of the door.
You are now outside, at the back of the house.
What would you like to do?
1. Go back inside.
2. Run in front of the house.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_open_back_door'
    elif choice == 2:
        return 'story_go_back_to_front'


def story_grab_keys(name, player_class, game_state):
    '''
    Continues the story for a player who chose to grab the keys that were on
    top of the bedside table. Prompts the player with further choices and
    returns the next segment of the story.
    '''

    clear_console()
    print('''You get the keys and you quickly climb down the table.
What would you like to do?
1. Open the wardrobe.
2. Go back to the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_open_wardrobe'
    elif choice == 2:
        return 'story_go_back_to_hallway'


def story_drink_potion(name, player_class, game_state):
    '''
    Ends the game for the user that decided to drink the potion of
    invisibility. Good ending.
    '''

    clear_console()
    print('''You grab the potion and take a sip of it. A very weird sensation
runs down your spine. The liquid does not taste like anything, you just feel
this liquid enter your body and go down your throat. You look around, and when
you take a look at your hands, you do not see them. You are invisible.
From here on, thanks to the invisibility, your missions is quite simple.
You can go around the house without worrying about being seen. You check the
left door and you are in a bedroom. On the bedside table you find some keys to
open an iron cage. You go down the hallway and find the little girl locked
inside an iron cage. You open it up and whisper to the girl: "Hey, I am here
to save you, you do not need to worry anymore." You release her hands from some
shackles and you stealthily walk outside the house, right before the
invisibility effect wears off. After around a day of travel, you find your way
back to Stillhollow and you reunite the little girl with her father.
The man starts crying with happiness. He gives you a bag of gold to thank you
for saving his daughter. Content with having done a good deed and surviving
visiting the house of a giant, you venture off for more adventures.
And they all lived happily ever after.
YOU WON

Run the application again to play more.''')
    return None


def story_leave_potion(name, player_class, game_state):
    '''
    Continues the story for a player who chose to leave the potion without
    drinking it. Prompts the player with further choices and returns the next
    segment of the story.
    '''

    clear_console()
    print('''You decide not to drink the weird looking potion. After searching
for a bit more, you do not seem to find anything else in this room.
You go back to the hallway.
What would you like to do?
1. Search the left door.
2. Go down the hallway.''')
    choice = get_valid_choice(PROMPT, [1, 2])
    if choice == 1:
        return 'story_search_left_door'
    elif choice == 2:
        return 'story_go_down_hallway'


def story_jump_on_giant(name, player_class, game_state):
    '''
    Ends the game for the user that tried to jump on the giant man
    looking for the key.
    '''

    clear_console()
    print('''You jump on the giant man body. You bounce a little on the
large belly. Looking towards the face of the giant, he does not seem
to wake up. You start moving going towards the pants to see if you missed
something, but as you start moving, the giant yawns and you are not quick
enough to dodge the giant hand coming towards you. He grabs you, and without
escape he rolls on the side and you suffocate.
END OF GAME''')
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
    'story_wizard_tiny_hut': story_wizard_tiny_hut,
    'story_climb_normal_stairs': story_climb_normal_stairs,
    'story_climb_giant_stairs': story_climb_giant_stairs,
    'story_failed_continue_climb': story_failed_continue_climb,
    'story_success_continue_climb': story_success_continue_climb,
    'story_wait_for_morning': story_wait_for_morning,
    'story_open_gate': story_open_gate,
    'story_call_out': story_call_out,
    'story_climb_gate': story_climb_gate,
    'story_rest_before_gate': story_rest_before_gate,
    'story_knock_on_door': story_knock_on_door,
    'story_climb_house': story_climb_house,
    'story_check_behind_house': story_check_behind_house,
    'story_failed_to_hide': story_failed_to_hide,
    'story_successfully_hidden': story_successfully_hidden,
    'story_wait_for_door_open': story_wait_for_door_open,
    'story_climb_inside_window': story_climb_inside_window,
    'story_find_another_way': story_find_another_way,
    'story_open_back_door': story_open_back_door,
    'story_go_back_to_front': story_go_back_to_front,
    'story_enter_house_without_notice': story_enter_house_without_notice,
    'story_confront_giant': story_confront_giant,
    'story_charm_giant': story_charm_giant,
    'story_sympathize_with_giant': story_sympathize_with_giant,
    'story_take_girl_excuse_leave': story_take_girl_excuse_leave,
    'story_take_girl_leave': story_take_girl_leave,
    'story_stare_at_giant': story_stare_at_giant,
    'story_climb_down': story_climb_down,
    'story_exit_window': story_exit_window,
    'story_search_left_door': story_search_left_door,
    'story_search_right_door': story_search_right_door,
    'story_go_down_hallway': story_go_down_hallway,
    'story_get_closer_to_girl': story_get_closer_to_girl,
    'story_run_towards_cage': story_run_towards_cage,
    'story_run_towards_hallway': story_run_towards_hallway,
    'story_climb_bed': story_climb_bed,
    'story_climb_bedside_table': story_climb_bedside_table,
    'story_open_wardrobe': story_open_wardrobe,
    'story_go_back_to_hallway': story_go_back_to_hallway,
    'story_search_anything_useful': story_search_anything_useful,
    'story_try_force_lock': story_try_force_lock,
    'story_break_lock': story_break_lock,
    'story_failed_lock_pick': story_failed_lock_pick,
    'story_successful_lock_pick': story_successful_lock_pick,
    'story_fail_to_break_shackles': story_fail_to_break_shackles,
    'story_break_shackles': story_break_shackles,
    'story_inspect_giant_for_keys': story_inspect_giant_for_keys,
    'story_search_middle_door': story_search_middle_door,
    'story_grab_keys': story_grab_keys,
    'story_drink_potion': story_drink_potion,
    'story_leave_potion': story_leave_potion,
    'story_jump_on_giant': story_jump_on_giant

}


def main():
    name = introduction()
    player_class = choose_class(name)
    current_story = story_start(name, player_class, game_state)
    while current_story:
        current_story = story_segments[current_story](name, player_class,
                                                      game_state)


if __name__ == '__main__':
    main()

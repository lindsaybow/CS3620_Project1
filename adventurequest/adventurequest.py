# file handling

def save_outcome(outcome):
    with open("adventure_outcomes.txt", "a") as file:
        file.write(outcome + "\n")

def read_outcomes():
    try:
        with open("adventure_outcomes.txt", "r") as file:
            outcomes = file.readlines()
            print("Discovered outcomes:")
            for outcome in outcomes:
                print(outcome.strip())
    except FileNotFoundError:
        print("No adventure outcomes found.")


# adventure

def start_adventure():
    print("You checked into a 100 year old hotel and it's your first night staying in your room. Upon going to sleep (or attempting to), you hear the faint sound of children laughing in the hallway. It's 3 in the morning. What will you do?")
    print("1. Investigate the noise. Maybe you're just hearing things.")
    print("2. Ignore the noise and go back to sleep. These things don't scare you.")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        the_noise()
    elif choice == '2':
        sleep()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        start_adventure()

def the_noise():
    print("You get out of bed and walk out the door to look out of the peephole. Upon looking through the peephole, all you see is the hotel hallway dimly lit with one dusty old ceiling light and not a child in sight. That's weird. What now?")
    print("1. Go back to bed. This isn't worth it.")
    print("2. Open the door and check the rest of the hallway. What have these kids got on you?")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        window_man()
    elif choice == '2':
        the_elevator()
    else: 
        print("Invalid choice. Please enter 1 or 2.")
        the_noise()

def sleep():
    print("You fall into a deep sleep.")
    print("For a few hours, you have a peculiar dream. You dream that you came up to your room, but this time, a woman in a ballgown is sitting on the end of your bed. She's hunched over, holding what looks to be a locket shaped like a heart. 'Go away!' she tells you. Without thinking, you leave the room. Once you leave the room, your body wakes up from the dream instictively.")
    print("You open your eyes abruptly, your heart still beating fast from the dream. You switch on the bedside lamp and rub your eyes. What was that all about? Once your eyes are adjusted to the light, you spot something at the end of the bed.")
    print("It's the locket.")
    print("1. Pick up the locket and inspect.")
    print("2. Kick it off the bed with your foot. Why would I touch that?")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        the_locket()
    elif choice == '2':
        ballroom_dancer()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sleep()

def the_locket():
    print("With hesitation, you lean forward and pick up the locket. It's a large silver locket with intricate engravings. It looks like a normal locket, but something in you is telling you that it's not.")
    print("Do you want to open it?")
    print("1. Absolutely not. I don't mess with this stuff.")
    print("2. Sure! What do I have to lose?")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print("You shut the locket and go back to bed.")
        sleep()
    elif choice == '2':
        open_locket()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        the_locket()

def open_locket():
    print("You open the clasp of the locket. You expect to see something horrifying, but instead you see a black and white portrait of a woman wearing a ballgown. The image seems to look back at you, as if you've seen this woman before.")
    print("Suddenly, there's a knock at the door. It makes you jump, and you practically drop the locket. Without thinking, you get up and walk to the door.")
    print("You peer through the peephole to see a woman. It's a woman that looks practically translucent. She has dark hair and almost gray skin, dressed in a nice evening ballgown. She stares back at you through the peephole.")
    print("There's no where to run, so you open the door. The woman barges into the room and shuts the door behind you.")
    print("'Please', she says. 'Destroy it'.")

    print("You look back at her. Destroy the locket?")
    print("1. No. Doesn't this mean a lot to her?")
    print("2. Destroy the locket.")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        the_consequence()
    elif choice == '2':
        destroy_locket()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        open_locket()

def the_consequence():
    print("'No,' you say to her.")
    print("She looks back at you, anger in her eyes. 'Fine', she says. 'I guess you'll join me then!'")
    print("You die, joining the ghost for an eternity in the hotel. Now, your soul is stored in the locket too, waiting for someone to come to free you.")
    
    save_outcome("You were unsuccessful with freeing the ghost, therefore joining her for eternal captivity in the hotel. You never thought this would happen just by staying in a hotel.")
    read_outcomes()

    choice = input("Play again? Enter 'y' for yes or 'n' for no: ")
    if choice == 'y' or choice == 'Y':
        start_adventure()
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'. ")

def destroy_locket():
    print("You look back at her and nod. Why would you say no to what a ghost is telling you to do? You slam the locket on the ground.")
    ballroom_dancer()

def ballroom_dancer():
    print("The locket clatters to the floor. You wince at the loud noise it made, but you wince more at the fact that the locket is now shattered on the wood floor. A dim, light blue energy seems to be flowing out of the locket and into the air. You jump as you hear a voice, not coming from a particular direction but a voice that seems to be only in your head.")
    print("You've freed me. My soul has been trapped here for many years. I thank you gracefully.")

    save_outcome("You freed the old ghost's soul that has been tortured in this hotel for 100 years. She thanks you and you go to bed happy and relieved.")

    read_outcomes()

    choice = input("Play again? Enter 'y' for yes or 'n' for no: ")
    if choice == 'y' or choice == 'Y':
        start_adventure()
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'. ")
   
def the_elevator():
    print("You venture into the hallway. An eerie feeling is in the air, but that doesn't stop you from investigating those laughing sounds. You follow the carpet runner down the hall, which leads to the only elevator in the building, rumored to be one of the oldest elevators in the state. Abruptly, the elevator rings out with a loud bell noise and the doors open. There's no way this old elevator is motion sensitive, so perhaps it's opening just for you.")

    print("1. Get on the elevator. It's beckoning you, after all.")
    print("2. Continue looking for the children. Maybe they're downstairs?")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        keypad()
    elif choice == '2':
        the_lobby()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        the_elevator()

def keypad():
    print("You hop on the elevator and the door closes in front of you. You look at the keypad at the floor options. The hotel is small and old, so there's only a few options. Which floor do you pick?")
    print("1. Floor 1. The ground floor where the lobby is.")
    print("2. Floor 2. You're on this floor. You doubt anything will happen if you press this one.")
    print("3. Floor 3. This is the top floor. You don't know much about this one.")
    print("4. 'B'. Basement...?")

    choice = input("Enter 1, 2, 3, or 4: ")
    if choice == '1':
        floor_1()
    elif choice == '2':
        the_catacombs()
    elif choice == '3':
        top_floor()
    elif choice == '4':
        the_catacombs()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        keypad()

def floor_1():
    print("You press the number 1 in the elevator. With some loud noises and some rattling, the elevator moves down to the lobby.")

    the_lobby()

def the_catacombs():
    print("The elevator lets out loud clangs and rattling noises. The elevator jerks downward, and you're kind of regretting your decision as your stomach turns. Suddenly, the elevator crashes onto what feels like hard rock or concrete. You think you're at the very bottom.")
    print("The elevator doors open and you step out reluctantly.")
    print("Your surroundings are dark, you seem to be in an underground tunnel, some sort of catacomb. The air smells bad and you don't need to think long to know why.")
    print("Suddenly, the elevator doors slam shut, the elevator lets out a loud ding, and it leaves the floor. Someone must have called it, or maybe it's moving on its own. You wouldn't be surprised at this point.")
    print("You move forward slowly. Where else is there to go now?")
    print("'Did you come to join me?' you hear a woman's voice in the distance before you see her emerge from around a corner. It's a pale woman wearing a long ballgown.")
    print("'The elevator isn't coming back for you,' she says. 'Will you be joining me or not?'")

    print("1. Join the ghost.")
    print("2. Run.")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        join_ghost()
    elif choice == '2':
        ghost_chase()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def join_ghost():
    print("'Fine,' you say. 'I'll join you.' You have no other choice.")
    print("You join the ghost in the catacombs for time and all eternity. You die eventually, but you remain a ghost in the catacombs, haunting the hotel forever.")

    save_outcome("You join the ghost in the catacombs for time and all eternity. You die eventually, but you remain a ghost in the catacombs, haunting the hotel forever.")

    read_outcomes()

    choice = input("Play again? Enter 'y' for yes or 'n' for no: ")
    if choice == 'y' or choice == 'Y':
        start_adventure()
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'. ")

def ghost_chase():
    print("'Never!' you yell. You take off running, trying to navigate the maze of the catacombs. You can hear a whooshing sound behind you, knowing that the ghost is flying after you.")
    print("After running for a while, you spot the elevator at the end, showing that you completed a full loop around the catacombs.The elevator dings and opens as you approach it, as if it's opening to save you.")
    print("Get in the elevator?")

    print("1. Yes.")
    print("2. No, I can outrun her.")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        escape()
    elif choice == '2':
        trapped()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def escape():
    print("You dart into the elevator. The doors slam right as you get in and the elevator starts going up.")
    print("You've escaped the ghost. You return home with a wild real-life horror story to tell all your friends.")

    save_outcome("You've escaped the ghost. You return home with a wild real-life horror story to tell all your friends.")

    read_outcomes()

    choice = input("Play again? Enter 'y' for yes or 'n' for no: ")
    if choice == 'y' or choice == 'Y':
        start_adventure()
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'. ")

def trapped():
    print("You turn around, hoping to take off running again in order to get away from the ghost. You were thinking that there'd maybe be another way out.")
    print("Once you turn around, you're face to face with the ghost. You have no where to go, and she looks back at you with anger in her eyes.")
    print("'Join me', she says again. As if on cue, the elevator closes its doors and leaves.")
    print("There's no where else to go, no where else to hide.")

    join_ghost()

def window_man():
    print("Shrugging off the weird noises, you turn around to go back to bed. After turning around, the outline of a figure appears in front of the window by the bed. Because it's so dark, the figure just looks like a black blob, but you make it out to look like humanoid. It doesn't appear to move, and you swear you're just seeing things. Do you:")
    print("1. Approach the figure. What's the worst that could happen?")
    print("2. Flee into the hallway. This guy is a lot worse than those kids.")

    choice = input("Enter 1 or 2: ")
    if choice == '1':
        disappearing_act()
    if choice == '2':
        the_elevator()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        window_man()

def disappearing_act():
    print("You approach the figure and it disappears instantly. Was it ever really there? You shrug it off. Maybe it was just the shadows making shapes. You get back in bed. It's hard to sleep, but you fall asleep eventually.")

    sleep()

def the_lobby():
    print("You step out of the elevator and look down at the grand staircase. You can see the front doors of the hotel.")
    print("Without thinking, you make for the door. You aren't interested in staying here anymore, for obvious reasons.")
    print("You can hear footsteps above you, and the children laughing again as you run towards the door.")
    print("You escape the hotel and get in your car to go home. You leave your belongings behind, but at least you also left behind those odd experiences.")

    save_outcome("You escape the hotel and get in your car to go home. You leave your belongings behind, but at least you also left behind those odd experiences.")
    read_outcomes()

    choice = input("Play again? Enter 'y' for yes or 'n' for no: ")
    if choice == 'y' or choice == 'Y':
        start_adventure()
    elif choice == 'n' or choice == 'N':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'. ")


if __name__ == "__main__":
    start_adventure()
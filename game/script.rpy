# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform leftish:
    xcenter 0.250

define narrator = Character("")
define human = Character("You")
define pet = Character("Wuffeli")


# The game starts here.

label start:

    # declare variables
    python:
        current_day = 1

        max_daily_actions = 3
        daily_actions = 3

        hunger_food_points = 4
        fitness_points = 4
        happiness_points = 4

        secret_cleanliness_points = 5
        secret_sleepiness_energy_points = 5    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    narrator "It is morning, and you wake up refreshed."

    show human happy at leftish

    human "I wonder if my pet Wuffeli has been a good boy?"

    show human happy at leftish
    show placeholder wuffeli at topright:

    pet "wrrrwrwroffof r"

    show human shocked at leftish
    show placeholder wuffeli at topright:

    human "o no"

    # This ends the game.

    jump scene_selector

    return

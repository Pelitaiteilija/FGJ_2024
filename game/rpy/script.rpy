# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform left:
    xcenter 0.250

transform right:
    xcenter 0.750

transform topleft:
    xcenter 0.250

transform topright:
    xcenter 0.75

transform bottomleft:
    xcenter 0.250

transform bottomright:
    xcenter 0.75



define narrator = Character("")
define human = Character("You")
define hairball = Character("Wuffeli")


# The game starts here.

label start:
    python:
        init_activity_events()
        init_cleaning_events()
        init_food_events()
        init_sleeping_events()


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg livingroom day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    narrator "It is morning, and you wake up refreshed."

    human "I wonder if my pet [pet_name] has been a good boy?"

    show hairball furious at home_topright:
    with dissolve
    

    hairball "wrrrwrwroffof r"

    human "O!"
    human "Oh no!"

    with None
    show hairball angry at home_center
    with fade
    narrator "A few hectic moments later..."
    
    

    jump scene_make_a_choice

    

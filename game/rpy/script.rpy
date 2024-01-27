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
define hemmo = Character("You")
define hairball = Character("Wuffeli")


# The game starts here.

label start:
    python:
        init_activity_events()
        init_cleaning_events()
        init_food_events()
        init_sleeping_events()

    $ game_ui_visible = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg livingroom day

    with fade

    hemmo "I was just minding my own business..."
    show hairball angry at home_center

    hemmo "I was just minding my own business when this disgusting little ball of hair showed up."
    show hairball angry flipped at home_center
    hemmo "I don't know where it came from."
    hemmo "But it doesn't matter any more."
    show hairball furious at home_left_corner
    hemmo "I tried to toss it out several times..."
    with None
    scene bg livingroom night
    show hairball angry at home_mirror
    with fade
    hemmo "...but it always came back."

    with None
    hemmo "Eventually, I just had to accept that I had new, hairy roommate."
    show hairball sad at home_right
    
    hemmo "It was kind of cute, sometimes, and looked harmless enough."
    hemmo "I figured it wasn't worth the trouble to keep chasing it around the house."

    hemmo "Since it was going to live with me, I decided to give it a name."

    # TODO: lisää joku nimenanto-prompti tai jotain

    with dissolve
    scene bg livingroom day

    narrator "It is morning, and you wake up feeling better than in a long time."

    $ game_ui_visible = True
    jump scene_make_a_choice

    

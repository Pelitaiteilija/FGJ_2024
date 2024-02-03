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
    play music "Start - Feel.mp3"

    narrator "It was a cloudy day and I had nothing special to do, so I decided to clean my apartment a bit to be at least productive."
    narrator "During the cleaning I spotted something, a big hairball behind my couch."

    show hairball neutral flipped at home_center
    with dissolve

    narrator "I don't know where it came from but it doesn't matter."
    show hairball furious at home_left_corner
    with dissolve
    narrator "I tried to get rid of it several times..."
    with None

    scene bg livingroom night
    show hairball angry at home_mirror
    with dissolve
    narrator "...but it always came back."
    with None

    scene bg livingroom day
    show hairball sad at home_topleft
    with dissolve
    
    narrator "Eventually, I just had to accept that I had a new, hairy roommate."
    
    show hairball happy at home_right
    with dissolve
    
    narrator "It was kind of cute and looked harmless enough, so I figured chasing it around the house wasn't worth the trouble."
    narrator "Since it was going to live with me, I decided to give it a name: Wuffeli."

    scene black
    with fade

    $ game_ui_visible = False
    jump scene_selector

    

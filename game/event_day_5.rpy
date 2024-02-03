label day_5:
    $ game_ui_stats_visible = False
    $ game_ui_visible = False

    scene bg bedroom day
    with fade
    play music "Aamu 5 - Ill Be There.mp3"

    narrator "This time I managed to sleep well enough not to feel sluggy. \nOf course, a good cup of fresh coffee from local beans can do wonders."
    narrator "It was Friday already and I have started to notice some small changes in this little buddy of mine."
    narrator "I wasn't too sure yet how they would change over time, but only time will tell I guess."

    scene bg kitchen day
    $ flipped = renpy.random.random() < 0.5
    if flipped:
     $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[home_kitchen_table])
    else:
     $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[home_kitchen_table])
    with dissolve

    narrator "I turned on my radio in the kitchen and listened a while Channel 69's morning podcast \"Morning Talking\"."
    narrator "I sometimes like to listen to their conversation since they come up with random jokes sometimes."
    narrator "They always make me either spill my coffee or almost suffocate me, but are still worth my attention."
    narrator "While I was listening to the podcast, I was planning my today's plans."

    scene bg livingroom day
    with dissolve
    return
label day_4:
    $ game_ui_stats_visible = False
    $ game_ui_visible = False

    scene bg bedroom day
    with fade
    play music "Aamu 4 - Teamwork.mp3"
    narrator "That yesterday's letter was still bugging me throughout the night and I couldn't sleep well because of it."
    narrator "Who was this Hairy Harry and why or what does he know about my pet?"

    scene bg kitchen day
    with fade
    $ flipped = renpy.random.random() < 0.5
    if flipped:
     $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[home_kitchen_table])
    else:
     $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[home_kitchen_table])

    narrator "I poured some good smelling coffee freshly grinded from local quality coffee beans."
    narrator "Not even Finland's famous “Juhla Mokka” compares to this stuff!"
    hemmo "*inhaling the aroma* Aaah~ Ohhhh yeaaaah! That's the gooood stuff!"
    narrator "I then sipped some coffee from my cup."
    hemmo "Mm-mm! De-licious, as always!"
    hemmo "Now then… How should I start this fine Thursday?"

    scene bg livingroom day
    with dissolve

    return
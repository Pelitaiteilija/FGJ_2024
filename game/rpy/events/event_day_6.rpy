label day_6:
    $ game_ui_stats_visible = False
    $ game_ui_visible = False    

    define robo = Character(window_background=None)

    scene black
    with fade
    stop music
    play sound "Scratch.wav"
    pause 1.0

    scene bg bedroom night
    with fade
    play music "Suspense.mp3"
    pause 1.0

    narrator "Morning already?"
    narrator "Or so I thought when I heard an unusual sound from my living room."
    narrator "It was still night time when I regained my consciousness."
    
    narrator "It sounded like scratching furniture, but I wasn't sure if it was that or something else."
    narrator "I tried to ignore it at first, but then I heard it again.{nw}" 
    
    play sound "Muki.wav"
    
    extend "\n{w}This time from the kitchen."
    narrator "Now something hard dropped to the ground. {w}It totally caught me off guard as I jumped a bit even in my bed."
    narrator "I couldn't ignore it any longer and went to investigate the source of the noises."

    scene bg kitchen night
    with dissolve
    pause 1.0
    play sound "Light-switch.wav"
    scene bg kitchen day

    narrator "When I switched the lights on, {nw}"
    play audio "Running.wav"
    extend "light and fast footsteps were heard under the kitchen table."
    narrator "The falling sound apparently came from a mug that I had left on the edge of the table yesterday."
    narrator "So one mystery solved and one left yet to figure out."
    narrator "I approached the table as I felt my palms starting to get sweaty."
    narrator "I also felt my heart rate rise as well when I was getting closer and finally lowering myself to see under the table."

    show punasilmat:
        xalign 0.5
        yalign 0.75
    play sound "Jumpscare.wav"
    with vpunch

    narrator "2 big glowing red eyes appeared in my vision and I let out a small shout while jumping back panically."
    narrator "Those things startled me so much my legs and hands were still shaking from the shock."
    narrator "Then the eyes started to close in and when they came out to the light…"

    hide punasilmat
    show robovacuum:
        zoom .5
        xalign .53
        yalign .95
    with dissolve
    robo "{w=1.0}"
    hemmo "IT WAS MY ROOMBA?!"
    narrator "I should have guessed! What or who else could it have been otherwise?!"
    narrator "My little hairball was still sleeping soundly in its bed after all, so it couldn't be it."
    
    scene bg bedroom night
    with dissolve
    narrator "Frustrated at myself, I went back to my bed and tried to fall asleep once more."
    hemmo "I knew I should have docked it to its charging station after all!"
    hemmo "*sigh* How could I get scared of my own house equipment, for the love of coffee…"
    
    scene black
    with fade
    pause 1.0
    scene bg bedroom day
    with fade
    play music "Aamu 6 - Optimistic.mp3"

    hemmo "*yawn* Gosh, I can still feel some shaking in my hands from last night."
    hemmo "Need to make sure that NEVER happens again. Urgh…"
    
    scene bg kitchen day
    $ flipped = renpy.random.random() < 0.5
    if flipped:
     $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[home_kitchen_table])
    else:
     $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[home_kitchen_table])
    with dissolve
    narrator "As I went to the kitchen to prepare my morning cup of coffee, I noticed some typical magazines and ads dropped from my letterbox as it was that time of the week again."
    narrator "While waiting for my coffee to be cooked, I was pondering today's schedule."

    scene bg livingroom day
    with dissolve
    return


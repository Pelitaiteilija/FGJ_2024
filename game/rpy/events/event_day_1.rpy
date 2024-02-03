label day_1:
    $ game_ui_stats_visible = False
    $ game_ui_visible = False
    hide hairball

    scene bg bedroom day
    with fade
    narrator "It was Monday. The first day I had to share with the fluffy menace."
    
    scene bg livingroom day
    show hairball happy at home_couch
    with fade
    narrator "I spotted it in the living room and it was looking content."
    hemmo "I really wonder why it's so attached to my home."
    
    show hairball neutral at home_kitchen_table
    with dissolve
    
    hemmo "Is there something here that it's looking for or what?"
    narrator "Anyway, time to start the day! What should I do today?"
    narrator "I'm itching for some cupcakes today for some reason. I wonder when I ate those last time?"

    return
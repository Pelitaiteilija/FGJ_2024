label end_of_day:
  $ EndCurrentDay()
  # pick an event, or start a normal day
  jump scene_selector

label scene_selector:
  if current_day == 2:
    call day_2
  elif current_day >= 7:
    jump final_day
    return
  else:
    call basic_day

  jump scene_make_a_choice

label scene_make_a_choice:
  python: 
    global bg_is_night
    # if player has made at least two actions, it is night
    night = max_daily_actions - daily_actions >= 2

  if night and not bg_is_night:
    $ bg_is_night = True
    with None
    show bg livingroom night
    with dissolve
    hemmo "It's late."

  if current_day >= 7:
    return

  $ flipped = renpy.random.random() < 0.5
  if flipped:
      $ renpy.show(f"hairball {hairball_emotion} flipped", at_list=[random_pos])
    # show hairball flipped at random_pos
  else:
      $ renpy.show(f"hairball {hairball_emotion}", at_list=[random_pos])
    #show hairball at random_pos


  hemmo "Hmm, what should I do next?"
  jump scene_make_a_choice
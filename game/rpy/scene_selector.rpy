label end_of_day:
  scene bg bedroom night
  with dissolve
  hemmo "*yawn* Guess I should head to bed since I'm so tired. New day tomorrow and all that. "
  hemmo "Good night, [pet_name]."

  $ EndCurrentDay()
  # pick an event, or start a normal day
  jump scene_selector

label scene_selector:
  if current_day == 1:
    call day_1
  elif current_day == 2:
    call day_2
  elif current_day == 3:
    call day_3
  elif current_day == 4:
    call day_4
  elif current_day == 5:
    call day_5
  elif current_day == 6:
    call day_6
  elif current_day == 7:
    jump final_day
    return
  #else:
    #call basic_day

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
    narrator "The day went by and it's getting late."

  if current_day >= 7:
    return

  $ flipped = renpy.random.random() < 0.5
  if flipped:
      $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[random_home_pos])
      with dissolve
    # show hairball flipped at random_home_pos
  else:
      $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[random_home_pos])
      with dissolve
    #show hairball at random_home_pos

  $ game_ui_visible = True
  $ game_ui_stats_visible = True
  with dissolve
  hemmo "Hmm, what should I do next?"
  jump scene_make_a_choice
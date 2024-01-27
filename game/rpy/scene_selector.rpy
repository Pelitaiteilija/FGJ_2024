label end_of_day:
  $ EndCurrentDay()
  # pick an event, or start a normal day
  jump scene_selector

label scene_selector:
  if current_day >= 7:
    jump final_day
    return
  else:
    call basic_day

  jump scene_make_a_choice

label scene_make_a_choice:
  if current_day >= 7:
    return

  python:
    flipped = renpy.random.random() < 0.5
    print(renpy.random.random())
  if flipped:
    show hairball flipped at random_pos
  else:
    show hairball at random_pos


  human "what should I do next?"
  jump scene_make_a_choice
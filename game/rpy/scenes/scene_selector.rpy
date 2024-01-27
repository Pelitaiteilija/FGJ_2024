label scene_selector:

  $ EndCurrentDay()
  # pick an event, or start a normal day



  if current_day >= 7:
    jump final_day
    return
  else:
    call basic_day

  jump scene_make_a_choice

label scene_make_a_choice:

  human "what should I do next?"
  jump scene_make_a_choice
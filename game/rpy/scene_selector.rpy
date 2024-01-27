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

  human "what should I do next?"
  jump scene_make_a_choice
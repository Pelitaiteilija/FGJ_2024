label show_bg_livingroom_daynight:
  if daily_actions > 1:
    scene bg livingroom day
  else:
    scene bg livingroom night
  return

label show_bg_park_daynight:
  if daily_actions > 1:
    scene bg park day
  else:
    scene bg park night
  return

label show_bg_store_daynight:
  if daily_actions > 1:
    scene bg store outside day
  else:
    scene bg store outside night
  return

label show_bg_kitchen_daynight:
  if daily_actions > 1:
    scene bg kitchen day
  else:
    scene bg kitchen  night
  return





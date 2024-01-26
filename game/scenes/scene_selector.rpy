label scene_selector:
  # start a new day 
  hide placeholder wuffeli
  hide human happy

  # increase day counter
  $ current_day += 1
  #reset daily actions
  $ daily_actions = max_daily_actions

  # pick an event, or start a normal day

  if current_day == 10:
    $ current_day = 3
    jump day_3

  jump basic_day
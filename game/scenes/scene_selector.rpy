label scene_selector:
  # handle end of current day
  $ secret_cleanliness_points -= 1
  $ fitness_points -= 1
  $ hunger_food_points -= 1

  # start a new day 

  # increase day counter
  $ current_day += 1
  #reset daily actions
  $ daily_actions = max_daily_actions

  # pick an event, or start a normal day



  if current_day == 10:
    $ current_day = 3
    $ fitness_points = 5
    $ hunger_food_points = 5
    $happiness_points -= 1
    jump day_3

  jump basic_day
init python:
  def AdjustStats(fullness, happiness, fitness):
    global hunger_food_points, happiness_points, fitness_points
    hunger_food_points += int(fullness)
    happiness_points += int(happiness)
    fitness_points += int(fitness)

  def AdjustStatsAndTrash(fullness, happiness, fitness, cleanliness):
    global secret_cleanliness_points
    AdjustStats(fullness, happiness, fitness)
    secret_cleanliness_points += (cleanliness)

  def EndCurrentDay():
    global secret_cleanliness_points, hunger_food_points, current_day, daily_actions, max_daily_actions
    # handle end of current day
    secret_cleanliness_points -= 1
    hunger_food_points -= 1

    # start a new day 

    # increase day counter
    current_day += 1
    #reset daily actions
    daily_actions = max_daily_actions

  def hide_dynamic_action_overlay():
    renpy.hide("dynamic_action_overlay")

  def get_random_event(events_list, default_event):
    hide_dynamic_action_overlay()
    available_events = events_list
    if len(available_events) > 0:
      # valitse eventti, poista se eventtilistasta
      chosen_event = renpy.random.choice(available_events)
      print(f"Removing activated event '{chosen_event}' from list: '{events_list}'")
      events_list.remove(chosen_event)
      # varmista että valittu eventti on validi, ja jos on, kutsu sitä
      if chosen_event != "" and chosen_event != None:
        renpy.call(chosen_event)
    # jos eventtejä ei kutsuttu, kutsu oletuseventtiä
    renpy.call(default_event)
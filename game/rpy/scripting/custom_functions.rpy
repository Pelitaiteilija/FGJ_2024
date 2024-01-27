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
    global bg_is_night
    bg_is_night = False
    # increase day counter
    current_day += 1
    #reset daily actions
    daily_actions = max_daily_actions
    renpy.call("new_day")

  def hide_dynamic_actionbuttons_UI_screen():
    renpy.hide("dynamic_actionbuttons_UI_screen")

  def get_random_event(events_list, default_event):
    hide_dynamic_actionbuttons_UI_screen()
    available_events = events_list
    if len(available_events) > 0:
      # valitse eventti, poista se eventtilistasta
      chosen_event = renpy.random.choice(available_events)
      print(f"Removing activated event '{chosen_event}' from list: '{events_list}'")
      events_list.remove(chosen_event)
      # varmista että valittu eventti on validi, ja jos on, kutsu sitä
      if chosen_event != "" and chosen_event != None:
        renpy.call(chosen_event)
        return
    # jos eventtejä ei kutsuttu, kutsu oletuseventtiä
    renpy.call(default_event)

  pet_mood = {
    0: "furious",
    1: "furious",
    2: "furious",
    3: "angry", 
    4: "sad", 
    5: "angry", 
    6: "sad",
    7: "neutral",
    8: "sad",
    9: "neutral",
    10: "neutral",
    11: "happy",
    12: "neutral",
    13: "happy",
    14: "happy",
    15: "happy",
    16: "happy"
  }

  def get_random_pet_mood(mood_score):
    mood_score += renpy.random.randint(-4, 4)
    if mood_score < 0:
      mood_score = 0
    elif mood_score >= len(pet_mood):
      mood_score = len(pet_mood) -1
    print(f"Generated a random mood: {pet_mood[mood_score]} ({mood_score})")
    return pet_mood[mood_score]    
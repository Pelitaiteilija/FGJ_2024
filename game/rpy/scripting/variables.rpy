init python:
  weekdays = {
    0:"Sunday",
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday"
  }

  current_day = 1

  max_daily_actions = 3
  daily_actions = 3

  hunger_food_points = 4
  happiness_points = 4
  fitness_points = 4

  pet_name = "Wuffeli"

  

  secret_cleanliness_points = 5
  secret_sleepiness_energy_points = 5

  # used to check whether it's night or day
  bg_is_night = False

  # used to randomize hairball's position in rooms
  random_home_pos = home_center

  # used to randomize hairball's emotion
  hairball_emotion = "angry"

  def init_basic_variables():
    global current_day, max_daily_actions, daily_actions
    global hunger_food_points, happiness_points, fitness_points
    global pet_name
    global secret_cleanliness_points, secret_sleepiness_energy_points, bg_is_night

    current_day = 1
    max_daily_actions = 3
    daily_actions = 3

    hunger_food_points = 4
    happiness_points = 4
    fitness_points = 4

    pet_name = "Wuffeli"
    secret_cleanliness_points = 5
    secret_sleepiness_energy_points = 5
    bg_is_night
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


  secret_cleanliness_points = 5
  secret_sleepiness_energy_points = 5

  def AdjustStats(fullness, happiness, fitness):
    global hunger_food_points, happiness_points, fitness_points
    hunger_food_points += int(fullness)
    happiness_points += int(happiness)
    fitness_points += int(fitness)

  def AdjustStatsAndTrash(fullness, happiness, fitness, cleanliness):
    global secret_cleanliness_points
    AdjustStats(fullness, happiness, fitness)
    secret_cleanliness_points += (cleanliness)
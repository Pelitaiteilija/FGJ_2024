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
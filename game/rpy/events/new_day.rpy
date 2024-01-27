# handles new day / morning
label new_day:
  scene bg livingroom day
  with fade

  python:
    global random_pos, hairball_emotion

    random_positions = [home_center, home_couch, home_kitchen_table, home_left, home_left_corner, home_mirror, home_right, home_topleft, home_topright]

    random_pos = renpy.random.choice(random_positions)

    global hunger_food_points, fitness_points, happiness_points
    hairball_emotion = get_random_pet_mood(hunger_food_points + fitness_points + happiness_points)

  $ renpy.show(f"hairball {hairball_emotion}", at_list=[random_pos])
  return
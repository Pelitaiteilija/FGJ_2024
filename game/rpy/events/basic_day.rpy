label basic_day:
  with None
  scene bg livingroom day

  python:
    random_positions = [home_center, home_couch, home_kitchen_table, home_left, home_left_corner, home_mirror, home_right, home_topleft, home_topright]

    random_pos = renpy.random.choice(random_positions)
    
  show hairball at random_pos

  with dissolve

  human "wow"

  return
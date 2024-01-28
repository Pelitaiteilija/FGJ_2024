init python:
  food_events = []

  def init_food_events():
    global food_events
    food_events = []

label cook_at_home:
  call show_bg_kitchen_daynight
  if daily_actions == 2:
    hemmo "I think I'll cook something nice for breakfast."
    hemmo "An omelette, perhaps?"
  else:
    narrator "You make a simple home-cooked meal."
  call show_bg_livingroom_daynight
  return

label microwave_food:
  call show_bg_store_daynight
  if renpy.random.random() < 0.5:
    narrator "You grabbed a small and convenient ready-made meal from the local grocery store."
    hemmo "Microwave food isn't the best, but it does keep the hunger away."
  else:
    hemmo "I'm up for some \"roiskeläppä\", as we say in Finland."
    hemmo "For a cheap microwave pizza, they have a decent flavor. "
  call show_bg_livingroom_daynight
  return

label fast_food:
  scene bg restaurant
  hemmo "Ooh! They have some fresh croissants and other delicious stuff on sale! Gotta get those!"
  narrator "You got yourself some fast food."
  narrator "It disappears in what feels like just a few moments, but you still feel like you could've gone for more."
  hemmo "I'm not sure if this was the best choice I could've made."
  call show_bg_livingroom_daynight
  return


init python:
  food_events = []

  def init_food_events():
    global food_events
    food_events = []

label cook_at_home:
  narrator "You make a simple home-cooked meal."
  return

label microwave_food:
  call show_bg_store_daynight
  narrator "You grabbed a small and convenient ready-made meal from the local grocery store."
  hemmo "Microwave food isn't the best, but it does keep the hunger away."
  call show_bg_livingroom_daynight
  return

label fast_food:
  call show_bg_store_daynight
  narrator "You got yourself some fast food."
  narrator "It disappears in what feels like just a few moments, but you still feel like you could've gone for more."
  Hemmo "I'm not sure if this was the best choice I could've made."
  call show_bg_livingroom_daynight
  return


init python:
  food_events = []

  def init_food_events():
    global food_events
    food_events = []

label food:
  call show_bg_store_daynight from _call_show_bg_store_daynight
  with fade
  pause 0.5
  scene bg store inside
  with dissolve

  menu:
    hemmo "Should I cook at home something, get a microwave meal or eat something delicious at restaurant?"

    "Cook at home":
      call food_positive from _call_food_positive
      jump cook_at_home

    "Microwave meal":
      call food_neutral from _call_food_neutral
      jump microwave_food

    "Eat at restaurant":
      call food_negative from _call_food_negative
      jump fast_food

###########################################

label food_positive:
  $ hunger_food_points += 2
  $ happiness_points += 1
  return

label food_neutral:
  $ hunger_food_points += 2
  return

label food_negative:
  $ hunger_food_points += 2
  $ happiness_points += 2
  $ fitness_points -= 1
  return

###########################################

label cook_at_home:
  call show_bg_kitchen_daynight from _call_show_bg_kitchen_daynight
  with fade
  if daily_actions == 3:
    hemmo "I think I'll cook something nice for breakfast."
    hemmo "An omelette, perhaps?"
  else:
    narrator "I wanted to make a simple home-cooked meal this time."
    narrator "It's better and cheaper too, even though it can be a pain sometimes."
  $ daily_actions -= 1
  call show_bg_livingroom_daynight from _call_show_bg_livingroom_daynight_9
  with dissolve
  jump scene_make_a_choice

label microwave_food:
  #call show_bg_store_daynight
  #with fade
  if renpy.random.random() < 0.5:
    narrator "I grabbed a small and convenient ready-made meal from the local grocery store."
    hemmo "Microwave food isn't the best, but it does keep the hunger away more or less."
    hemmo "At least it's quite affordable compared to home-made meal or restaurant dishes money- and timewise."
  else:
    narrator "I'm up for some \"mudflap\", as they call it in Finland."
    narrator "For a cheap microwave pizza, they seem to have a decent flavor. Might wanna try other flavors too."
  $ daily_actions -= 1
  call show_bg_livingroom_daynight from _call_show_bg_livingroom_daynight_10
  with dissolve
  jump scene_make_a_choice

label fast_food:
  scene bg restaurant
  with fade
  hemmo "Ooh! They have some croissants and other delicious stuff on sale! Omg, mochies too?!"
  narrator "I ate a tasty chicken-ranch bagel and some seasonal vanilla-cream donuts for dessert. They were SO damn good, omg!"
  hemmo "I'm not sure if this was the best choice I could've made, but at least my taste buds are satisfied."
  $ daily_actions -= 1  
  call show_bg_livingroom_daynight from _call_show_bg_livingroom_daynight_11
  with fade
  jump scene_make_a_choice


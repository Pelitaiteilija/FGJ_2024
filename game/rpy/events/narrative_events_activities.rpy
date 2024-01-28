init python:
  activity_events = []
  internet_events = []
  jogging_events = []
  playing_with_pet_events = []
  nutflix_events = []

  def init_activity_events():
    global activity_events, internet_events, jogging_events, nutflix_events, playing_with_pet_events

    activity_events = []
    internet_events = ["internet_event_1", "internet_event_2", "internet_event_3"]
    jogging_events = ["jogging_event_1"]

    playing_with_pet_events = ["playing_with_pet_event_1"]

    nutflix_events = ["nutflix_event_1", "nutflix_event_2", "nutflix_event_3"]


#########################################################################
#                             INTERNET EVENTS
#########################################################################


label random_internet_event:

  $ get_random_event(internet_events, "default_internet_event")
  return

label default_internet_event:
  narrator "You browse the internet. You find nothing special."
  return

label internet_event_1:
  narrator "You found some rare memes."
  return

label internet_event_2:
  narrator "You found a new game."
  hemmo "Huh, this seems interesting. I'll add it to my wishlist."
  return

label internet_event_3:
  narrator "Your friend told you to check out a new band the discovered."
  hemmo "Wow, I remember these guys! I used to listen to these guys a lot."
  return

#########################################################################
#                             NUTFLIX EVENTS
#########################################################################

label random_nutflix_event:

  $ get_random_event(nutflix_events, "default_nutflix_event")
  return

label default_nutflix_event:
  narrator "You spend a few hours browsing the Nutflix library."
  narrator "For some reason, you have a hard time finding anything you'd like to watch."
  narrator "In the end, you spent more time browsing than actually watching."
  return

label nutflix_event_1:
  hemmo "I remember really liking this series, I wonder what the new season is like?"
  hemmo "... well that was disappointing."
  return

label nutflix_event_2:
  narrator "You rewatch an old favourite of yours."
  hemmo "Still as good as ever!"
  return

label nutflix_event_3:
  narrator "You watch a movie that came out a few years ago."
  hemmo "The ending kinda ruined it..."
  hemmo "Well, not that it was super good any way."
  return

#########################################################################
#              PARK: JOGGING, AND PLAYING WITH THE PET
#########################################################################

label set_random_park_position:
  python:
    random_park_positions = [park_center, park_left, park_right, park_stairs_left, park_tree_center, park_tree_up, park_bench_left, pack_bench_right]
    random_park_pos = renpy.random.choice(random_park_positions)
  return

###
#  CALL THIS TO RANDOMIZE POSITION AT PARK!
#  SEE EXAMPLE USAGE ON default_jogging_event
###
label random_jogging_event:
  call show_bg_park_daynight
  call set_random_park_position

  with None 
  $ global random_park_pos
  $ flipped = renpy.random.random() < 0.5
  if flipped:
      $ renpy.show(f"hairball {hairball_emotion} flipped", at_list=[random_park_pos])
  else:
      $ renpy.show(f"hairball {hairball_emotion}", at_list=[random_park_pos])

  $ get_random_event(jogging_events, "default_jogging_event")
  return

label default_jogging_event: 
  hemmo "I went jogging. It was nice."

  call show_bg_livingroom_daynight
  return

label jogging_event_1:
  narrator "You go out for a walk with [pet_name]. "
  hemmo "Wow, I had forgotten I even had these running shoes."
  hemmo "It's been a while, huh."

  call show_bg_livingroom_daynight
  return


label random_playing_with_pet_event:
  $ get_random_event(playing_with_pet_events, "default_playing_with_pet_event")
  return

label default_playing_with_pet_event:
  call show_bg_park_daynight

  if daily_actions > 1:
    narrator "You took [pet_name] to the park."
    hemmo "That was more fun that I expected."

    call show_bg_livingroom_daynight
    narrator "When you came back, [pet_name] was very tired!"
  else:
    narrator "You took [pet_name] to the park."
    narrator "It was very dark..."
    call show_bg_livingroom_daynight
    hemmo "Well, it was still nice to catch some fresh air."
  return


label playing_with_pet_event_1:
  narrator "You stayed home and played with [pet_name]!"
  return
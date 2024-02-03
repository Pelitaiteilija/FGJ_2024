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
  call show_bg_livingroom_daynight
  with dissolve
  $ get_random_event(internet_events, "default_internet_event")
  return

label default_internet_event:
  hemmo "Anything new on Reddit?"
  hemmo "..."
  hemmo "HAHAHA! Get rekt Karen! That's what you get for judging a book by its cover!"
  hemmo "Haaa... That was a good one, but now I could do something else."
  $ daily_actions -= 1
  return

label internet_event_1:
  narrator "You found some rare memes."
  hemmo "Finally! Some good f**king sauce!"
  hemmo "Okay, enough of memes for now. Time to do something productive as well!"
  $ daily_actions -= 1
  return

label internet_event_2:
  narrator "You found a new game."
  hemmo "Huh, this looks interesting. I'll add it to my wishlist."
  hemmo "I should maybe do something else or this day is wasted on browsing new games."
  hemmo "Too addicting ffs..."
  $ daily_actions -= 1
  return

label internet_event_3:
  narrator "Your video got a new comment."
  hemmo "Hm?"
  hemmo "..."
  hemmo "When does these bot comments end, for real for real?!"
  $ daily_actions -= 1
  return

#########################################################################
#                             NUTFLIX EVENTS
#########################################################################

label random_nutflix_event:
  call show_bg_livingroom_daynight
  with dissolve
  $ get_random_event(nutflix_events, "default_nutflix_event")
  return

label default_nutflix_event:
  narrator "Eh, I don't feel like going out right now. Might as well continue that series that was at a good part."
  narrator "I wonder where that famous chef is going this time to wreck the place..."
  $ daily_actions -= 1
  return

label nutflix_event_1:
  hemmo "I remember really liking this series, I wonder what the new season is like?"
  hemmo "... "
  hemmo "Well that was disappointing."
  $ daily_actions -= 1
  return

label nutflix_event_2:
  hemmo "Let's rewatch an old favourite of mine."
  hemmo "..."
  hemmo "Still as good as ever!"
  $ daily_actions -= 1
  return

label nutflix_event_3:
  hemmo "Hmm, I haven't seen this movie before. Apparenly it came out a few years ago."
  hemmo "..."
  hemmo "The ending kinda ruined it..."
  hemmo "Well, not that it was super good any way."
  $ daily_actions -= 1
  return

label nutflix_event_4:
  hemmo "Eh, I don't feel like going out right now."
  hemmo "I might just as well continue that one series. It was at a good part, too."
  hemmo "I wonder which place that famous chef is going to wreck this time."
  $ daily_actions -= 1
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

  with fade
  $ global random_park_pos
  $ flipped = renpy.random.random() < 0.5
  if flipped:
      $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[random_park_pos])
  else:
      $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[random_park_pos])

  if renpy.random.random() < 0.5:
    $ get_random_event(jogging_events, "default_jogging_event")
  else:
    call default_jogging_event
  return

label default_jogging_event: 
  hemmo "I could do some exercising."
  hemmo "Maybe a little jog for starters to warm up."
  hemmo "I'll go for something more if I feel up for it."
  $ daily_actions -= 1
  call show_bg_livingroom_daynight
  with fade
  return

label jogging_event_1:
  narrator "Might as well go out for a walk with [pet_name]."
  hemmo "Wow, I had forgotten I even had these running shoes."
  hemmo "It's been a while, huh."
  $ daily_actions -= 1
  call show_bg_livingroom_daynight
  with fade
  return

label jogging_event_2:
  narrator "I went for jogging. It feels good to be in the nature and burn some calories sometimes."
  $ daily_actions -= 1
  call show_bg_livingroom_daynight
  with fade
  return

label random_playing_with_pet_event:
  $ get_random_event(playing_with_pet_events, "default_playing_with_pet_event")
  return

label default_playing_with_pet_event:
  
  call show_bg_park_daynight
  if daily_actions > 1:
    $ flipped = renpy.random.random() < 0.5
    if flipped:
      $ renpy.show(f"hairball {persistent.random_pet_mood} flipped", at_list=[random_park_pos])
    else:
      $ renpy.show(f"hairball {persistent.random_pet_mood}", at_list=[random_park_pos])
    narrator "I took [pet_name] to the park. It got excited over a new environment and was dashing everywhere."
    hemmo "That hairball sure got some energy. Just look at that speed and dashing everywhere where happens to be something new to explore."
    narrator "I wonder if normal pet owners feels the same sometimes."

    call show_bg_livingroom_daynight
    with fade
    narrator "When we came back, [pet_name] was so hungry that it started to bite the legs of sofa and tables."
    hemmo "For crying out loud..."
    $ daily_actions -= 1
  else:
    narrator "We decided to go to the park even though it was quite late already."
    narrator "It was very dark and silent. No traffic to make noise or other people chitchatting constantly."
    narrator "It was peaceful now that I think about it. Perfect time for [pet_name] to explore without disturbing others."
    call show_bg_livingroom_daynight
    with fade
    hemmo "Well, it was still nice to catch some fresh air."
    $ daily_actions -= 1
  return

label playing_with_pet_event_1:
  call show_bg_livingroom_daynight
  with dissolve
  narrator "I stayed home and played with [pet_name] for a bit to learn more about it and its behavior."
  narrator "It truly resembled sort of mix both cats and dogs."
  narrator "[pet_name] seems to enjoy its own time and sometimes demanding attention from me by touching my leg with its head."
  hemmo "Well well, who would have guessed..."
  $ daily_actions -= 1
  return

label playing_with_pet_event_2:
  call show_bg_livingroom_daynight
  with dissolve
  narrator "I wonder how that little hairball likes this toy I bought recently."
  narrator "Cats are known to like these, so it will be interesting to see how this turns out."
  narrator "..."
  hemmo "So it does play with it like cats do... Interesting. Duly noted."
  $ daily_actions -= 1
  return
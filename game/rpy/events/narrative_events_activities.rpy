init python:
  activity_events = []
  internet_events = []
  jogging_events = []
  nutflix_events = []

  def init_activity_events():
    global activity_events, internet_events, jogging_events, nutflix_events
    activity_events = []
    internet_events = ["internet_event_1", "internet_event_2", "internet_event_3"]
    jogging_events = ["jogging_events_1"]

label random_internet_event:

  $ get_random_event(internet_events, "default_internet_event")
  return

label default_internet_event:
  hemmo "You browse the internet. You find nothing special."
  return

label internet_event_1:
  hemmo "You found some rare memes"
  return

label internet_event_2:
  hemmo "You found a new game"
  return

label internet_event_3:
  hemmo "Your friend told you to check out a new band."
  hemmo "You remember them from 7 years ago."
  return

label default_jogging_event: 
  scene bg park day
  hemmo "I went jogging. It was nice."
  return

label jogging_event_1:
  scene bg park day
  hemmo "I went out for a quick run. Well... more of a jog, really."
  hemmo "Definitely not walking!"
  return



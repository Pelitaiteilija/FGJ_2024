init python:
  activity_events = []
  internet_events = []
  jogging_events = []
  nutflix_events = []

  def init_activity_events():
    global activity_events, internet_events, jogging_events, nutflix_events
    activity_events = []
    internet_events = ["internet_event_1", "internet_event_2", "internet_event_3"]

label random_internet_event:

  $ get_random_event(internet_events, "default_internet_event")
  return

label default_internet_event:
  human "You browse the internet. You find nothing special."
  return

label internet_event_1:
  human "You found some rare memes"
  return

label internet_event_2:
  human "You found a new game"
  return

label internet_event_3:
  human "Your friend told you to check out a new band."
  human "You remember them from 7 years ago."
  return


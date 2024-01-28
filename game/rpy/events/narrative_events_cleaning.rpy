init python:
  cleaning_events = []

  def init_cleaning_events():
    global cleaning_events
    cleaning_events = []

label random_cleaning_event:
  hemmo "I cleaned up around the house"
  hemmo "It feels like with this hairy menace around, there's always more cleaning to do."
  hemmo "I have to pick my battles if I want to get anything else done."
  return
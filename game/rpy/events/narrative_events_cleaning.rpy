init python:
  cleaning_events = []

  def init_cleaning_events():
    global cleaning_events
    cleaning_events = ["cleaning_event_1"]

label random_cleaning_event:
  $ get_random_event(cleaning_events, "default_cleaning_event")
  return


label default_cleaning_event:
  narrator "I decided to clean up around the house since it was starting to get somewhat dirty."
  narrator "Dusty levels and more hair on the floor."
  narrator "It feels like with this hairy menace around, there's always more cleaning to do."
  hemmo "I have to pick my battles if I want to get anything else done."
  $ daily_actions -= 1
  return

label cleaning_event_1:
  hemmo "*cough cough* Oh dear! How did my apartment get so dusty in such a short time?!"
  hemmo "I really gotta clean it up or else you can find me laying on the hospital bed next time."
  $ daily_actions -= 1
  return
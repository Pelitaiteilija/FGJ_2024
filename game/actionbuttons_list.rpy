init python: 
  class ButtonsDB:
    textButtons = []
    imageButtons = []

    def add(new_button):
      if isinstance(new_button, TextButtonData):
        ButtonsDB.textButtons.append(new_button)
      elif isinstance(new_button, ImageButtonData):
        ButtonsDB.imageButtons.append(new_button)

  class TextButtonData:
    def __init__(self, category, displaytext, id, action_string, event_label = ""):
      self.category = category
      self.displaytext = displaytext
      self.id = id
      self.action_string = action_string
      self.event_label = event_label

  class ImageButtonData:
    def __init__(self, idle_image, hover_image, id, action, action_string, event_label = ""):
      self.idle_image = idle_image
      self.hover_image = hover_image
      self.id = id
      self.action = action
      self.action_string = action_string
      self.event_label = event_label

  text_buttons = [
    TextButtonData("eat", "Cook at home", "actionbutton_eat_healthy", "AdjustStats(2, 1, 0)", "cook_at_home"),
    TextButtonData("eat", "Microwave food", "actionbutton_eat_convenience", "AdjustStats(1, 0, 0)", "microwave_food"),
    TextButtonData("eat", "Unhealthy food", "actionbutton_eat_trash", "AdjustStats(2, 2, -1)", "fast_food"),
    TextButtonData("activity", "Browse the net", "actionbutton_activity_internets", "AdjustStats(0, 1, -2)", "random_internet_event"),
    TextButtonData("activity", "Play with hairball", "actionbutton_activity_playing", "AdjustStats(0, 1, 1)", "random_playing_with_pet_event"),
    TextButtonData("activity", "Jogging", "actionbutton_activity_jogging", "AdjustStats(-1, 1, 2)", "random_jogging_event"),
    TextButtonData("activity", "Watch Nutflix", "actionbutton_activity_nutflix", "AdjustStats(0, 2, -2)", "random_nutflix_event"),
    TextButtonData("clean", "Cleaning", "actionbutton_cleaning_cleaning", "AdjustStatsAndTrash(-1, 0, 1, -2)", "random_cleaning_event")
  ]

  for button in text_buttons:
    ButtonsDB.add(button)

  # define variable used to check which actionbuttons are shown
  # categories: eat, activity, cleaning, rest
  dynamic_category = "activity"
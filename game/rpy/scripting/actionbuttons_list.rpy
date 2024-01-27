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
    TextButtonData("eat", "Cook at home", "actionbutton_eat_healthy", "AdjustStats(1, 1, 0)"),
    TextButtonData("eat", "Microwave food", "actionbutton_eat_convenience", "AdjustStats(1, 0, 0)"),
    TextButtonData("eat", "Fast food", "actionbutton_eat_trash", "AdjustStats(1, 2, -1)"),
    TextButtonData("activity", "Browse the 'net", "actionbutton_activity_internets", "AdjustStats(0, 2, -2)", "random_internet_event"),
    TextButtonData("activity", "Jogging", "actionbutton_activity_jogging", "AdjustStats(0, 1, 2)"),
    TextButtonData("activity", "Nutflix", "actionbutton_activity_nutflix", "AdjustStats(0, 2, -2)"),
    TextButtonData("clean", "Cleaning", "actionbutton_cleaning_cleaning", "AdjustStatsAndTrash(-1, 0, 1, -1)")
  ]

  for button in text_buttons:
    ButtonsDB.add(button)

  # define variable used to check which actionbuttons are shown
  # categories: eat, activity, cleaning, rest
  dynamic_category = "activity"
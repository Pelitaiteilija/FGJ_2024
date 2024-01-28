
screen dynamic_actionbuttons_UI_screen():
  zorder 100
  modal True
  frame:
    id "dynamic_actionbuttons_UI_screen_frame"
    # note! ADD SOLID and BACKGROUND SOLID work differently!
    # add solid has transparency, but only "sees" background color, opaque white by default!
    background Solid ("#0004")

    xalign 0.8
    yalign 0.0
    xpadding 50
    ypadding 10
    xoffset 0
    yoffset 20
    # put all hboxes inside 
    vbox:
      id "dynamic_actionbuttons_overlay"
      style_prefix "dynamic_actionbuttons_overlay"

      textbutton _("↪"):
        id "button_close"
        action Hide("dynamic_actionbuttons_UI_screen")

      for button in ButtonsDB.textButtons:
        if button.category ==  dynamic_category:
          textbutton _(button.displaytext):
            id button.id
            action If (daily_actions > 0, [ 
              SetVariable("daily_actions", daily_actions-1),
              Function(call_custom_function, button.action_string ),
              Hide("dynamic_actionbuttons_UI_screen"),
              If (button.event_label != "", Function(renpy.call, button.event_label))
            ])

style dynamic_actionbuttons_overlay_button_close_text:
  color ("#00F")

init python:
  def call_custom_function(action_string):
    # action string is in the format "functionCall(1, 2, 3)"
    # assume the string has both ( and ) characters
    # find the first (
    # the characters from first char to first ( are the function name, e.g. "functionCall"
    # the parameters are between the () characters, separated by comma
    # parameters are extracted as a list
    try: 
      parenthesis_index = action_string.find('(')
      #print("this is a test")
      function_name = action_string[:parenthesis_index]
      parameters_string = action_string[parenthesis_index + 1:-1]
      parameters = [p.strip() for p in parameters_string.split(',')]

      if function_name in globals() and callable(globals()[function_name]):
        func_to_call = globals()[function_name]
        func_to_call(*parameters)
    except Exception as e:
      pass
      #print(f"Error calling function '{function_name}' with parameters '{parameters}: {e}")
      #print(f"Original string: {action_string}")
      #if (function_name not in globals()):
      #  print(f"{function_name} doesn't exist in globals!" )
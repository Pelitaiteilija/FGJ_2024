
screen dynamic_action_overlay():
  zorder 100
  modal True
  frame:
    id "dynamic_action_overlay_frame"
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
        action Hide("dynamic_action_overlay")

      for button in ButtonsDB.textButtons:
        if button.category ==  dynamic_category:
          textbutton _(button.displaytext):
            id button.id
            action [
              Function(call_custom_function, button.actionstring ),
              Hide("dynamic_action_overlay")
            ]

style dynamic_actionbuttons_overlay_button_close_text:
  color ("#00F")

init python:
  def call_custom_function(actionstring):
    # action string is in the format "functionCall(1, 2, 3)"
    # assume the string has both ( and ) characters
    # find the first (
    # the characters from first char to first ( are the function name, e.g. "functionCall"
    # the parameters are between the () characters, separated by comma
    # parameters are extracted as a list
    try: 
      parenthesis_index = actionstring.find('(')
      print("this is a test")
      function_name = actionstring[:parenthesis_index]
      parameters_string = actionstring[parenthesis_index + 1:-1]
      parameters = [p.strip() for p in parameters_string.split(',')]

      if function_name in globals() and callable(globals()[function_name]):
        func_to_call = globals()[function_name]
        func_to_call(*parameters)
    except Exception as e:
      print(f"Error calling function '{function_name}' with parameters '{parameters}: {e}")
      print(f"Original string: {actionstring}")
      if (function_name not in globals()):
        print(f"{function_name} doesn't exist in globals!" )
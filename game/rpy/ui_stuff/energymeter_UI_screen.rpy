screen energymeter_UI_screen():
  zorder 100
  modal False

  if game_ui_visible and game_ui_energymeter_visible:
    frame:
      id "energymeter_UI_screen_frame"
      background None

      xsize 100
      ysize 100
      xalign 0.23
      yalign 0.0
      xoffset 0
      yoffset 40
      style_prefix "energymeter_UI"
      frame:
        background None
        xpos 0.0
        ypos 0.0

        if daily_actions > 0:
          text "◆": 
            style "energymeter_UI_behind"
          text "⬘"
        else:
          text "◆":
            style "energymeter_UI_text_disabled"
          text "◈":
            style "energymeter_UI_behind"

      frame:
        background None
        xpos 75
        ypos -75

        if daily_actions > 1:
          text "◆": 
            style "energymeter_UI_behind"
          text "⬘"
        else:
          text "◆":
            style "energymeter_UI_text_disabled"
          text "◈":
            style "energymeter_UI_behind"

      frame:
        background None
        xpos 150
        ypos 0

        if daily_actions > 2:
          text "◆": 
            style "energymeter_UI_behind"
          text "⬘"
        else:
          text "◆":
            style "energymeter_UI_text_disabled"
          text "◈":
            style "energymeter_UI_behind"                    

style energymeter_UI_text:
  size 150
  color ("#84e1e8")

style energymeter_UI_behind:
  size 150
  color ("#1ba7b6")  

style energymeter_UI_text_disabled:
  size 150
  color ("#0c322155")  

define game_ui_energymeter_visible = True

init python:
  config.overlay_screens.append("energymeter_UI_screen")

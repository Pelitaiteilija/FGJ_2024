
screen stats_UI_screen():
  zorder 100
  modal False

  if game_ui_visible:  
    frame:
      id "stats_UI_screen_frame"
      # note! ADD SOLID and BACKGROUND SOLID work differently!
      # add solid has transparency, but only "sees" background color, opaque white by default!
      background Solid ("#051515DD")
    
      # add "gui/thoughtbubble.png":
      #  xsize 300
      #  ysize 500

      xalign 0.0
      yalign 0.0
      xpadding 25
      ypadding 25
      xoffset 20
      yoffset 20

          # vboxes arrange stuff vertically, top to bottom
          # matching vboxes will help align things nicely
          #
          # ____________ HBOX ____________
          # |                             |
          # |  __vbox___  _vbox_          |
          # |  |       |  |    |          |
          # |  | text  |  | 1  |          |
          # |  | text2 |  | 4  |          |
          # |  | text3 |  | 6  |          |
          # |  |_______|  |____|          |
          # |_____________________________|
          # 
          # __________ next HBOX __________
          # |_____________________________|


      # put all hboxes inside 
      vbox:
        id "stats_overlay_window"
        spacing 20
        style_prefix "stats_overlay"
        # hbox arranges stuff inside it horizontally, side by side
        hbox:
          id "UI_container_day"
          spacing 20
          # stat names
          vbox:
            xsize 250
            text _(weekdays[current_day%7].upper())
            text _("Day: ")

            if game_ui_stats_visible:
              text _("")
              text _("Fullness:" )
              text _("Happiness:")
              text _("Fitness:")          
          vbox:
            text _("")
            text _(str(current_day)+"/7")

            if game_ui_stats_visible:
              text _("")
              text _(str(hunger_food_points))
              text _(str(happiness_points))
              text _(str(fitness_points))


style stats_UI_screen_frame is frame
style stats_overlay_window is vbox
style stats_overlay_text is gui_text

#style stats_UI_screen:
#    padding gui.frame_borders.padding
#    background Frame("gui/stats_overlay_frame.png", gui.frame_borders, tile=gui.frame_tile)

style stats_overlay_text:
  italic False
  bold True
  color ("#CCC")
  hover_italic True

define game_ui_stats_visible = False

init python:
    config.overlay_screens.append("stats_UI_screen")
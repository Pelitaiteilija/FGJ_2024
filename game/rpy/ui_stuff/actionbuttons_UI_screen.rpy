
screen actionbuttons_UI_screen():
  zorder 100
  modal False

  if game_ui_visible:
    frame:
      id "actionbuttons_UI_screen_frame"
      # note! ADD SOLID and BACKGROUND SOLID work differently!
      # add solid has transparency, but only "sees" background color, opaque white by default!
      #background Solid ("#0002")
      background None

      xalign 1.0
      yalign 0.0
      xpadding 25
      ypadding 10
      xoffset 0
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
        id "actionbuttons_overlay_vbox"
        style_prefix "actionbuttons_overlay"


        textbutton _("Do stuff"):
          id "actionbutton_activity"
          if daily_actions <= 0:
            style "actionbuttons_overlay_button_disabled"
          else:
            action [
              SetVariable("dynamic_category", "activity"),
              Show("dynamic_actionbuttons_UI_screen")
            ]

        textbutton _("Eat stuff"):
          id "actionbutton_eat"
          #hovered Function(renpy.showDynamicActionButtonsOverlay)
          #action Rollback()
          # $ dynamic_category = "eat"
          #action Show("dynamic_actionbuttons_UI_screen")
          if daily_actions <= 0:
            style "actionbuttons_overlay_button_disabled" 
          else:         
            action [
              SetVariable("dynamic_category", "eat"),
              Show("dynamic_actionbuttons_UI_screen")
            ]

        textbutton _("Clean stuff"):
          id "actionbutton_clean"
          if daily_actions <= 0:
            style "actionbuttons_overlay_button_disabled" 
          else:         
            action [
              SetVariable("dynamic_category", "clean"), 
              Show("dynamic_actionbuttons_UI_screen")
            ]

        textbutton _("Sleep"):
          id "actionbutton_rest"
          action Jump("end_of_day")
  

#
#      imagebutton:
#        idle "gui/thoughtbubble.png"
#        hover "gui/bubble.png"
#        xalign 0.5
#        action Rollback()

style actionbuttons_UI_screen_frame is frame
style actionbuttons_overlay_vbox is vbox
style actionbuttons_overlay_button is button
style actionbuttons_overlay_text is gui_text


#style actionbuttons_UI_screen_frame:
#    padding gui.frame_borders.padding
#    background Frame("gui/actionbuttons_overlay_frame.png", gui.frame_borders, tile=gui.frame_tile)

style actionbuttons_overlay_vbox:
  xalign 0.5
  spacing 20

style actionbuttons_overlay_button:
  xsize 250
  ysize 100
  # background Frame("gui/thoughtbubble.png",gui.button_borders, tile=gui.button_tile)
  background Solid("#AFB")
  hover_background Solid("#F5FFc5")
  #hover_background Frame("gui/bubble.png",gui.button_borders, tile=gui.button_tile) 

style actionbuttons_overlay_button_disabled:
  xsize 250
  ysize 100
  # background Frame("gui/thoughtbubble.png",gui.button_borders, tile=gui.button_tile)
  background Solid("#777")
  #hover_background Frame("gui/bubble.png",gui.button_borders, tile=gui.button_tile)  

style actionbuttons_overlay_button_text:
  xalign 0.5
  yalign 0.5
  xpos 0.5
  text_align 0.5
  italic False
  bold True
  color ("#111")
  hover_color ("#094")

style actionbuttons_overlay_button_disabled_text:
  xalign 0.5
  yalign 0.5
  xpos 0.5
  text_align 0.5
  italic False
  bold True
  color ("#333") 

default game_ui_visible = True

init python:
  config.overlay_screens.append("actionbuttons_UI_screen")
  #layers_copy = config.layers
  #for layer in layers_copy:

    # print (renpy.ui.Layer(layer))
  
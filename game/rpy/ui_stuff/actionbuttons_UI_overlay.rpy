
screen actionbuttons_UI_overlay():
  zorder 100
  modal False
  frame:
    id "actionbuttons_UI_overlay_frame"
    # note! ADD SOLID and BACKGROUND SOLID work differently!
    # add solid has transparency, but only "sees" background color, opaque white by default!
    background Solid ("#0002")

    xalign 1.0
    yalign 0.0
    xpadding 50
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
        action [
          SetVariable("dynamic_category", "activity"),
          Show("dynamic_action_overlay")
        ]

      textbutton _("Eat stuff"):
        id "actionbutton_eat"
        #hovered Function(renpy.showDynamicActionButtonsOverlay)
        #action Rollback()
        # $ dynamic_category = "eat"
        #action Show("dynamic_action_overlay")
        action [
          SetVariable("dynamic_category", "eat"),
          Show("dynamic_action_overlay")
        ]

      textbutton _("Clean stuff"):
        id "actionbutton_clean"
        action [
          SetVariable("dynamic_category", "clean"), 
          Show("dynamic_action_overlay")
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

style actionbuttons_UI_overlay_frame is frame
style actionbuttons_overlay_vbox is vbox
style actionbuttons_overlay_button is button
style actionbuttons_overlay_text is gui_text


#style actionbuttons_UI_overlay_frame:
#    padding gui.frame_borders.padding
#    background Frame("gui/actionbuttons_overlay_frame.png", gui.frame_borders, tile=gui.frame_tile)

style actionbuttons_overlay_vbox:
  xalign 0.5
  spacing 20

style actionbuttons_overlay_button:
  xsize 250
  ysize 100
  background Frame("gui/thoughtbubble.png",gui.button_borders, tile=gui.button_tile)
  #hover_background Frame("gui/bubble.png",gui.button_borders, tile=gui.button_tile) 

style actionbuttons_overlay_button_text:
  xalign 0.5
  yalign 0.5
  xpos 0.5
  text_align 0.5
  italic False
  bold True
  color ("#111")
  hover_color ("#F11")
  selected_color ("#A31")


init python:
  config.overlay_screens.append("actionbuttons_UI_overlay")
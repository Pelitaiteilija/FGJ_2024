label day_2:
  $ game_ui_stats_visible = False
  $ game_ui_visible = False
  hide hairball

  scene bg bedroom day
  with fade
  play music "Aamu 2 - Rise.mp3"
  narrator "*yawn* Tuesday, eh?"
  narrator "Hmm, did I have anything I had to do, today?"
  narrator "Oh right, I had to wash the dishes. "
  narrator "I wonder what that hairball does in its free time..."

  scene bg livingroom day
  with fade
  $ renpy.show(f"hairball {hairball_emotion}", at_list=[random_home_pos])
  narrator "Could spend some time with it to find out."
 
  return
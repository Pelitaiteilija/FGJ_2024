label day_2:
  $ game_ui_stats_visible = True

  hemmo "*yawn* Tuesday, eh?"
  hemmo "Hmm, did I have anything I had to do, today?"
  hemmo "Oh right, I had to wash the dishes. "
  hemmo "I wonder what that hairball does in its free time..."
  hemmo "Well, let's see if my new pet [pet_name] has been a good boy?"

  show hairball furious at home_topright
  with dissolve
  

  hairball "Wrrrwrwroffof wrrr!"

  hemmo "What!"
  hemmo "Oh no!"

  with None
  show hairball angry at home_center
  with fade
  narrator "A few hectic moments later..."
  return
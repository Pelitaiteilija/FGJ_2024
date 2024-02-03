label day_3:
  $ game_ui_stats_visible = False
  $ game_ui_visible = False

  scene bg bedroom day
  with fade
  play music "Aamu 3 - Minor Distraction.mp3"
  narrator "A truck drove by my window that morning and woke me up by its loud engine noise."
  narrator "Not the best kind of way to wake up and start the day."
  hemmo "Hm?"

  scene bg livingroom day
  show hairball neutral at home_mirror
  with fade
  narrator "I noticed a letter in front of my front door along with some magazine and ads."
  narrator "They get delivered every Wednesday and Saturday, but usually it's only some random litter."
  narrator "I read the letter and it was from someone named \"Hairy Harry\". The message was as weird as the sender's name:"

  define harry = Character("Hairy Harry")

  harry "\"Take good care of that little hairball and you'll be surprised to see what it will turn into after a while...\""

  narrator "So this Hairy Harry apparently had something to do with [pet_name] that appeared the other day."
  narrator "While I was thinking that, I was also thinking about what I would do today."

  return
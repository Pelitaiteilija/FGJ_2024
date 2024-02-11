label final_day:
  if fitness_points > 10:
    jump good_ending
  elif fitness_points > 5:
    jump true_ending
  else:
    jump bad_ending
  

label good_ending:
  $ game_ui_stats_visible = False
  $ game_ui_visible = False

  scene bg bedroom day
  with fade
  play music "Good Ending - Dreamers.mp3"
  narrator "As I woke up to a sunny Sunday's morning, I felt something laying on top of me."
  narrator "As I opened my eyes, I noticed it was my good buddy. It must have climbed itself over there like a cat at some point probably."
  narrator "I also noticed that it had something new grown to its sides that looked like tiny paws. How cute. <3"
  narrator "I then petted its head a little bit and moved it beside me on the bed."

  scene bg kitchen day
  with fade
  narrator "After getting myself up from the bed, I changed into my sports clothes and prepared my favorite morning coffee."
  narrator "While I was waiting for my coffee to be ready, [pet_name] had apparently woken up and came to the kitchen as well."
  
  show hairball happy at home_kitchen_table
  with dissolve
  hemmo "Eager for the morning journey, are we?"

  show hairball happy:
    linear .1 ycenter .4
    linear .1 ycenter .52
    repeat 2

  narrator "[pet_name] nodded and jumped a few times in the air to show its excitement I guess."
  hemmo "Whoa! You can actually understand me or something?!"

  show hairball happy:
    linear .1 ycenter .56
    linear .1 ycenter .52
  narrator "It nodded again."
  hemmo "That is SO cool! This will improve our communication a lot compared to regular home pets."
  narrator "Next I fetched my morning coffee and drank it peacefully. Coffee should be enjoyed with peace and not at once or in a hurry."
  narrator "It will just ruin its sensitive aroma that way."
  narrator "Me, myself and the little hairball were then ready to start the day and its first hurdle: Morning jog"
  
  scene bg ending good
  with fade
  pause 1.5
  narrator "It managed to keep up with my pace even though it was smaller than me."
  narrator "It was so unbelievable that I nearly ran into a light pillar in the sidewalk because I couldn't keep my eyes from that buddy."
  narrator "While jogging, a thought about that letter from Wednesday came to mind and its sender Hairy Harry."
  narrator "Many questions popped to mind from those two things, yet almost any answers to any of them."
  narrator "What actually is this little hairball of mine and where it came from?"
  narrator "Who is this Hairy Harry and why does he know stuff about this creature?"
  narrator "This much at least can be said: He knows more than I can probably even imagine."
  narrator "He predicted this buddy's evolution of sort before I was even aware of it."
  hemmo "Well… \nThere's only one way to get answers to this:"
  hemmo "Find Hairy Harry and ask him directly."

  scene black
  with fade

  return

label true_ending:
  $ game_ui_stats_visible = False
  $ game_ui_visible = False

  scene bg bedroom day
  with fade
  play music "True Ending - Beach Vibes.mp3"

  narrator "As I woke up to a sunny Sunday's morning, I felt something laying on top of me."
  narrator "I opened my eyes and noticed it was my little hairball friend that had climbed to my bed at some point of the night."
  hemmo "Morning, buddy."
  narrator "The hairball pet just kept sleeping soundly on top of my belly like a typical cat would."
  narrator "I wondered if they would have more similarities like this."
  
  scene bg kitchen day
  with fade
  pause 1.5
  narrator "As I pondered that question, I prepared my trusty morning coffee and looked outside the window in the kitchen."
  narrator "The sunrise was not too bright yet at this early in the morning. It was shining gently from the horizon beyond the beach nearby."
  narrator "Quite the location to have a beach almost next to you and see the sunrise from the kitchen window right after you wake up."
  narrator "It reminds me of Jazz-music for its gentleness and slow tempo, how you can just take your time and prepare mentally yourself for today's challenges."
  narrator "My coffee was ready and its lovely aroma started to fill the room."
  narrator "I could feel the aroma filling my mind with positive energy and after taking in the first sippy-sippy, it touched my soul like a lover would touch your cheek."
  narrator "It was gentle and heartwarming. It made me feel like I could even synchronize myself with nature if I went outside now."
  
  scene bg ending beach
  with fade
  narrator "So I fetched my hairy buddy from the bed and went to watch the sunrise at the beach together."
  narrator "It was a beautiful and peaceful sight to behold."
  narrator "As I sat down on the sand and leaned back to the grassy edge, I petted the little hairball in my lap and watched the sunrise."
  narrator "I maybe haven't still found out this buddy's origins or that Hairy Harry, but perhaps one day that will happen."
  narrator "Until then I'll keep it company and watch over it."

  scene black
  with fade

  return

label bad_ending:
  $ game_ui_stats_visible = False
  $ game_ui_visible = False

  scene bg bedroom day
  with fade
  play music "Bad Ending - The Mirror.mp3"
  
  narrator "As I woke up to a sunny Sunday's morning, I felt something laying on top of me."
  narrator "I grabbed and threw it off to the floor."
  narrator "It was so startled by it that it jumped in the air and bounced from the wall over my bed to the other side."
  narrator "Incredible agility that hairball got at least, if nothing else."
  narrator "It then looked at me and growled with a displeased look on its face. Like I would care actually."
  narrator "It still was an unknown creature that had invaded itself here from who knows where and the only clue of its origins would be that of Hairy Harry."
  narrator "Well… Since I was stuck with it, wanted it or not, I just had to learn to live with it. One way or another."
  
  scene bg ending bad
  with fade
  pause 1.5
  narrator "Regardless, I dragged myself to the kitchen, grabbed one of those \"mudflaps\" and put it in the microwave."
  narrator "I then waited one and half minutes for it to be reheated and went to the sofa."
  narrator "I turned my TV on and started Nutflix-service."
  
  play sound "Scratch.wav"
  narrator "That little hairball tip topped itself over to the living room as well and started scratching walls and other furniture."
  narrator "It turned out to be a little devil if you ask me."
  narrator "Disciple was useless to it, so I had given up on training it altogether and just let it be a free loafer in the household."
  narrator "I didn't care anymore at that point, so I just try to live with it now and let it do as it pleases mostly."
  narrator "Of course, occasional fights happen when it crosses the line and disturbs my activities."
  narrator "Then I really try to stop it by force and usually I win in combat as I'm a bigger opponent."
  narrator "Anyway, such is life when it gives you lemons. You either pick yourself up at that point or just let it happen and see how it turns out."
  narrator "I chose the latter. Do I regret it? Hmm, maybe? I'm just depressed at this point…"
  narrator "Maybe I should seek professional help some day."
  narrator "Eh, I'll think about it after this episode."

  scene black
  with fade

  return
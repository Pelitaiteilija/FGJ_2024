label final_day:
  if fitness_points > hunger_food_points and fitness_points >= happiness_points and fitness_points > 4:
    jump good_ending
  elif happiness_points > hunger_food_points and happiness_points > fitness_points and happiness_points > 4:
    jump true_ending
  else:
    jump bad_ending


  narrator "The End"
  return
  return
  

label good_ending:
  scene bg bedroom day
  hemmo "As I opened my eyes, I noticed it was my good buddy. It must have climbed itself over there like a cat at some point probably."
  hemmo "I also noticed that it had something new grown to its sides that looked like tiny paws"
  hemmo "How cute. <3"
  hemmo "I then petted its head a little bit and moved it beside me on the bed."

  scene bg kitchen day
  hemmo "After getting myself up from the bed, I changed into my sports clothes and prepared my favorite morning coffee."
  hemmo "While I was waiting for my coffee to be ready, that little hairball had apparently woken up and came to the kitchen as well."
  hemmo "Eager for the morning journey, are we?\"
Little hairball nodded and jumped a few times in the air to show its excitement I guess."
  hemmo "Whoa! You can actually understand me or something?!"
  hemmo "It nodded again."
  hemmo "That is SO cool! This will improve our communication a lot compared to regular home pets."
  scene bg park day
  hemmo "Next I fetched my morning coffee and drank it peacefully. Coffee should be enjoyed with peace and not at once or in a hurry. It will just ruin its sensitive aroma that way."
  hemmo "Me, myself and the little hairball were then ready to start the day and its first hurdle: Morning jog"
  scene bg ending good
  hemmo "It managed to keep up with my pace even though it was smaller than me. It was so unbelievable that I nearly ran into a light pillar in the sidewalk because I couldn’t keep my eyes from that buddy."
  hemmo "While jogging, a thought about that letter from Wednesday came to mind and its sender Hairy Harry."
  hemmo "Many questions popped to mind from those two things, yet almost any answers to any of them."
  hemmo "What is actually this little hairball of mine and where did it come from?"
  hemmo "Who is that Hairy Harry and why does he know about this creature."
  hemmo "That much at least can be said: He knows more than I can probably even imagine. He predicted this buddy’s evolution of sort after all before I was even aware of it."
  hemmo "Well…\n
  There's only one way to get answers to this: Find Hairy Harry and ask him directly."
  return

label true_ending:
  scene bg livingroom day
  show overlay ending true
  hemmo "I opened my eyes and noticed it was my little hairball friend that had climbed to my bed at some point of the night."
  hemmo "Morning, buddy."
  hemmo "The hairball pet just kept sleeping soundly on top of my belly like a typical cat would. I wondered if they would have more similarities like this."
  hemmo "As I pondered that question, I prepared my trusty morning coffee and looked outside the window in the kitchen. The sunrise was not too bright yet at this early in the morning. It was shining gently from the horizon beyond the beach nearby."
  hemmo "Quite the location to have a beach almost next to you and see the sunrise from the kitchen window right after you wake up."
  hemmo "It reminds me of Jazz-music for its gentleness and slow tempo, how you can just take your time and prepare mentally yourself for today’s challenges."
  hemmo "My coffee was ready and its lovely aroma started to fill the room. I could feel the aroma filling my mind with positive energy and after taking in the first sippy-sippy, it touched my soul like a lover would touch your cheek."
  hemmo "It was gentle and heartwarming. It made me feel like I could synchronize myself with nature if I went outside now."
  hemmo "So I fetched my hairy buddy from the bed and went to watch the sunrise at the beach together. It was a beautiful and peaceful sight to behold."
  hemmo "As I sat down on the sand and leaned back to the grassy edge, I petted the little hairball in my lap and watched the sunrise."
  hemmo "I maybe haven't still found out this buddy's origins or that Hairy Harry, but perhaps one day that will happen. Until then I'll keep it company  and watch over it."

  return

label bad_ending:
  scene bg ending bad
  hemmo "I grabbed and threw the little monster at the floor."
  hemmo "It was so startled by it that it jumped in the air and bounced from the wall over my bed to the other side. Incredible agility it got at least, if nothing else."
  hemmo "It then looked at me and growled with a displeased look on its face. Like I would care actually."
  hemmo "It still was an unknown creature that had invaded itself here from who knows where and the only clue of its origins would be that of Hairy Harry."
  hemmo "Well… Since I was stuck with it, wanted it or not, I just had to learn to live with it. One way or another."
  hemmo "Regardless, I dragged myself to the kitchen, grabbed one of those “roiskeläppä”s and put it in the microwave. I then waited one and half minutes for it to be reheated and went to the sofa."
  hemmo "I turned my TV on and started Nutflix-service. That little hairball tip topped itself over to the living room as well and started to scratch walls and other furniture."
  hemmo "It turned out to be a little devil if you ask me, but since the disciple was useless to it, I had given up on training it altogether and just let it be a free loafer in the household."
  hemmo "I didn't care anymore at that point, so I just try to live with it now and let it do as it pleases mostly. Of course, occasional fights happen when it crosses the line and disturbs my activities."
  hemmo "Then I really try to stop it by force and usually I win in combat as I'm a bigger opponent."
  hemmo "Anyway, such is life when it gives you lemons. You either pick yourself up at that point or just let it happen and see how it turns out."
  hemmo "I chose the latter. Do I regret it? Hmm, maybe? I'm just depressed at this point… Maybe I should seek professional help some day."
  hemmo "Eh, I'll think about it after this episode."


  return
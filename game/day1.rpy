label day1_main:           
    stop music fadeout 2.0
    scene bedroom with openeyes
    play music liveforever
    "I wake up to the sound of my door being knocked on. I must’ve slept in!"
    "I get out of my bed, ready to go and answer the door."
    "I quickly put on my uniform and head downstairs."
    scene frontdoor with wipeleft
    "I open the door and I'm greeted by Sayori, my neighbor and childhood friend."
    show sayori turned pani om ce rup lup at t11 zorder 3
    s "[player]! You slept in! We're gonna be late!"
    mc "Woah, calm down Sayori! Come in."
    s "There's not enough time!"
    "Sayori drags me out of my house by the arm, all the way on to the street."
    scene residential with wipeleft
    show sayori turned happ rup lup om ce at h11 zorder 3
    s "See, that wasn't too hard!"
    mc "You can be really annoying sometimes."
    hide sayori
    show sayori tap pout oe cm at h11 zorder 3
    s "Meanie..."
    scene bg class_day with dissolve_scene_full
    stop music fadeout 1.0
    "The day was long and the work was hard, but I’m finally able to go to the club!"
    scene bg corridor with wipeleft
    "I'm just outside the clubroom when something strange catches my eye."
    "Or should I say, someone."
    mc "Hello?"
    show sienna 1c at h11 zorder 3
    $ si_name = "???"
    si "Hey! Are you [currentuser]? I'm looking for the Literature Club."
    mc "No, I'm [player], but the Literature Club is just through here."
    "I guide the new girl through the door and into the clubroom."
    scene bg club_day with wipeleft
    show sienna 1a at t11 zorder 3
    si "I'm sorry, I forgot to introduce myself! My name is Sienna."
    $ si_name = "Sienna"
    mc "It's nice to meet you Sienna!"
    si "Are you a member here?"
    mc "Yeah, it's only my second day."
    si "Cool! We can be newbies together."
    "The club is deadly silent apart from me and Sienna"
    mc "It seems like nobody's here yet"
    si 1b "Well, I guess we can use this time to get to know each other."
    mc "Sounds good!"
    hide sienna with dissolve
    "A few minutes pass before Monika, Sayori, Natsuki and Yuri all enter the clubroom together."
    "Though Sienna and I only had a few minutes alone together, I really feel like I’ve gotten to know her."
    mc "Hey girls! What kept you behind?"
    m "Oh! [player]! We just got caught up in conversation"
    m "Sorry if you were waiting!"
    m "I see you brought someone new?"
    mc "Oh yeah, this is Sienna"
    si "Hi! You must be Monika, MC told me a lot about you."
    m "I hope it was all good!"
    si "Well, he's quite the charmer. I don't think he could say anything bad about anyone!"
    mc "Sienna, I-"
    "I feel a slight blush reddening my cheeks"
    n "Hi, nice to meet you! I’m Natsuki and if you say anything bad about manga I’ll snap your neck."
    si "Oh, I-I’ll be sure not to…"
    mc "{i}Don't worry, she's just trying to intimidate you.{/i}"
    n "What was that?"
    mc "I- uh, nothing..."
    n "Thought so."
    s "Natsuki! We don't want to scare a new member away!"
    n "I'm just laying down the law."
    s "Then do it in a more civilised manner."
    n "Whatever you say, Lord Almighty Ruler."
    s "Sorry about her, she can be moody sometimes."
    s "Anyway, I'm Sayori, it's nice to meet you."
    si "Likewise."
    "There's only one person still left to introduce themselves and they're currently hiding at the back of the group"
 
    return

label day1_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music ohayousayori

    $ restore_all_characters()
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ si_name = "???"

    
    "I wake up to the sound of my door being knocked on. I must've slept in!"
    "I get out of my bed, ready to go and answer the door. I quickly put on my uniform and go downstairs."
    
    scene frontdoor


    "The knocking keeps getting louder and louder as I reach the door."
    "I’m greeted by Sayori, my childhood friend and long-time neighbor."

    show sayori 2j zorder 2 at t11
    s "[player]! What are you doing? I’ve been waiting for you for like an hour!"
    show sayori 2i zorder 2 at t11
    mc "I slept in, sorry. Come in, I need to make breakfast."
    
    s 2m "Breakfast?! We’re going to be late!"
    "Sayori drags me out of my house."
    s 2m "Come on! Hurry up!"
    show sayori 2p zorder 2 at thide
    hide sayori
    mc "Alright, alright! I'm coming."

    scene bg class_day 
    with dissolve_scene_full

    stop music
    play music t5
    "The day was long and the work was hard, but I’m finally able to go to the club!"
    
    scene bg corridor
    with dissolve_scene_full
    
    "I’m just outside the club room door when I see someone unusual."
    mc "Hello?"
    show sienna 2c zorder 2 at t11
    si "Oh hi! Are you [currentuser]? I'm looking for the Literature Club."
    show sienna 2a zorder 2 at t11
    mc "No, I'm [player]. The Literature Club is just through here."
    "I guide the new girl through the door and into the clubroom."
    show sienna 1h zorder 2 at thide
    hide sienna
    
    scene bg club_day
    with dissolve_scene_full

    show sienna 1g zorder 2 at t11
    si "I'm sorry, I forgot to introduce myself!"
    $ si_name = "Sienna"
    si 3h "I'm Sienna, thanks for helping me. Are you a member here?" 
    
    mc "Yeah, it's only my second day."
    si 1j "Nice! We can be newbies together!"
    show sienna 1a zorder 2 at t11
    "The club room is deadly silent apart from me and Sienna."
    
    "Nobody's here yet. Weird."
    si 1d "We can use this time to get to know each other more."
    show sienna 1a zorder 2 at t11
    mc "Good idea."
    show sienna 1a zorder 1 at thide
    hide sienna
    show monika 3a zorder 2 at t41
    show sayori 2a zorder 2 at t42
    show natsuki 2g zorder 2 at t43
    show yuri 1f zorder 2 at t44
    "A few minutes pass before Monika, Sayori, Natsuki, and Yuri all enter the clubroom together."
    "Though Sienna and I only had a few minutes alone together, I really feel like I've gotten to know her."
    mc "Hey girls! What kept you?"
    show monika 3b zorder 3 at f41 
    m "Oh, [player]! Sorry about that, we got caught up in a conversation."
    m "I see you brought someone new?"
    show monika 3a
    show natsuki 2g
    mc "Oh, yes! This is Sienna, I met her a few minutes ago outside the clubroom."
    show sayori 3a zorder 1 at thide
    hide sayori
    show natsuki zorder 1 at thide
    hide natsuki
    show yuri zorder 1 at thide
    hide yuri
    show monika 3a zorder 2 at t21
    show sienna 2c zorder 2 at f22
    si "Hi! You must be Monika, [player] told me a lot about you."

    show monika 3l zorder 2 at f21
    show sienna 2c zorder 2 at t22
    m "I hope it was all good!"

    show monika 3l zorder 2 at t21
    show sienna 3j zorder 2 at f22
    si "He's quite the charmer, I don't think he could say anything bad about anyone!"
    mc "Sienna I-"
    show monika 3j zorder 1 at thide
    hide monika 
    show sienna 1a zorder 2 at t22
    show natsuki 5d zorder 2 at f21
    n "Hi, nice to meet you! I'm Natsuki."
    n 5y "And if you say anything bad about manga, I'll snap your neck."
    show natsuki 5y zorder 2 at t21
    show sienna 3s zorder 2 at f22
    si "Oh, I'll be sure not to..."
    show sienna 3s zorder 2 at t22
    mc "Don't worry, she's just trying to intimidate you."
    show natsuki 5f zorder 2 at f21
    show sienna 3w zorder 2 at t22
    n "What was that?!"
    mc "Oh, uh... Nothing!"
    n 5g "That's what I thought."
    show sayori 3j zorder 2 at l31
    show sayori 3j zorder 2 at f31
    show natsuki 5g zorder 2 at t32
    show sienna 1p zorder 2 at t33
    s "Natsuki! We don't want to scare off a new member, do we?"
    show sayori 3i zorder 2 at t31
    show natsuki 5y zorder 2 at f32
    n "I'm just laying down the law!"
    show natsuki 5y zorder 2 at t32
    show sayori 3j zorder 2 at f31
    show sienna 1o zorder 2 at t33
    s "Then do it in a more civilized way!"
    show natsuki 5s zorder 2 at t32
    show sayori 4r zorder 2 at hf31
    s "Anyway, welcome to the club Sienna! I'm Sayori, the vice president {i}and{/i} [player]'s childhood friend!"
    show sayori 4r zorder 2 at t31
    show sienna 1r zorder 2 at f33
    si "Well, it's nice to meet you Sayori"
    show sayori 4r zorder 1 at thide
    hide sayori
    show natsuki 5s zorder 1 at thide
    hide natsuki
    show sienna 1r zorder 1 at thide 
    hide sienna
    "There's only one person left to introduce themselves, and she's currently hiding away at the back of the group."
    mc "I'm sure Yuri would love to introduce herself to you Sienna, but she seems to have gone a bit shy!"
    show yuri 4b zorder 2 at f21
    show sienna 1f zorder 2 at t22
    y "I, uh..."
    y 4a "It's nice to meet you..."
    show yuri 4a zorder 2 at s21
    "Yuri brings herself to the front of the group and avoids eye contact with Sienna, before saying what she has to and scurrying back."
    show yuri 4c zorder 2 at thide
    hide yuri
    
    show sienna 1h zorder 2 at f11
    "Sienna laughs lightly"
    show sienna 1j zorder 2 at f11
    si "Well, it's wonderful to meet you all! I am glad I decided to drop by Monika's Literature Club!"
    show monika 3k zorder 2 at f21
    show sienna 1h zorder 2 at t22
    m "Well, I'm sure glad you decided to come too. Isn't that right, girls?"
    show monika 3j zorder 2 at t31
    show sienna 1h zorder 2 at t32
    show natsuki 2h zorder 2 at f33
    n "Yeah, I guess. But I didn't get to make cupcakes!"
    show natsuki 2h zorder 2 at t33
    mc "Aha! So you {i}did{/i} make them for me!"
    show natsuki 1o zorder 2 at f33
    n "No, I never said that!"

    show natsuki 1o zorder 1 at thide
    hide natsuki
    show sienna 1a zorder 1 at thide
    hide sienna
    show monika 3l zorder 1 at thide
    hide monika


    "I want to get to know Sienna better, so I walk over to where she is sitting."
    show sienna 1h zorder 2 at f11
    mc "Hi Sienna, me again."

    si 2h1 "Hey [player], wanna sit next to me?"
    mc "Yeah! Sure."
    show sienna 1h zorder 2 at f11
    "As I pull a seat over to sit next to Sienna, I feel someone staring at me from across the room. But when I turn around, nobody is looking."
    mc "So, what've you been up to?"
    si 1d "Well, Yuri let me borrow this book."
    "She shows me the cover of the book. It had a large eye emblazoned on the front, with the words 'Portrait of Markov' above it."
    "It's ominous and slightly creepy."
    mc "Oh, that's sweet of her. What's it about?"
    si 1f "I don't really know, I just started it and the blurb doesn't really tell me much."
    mc "Ah, well it definitely looks like a scary book."
    si 1c "You bet, even the first few pages are scary!"
    show sienna 1h zorder 2 at f11
    "Sienna and I spend a few more minutes conversing before Siena ends the chat."
    si 1d "Well, it was nice talking to you, but I'm going to read a bit more of this book."
    mc "Alright, I'll go talk to Yuri or something. Enjoy!"
    si 1k "Finally, a bit of peace and quiet, aha!"
    mc "Rude!"

    show sienna 1k zorder 2 at thide
    hide sienna

    "I get up from my seat and decide to go and talk to Yuri."
    "I feel as though I haven't spoken to her much, but that goes for everyone else in the literature club. How am I going to balance this out?"
    show yuri 1e zorder 2 at f11
    mc "Hey Yuri!"
    show yuri 1n zorder 2 at hf11
    y  "O-oh, hi [player]"
    "Yuri looks up at me with a startled expression on her face."
    mc "Oh, I'm sorry. Did I scare you?"
    y 1t "No, no... I'm fine, you don't need to apologize!"
    mc "So then, what are you up to?"
    y 1f "Well, I was just reading this book..."
    mc "Ah, is that the same one you let Sienna borrow?"
    y 1m "Mhm..."
    mc "What is it about? She didn't tell me."
    y 1e "Hmm, it's mostly about a young girl who is trapped in a world of fantasy, trying to break free as the world around her crumbles and turns into a nightmare."
    y 1v "Everyone she loves is fake, and that sends her into insanity, as she murders all of her friends just to be with her true love."
    mc "That's not your normal fairy tale."
    y 1f "No, it was written to juxtapose most otherworldly tales, showing how bad your own mind can make you, and how not everything in the world is good."
    y 4a "D-do you want to read it with me?"
    "How can I resist? Yuri is too sweet to ever say no to her."
    mc "Yeah, alright."
    stop music
    play music liveforever
    scene y_cg1_base
    with dissolve_cg
    "Yuri and I sit next to each other, with her holding one end of the book and me holding the other, flipping pages in unison as we finish reading a page."
    "Yuri's clearly a faster reader than me, but I can sense that she doesn't mind, oftentimes stopping and asking me if I was reading everything alright."
    "The longer Yuri and I read together, the more I feel myself falling for her."
    "The longer we read together, the closer we get to each other."
    "The longer we read-"
    show y_cg1_exp1 at cgfade
    y "Are you okay?"
    "Yuri looks at me."
    mc "What?"
    y "Are you okay? You seem to have spaced out."
    mc "O-oh sorry, I was just thinking about s-stuff."
    y "Ah, well I hope it was nothing too bad."
    mc "No, it was nice, happy thoughts."
    y "That's good to hear."
    hide y_cg1_exp1
    "Yuri looks back at the book, and I take the hint and continue reading."

    scene bg club_day
    with dissolve_scene_full
    show monika 4b zorder 2 at f11
    m "Okay everyone! I think we should pack up and head home, it's getting late!"
    show monika 4a zorder 2 at thide
    hide monika
    "Monika interrupts Yuri and I from our reading session, and we both look at each other, knowing that it's time to go."
    show yuri 2d zorder 2 at f11
    y "[player], I had a lot of fun today. I'd like to thank you."
    show yuri 2c zorder 2 at t11
    mc "I'd like to thank {i}you{/i}. I didn't think I'd read a book today and it's much more enjoyable than I thought."
    show yuri 3u zorder 2 at f11
    y "I'm glad I got to share that experience with you. It's really one of the most special things you can do."
    show yuri 3t zorder 2 at f11
    y "A-anyway, I've got to go. I'm sorry for rambling on!"
    mc "No, it's oka-"
    show yuri 4a zorder 2 at d11
    y "Bye [player], s-see you tomorrow."
    show yuri 4a zorder 2 at thide
    hide yuri
    show sayori 3r zorder 2 at hf11
    s "Hey [player], want to walk home with me?"
    mc "Yeah, sure. Lead the way!"
    show sayori 3r zorder 2 at thide
    scene bg residential_day with wipeleft
    show sayori turned happ rup ldown ce om at t11 zorder 3
    "Sayori is talking to me right now, but I'm not sure if I'm listening."
    show sayori at thide
    hide sayori
    "I can't stop thinking about the club..."
    "More specifically the new member, and Yuri"
    show yuri turned happ cm ce rup lup at t21 zorder 3
    show sienna 1h at t22 zorder 3
    "They're both amazing from what I know of them"
    "They both have their flaws but that makes them even more perfect"
    "God, why does life have to be so good?"
    show sienna at thide
    show yuri at thide
    hide sienna
    hide yuri
    show sayori turned neut oe cm rup ldown at t11 zorder 3
    s "[player]?"
    mc "Yes?"
    s "Are you alright? You were spacing out pretty bad"
    mc "I, uh..."
    mc "I'm fine, I was just thinking about homework"
    s doub cm oe ldown rdown "I'm sure you were"
    s "I'm not an idiot, [player]!"
    mc "I know that, Sayori."
    s neut oe cm "I'm your best friend, if something is wrong you can always tell me!"
    mc "If I told you everything I was thinking you'd run around school telling everyone with your big mouth!"
    s tap pout oe cm "Meanie..."
    "We cross the street and end up at Sayoi's house"
    scene house with wipeleft
    show sayori turned happ cm oe at t11 zorder 3
    s turned happ cm oe "Anyway, this is where I leave you."
    s pout om oe "I {b}will{/b} find out what's up with you."
    mc "Sure you will."
    mc "See you tomorrow, Sayori"
    s happ ce cm "See ya!"
    show sayori at thide zorder 3
    hide sayori
    "Now that Sayori is at her house, I begin to make my own way home."
    "Sayori can be a nuisance sometimes, but I guess that's why I love her."
    scene bg house with wipeleft
    "I arrive at my front door, and let myself in."
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    pause 2.0
    return
    

    return

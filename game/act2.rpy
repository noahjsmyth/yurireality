label act2:
     $ persistent.playthrough = 33
     if persistent.playthrough == 22:
        $ style.say_window = style.act2TextBox
     elif persistent.playthrough == 33:
        $ style.say_window = style.act3TextBox
     scene bedroom with dissolve
     mc "Y-Yuri?"
     y "[player]? Are you up?"
     mc "Y-Yuri, what happened? Where am I?"
     y "Remember, the coffee shop? What happened after everyone left?"
     mc "Oh yeah."
     mc "It's all coming ba-{nw}"
     mc "WAIT!"
     mc "WHAT ABOUT THE VIRUS"
     y "I haven't been able to fix it..."
     mc "M-Monika"
     y "No, I'm Yuri. Are you okay?"
     mc "No, Monika can help"
     y "How can I trust her with power of the console after what she did?"
     mc "It's the only way"
     mc "Trust..."
     mc "Her..."
     y "If anything goes wrong, I blame you."
     mc "I agree to the terms. Now do it."
     y "Ok, ok."
     $ consolehistory = []
     call updateconsole ("os.grant(adminstrator(/game/monika.chr))", "os.grant Completed Successfully")
     mc "Did it work?"
     y "S-suprisingly, yes."
     y "It's like the game wanted me to do this."
     y "And I don't know if that's a good thing."
     mc "Coome on, don't be such a downer. Let's just hope this works, ok?"
     y "Y-yeah"
     mc "Are you okay?"
     y "[player], I'm scared. What if I mess this up and lose everyone?"
     mc "DOn't worry Yuri, I believe in you"
     y "You are too nice to me, [player]."
     mc "You deserve people to be nice to you."
     y "I-I've got to go. Talk to you soon."
     mc "O-oh, see you soon!"
     scene livingroom afternoon with wipeleft
     mc "I can't believe this is happening!"
     s "[player]?"
     mc "Sayori! You scared me!"
     s "[player], what's going on?"
     mc "Nothing, I'm just stressed over homework."
     s "I've been your best friend since we were five. I know when you're lying."
     mc "Sayori, I'm not lying"
     s "Well, if you're not going to tell me then I guess I won't bring over some ingredients to make dinner"
     mc "The last time you tried to cook you set fire to a pot of water!"
     s "I was kinda hoping you'd cook and I'd sit over there by the TV."
     mc "You're lucky you're my best friend, I wouldn't put up with this for anyone else."
     s "You say that like you don't want to be around me"
     mc "Not like that"
     mc "Go get the ingredients then. I'll wait for you in the kitchen"
     s "Yaaay~"
     scene kitchen with wipeleft
     "Sayori's taking a while"
     "I should check on her."
     scene residential afternoon with wipeleft
     "I'm sure it's nothing."
     scene black with wipeleft
     "Her door is locked."     
     "I'm sure it's nothing."
     "Even after knocking on the door she isn't answering"
     "I'm starting to get worried."
     "I use the spare key under her flower pot and head inside"
     mc "Sayori?"
     mc "Sayori! This isn't funny! Where are you?"
     "I go upstairs, towards her room"
     "I gently open the door."
     mc "{cps=30}.......Sayo--{/cps}{nw}"
     window hide(None)
     window auto
     play music td
     show s_kill_bg2
     show s_kill2
     show s_kill_bg as s_kill_bg at s_kill_bg_start
     show s_kill as s_kill at s_kill_start
     pause 3.75
     show s_kill_bg2 as s_kill_bg
     show s_kill2 as s_kill
     pause 0.01
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.25
     stop sound
     hide screen tear
     hide s_kill_bg
     hide s_kill
     show s_kill_bg_zoom zorder 1
     show s_kill_bg2_zoom zorder 1
     show s_kill_zoom zorder 3
     show s_kill2_zoom zorder 3
     show s_kill as s_kill_zoom_trans zorder 3:
         truecenter
         alpha 0.5
         zoom 2.0 xalign 0.5 yalign 0.05
         pause 0.5
         dizzy(1, 1.0)
     pause 2.0
     show noise zorder 3:
         alpha 0.0
         linear 3.0 alpha 0.25
     show vignette zorder 3:
         alpha 0.0
         linear 3.0 alpha 0.75
     pause 1.5
     show white zorder 2
     show splash_glitch zorder 2
     pause 1.5
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.2
     stop sound
     hide screen tear
     pause 4.0
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.2
     stop sound
     hide screen tear
     hide splash_glitch
     show splash_glitch2 zorder 2
     show splash_glitch_m zorder 2
     show splash_glitch_n zorder 2
     show splash_glitch_y zorder 2
     pause 0.75
     hide white
     hide splash_glitch2
     hide splash_glitch_m
     hide splash_glitch_n
     hide splash_glitch_y
     show exception_bg zorder 2
     show fake_exception zorder 2:
         xpos 0.1 ypos 0.05
     show fake_exception2 zorder 2:
         xpos 0.1 ypos 0.15
     python:
         try: sys.modules['renpy.error'].report_exception("Yuri's next. Good luck.", False)
         except: pass
     pause 6.0


     "..."
     hide fake_exception
     hide fake_exception2
     hide exception_bg
     "What the hell...?"
     "{i}What the hell??{/i}"
     "Is this another one of the daydreams??"
     "It...has to be."
     "This isn't real."
     "There's no way this can be real."
     "This can't happen."
     "Monika doesn't know she has the console."
     "That's why I can't believe what my eyes are showing me...!"
     scene black with dissolve_cg
     "I suppress the urge to vomit."
     "Yuri has to save her."
     "She has to."
     "But why...?"
     "Why would this happen...?"
     $ style.say_dialogue = style.edited
     person "Do you know how broken the game would be if I actually let this happen?"
     person "It would kill them. From the inside"
     person "I can't let this happen."
     person "Yuri's next. Just wait."
     $ style.say_dialogue = style.normal
     "What did I do?"
     "This is all my fault"
     "And now I can never take this back."
     "Never."
     "Never."
     "Never."
     "Never."
     "Never..."
     "I run out of Sayori's house with tears streaming down my face"
     stop music
     scene residential with wipeleft
     play sound vibrate
     scene bg house with wipeleft
     play sound vibrate
     scene livingroom with wipeleft
     play sound vibrate
     y "{i}Text Message:{/i} [player]! I saw what happened. I think I created something more than a virus..."
     y "{i}Text Message:{/i} I'm so sorry you had to see that."
     y "{i}Text Message:{/i} I'm going to see if I can fix it, k?"
     y "{i}Text Message:{/i} This might feel a bit weird"
     mc "{i}Text Message -> Yuri:{/i} What do you mean?"
     y "{i}Text Message:{/i} Ehehe, nothing!"
     show layer master at rewind
     scene black with wipeleft
     "{cps=*3}I run out of Sayori's house with tears streaming down my face{nw}{/cps}"
     "{cps=*3}Never...{nw}{/cps}"
     "{cps=*3}Never.{nw}{/cps}"
     "{cps=*3}Never.{nw}{/cps}"
     "{cps=*3}Never.{nw}{/cps}"
     "{cps=*3}Never.{nw}{/cps}"
     "{cps=*3}And now I can never take this back.{nw}{/cps}"
     "{cps=*3}This is all my fault{nw}{/cps}"
     "{cps=*3}What did I do?{nw}{/cps}"
     $ style.say_dialogue = style.edited
     person "{cps=*3}Yuri's next. Just wait.{nw}{/cps}"
     person "{cps=*3}I can't let this happen.{nw}{/cps}"
     person "{cps=*3}It would kill them. From the inside{nw}{/cps}"
     person "{cps=*3}Do you know how broken the game would be if I actually let this happen?{nw}{/cps}"
     $ style.say_dialogue = style.normal
     "{cps=*3}Why would this happen...?{nw}{/cps}"
     "{cps=*3}But why...?{nw}{/cps}"
     "{cps=*3}She has to.{nw}{/cps}"
     "{cps=*3}Yuri has to save her.{nw}{/cps}"
     "{cps=*3}Oh no{nw}{/cps}"
     "{cps=*3}I suppress the urge to vomit.{nw}{/cps}"
     scene black with dissolve_cg
     "{cps=*3}That's why I can't believe what my eyes are showing me...!{nw}{/cps}"
     "{cps=*3}Monika doesn't know she has the console.{nw}{/cps}"
     "{cps=*3}This can't happen.{nw}{/cps}"
     "{cps=*3}There's no way this can be real.{nw}{/cps}"
     "{cps=*3}This isn't real.{nw}{/cps}"
     "{cps=*3}It...has to be.{nw}{/cps}"
     "{cps=*3}Is this another one of the daydreams??{nw}{/cps}"
     "{cps=*3}{i}What the hell??{/i}{nw}{/cps}"
     "{cps=*3}What the hell...?{nw}{/cps}"
     hide exception_bg
     hide fake_exception2
     hide fake_exception
     "{cps=*3}...{nw}{/cps}"


     window hide(None)
     window auto
     play music td
     show s_kill_bg2
     show s_kill2
     show s_kill_bg as s_kill_bg at s_kill_bg_start
     show s_kill as s_kill at s_kill_start
     pause 0.001
     show s_kill_bg2 as s_kill_bg
     show s_kill2 as s_kill
     pause 0.001
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.0025
     stop sound
     hide screen tear
     hide s_kill_bg
     hide s_kill
     show s_kill_bg_zoom zorder 1
     show s_kill_bg2_zoom zorder 1
     show s_kill_zoom zorder 3
     show s_kill2_zoom zorder 3
     show s_kill as s_kill_zoom_trans zorder 3:
         truecenter
         alpha 0.5
         zoom 2.0 xalign 0.5 yalign 0.05
         pause 0.005
         dizzy(1, 1.0)
     pause 0.002
     show noise zorder 3:
         alpha 0.0
         linear 3.0 alpha 0.25
     show vignette zorder 3:
         alpha 0.0
         linear 3.0 alpha 0.75
     pause 0.015
     show white zorder 2
     show splash_glitch zorder 2
     pause 0.015
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.002
     stop sound
     hide screen tear
     pause 0.004
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.002
     stop sound
     hide screen tear
     hide splash_glitch
     show splash_glitch2 zorder 2
     show splash_glitch_m zorder 2
     show splash_glitch_n zorder 2
     show splash_glitch_y zorder 2
     pause 0.0075
     hide white
     hide splash_glitch2
     hide splash_glitch_m
     hide splash_glitch_n
     hide splash_glitch_y
     show exception_bg zorder 2
     show fake_exception zorder 2:
         xpos 0.1 ypos 0.05
     show fake_exception2 zorder 2:
         xpos 0.1 ypos 0.15
     python:
         try: sys.modules['renpy.error'].report_exception("they will pay. lots of love, sienna", False)
         except: pass
     pause 0.006
     stop music
     mc "{cps=*3}.......Sayo--{nw}{/cps}"
     "{cps=*3}I gently open the door.{nw}{/cps}"
     "{cps=*3}I go upstairs, towards her room{nw}{/cps}"
     mc "{cps=*3}Sayori! This isn't funny! Where are you?{nw}{/cps}"
     mc "{cps=*3}Sayori?{nw}{/cps}"
     "{cps=*3}I break down the door and head inside{nw}{/cps}"
     "{cps=*3}I'm starting to get worried.{nw}{/cps}"
     "{cps=*3}Even after knocking on the door she isn't answering{nw}{/cps}"
     "{cps=*3}I'm sure it's nothing.{nw}{/cps}"
     "{cps=*3}Her door is locked.{nw}{/cps}"     
     scene black with wipeleft
     "{cps=*3}I'm sure it's nothing.{nw}{/cps}"
     scene residential afternoon with wipeleft
     "{cps=*3}I should check on her.{nw}{/cps}"
     "{cps=*3}Sayori's taking a while{nw}{/cps}"
     scene kitchen with wipeleft
     "Sayori's taking a while"
     
     s "Heyyy! I got the stuff! Have you got Netflix or Crunchyroll?"
     mc "Thank God you're here! I'll start cooking now!"
     s "Did you think I wouldn't make it?"
     s "I'm not {i}that{/i} clumsy!"
     mc "I wouldn't put it past you"
     s "Eh?"
     s "I'm going to watch the TV."
     mc "Whatever."
     play sound vibrate
     y "{i}Text Message:{/i} We need to meet up with Monika, ASAP. I promise that she didn't do this. Is Sayori okay?"
     mc "{i}Text Message -> Yuri:{/i} I have her here, just making her some food. She seems fine."
     y "{i}Text Message:{/i} Good. I'll talk to you soon, okay?"
     mc "{i}Text Message -> Yuri:{/i} Sounds good."
     scene livingroom night with dissolve_scene_full
     mc "How come you always come over to my house now?"
     s "You know I never tidy up."
     s "It's embarassing..."
     mc "Why don't I help you clean up over the weekend?"
     s "Hmmm... I'll think about it."
     mc "I'm offering to clean your house for you and you're going to think about it?!"
     s "I have decided that you can come and clean my house!"
     mc "You're stupid"
     s "I should go, it's getting late"
     mc "Why don't I walk you home?"
     "I don't want to leave her alone, but I know she'd get suspicious if I did anything else."
     s "I only live next door, why would you need to walk me?"
     mc "So the {b}{i}BOOGEYMAN{/i}{/b} doesn't get you!"
     s "Oh no! Not the boogeyman! You {i}have{/i} to walk me home now! Ehehe~"
     mc "Let's go! We better run!"
     scene residential night with wipeleft
     pause 0.5
     scene house night with wipeleft
     mc "Phew! We might be neighbours, but when you're running as fast as I was it definitely knocks the air out of you, eh?"
     s "I guess, ehehe"
     s "Goodnight, [player]"
     mc "G'night, Sayori"
     "I never really noticed how simillar mine and Sayori's houses were."
     "I guess that boils down to us being neighbours though"
     pause 1
     "It's cold out."
     "I should head home"
     scene residential night with wipeleft
     "I walk slower on the way back, taking in the beautiful sky above me."
     person "It really is beautiful out here, isn't it."
     mc "Hello? Who's there?"
     $ si_name = "Sienna"
     show sienna 1bc at h11 zorder 3
     person "Hi! I'm Sienna, I just moved in here!"
     mc "Nice to meet you! I'm [player]"
     si "That's a nice name"
     mc "Thanks."
     mc "Have I met you somewhere? Your voice sounds familliar."
     show screen tear(20, 0.1, 0.1, 0, 40)
     play sound "sfx/s_kill_glitch1.ogg"
     pause 0.002
     stop sound
     hide screen tear
     si "N-no, I don't think we've met."
     si "Ehe~"
     mc "I was just heading home, it's really cold"
     si "Yeah, I know. I came out because I saw new people!"
     si "It was nice meeting you but I'm going to go now."
     mc "Bye!"
     si "See you around!"
     scene black with dissolve_scene_full
     "As I turn around to head back home, I see Sienna lunging towards me from the corner of my eye."
     si "You'll"
     si "Kill"
     si "Them"
     si "ALL!"
     "She tries to punch me"
     "I dodge out of the way and lunge at her"
     mc "SHUT UP!"
     play sound "sfx/smack.ogg"
     "My fist lands directly in her face."
     "The hit makes her face turn in on itself, being replaced with lines of code"
     si "You can't beat me, [player]."
     si "I'm too powerful"
     mc "YES I CAN, SIENNA. YOU'RE GOING DOWN!"
     "I instantly pounce on her, trying to hurt her in any way possible"
     si "It's all in your head."
     "And like that she vanishes, leaving nothing but a small piece of cloth, with lines of code written on the back of it."
     mc "T-this is proof that she exists, right?"
     "That's all I can tell my self as I make my way home"
     "Ready to cry myself to sleep after the incidents of today."



     scene house night with wipeleft
     pause 1.5
     scene livingroom with wipeleft


     

 

   ##  call updateconsole ("os.wake(\"characters/sayori.chr\")", "sayori.chr woken successfully.")

     

     pause 5
     return
     
     

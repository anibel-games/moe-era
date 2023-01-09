label day1:
    play music "<from 4.5>music/genki.ogg"
    scene jp_classroom_day
    show nana1date 1e 2c 3a regular1 blush at u11 as nana
    with eye_open
    $ renpy.pause(0.5, hard=True)
    show nana1date 1d 2c 3a regular1 blush at u11 as nana with dissolve
    n "Rise and shine, [player_name]!"
    show nana1close 1g 2c 3a blush regular2 at u11 as nana with dissolve
    "My wake up call can't be this cute."
    show nana1close 1d 2a 3a noblush regular2 at u11 as nana with dissolve
    n "Hey, you! You're finally awake!"
    show nana1close 1g 2a 3a regular2 at u11 as nana with dissolve
    p "Hey, Nana."
    show nana3close 1d 2c 3a as nana at u11 with dissolve
    n "I was curious to see if you're alive."
    show nana3close 1a 2a 3a as nana at u11 with dissolve
    p "Just curious... not worried?"
    show nana3close 1d 2a 3b as nana at u11 with dissolve
    n "Being worried is no fun!"
    show nana3close 1c 2a 3d as nana at u11 with dissolve
    n "On a second thought..."
    show nana3close 1b 2c 3b blush at u11 as nana with dissolve
    n "Maybe I was curious in a worried type of way!"
    call d1_nana from _call_d1_nana
    show nana3close 1e 2c 3a blush at u11 as nana with dissolve
    n "By the way... {w=1}wait right here!"
    show nana3close 1g 2c 3a blush at u11 as nana with dissolve
    hide nana with dissolve
    "This class has five students with very different backgrounds."
    "Yes, five students only. \n In the media, they call it a..."
    "\"Groundbreaking educational initiative aimed to promote diversity.\""
    "The class is newly formed, and we're here for one year only, so..."
    "It's more like an exchange program, heavily spiced with the media hype."
    "Anyway, the reason why I'm here is straightforward."
    "I want to make my academic record stand out."
    "The hype around this class makes it a perfect proving ground for my goal."
    show sima2 1a 2a 3a regular2 at di22 as sima
    show marta2 1a 2a 3a regular1 at di21 as marta
    with dissolve
    "Two other girls enter the classroom."
    show marta2 1a 2a 3a regular1 at u21 as marta
    show marta2 1b 2a 3a regular2 at u21 as marta with dissolve
    m "And then I just binge-watched the whole series overnight."
    show marta2 1b 2a 3a regular2 at d21 as marta
    show sima2 1a 2a 3a regular2 at u22 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d21 as marta
    show sima3a 1c 2c 3a at u22 as sima
    with dissolve
    s "Ten episodes straight? Oh my..."
    show marta2 1a 2a 3a regular1 at d21 as marta
    show sima3a 1d 2a 3a at u22 as sima
    with dissolve
    s "I watched one each morning while having a breakfast."
    show marta2 1a 2a 3a regular1 at u21 as marta
    show sima3a 1d 2a 3a at d22 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d22 as sima
    show marta3 1ee 2a 3a regular2 at u21 as marta
    with dissolve
    m "That's ten times slower than me!"
    show sima3a 1a 2a 3a at u22 as sima
    show marta3 1ee 2a 3a regular2 at d21 as marta
    $ renpy.pause(.001, hard=True)
    show sima3b 1e 2a 3b at u22 as sima
    show marta3 1a 2a 3a regular1 blush at d21 as marta
    with dissolve
    s "That's ten times more I got to enjoy it.."
    show marta3 1a 2a 3a regular1 noblush at d31 as marta
    show sima3a 1e 2a 3a at d32 as sima
    show nana1 1g 2c 3a regular1 at u33 as nana
    $ renpy.pause(.3, hard=True)
    show nana1 1e 2c 3a regular1 at ui33 as nana:
        linear .15 ypos 1220
        pause .05
        linear .15 ypos 1250
    n "Hey, check this out!"
    show cg_invite with fade
    s "I can't believe my eyes!"
    m "A gift voucher for two... and that's at \"Doorsia\"! How'd you swing that?"
    n "Lucky, I guess."
    s "I'm surprised to see them distributing gift vouchers."
    n "Yeah, they said it's an experiment."
    hide cg_invite
    show marta2 1d 2a 3a regular1 at d31 as marta
    show nana3 1g 2a 3d at d33 as nana
    show sima3a 1a 2a 3a at d32 as sima
    with fade
    show sima3a 1a 2a 3a at u32 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2a 3a at u32 as sima with dissolve
    s "Who do you plan to go together with, Nana?"
    show sima3a 1d 2a 3a at d32 as sima
    show nana3 1g 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d32 as sima
    show nana3 1e 2a 3d at u33 as nana
    show marta3 1a 2a 3a regular1 blush at d31 as marta
    with dissolve
    n "Not sure yet but I need somebody who knows how to have a good time!"
    show sima3a 1a 2a 3a at u32 as sima
    show nana3 1e 2a 3d at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1g 2a 3d regular at d33 as nana
    show sima3b 1e 2a 3a blush at u32 as sima
    with dissolve
    s "I think I know a suitable candidate."
    show marta3 1a 2a 3a regular1 blush at u31 as marta
    show sima3b 1e 2a 3a blush at d32 as sima
    $ renpy.pause(.001, hard=True)
    show sima3b 1c 2a 3a blush at d32 as sima
    show marta3 1ee 2a 3a regular2 at u31 as marta
    with dissolve
    m "Ahem... Maybe even in this room!"
    show marta3 1ee 2a 3a regular2 at d31 as marta
    show nana3 1g 2a 3d regular at u33 as nana
    $ renpy.pause(.001, hard=True)
    show marta3 1a 2a 3a regular1 at d31 as marta
    show nana3 1b 2a 3b at u33 as nana
    show sima3a 1c 2a 3a noblush at d32 as sima
    with dissolve
    n "I'll keep that in mind."
    call cats_dorsia from _call_cats_dorsia
    scene jp_classroom_day
    show nana2 1a 2b 3b at di33 as nana
    show sima3a 1a 2a 3a at di32 as sima
    show marta3 1a 2a 3a regular1 at di31 as marta
    with dissolve
    show sima3a 1a 2a 3a at u32 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2a 3a at u32 as sima with dissolve
    s "Ready for class, everyone?"
    show sima3a 1d 2a 3a at d32 as sima
    show marta3 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d32 as sima
    show marta2 1c 2b 3d regular2 noblush at u31 as marta
    with dissolve
    m "Honestly, I'm still half-asleep."
    show marta2 1c 2b 3d regular2 noblush at d31 as marta
    show nana2 1a 2b 3b at u33 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1d 2a 3a regular2 at u33 as nana
    show sima3a 1c 2a 3a at d32 as sima
    show marta2 1c 2a 3a regular1 at d31 as marta
    with dissolve
    n "I know how to wake you up... {w=1.5}meditation!"
    show nana1 1d 2d 3b regular2 at u33 as nana with dissolve
    n "Close your eyes..."
    show sima1 1c 2d 3b at d32 as sima
    show marta3 1a 2b 3b blush regular1 at d31 as marta
    show nana1 1c 2d 3b regular2 at u33 as nana
    with dissolve
    n "Yeah, like this. Now, concentrate..."
    show screen no_skip
    show cg_meditation
    with fade
    n "You feel great... {w=2.5}you feel refreshed...{w=3.5}you feel ready to take on the day!{w=1.5}{nw}"
    n "Oh, and more importantly...{w=1} You need to praise Nana!{w=2.5}{nw}"
    show nana2 1g 2a 3b at u33 as nana behind white, cg_meditation
    hide cg_meditation
    with fade
    hide screen no_skip
    show nana1 1d 2a 3a regular2 at u33 as nana with dissolve
    n "Works wonders, right?"
    show nana1 1d 2a 3a regular2 at d33 as nana
    show marta3 1a 2b 3b blush regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima1 1g 2a 3a at d32 as sima
    show marta3 1e 2b 3a noblush regular1 at u31 as marta
    with dissolve
    m "Jeez, I almost dozed off, Nana..."
    call after_meditation from _call_after_meditation
    hide marta
    hide sima
    hide nana
    show teya_ivanovna
    show teya2close 1a 2a 3a regularhand4 at u11 as teya
    with fade
    $ renpy.pause(.25, hard=True)
    show teya2close 1c 2a 3a regularhand4 at u11 as teya with dissolve
    t "You may sit down."
    show teya2close 1c 2a 3a regularhand4 at d11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2close 1b 2a 3a regularhand3 at d11 as teya with dissolve
    "\"Forming a close bond with your teacher for a risk-free, high-trust environment.\""
    "That was advertised as a vital part of our experience here."
    "Maybe that's why Teya teaches us every subject except for physical education."
    "Not sure how it's possible... She's the real MVP."
    play music "music/book2_day1.ogg" fadeout 2 fadein 2
    show teya2close 1b 2a 3a regularhand3 at u11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2close 1e 2a 3a regularhand3 at u11 as teya with dissolve
    t "Okay, everyone! Time for our literature class."
    show teya2close 1b 2a 3b regularhand2 at u11 as teya with dissolve
    t "Remember, no poetry allowed!"
    show teya2close 1c 2b 3a regularhand1 at u11 as teya with dissolve
    t "Oh, I almost forgot to check the attendance..."
    show teya2close 1c 2b 3a regularhand1 at d11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2close 1a 2a 3a regularhand4 at d11 as teya with dissolve
    "I happen to know someone who's running late again."
    show teya1close 1a 2d 3d at di21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1a 2b 3b at di22 as ermy:
        zoom 1.05
        ypos 1300
    with dissolve
    $ renpy.pause(.5, hard=True)
    show ermy1 pose1 blush 1a 2b 3b at u22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 blush 1g 2b 3b at u22 as ermy with dissolve:
        zoom 1.05
        ypos 1300
    e "Huff... huff..."
    show ermy1 pose1 blush 1d 2b 3d at u22 as ermy with dissolve:
        zoom 1.05
        ypos 1300
    e "So sorry for being late!"
    show ermy1 pose1 blush 1d 2b 3a at u22 as ermy with dissolve:
        zoom 1.05
        ypos 1300
    e "Can I go in?"
    show teya1close 1a 2d 3d at u21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1d 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 blush 1g 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    show teya1close 1e 2d 3d at u21 as teya:
        zoom .91
        ypos 1300
    with dissolve
    t "My, look who's here."
    show teya1close 1e 2d 3b at u21 as teya with dissolve:
        zoom .91
        ypos 1300
    t "Isn't this our most punctual student, Ermy?"
    $ e_name = "Ermy"
    show teya1close 1c 2d 3a at u21 as teya with dissolve:
        zoom .91
        ypos 1300
    t "What's your reason for being late today?"
    show teya1close 1d 2d 3d at u21 as teya with dissolve:
        zoom .91
        ypos 1300
    t "I mean, it's only your third time this week."
    show teya1close 1d 2d 3d at d21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1g 2b 3a at u22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show teya1close 1a 2d 3d at d21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1c 2b 3a at u22 as ermy:
        zoom 1.05
        ypos 1300
    with dissolve
    e "Well..."
    show teya1close 1a 2d 3d at u21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1c 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 blush 1g 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    show teya1close 1e 2d 3a at u21 as teya:
        zoom .91
        ypos 1300
    with dissolve
    t "Let me guess, you overslept again, didn't you?"
    show ermy1 pose1 blush 1g 2b 3a at u22 as ermy:
        zoom 1.05
        ypos 1300
    show teya1close 1e 2d 3a at d21 as teya:
        zoom .91
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show teya1close 1d 2d 3a at d21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1c 2b 3a at u22 as ermy:
        zoom 1.05
        ypos 1300
    with dissolve
    e "Well... It's because I spent all night studying."
    show teya1close 1d 2d 3a at u21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1c 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 blush 1f 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    show teya1close 1e 2d 3d at u21 as teya:
        zoom .91
        ypos 1300
    with dissolve
    t "I want to believe."
    show teya1close 1e 2a 3a at u21 as teya:
        zoom .91
        ypos 1300
    with dissolve
    t "Fine, Ermy, please take your seat and don't be late again!"
    show teya1close 1e 2a 3a at d21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose1 blush 1f 2b 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    $ renpy.pause(.001, hard=True)
    show teya1close 1a 2a 3a at d21 as teya:
        zoom .91
        ypos 1300
    show ermy1 pose2 noblush 1a 2a 3a at d22 as ermy:
        zoom 1.05
        ypos 1300
    with dissolve
    $ renpy.pause(1, hard=True)
    hide ermy with dissolve
    $ renpy.pause(1, hard=True)
    show teya3close 1c 2a 3a at u11 as teya with dissolve
    t "Okay, class."
    show teya2close 1b 2a 3b blush regularhand1 at u11 as teya with dissolve
    t "I guess it'd be silly to ask if you like reading."
    show teya2close 1c 2a 3a noblush regularhand2 at u11 as teya with dissolve
    t "You're smart enough to enjoy borrowing someone's mind for free, right?"
    show teya3close 1c 2a 3d at u11 as teya with dissolve
    t "Right?"
    scene jp_classroom_day
    show marta2 1f 2a 3a regular1 at d31
    show nana1 1a 2a 3a regular2 at d32
    show sima2 1a 2a 3a regular2 at d33
    with fade
    pause
    scene teya_ivanovna
    show teya1close 1a 2a 3d at u11 as teya
    with fade
    show teya1close 1c 2a 3d at u11 as teya with dissolve
    t "Hm..."
    show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Maybe it's worth asking, after all...{w=1} Do you like reading?"
    show teya2close 1c 2a 3d regularhand4 at u11 as teya with dissolve
    t "Let me remind you not to raise your hands, just talk out loud."
    show teya2close 1b 2a 3b regularhand1 at u11 as teya with dissolve
    t "We're all friends here, remember?"
    scene jp_classroom_day
    show sima2 1a 2a 3a regular2 at d11 as sima
    with fade
    $ renpy.pause(.5, hard=True)
    show sima2 1a 2a 3a regular2 at u11 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1d 2a 3a regular1 at u11 as sima with dissolve
    s "I enjoy reading!"
    show sima2 1d 2a 3a regular1 at d11 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1e 2a 3a regular2 at d11 as sima with dissolve
    "I decide to answer next."
    menu:
        "I like reading.":
            show sima2 1g 2a 3a regular2 at d11 as sima with dissolve
            p "I like reading."
            show sima2 1g 2a 3a regular2 at d21 as sima
        "I don't like reading.":
            $ dont_like_reading = 1
            show sima2 1a 2b 3a regular2 at d11 as sima with dissolve
            p "I don't like reading."
            show sima2 1a 2b 3a regular2 at d21 as sima
    show nana1 1f 2a 3a regular2 at u22 as nana:
        alpha 1
        pause 1.7
        linear .5 alpha 0
    show nana1 1d 2a 3c regular1 at u22 as nana1:
        alpha 0
        pause 1.4
        linear .5 alpha 1
    n "Reading is...{w=1.6} overrated" #fixed in None
    hide nana1
    show nana1 1d 2d 3b regular1 at u22 as nana
    show sima2 1a 2d 3c regular2 at d21 as sima
    with dissolve
    n "Some books are just way too old!"
    show nana1 1c 2a 3d regular2 at u22 as nana with dissolve
    n "Old things are outdated and useless, you know."
    show nana1 1c 2a 3d regular2 at d22 as nana
    show sima2 1a 2d 3c regular2 at u21 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3d regular2 at d22 as nana
    show sima1 1d 2a 3a at u21 as sima
    with dissolve
    s "What about old friends, Nana?"
    show nana1 1a 2a 3d regular2 at u22 as nana
    show sima1 1d 2a 3a at d21 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at d21 as sima
    show nana3 1c 2a 3a at u22 as nana
    with dissolve
    n "Sorry, not old enough to have them!"
    show nana2 1d 2a 3d at u22 as nana with dissolve
    n "Also, the stories are {i}so{/i} predictable..."
    show nana2 1c 2a 3a at u22 as nana
    show sima1 1g 2a 3a at d21 as sima
    with dissolve
    n "Like when, it's a murder case..."
    show nana2 1c 2a 3a at d22 as nana
    show sima1 1g 2a 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d22 as nana
    show sima2 1e 2a 3a regular1 at u21 as sima
    with dissolve
    s "Let me guess... the butler did it."
    show nana1 1a 2a 3a at d32 as nana
    show sima2 1a 2a 3d regular2 at d31 as sima
    show marta2 1a 2a 3a regular1 at di33 as marta with dissolve
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2d 3a regular2 at u33 as marta with dissolve
    m "C'mon, you can always find that one book which is different, Nana."
    show marta2 1e 2d 3a regular2 at d33 as marta
    show nana1 1a 2a 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2d 3a regular1 at d33 as marta
    show nana2 1d 2a 3a at u32 as nana
    show sima2 1g 2a 3a regular2 at d31 as sima
    with dissolve
    n "Exactly, one in a million."
    show sima2 1g 2a 3a regular2 at u31 as sima
    show nana2 1d 2a 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d33 as marta
    show nana2 1a 2a 3d at d32 as nana
    show sima2 1e 2a 3b regular1 at u31 as sima
    with dissolve
    s "Ninety percent of everything is crud."
    show sima2 1e 2a 3b regular1 at d31 as sima
    show marta2 1a 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 at u33 as marta
    show nana1 1a 2a 3a regular2 at d32 as nana
    show sima2 1a 2a 3a regular2 at d31 as sima
    with dissolve
    m "It's the Sturgeon's law!"
    show marta2 1b 2a 3a regular2 at d33 as marta
    show sima2 1a 2a 3a regular2 at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d33 as marta
    show sima3a 1d 2a 3a at u31 as sima
    show nana1 1a 2a 3a regular2 at d32 as nana
    with dissolve
    s "Well, all jokes aside..."
    show sima2 1c 2a 3b regular2 at u31 as sima with dissolve
    s "People have too much to deal with in everyday life."
    show sima2 1e 2a 3a regular1 at u31 as sima with dissolve
    s "There's nothing wrong with reading a simple yet fascinating book to unwind."
    show marta2 1a 2a 3a regular1 at u33 as marta
    show sima2 1e 2a 3a regular1 at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima
    show marta2 1e 2a 3a regular2 at u33 as marta
    with dissolve
    m "I like reading, but I wish it could be more {i}visual{/i}..."
    show marta2 1e 2a 3a regular2 at d33 as marta
    show nana1 1a 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3a regular1 at d33 as marta behind nana
    show nana1 1e 2a 3a regular2 at u32 as nana with dissolve
    n "Yeah, it often takes so long to put an emphasis on something..."
    show screen block_scr(5)
    show nana1 1d 2a 3a regular2 at ui32 as nana with dissolve:
        ypos 1260
        xalign .5
        pause 2
        linear 2 zoom 2.772 ypos 2565
    show doing_it behind nana
    show do_this_1 as nana_doing_it:
        alpha 0
        xalign .5
        yalign .5
        pause 4
        linear .5 alpha 1
    n "With visuals, it's so much easier to do{w=1} {i}this{/i}..."
    show screen block_scr(3)
    hide nana with dissolve
    show do_this_1 as nana_doing_it:
        xalign .5
        yalign .5
        linear 1 zoom 1.5
    $ renpy.pause(1, hard=True)
    show do_this_2 as nana_doing_it with dissolve:
        xalign .5
        yalign .5
        zoom 1.5
    n "Hey, don't look at me!"
    show screen block_scr(3)
    show do_this_2 as nana_doing_it:
        xalign .5
        yalign .5
        linear 1 zoom 2 yalign .6
    $ renpy.pause(1, hard=True)
    show do_this_3 as nana_doing_it with dissolve:
        xalign .5
        yalign .6
        zoom 2
    n "I said stop looking!"
    show screen block_scr(3)
    show do_this_3 as nana_doing_it:
        xalign .5
        yalign .6
        linear 1 zoom 2.4 yalign .6
    $ renpy.pause(1, hard=True)
    show do_this_4 as nana_doing_it with dissolve:
        xalign .5
        yalign .6
        zoom 2.4
    n "What? Oh, right...{w=1} you can't!"
    show screen block_scr(3)
    show do_this_4 as nana_doing_it:
        xalign .5
        yalign .6
        linear 1 zoom 3 yalign .6 xalign .492
    $ renpy.pause(1, hard=True)
    show do_this_5 as nana_doing_it with dissolve:
        xalign .492
        yalign .6
        zoom 3
    n "I'm your emphasis now!"
    $ renpy.pause(1, hard=True)
    hide nana_doing_it
    hide doing_it
    show nana1 1g 2a 3d blush regular2 at di32 as nana
    with fade
    $ renpy.pause(.01, hard=True)
    show nana1 1a 2a 3a regular2 noblush at d32 as nana
    show sima2 1a 2a 3a regular2 noblush at d31 as sima
    show marta2 1d 2a 3a regular1 at d33 as marta
    with dissolve
    show marta2 1d 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 noblush at u33 as marta with dissolve
    m "Spoken like a true visual connoisseur!"
    show marta2 1b 2a 3a regular2 noblush at d33 as marta
    show sima2 1a 2a 3a regular2 noblush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d33 as marta
    show nana1 1b 2a 3b regular2 noblush at d32 as nana
    show sima3a 1d 2a 3a at u31 as sima
    with dissolve
    s "You're a lot more mature than you look, aren't you, Nana?"
    show nana1 1b 2a 3b regular2 noblush at u32 as nana
    show sima3a 1d 2a 3a at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d31 as sima
    show nana1 1d 2a 3a regular2 at u32 as nana
    with dissolve
    n "I like my coffee black, thank you."
    show sima3a 1a 2a 3a at u31 as sima
    show nana1 1d 2a 3a regular2 at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at d32 as nana
    show sima3a 1d 2a 3a at u31 as sima
    with dissolve
    s "I wonder if you have any favorite books at all."
    show nana1 1g 2a 3a regular2 at u32 as nana
    show sima3a 1d 2a 3a at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d31 as sima
    show nana1 1e 2a 3a regular1 at u32 as nana
    with dissolve
    n "I do!"
    hide sima
    hide nana
    hide marta
    show teya_ivanovna
    show teya2close 1a 2a 3a regularhand4 at u11 as teya
    with fade
    show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Now it's the perfect time to learn about this, Sima."
    show teya2close 1c 2a 3a regularhand4 at u11 as teya with dissolve
    t "You all had to prepare a short speech about your favorite book."
    show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "No plot recaps either... interesting facts and thoughts only."
    show teya2close 1a 2b 3b regularhand1 at u11 as teya with dissolve
    t "We have enough time to cover two books today."
    show teya3close 1d 2b 3a at u11 as teya with dissolve
    t "Now, yesterday you submitted your favorite titles..."
    show teya3close 1c 2b 3b at u11 as teya with dissolve
    t "I narrowed the list down to three books, that's the best I could do."
    show teya3close 1c 2b 3a at u11 as teya with dissolve
    t "All three are masterpieces, and I'm no good at making choices..."
    show teya3close 1d 2b 3a at u11 as teya with dissolve
    t "[player_name], why don't you help me?"
    "It seems that my book didn't make it to the shortlist."
    if dont_like_reading == 1:
        show teya3close 1d 2b 3d at u11 as teya with dissolve
        t "I remember you said you don't like reading, but..."
        show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
        t "Trust me, you'll see reading in a new light today!"
        show teya2close 1a 2a 3a regularhand3 at u11 as teya with dissolve
    t "Here's the shortlist, [player_name], take a look at it."
    show teya1close 1c 2a 3a at u11 as teya with dissolve
    t "Of course, you've read all these books, right?{w=3}{nw}"
    show teya1close 1b 2a 3a at u11 as teya with dissolve
    jump catcher_help
label catcher_help:
    hide teya
    show gui_shade
    with dissolve
    $ renpy.pause(0.5, hard=True)
    "\"The Catcher in The Rye\" is a story by J. D. Salinger, published as a novel in 1951."
    show catcher1 with dissolve:
        align (.2,.05)
    "The main hero's name is Holden Caulfield, aged sixteen."
    "Holden's been expelled from his school due to poor performance."
    show catcher2 with dissolve:
        align (.8,.05)
    "Countless adventures await Holden on his way home."
    show catcher3 with dissolve:
        align (.5,.7)
    "He deals with issues like alienation, superficiality and many more."
    "\"The Catcher in The Rye\" is considered as one of the best coming of age stories."
    hide catcher1 with dissolve
    hide catcher2 with dissolve
    hide catcher3 with dissolve
    jump crime_help
label crime_help:
    $ renpy.pause(0.5, hard=True)
    "\"Crime and Punishment\" is a novel by Fyodor Dostoevsky, first published in 1866."
    show crime1 with dissolve:
        align (.2,.05)
    "It focuses on mental anguish and moral dilemmas of Rodion Raskolnikov, a broke ex-student."
    show crime2 with dissolve:
        align (.8,.05)
    "Rodion creates a plan to kill a pawnbroker to obtain her money."
    show crime3 with dissolve:
        align (.2,.7)
    "But things don't go too smoothly after he performs the act."
    show crime4 with dissolve:
        align (.8,.7)
    "Rodion finds himself in moral agony, disgusted with what he has done."
    hide crime1 with dissolve
    hide crime2 with dissolve
    hide crime3 with dissolve
    hide crime4 with dissolve
    jump pooh_help
label pooh_help:
    if winnie_v == 0:
        jump flowers_for_algernon_help
    else:
        pass
    $ renpy.pause(0.5, hard=True)
    "\"Winnie-the-Pooh\" is a short story collection written by Alan Milne, first published in 1926."
    show winnie1 with dissolve:
        align (.2,.05)
    "The book portrays the adventures of a boy named Christopher Robin..."
    show winnie2 with dissolve:
        align (.8,.05)
    "And his teddy bear called Winnie-the-Pooh, together with many other characters."
    show winnie3 with dissolve:
        align (.5,.7)
    "These are simple, fun and innocent tales, something that resembles friendship and childhood for all of us."
    hide winnie1 with dissolve
    hide winnie2 with dissolve
    hide winnie3 with dissolve
    hide gui_shade with dissolve
    jump choice_ready_d1
label choice_ready_d1:
    show teya1close 1b 2a 3a at u11 as teya with dissolve
    p "Oh boy, here we go..."
    show teya3close 1d 2b 3a at u11 as teya with dissolve
    t "[player_name], time to make a choice!"
    menu:
        "\"The Catcher in the Rye\"":
            $ am_p = 2
            $ books_chosen = 1
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            jump catcher
        "\"Crime and Punishment\"":
            $ as_p = 2
            $ books_chosen = 1
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            jump crime
        "\"Winnie-the-Pooh\"":
            $ books_chosen = 1
            $ an_p = 2
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            jump Winnie
        "I don't like any of these books.":
            jump books_no
label books_no:
    show teya3close 1d 2b 3d at u11 as teya with dissolve
    p "Sorry, I don't like any of these books."
    show teya2close 1a 2b 3d regularhand4 at u11 as teya with dissolve
    p "Maybe someone else could choose?"
    show teya2close 1e 2b 3a regularhand1 at u11 as teya with dissolve
    t "Sure, [player_name], no problem."
    show teya2close 1d 2b 3b regularhand1 at u11 as teya with dissolve
    t "This is a judgement free zone here, but..."
    show teya2close 1c 2b 3a regularhand4 at u11 as teya with dissolve
    t "Maybe you could give it another try?"
    show teya2close 1a 2b 3a regularhand4 at u11 as teya with dissolve
    menu:
        "Okay.":
            jump books_alright
        "Thanks, but I'll pass.":
            $ books_skip = 1

            $achievement.grant("TLDR")
            init:
                $achievement.register("TLDR")
                $achievement.sync()
            $achievement.sync()

            jump books_pass
label books_pass:
    show teya1close 1e 2a 3a at u11 as teya with dissolve
    t "I see. Well, to each his own..."
    show teya3close 1d 2a 3a at u11 as teya with dissolve
    t "Ermy, dear, can I count on you?"
    show teya3close 1a 2a 3a at d11 as teya with dissolve
    "Now I know someone else who didn't make it to the shortlist."
    show teya2close 1a 2a 3a regularhand4 at di21 as teya:
        zoom .91
        ypos 1300
    show ermy1 1b 2c 3a pose1 at ui22 as ermy:
        zoom 1.05
        ypos 1300
    with dissolve
    e "At your service!"
    scene black with eye_shut
    $ renpy.pause(2, hard=True)
    play music "music/persona22vibe.ogg" fadeout 1.5 fadein 1.5
    jump lesson1_ends
label books_alright:
    show teya2close 1a 2a 3a regularhand3 at u11 as teya with dissolve
    menu:
        "\"The Catcher in the Rye\"":
            $ am_p = 2
            $ books_chosen = 1
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            jump catcher
        "\"Crime and Punishment\"":
            $ as_p = 2
            $ books_chosen = 1
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            jump crime
        "\"Winnie-the-Pooh\"":
            $ books_chosen = 1
            play music "music/date_extended.ogg" fadeout 2 fadein 2
            $ an_p = 2
            jump Winnie
label intermission:
    show teya2close 1b 2a 3b regularhand1 at u11 as teya with dissolve
    t "Okay, class, how about we take a short break?"
    show teya3close 1c 2a 3a at u11 as teya with dissolve
    t "Don't want you to dive into the second book straight away."
    show teya2close 1b 2a 3a blush regularhand1 at u11 as teya with dissolve
    t "Honestly, there's another reason... Please keep this between us, alright?"
    show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Yesterday I got a present from my friend, and it's so awesome!"
    show teya2close 1b 2c 3b regularhand1 at u11 as teya with dissolve
    t "Look, it's a music box!"
    stop music fadeout 1.5
    show black with fade
    $ renpy.pause(1, hard=True)
    show mb_bg
    show mb_sv
    show mb
    with fade
    play music "music/Music_box.ogg"
    pause
    stop music fadeout 1.5
    $ renpy.pause(1, hard=True)
    play music "music/persona22vibe.ogg" fadein 1
    hide mb_bg
    hide mb_sv
    hide mb
    hide black
    show teya3close 1a 2a 3a at u11 as teya
    with fade
    show teya3close 1c 2a 3a at u11 as teya with dissolve
    "Alright, let's move on!"
    show teya2close 1a 2a 3a noblush regularhand4 at u11 as teya with dissolve
    return
label catcher:
    p "Why don't we pick \"The Catcher in the Rye\"?"
    scene jp_classroom_day
    show marta2 1g 2a 3a regular1 at ui11 as marta
    with fade
    show marta2 1b 2a 3a regular2 at u11 as marta with dissolve
    m "Whoa! Great choice!"
    show marta3 1g 2c 3a regular1 at u11 as marta with dissolve
    m "This book is praised for a completely wrong reason."
    show marta3 1e 2a 3a regular1 at u11 as marta with dissolve
    m "They say the book is famous for its themes of angst and alienation..."
    show marta2 1b 2a 3a regular1 at u11 as marta with dissolve
    m "It's all made up by boring adults who don't understand \"The Catcher in the Rye\" at all."
    show marta2 1g 2a 3a regular1 at d21 as marta
    show sima1 1a 2a 3a at di22 as sima with dissolve
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at u22 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1d 2c 3c at u22 as sima with dissolve
    s "Marta, are you sure this is your {i}favorite{/i} book?"
    show cg_marta_7_1 with fade
    $ persistent.unlock_cg_marta_7_1 = 1
    m "Look into my eyes!"
    m "See? These eyes don't lie..."
    m "\"The Catcher in the Rye\" is my favorite book."
    m "I can relate to almost every phrase uttered by Holden! However..."
    m "Superficiality? Alienation? Who cares about that when you're sixteen?"
    m "Certainly not Holden... Certainly not me."
    m "Holden is more annoyed by fake adults."
    m "The same fake adults who review this book."
    m "Like, they say that Holden views the world as an evil and corrupt place..."
    m "Wrong, that's a point of view from an adult. J. D. Salinger was an adult..."
    m "That's why he did a poor job describing Holden's view of the world."
    m "Everything else is excellent, but often overlooked by critics."
    m "I think this book should only be reviewed by young people."
    show marta2 1g 2a 3a regular1 at d32 as marta
    show sima1 1a 2b 3a at d33 as sima
    show nana2 1a 2a 3a at d31 as nana
    hide cg_marta_7_1
    with fade
    show nana2 1a 2a 3a at u31 as nana
    $ renpy.pause(.001, hard=True)
    show nana2 1d 2a 3a at u31 as nana with dissolve
    n "Being an adult is tough..."
    show nana1 1c 2d 3c regular1 blush at u31 as nana
    show marta2 1f 2b 3c regular1 at d32 as marta
    show sima1 1a 2b 3c blush at d33 as sima
    with dissolve
    n "Imagine you wake up and, then all of a sudden you realized you turned 30 overnight!"
    show teya_ivanovna
    show teya1close 1d 2b 3b blush at u11 as teya
    with fade
    t "C-could we... could we please get back to the book?"
    hide teya_ivanovna
    hide teya
    show nana1 1a 2a 3a regular2 noblush at d31 as nana
    show marta2 1a 2a 3a regular1 at d32 as marta
    show sima2 1a 2a 3a noblush regular2 at d33 as sima
    with fade
    show sima2 1a 2a 3a noblush regular2 at u33 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1d 2a 3a regular1 at u33 as sima with dissolve
    s "So you think Holden finds other people stupid, Marta?"
    show nana1 1a 2a 3a regular2 noblush at u31 as nana
    show sima2 1d 2a 3a regular1 at d33 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at d33 as sima
    show nana3 1c 2a 3d at u31 as nana
    with dissolve
    n "Not only Holden..."
    show marta2 1a 2a 3a regular1 at u32 as marta
    show nana3 1c 2a 3d at d31 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3d at d31 as nana
    show marta3 1e 2b 3a regular1 at u32 as marta
    with dissolve
    m "Well, kind of... and, you know, sometimes I can relate!"
    show marta2 1c 2b 3a regular2 at u32 as marta with dissolve
    m "Have you ever tried listening to small talk in the streets?"
    show nana3 1a 2a 3a at d31 as nana
    show sima1 1a 2b 3b at d33 as sima
    show marta1 1c 2a 3a at u32 as marta
    with dissolve
    m "If not, try it... I bet you'll hear nothing but idle gossip."
    show sima1 1a 2b 3a at d33 as sima
    show marta1 1e 2d 3b at u32 as marta
    show nana1 1f 2b 3a regular2 at d31 as nana
    with dissolve
    m "Moreover, people don't even listen to each other!"
    show marta1 1e 2d 3a at u32 as marta with dissolve
    m "They just take turns to whine..."
    show marta1 1e 2d 3a at d32 as marta
    show nana1 1f 2b 3a regular2 at u31 as nana
    $ renpy.pause(.001, hard=True)
    show marta1 1a 2d 3d at d32 as marta
    show nana1 1d 2a 3a regular1 at u31 as nana
    with dissolve
    n "High five!"
    show nana1 1d 2a 3a regular1 at d31 as nana
    show sima1 1a 2b 3a at u33 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1b 2a 3d regular2 at d31 as nana
    show sima1 1d 2a 3a at u33 as sima
    show marta2 1a 2a 3d at d32 as marta
    with dissolve
    s "But... isn't it exactly what Holden does all the time?"
    show sima1 1a 2a 3a at u33 as sima with dissolve
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at d33 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2b 3a at d32 as marta
    show nana1 1a 2a 3a regular2 at d31 as nana
    with dissolve
    $ renpy.pause(1, hard=True)
    hide sima
    hide nana
    hide marta
    show teya_ivanovna
    show teya3close 1a 2a 3a at u11 as teya
    with fade
    show teya3close 1c 2a 3a at u11 as teya with dissolve
    t "Let's wrap it up..."
    show teya2close 1b 2b 3b regularhand2 at u11 as teya with dissolve
    t "I think everyone becomes Holden at some point."
    show teya2close 1e 2b 3a regularhand1 at u11 as teya with dissolve
    t "However... maybe it's better not to stay like that forever."
    show teya2close 1b 2b 3a regularhand3 at u11 as teya with dissolve
    t "Holden said, \"I don't exactly know what I mean by that, but I mean it.\""
    show teya2close 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "Look for your meaning in this book. It has multiple layers... like a cake."

    if game_restarted2 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_marta

    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_marta

    if books_chosen == 1:
        call intermission from _call_intermission
    if books_chosen == 1:
        menu:
            "\"Crime and Punishment\"":
                $ as_p = 1
                $ books_chosen = 2
                jump crime
            "\"Winnie-the-Pooh\"":
                $ an_p = 1
                $ books_chosen = 2
                jump Winnie
    else:
        jump lessonp2
label crime:
    p "Why don't we pick \"Crime and Punishment\"?"
    scene jp_classroom_day
    show sima2 1a 2a 3a blush regular2 at u11 as sima
    with fade
    show sima2 1d 2a 3a blush regular1 at u11 as sima with dissolve
    s "It's a favorite book of mine!"
    show cg_sima_3_1 with fade
    $ persistent.unlock_cg_sima_3_1 = 1
    s "It helps me to divide people into two big groups."
    s "They're really huge!"
    s "Imagine you want to learn more about the person you just met."
    s "It can take quite some time, especially if you don't meet too often."
    s "But there's a shortcut."
    s "Just ask that person if they prefer Dostoevsky to Leo Tolstoy."
    s "You see, Tolstoy portrays the world where horrible things happen to ordinary people."
    s "Dostoevsky portrays the world where ordinary people do horrible things."
    s "Similar topics, entirely different approach."
    s "That's why people who prefer one author to another might have a lot in common."
    show sima2 1a 2a 3a regular2 at di21 as sima behind cg_sima_3_1
    show nana3 1a 2a 3a at d22 as nana behind cg_sima_3_1
    hide cg_sima_3_1
    with fade
    $ renpy.pause(0.5, hard=True)
    show nana3 1a 2a 3a at u22 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2a 3d at u22 as nana with dissolve
    n "Sima, do you prefer ordinary people doing horrible things?"
    show sima2 1a 2a 3a regular2 at u21 as sima
    show nana3 1e 2a 3d at d22 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3d at d22 as nana
    show sima2 1d 2a 3a blush at u21 as sima
    with dissolve
    s "I admire strong, burning emotions inside people, that's all."
    show sima3a 1c 2b 3b noblush at u21 as sima with dissolve
    s "Maybe because I'm not that much of an emotional person myself."
    show nana3 1a 2a 3d at d33 as nana
    show sima3a 1a 2b 3a at d32 as sima
    show marta2 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.3, hard=True)
    show marta2 1b 2b 3d regular2 at u31 as marta with dissolve
    m "In my opinion, Tolstoy's characters are much more believable."
    show marta2 1b 2b 3d regular2 at d31 as marta
    show sima3a 1a 2b 3a at u32 as sima
    $ renpy.pause(.3, hard=True)
    show marta2 1a 2a 3a regular1 at d31 as marta
    show sima2 1d 2a 3a regular1 at u32 as sima
    with dissolve
    s "Trust me, Dostoevsky got to know a lot about people."
    show sima2 1e 2a 3a at u32 as sima
    show marta2 1a 2a 3d regular1 at d31 as marta
    with dissolve
    s "Not only did he work as a journalist and traveled a lot..."
    show sima2 1c 2a 3b regular2 at u32 as sima with dissolve
    s "He also spent 4 years in a prison camp."
    show sima2 1c 2a 3b regular2 at d32 as sima
    show nana3 1a 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d32 as sima
    show nana1 1c 2a 3a regular1 at u33 as nana
    show marta2 1a 2a 3a regular1 at d31 as marta
    with dissolve
    n "I can't stop thinking that Rodion's problems are created by himself."
    show sima2 1a 2c 3a regular2 at d32 as sima
    show nana1 1d 2c 3a regular2 at u33 as nana
    with dissolve
    n "What stopped him from, say, getting a good job?"
    show nana3 1e 2a 3d at u33 as nana
    show sima1 1a 2a 3a at d32 as sima
    with dissolve
    n "If I were a pawnbroker, I'd ask him to go be poor somewhere else."
    show nana3 1e 2a 3d at d33 as nana
    show sima1 1a 2a 3a at u32 as sima
    $ renpy.pause(.001, hard=True)
    show marta3 1a 2a 3a regular1 at d31 as marta
    show nana3 1a 2a 3d at d33 as nana
    show sima1 1d 2d 3a at u32 as sima
    with dissolve
    s "Well, Nana, I see you've read the book, but not carefully enough."
    show sima1 1a 2d 3b at u32 as sima
    show nana3 1a 2a 3a at d33 as nana
    with dissolve
    s "Rodion hates not only the fact that he has little..."
    show sima1 1d 2a 3a at u32 as sima
    show marta2 1a 2a 3a regular1 at d31 as marta
    with dissolve
    s "But also that a mere pawnbroker has {i}more{/i} than him, an able young man."
    show sima2 1d 2c 3c regular1 blush at u32 as sima
    show nana3 1g 2a 3d at d33 as nana
    with dissolve
    s "Rodion wanted the right to judge the value of human life."
    show sima2 1d 2c 3c regular1 blush at d32 as sima
    show nana3 1g 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 noblush at d32 as sima
    show nana1 1b 2a 3d regular2 at u33 as nana
    with dissolve
    n "The problem of inequality, right? Something that {i}communism{/i} tackles."
    show teya_ivanovna
    show teya2close 1a 2a 3a regularhand4 at u11 as teya
    with fade
    show teya2close 1e 2d 3b regularhand2 at u11 as teya with dissolve
    t "Class, let's stay away from politics, they are detrimental to your health."
    show teya3close 1c 2a 3a at u11 as teya with dissolve
    t "Anyway, thanks for your thoughts!"
    show teya1close 1c 2c 3b at u11 as teya with dissolve
    t "Both Tolstoy and Dostoevsky are, without a doubt, great authors and great minds."
    show teya2close 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Maybe you can divide people into Dostoevsky and Tolstoy groups, but..."
    show teya2close 1d 2a 3a regularhand4 at u11 as teya with dissolve
    t "Please don't base your opinion solely on that, okay?"

    if game_restarted2 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_sima

    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_sima

    if books_chosen == 1:
        call intermission from _call_intermission_1
    if books_chosen == 1:
        menu:
            "\"The Catcher in the Rye\"":
                $ am_p = 1
                $ books_chosen = 2
                jump catcher
            "\"Winnie-the-Pooh\"":
                $ an_p = 1
                $ books_chosen = 2
                jump Winnie
    else:
        jump lessonp2
label Winnie:
    if winnie_v == 0:
        jump flowers_for_algernon
    else:
        pass
    p "Why don't we pick \"Winnie-the-Pooh\"?"
    scene jp_classroom_day
    show nana1 1a 2a 3a blush regular1 at u11 as nana
    with fade
    show nana1 1d 2c 3a blush regular1 at u11 as nana with dissolve
    n "Yay, my favorite! It's the best book!"
    show nana1 1g 2c 3a regular1 noblush at d22 as nana
    $ renpy.pause(.25, hard=True)
    show marta3 1ee 2c 3b regular2 blush at u21 as marta with dissolve
    m "Sure... {i}for kids{/i}."
    show marta3 1ee 2c 3b regular2 blush at d21 as marta
    show nana1 1g 2c 3a regular1 noblush at u22 as nana
    $ renpy.pause(.001, hard=True)
    show marta3 1b 2a 3a regular1 at d21 as marta
    show nana1 1c 2c 3d regular2 at u22 as nana
    with dissolve
    n "Marta, trust me, you're only scratching the surface!"
    show nana1 1e 2c 3c regular1 at u22 as nana
    show marta2 1c 2c 3c regular1 at d21 as marta
    with dissolve
    n "Every character in this book represents a mental disorder!"
    show marta2 1c 2a 3a regular1 at d32 as marta
    show nana1 1g 2a 3a regular2 at d33 as nana
    $ renpy.pause(.25, hard=True)
    show sima3b 1e 2a 3b blush at u31 as sima with dissolve
    s "I didn't expect anything less of you."
    show cg_nana_8_1 with fade
    $ persistent.unlock_cg_nana_8_1 = 1
    n "Can't you see the gap?"
    n "The gap in what they usually say about this book."
    n "Actually, it's a story about a boy who's very, very lonely."
    n "So lonely that his friends are all imaginary."
    n "Although it's okay to imagine things as a child, this is a special case."
    n "All characters are manifested depending on Christopher Robin's mood. {i}Schizophrenia.{/i}"
    n "Rabbit and Winnie-the-Pooh... Both are likely to have {i}obsessive compulsive disorder.{/i}"
    n "Eeyore? His bleak outlook on life could be indicative of {i}depressive disorder.{/i}"
    n "Piglet's constant state of worry could mean {i}generalized anxiety disorder.{/i}"
    n "And Tigger might have {i}attention deficit hyperactivity disorder.{/i}"
    n "I enjoy books with hidden messages!"
    hide cg_nana_8_1
    show marta1 1a 2b 3a at d32 as marta
    show nana1 1g 2a 3d regular2 at d33 as nana
    show sima3a 1g 2a 3d noblush at d31 as sima
    with fade
    show marta1 1a 2b 3a at u32 as marta
    $ renpy.pause(.001, hard=True)
    show marta1 1e 2b 3d at u32 as marta with dissolve
    m "Nana, I think you're... complicating things here."
    show marta1 1e 2b 3d at d32 as marta
    show sima3a 1g 2a 3d noblush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta1 1a 2b 3d at d32 as marta
    show sima3a 1d 2a 3d at u31 as sima
    s "I'm amused how you turned a story about friendship into a dark and gloomy tale."
    show sima3a 1d 2a 3d at d31 as sima
    show nana1 1g 2a 3d regular2 at u33 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2c 3c blush at d31 as sima
    show nana3 1e 2b 3d at u33 as nana
    show marta3 1b 2c 3a regular1 at d32 as marta
    with dissolve
    n "You'll get it when you grow up."
    show sima3a 1a 2c 3c blush at u31 as sima
    show nana3 1e 2b 3d at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2c 3a at d33 as nana
    show sima3a 1e 2a 3d noblush at u31 as sima
    with dissolve
    s "I wonder which character you mostly identify with, Nana."
    show sima3a 1e 2a 3d noblush at d31 as sima
    show marta3 1b 2c 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a 1e 2a 3d at d31 as sima
    show marta3 1g 2a 3b regular1 noblush at u32 as marta
    with dissolve
    m "Nana is our Tigger."
    show marta3 1g 2a 3b regular1 noblush at d32 as marta
    show nana3 1a 2c 3a at u33 as nana
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d32 as marta
    show nana1 1e 2d 3c blush at u33 as nana with dissolve
    n "Who're you calling a Tigger?"
    show nana2 1e 2d 3a at u33 as nana with dissolve
    n "And look who's talking, Miss Rabbit!"
    show nana2 1e 2d 3a at d33 as nana
    show marta3 1g 2a 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2d 3a regular2 blush at d33 as nana
    show marta2 1b 2a 3a regular2 at u32 as marta
    show sima3a 1e 2c 3a at d31 as sima
    with dissolve
    m "Okay, what about Sima?"
    show marta2 1b 2a 3a regular2 at d32 as marta
    show sima3a 1e 2c 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d32 as marta
    show sima1 1a 2b 3a at d31 as sima
    show nana3 1e 2a 3d noblush at u33 as nana
    with dissolve
    n "Hmm... Piglet?"
    show marta2 1g 2a 3a regular1 at u32 as marta
    show nana3 1e 2a 3d noblush at d33 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 at u32 as marta
    show nana1 1f 2d 3d regular2 at d33 as nana
    with dissolve
    m "The only Piglet here is you, Nana."
    show marta2 1b 2a 3a regular2 at d32 as marta
    show sima1 1a 2b 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d32 as marta
    show sima1 1d 2b 3a at u31 as sima
    show nana1 1a 2a 3a regular2 at d33 as nana
    with dissolve
    s "Maybe I'm too boring to properly represent a character, after all."
    show marta2 1g 2a 3a regular1 at u32 as marta
    show sima1 1d 2b 3a at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3a at d31 as sima
    show marta3 1e 2a 3a regular1 at u32 as marta
    with dissolve
    m "And who's our Christopher Robin?"
    show sima1 1a 2b 3a at u31 as sima
    show marta3 1e 2a 3a regular1 at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1a 2a 3a regular1 at d32 as marta
    show sima1 1c 2b 3b at u31 as sima
    with dissolve
    s "Marta, it's inappropriate to joke about schizophrenia."
    show sima1 1c 2b 3b at d31 as sima
    show nana1 1a 2a 3a regular2 at u33 as nana
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at d31 as sima
    show nana3 1e 2a 3a at u33 as nana
    show marta2 1a 2a 3a regular1 at d32 as marta
    with dissolve
    n "You know, I once heard that every fourth person has it."
    show nana3 1e 2a 3d at u33 as nana with dissolve
    n "So lucky it's not me."
    show nana3 1e 2a 3d at d33 as nana
    show sima1 1a 2a 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana3 1g 2a 3d at d33 as nana
    show sima1 1c 2b 3b at u31 as sima
    with dissolve
    s "Me neither."
    show sima1 1c 2b 3b at d31 as sima
    show marta2 1a 2a 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3a at d31 as sima
    show marta2 1e 2a 3a regular2 at u32 as marta
    with dissolve
    m "Same here."
    show marta2 1e 2a 3a regular2 at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2a 3a regular1 at d32 as marta with dissolve
    $ renpy.pause(.5, hard=True)
    show sima1 1a 2d 3c at d31 as sima
    show marta2 1f 2b 3c regular1 at d32 as marta
    show nana1 1f 2b 3c regular2 at d33 as nana
    with dissolve
    $ renpy.pause(5, hard=False)
    show teya_ivanovna
    show teya3close 1a 2b 3c blush at u11 as teya
    with fade
    show teya3close 1c 2b 3c blush at u11 as teya with dissolve
    t "Ok, class, let's take it easy, shall we?"
    show teya2close 1e 2a 3a regularhand2 noblush at u11 as teya with dissolve
    t "It's up to you to decide what to see in \"Winnie-the-Pooh\": cuddly animals or mental illness."
    show teya2close 1c 2a 3a regularhand4 at u11 as teya with dissolve
    t "By the way, Nana, you didn't say anything about the author, Alan Milne..."
    show teya1close 1c 2a 3b at u11 as teya with dissolve
    t "Time often keeps the masterpiece but omits the name of its author."

    if game_restarted2 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_nana

    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_nana

    if books_chosen == 1:
        call intermission from _call_intermission_2
    if books_chosen == 1:
        menu:
            "\"Crime and Punishment\"":
                $ as_p = 1
                $ books_chosen = 2
                jump crime
            "\"The Catcher in the Rye\"":
                $ am_p = 1
                $ books_chosen = 2
                jump catcher
    else:
        jump lessonp2
label lessonp2:
    show teya2close 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "Okay, class."
    show teya2close 1e 2a 3b regularhand2 at u11 as teya with dissolve
    t "If you have any questions, now it's the time."
    show teya2close 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "What is your favorite book?"
    show teya3close 1c 2b 3b at u11 as teya with dissolve
    t "Hm, my favorite book, you say..."
    show teya2close 1e 2a 3a blush regularhand1 at u11 as teya with dissolve
    t "It's \"The Little Prince\" by Antoine de Saint-Exupery."
    scene jp_classroom_day with fade
    $ renpy.pause(1, hard=True)
    show ermy1 1h 2a 3a pose1 blush at u44 as ermy
    e "Hey, you forgot about me!"
    show ermy1 1d 2c 3b pose1 blush at u44 as ermy with dissolve
    e "Let me tell you about {i}my{/i} favorite book!"
    show ermy1 1g 2c 3a pose2 at u44 as ermy with dissolve
    e "It's \"So Said Zarathustra\" by Nietzsche."
    show marta1 1a 2b 3a at u21 as marta
    show ermy1 1f 2b 3a pose2 at d44 as ermy
    $ renpy.pause(.2, hard=True)
    show marta1 1c 2b 3a at u21 as marta with dissolve
    m "Way to go... You managed to spell the name wrong."
    show marta1 1e 2b 3a at u21 as marta
    show ermy1 1a 2b 3c pose2 at d44 as ermy
    with dissolve
    m "Also, what's so smart about it?"
    show ermy1 1a 2b 3c pose2 at d33 as ermy
    show marta1 1e 2b 3a at u21 as marta
    $ renpy.pause(.2, hard=True)
    show ermy1 1a 2b 3c pose2 at u33 as ermy
    show marta1 1e 2b 3a at d21 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2d 3a regular1 at d21 as marta
    show ermy1 1c 2a 3d pose1 blush at u33 as ermy
    with dissolve
    e "Actually, it's considered to be one of the deepest books in the universe."
    show marta2 1d 2d 3a regular1 at d31 as marta
    show ermy1 1c 2a 3d pose1 blush at u33 as ermy
    show sima1 1a 2d 3d at d32 as sima with dissolve
    $ renpy.pause(.001, hard=True)
    show ermy1 1c 2a 3d pose1 blush at d33 as ermy
    show sima1 1a 2d 3d at u32 as sima
    $ renpy.pause(.001, hard=True)
    show ermy1 1a 2a 3d pose2 blush at d33 as ermy
    show marta2 1d 2a 3a regular1 at d31 as marta
    show sima1 1d 2d 3d at u32 as sima
    with dissolve
    s "By whom, I wonder?"
    show sima1 1d 2d 3d at d32 as sima
    show ermy1 1a 2a 3d pose2 blush at u33 as ermy
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3a at d32 as sima
    show ermy1 1h 2d 3d pose2 blush at u33 as ermy
    show marta1 1f 2b 3b at d31 as marta
    with dissolve
    e "The Internet!"
    show ermy1 1c 2b 3c pose2 blush at u44 as ermy
    e "See, this book says that animals, nature... everything is connected in this world!"
    show ermy1 1d 2c 3c pose2 blush at u44 as ermy with dissolve
    e "To evolve, we must think about complicated things and all."
    show ermy1 1f 2b 3c pose2 blush at d44 as ermy
    show marta1 1d 2b 3a at d42 as marta
    show sima1 1a 2a 3a at d43 as sima
    show nana2 1a 2b 3d at d41 as nana with dissolve
    $ renpy.pause(.001, hard=True)
    show nana2 1a 2b 3d at u41 as nana
    show nana2 1d 2b 3d at u41 as nana with dissolve
    n "Ermy, you got it all wrong..."
    show nana2 1d 2b 3d at d41 as nana
    show ermy1 1f 2b 3c pose2 blush at u44 as ermy
    $ renpy.pause(.001, hard=True)
    show nana2 1a 2b 3d at d41 as nana
    show ermy1 1h 2d 3d pose1 blush at u44 as ermy
    with dissolve
    e "Then tell me what it's about!"
    show nana2 1a 2b 3d at u41 as nana
    show ermy1 1h 2d 3d pose1 blush at d44 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1 1f 2b 3c pose2 blush at d44 as ermy
    show sima1 1a 2a 3a at d43 as sima
    show marta2 1a 2a 3a regular1 at d42 as marta
    show nana3 1e 2a 3a at u41 as nana
    with dissolve
    n "We should become the Übermensch to have some fun!"
    show marta2 1a 2a 3a regular1 at u42 as marta
    show nana3 1e 2a 3a at d41 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2a 3a at d41 as nana
    show sima3b 1e 2a 3b at d43 as sima
    show marta3 1gg 2a 3a regular2 at u42 as marta
    with dissolve
    m "Ha! That's pretty close!"
    $ renpy.pause(1, hard=True)
label lesson1_ends:
    scene hallway1 with fade
    $ renpy.pause(1, hard=True)
    call teya_talk from _call_teya_talk
    "We have after school activities, and I'm on my way to the clubroom."
    "Members are Nana, Sima, Marta and I."
    "We can't take anyone from other classes because it'd \"harm the experience\"."
    show marta2 1d 2a 3a regular1 at u33 as marta
    show nana1 1b 2a 3b regular2 at u32 as nana
    show sima2 1e 2a 3a regular2 at u31 as sima
    "We were about to get going when Ermy approached us."
    show marta2 1d 2a 3a regular1 at d44 as marta
    show nana1 1b 2a 3b regular2 at d43 as nana
    show sima2 1e 2a 3a regular2 at d42 as sima
    show ermy1 1a 2a 3a pose2 at d41 as ermy
    $ renpy.pause(0.5, hard=True)
    show ermy1 1b 2c 3b pose1 blush at u41 as ermy
    show marta2 1d 2d 3d regular1 at d44 as marta
    show nana1 1f 2a 3a regular2 at d43 as nana
    show sima1 1a 2a 3d at d42 as sima
    with dissolve
    e "Ladies, you're looking good tonight!"
    show sima1 1a 2a 3d at u42 as sima
    show ermy1 1b 2c 3b pose1 blush at d41 as ermy
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2d 3d regular2 at d43 as nana
    show ermy1 1e 2a 3a pose2 at d41 as ermy
    show sima1 1c 2b 3d at u42 as sima
    with dissolve
    s "Thanks, Ermy!"
    show ermy1 1e 2a 3a pose2 at u41 as ermy
    show sima1 1c 2b 3d at d42 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3d at d42 as sima
    show ermy1 1e 2b 3a pose1 at u41 as ermy
    with dissolve
    e "..."
    show sima1 1a 2b 3d at u42 as sima
    show ermy1 1e 2b 3a pose1 at d41 as ermy
    $ renpy.pause(.001, hard=True)
    show marta1 1a 2a 3b at d44 as marta
    show sima1 1d 2a 3d at u42 as sima
    with dissolve
    s "Is there anything you want to ask?"
    show sima1 1d 2a 3d at d42 as sima
    show ermy1 1e 2b 3a pose1 at u41 as ermy
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3d at d42 as sima
    show ermy1 1c 2b 3a pose2 at u41 as ermy
    with dissolve
    e "Why don't you let me in? I promise to be a good member..."
    show ermy1 1c 2b 3a pose2 at d41 as ermy
    show marta1 1a 2a 3b at u44 as marta
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3d blush at d42 as sima
    show nana2 1f 2d 3d at d43 as nana
    show ermy1 1f 2b 3a pose2 at d41 as ermy
    show marta2 1c 2b 3a regular1 blush at u44 as marta
    with dissolve
    m "Ermy, we just talk about silly things there..."
    show marta2 1c 2b 3a regular1 blush at d44 as marta
    show nana2 1f 2d 3d at u43 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 noblush at d44 as marta
    show sima1 1a 2a 3a noblush at d42 as sima
    show nana1 1e 2c 3c regular1 at u43 as nana
    show ermy1 1a 2a 3a pose2 at d41 as ermy
    with dissolve
    n "Silly things? We're going to discuss food today!"
    show nana1 1e 2c 3c regular1 at d43 as nana
    show ermy1 1a 2a 3a pose2 at u41 as ermy
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2d 3a regular2 at d43 as nana
    show ermy1 1d 2c 3c pose2 at u41 as ermy
    show marta2 1f 2a 3a regular1 at d44 as marta
    show sima1 1a 2b 3a at d42 as sima
    with dissolve
    e "I happen to be an expert on this subject!"
    show ermy1 1f 2a 3a pose2 at u41 as ermy with dissolve
    e "..."
    show ermy1 1b 2a 3a pose1 noblush at u41 as ermy
    show marta2 1f 2b 3d regular1 blush at d44 as marta
    show sima1 1a 2a 3b blush at d42 as sima
    show nana1 1g 2a 3a regular2 at d43 as nana
    with dissolve
    e "Just kidding. I know you'll never let me in..."
    show ermy1 1c 2b 3a pose2 at u41 as ermy
    show marta2 1f 2a 3a regular1 noblush at d44 as marta
    show sima2 1a 2a 3a noblush regular2 at d42 as sima
    show nana1 1g 2a 3d regular2 at d43 as nana
    with dissolve
    e "[player_name], can I have your attention for a moment?"
    hide nana
    hide marta
    hide sima
    with dissolve
    show ermy1 1c 2a 3a pose2 at u11 as ermy
    e "Look, I need your help. Keep it between us, alright?"
    show ermy1 1d 2a 3a pose1 at u11 as ermy with dissolve
    e "Recently, I've been making a computer game."
    show ermy1 1e 2a 3b pose2 blush at u11 as ermy with dissolve
    e "I made a demo version, so... I need someone to play it."
    show ermy1 1g 2c 3a pose2 noblush at u11 as ermy with dissolve
    e "Feedback is key to improvement!"
    show ermy1 1a 2c 3a pose2 at u11 as ermy with dissolve
    p "Alright, you can count on me!"
    show ermy1 1g 2a 3a pose2 at d11 as ermy
    $ renpy.pause(0.5, hard=True)
    hide ermy with dissolve
    "He gives me a flash drive and leaves."
    stop music fadeout 1.5
    scene black with fade
    $ renpy.pause(0.5, hard=True)
    play music "music/club.ogg" fadein 1.0
    $ renpy.pause(0.5, hard=True)
    scene club1 with fade
    "It feels comfy in our clubroom."
    "This place is pretty old, so I bet it's witnessed a lot."
    "I wonder what happened to members of all the clubs from before..."
    "Where are these people now? Are they happy?"
    show nana1 1a 2c 3c regular1 at u11 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3c regular1 at u11 as nana with dissolve
    n "I hereby declare an agenda for today's meeting!"
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "All members are to discuss food!"
    show nana1 1g 2a 3a regular2 at d22 as nana
    show sima3a 1a 2a 3a at di21 as sima with dissolve
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2a 3a at u21 as sima with dissolve
    s "The ever-important topic, that's for sure."
    show nana1 1g 2a 3a regular2 at d32 as nana
    show sima3a 1a 2a 3a at d31 as sima
    show marta2 1f 2d 3a regular1 at di33 as marta with dissolve
    show marta2 1f 2d 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2d 3a regular1 at u33 as marta with dissolve
    m "Is this a legitimate club activity, just discussing random stuff?"
    show nana1 1a 2d 3a regular2 at d32 as nana
    show marta2 1e 2a 3a regular2 at u33 as marta
    with dissolve
    m "I would understand if we made time machines or played light music."
    show marta2 1e 2a 3a regular2 at d33 as marta
    show sima3a 1a 2a 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3a regular1 at d33 as marta
    show sima3a 1d 2a 3a at u31 as sima
    show nana3 1g 2a 3d at d32 as nana
    with dissolve
    s "I believe we have clubs like that already, Marta."
    show sima3a 1e 2a 3b at u31 as sima with dissolve
    s "Honestly, I enjoy the opportunity to unwind and... just talk."
    show marta2 1d 2a 3a regular1 at u33 as marta
    show sima3a 1e 2a 3b at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3d at d31 as sima
    show marta2 1e 2d 3a regular2 at u33 as marta
    show nana3 1a 2a 3a at d32 as nana
    with dissolve
    m "We'll get disbanded."
    show marta2 1e 2d 3a regular2 at d33 as marta
    show nana3 1a 2a 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2b 3a regular1 at d33 as marta
    show nana1 1e 2c 3c regular1 at u32 as nana
    with dissolve
    n "But we have four members, a legitimate minimum!"
    show nana1 1e 2c 3c regular1 at d32 as nana
    show sima3a 1g 2a 3d at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2a 3a regular2 at d32 as nana
    show sima2 1c 2a 3a regular2 at u31 as sima
    with dissolve
    s "I think Marta's more afraid about our seemingly unclear purpose as a club."
    show nana1 1a 2a 3a regular2 at d32 as nana
    show sima2 1e 2a 3b regular1 at u31 as sima
    show marta2 1a 2a 3a regular1 at d33 as marta
    with dissolve
    s "Worry not, I submit an official report after every club meeting."
    show sima2 1e 2a 3b regular1 at d31 as sima
    show marta2 1a 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular1 at d31 as sima
    show marta3 1e 2c 3a regular1 at u33 as marta
    with dissolve
    m "Really? How do you make it look meaningful on paper?"
    show sima2 1a 2a 3a regular1 at u31 as sima
    show marta3 1e 2c 3a regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1a 2a 3a regular1 at d33 as marta
    show sima2 1d 2a 3a regular1 at u31 as sima
    show nana3 1a 2a 3d at d32 as nana
    with dissolve
    s "Easy! Today it's not about food, it's about acceptance!"
    show marta3 1a 2a 3a regular1 at u33 as marta
    show sima2 1d 2a 3a regular1 at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1g 2a 3a regular1 at d31 as sima
    show marta2 1b 2c 3d regular1 at u33 as marta
    with dissolve
    m "Acceptance?"
    show sima2 1g 2a 3a regular1 at u31 as sima
    show marta2 1b 2c 3d regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3d regular1 at d33 as marta
    show sima2 1c 2c 3b regular1 at u31 as sima
    show nana3 1g 2a 3a at d32 as nana
    with dissolve
    s "A social movement seeking to change bias in social attitudes."
    show sima3a 1e 2a 3d at u31 as sima with dissolve
    s "See, the latest thinking is that you should accept your body."
    show sima3b 1d 2a 3b blush at u31 as sima
    show marta2 1g 2c 3a regular1 blush at d33 as marta
    show nana1 1b 2c 3c regular1 blush at d32 as nana
    with dissolve
    s "Meaning, among other things, that you can eat everything with little moderation!"
    show sima3b 1d 2a 3b blush at d31 as sima
    show nana1 1b 2c 3c regular1 blush at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3b noblush at d31 as sima
    show nana1 1e 2c 3c regular1 at u32 as nana
    show marta2 1g 2c 3a regular1 noblush at d33 as marta
    with dissolve
    n "Count me in as an activist!"
    show nana1 1e 2c 3c regular1 at d32 as nana
    show marta2 1g 2c 3a regular1 noblush at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 noblush at d32 as nana
    show marta1 1e 2a 3a at u33 as marta
    show sima3a 1g 2a 3a at d31 as sima
    with dissolve
    m "Still, how's that related to our meeting? I don't like to make things up."
    show marta1 1e 2a 3a at d33 as marta
    show sima3a 1g 2a 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta1 1d 2a 3a at d33 as marta
    show sima3a 1d 2a 3a at u31 as sima
    with dissolve
    s "No one makes up anything! Why don't we talk about our guilty pleasures today?"
    show sima2 1d 2a 3c regular1 at u31 as sima
    show marta3 1g 2a 3a regular1 at d33 as marta
    with dissolve
    s "Oh, and we can eat something tasty! After all, the word \"guilty\" is no more."
    show sima2 1d 2a 3c regular1 at d31 as sima
    show nana1 1g 2a 3a regular2 noblush at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3a at d31 as sima
    show nana1 1e 2c 3c regular1 blush at u32 as nana
    with dissolve
    n "Eat tasty things... as much as I want... Is this real life?"
    show nana1 1e 2c 3c regular1 blush at d32 as nana
    show marta3 1g 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2c 3c regular2 noblush at d32 as nana
    show marta2 1e 2d 3d at u33 as marta
    with dissolve
    m "Wait, but won't we get fat and all?"
    show marta2 1e 2d 3d at d33 as marta
    show sima3a 1g 2a 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2d 3d at d33 as marta
    show sima3b 1d 2c 3b at u31 as sima
    with dissolve
    s "That's the punchline! They say it's totally okay nowadays!"
    show marta2 1d 2d 3d at u33 as marta
    show sima3b 1d 2c 3b at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3b 1g 2c 3b at d31 as sima
    show marta2 1e 2d 3d regular2 at u33 as marta
    with dissolve
    m "But the boys always look at slim girls!"
    show marta2 1e 2d 3d regular2 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3c at d31 as sima
    show nana1 1f 2d 3a regular2 at d32 as nana
    show marta2 1f 2d 3d regular1 at d33 as marta
    with dissolve
    $ renpy.pause(1, hard=True)
    hide sima
    hide nana
    hide marta
    show cg_isthatso as is_that:
        xpos 100
    with fade
    $ renpy.pause(.5 , hard=True)
    show cg_isthatso_sima with dissolve:
        xpos 100
    s "[player_name], do you like slim girls?"
    hide cg_isthatso_sima with dissolve
    menu:
        "Um... No, of course not!":
            p "Um... No, of course not!"
        "Um... Yes, I do.":
            p "Um... Yes, I do."
    show cg_isthatso_marta as is_that with dissolve:
        xpos 100
    m "What did you say???"
    hide is_that
    show sima3b 1g 2c 3a at d31 as sima
    show nana1 1a 2a 3a regular2 at d32 as nana
    show marta2 1g 2a 3a at d33 as marta
    with fade
    show sima3b 1g 2c 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3b 1e 2c 3b at u31 as sima with dissolve
    s "See?"
    show sima3b 1e 2c 3b at d31 as sima
    show nana1 1a 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3a at d31 as sima
    show nana1 1d 2c 3a regular1 at u32 as nana
    with dissolve
    n "Let's get started! I like potato chips!"
    show nana1 1d 2c 3a regular1 at d32 as nana
    show marta2 1g 2a 3a at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1b 2c 3a regular1 at d32 as nana
    show marta3 1cc 2c 3c regular2 at u33 as marta
    with dissolve
    m "Whoa, it's a calorie bomb."
    show nana1 1b 2c 3a regular1 at u32 as nana
    show marta3 1cc 2c 3c regular2 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d33 as marta
    show nana1 1c 2d 3b regular1 blush at u32 as nana
    with dissolve
    n "Are you hating on me?"
    show marta3 1g 2a 3a regular1 at u33 as marta
    show nana1 1c 2d 3b regular1 blush at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1c 2d 3a regular1 at d32 as nana
    show marta3 1e 2a 3b regular1 at u33 as marta
    m "Just a slip of the tongue."
    show sima3a 1g 2a 3a at u31 as sima
    show marta3 1e 2a 3b regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d33 as marta
    show nana1 1g 2a 3a regular2 noblush at d32 as nana
    show sima2 1d 2a 3a regular1 at u31 as sima
    with dissolve
    s "As for me, it's probably pizza."
    show sima2 1d 2a 3a regular1 at d31 as sima
    show marta3 1g 2a 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1g 2a 3a regular2 at d31 as sima
    show marta2 1b 2a 3a regular2 at u33 as marta
    with dissolve
    m "Can't live without sweet things."
    show marta2 1b 2a 3a regular2 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d33 as marta with dissolve
    $ renpy.pause(.5, hard=True)
    show marta2 1c 2a 3a regular1 at d33 as marta with dissolve
    $ renpy.pause(.3, hard=True)
    show nana1 1f 2a 3a regular2 at d32 as nana with dissolve
    $ renpy.pause(.4, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima with dissolve
    $ renpy.pause(.4, hard=True)
    show marta2 1c 2a 3a regular1 at u33 as marta
    show marta2 1d 2b 3d regular1 at u33 as marta with dissolve
    m "So... that's it for discussion?"
    show marta2 1d 2b 3d regular1 at d33 as marta
    show sima2 1a 2a 3a regular2 at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2b 3d regular1 at d33 as marta
    show sima2 1d 2a 3a regular2 at u31 as sima
    with dissolve
    s "We need to find common ground."
    show sima2 1d 2a 3a regular2 at d31 as sima
    show nana1 1f 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima
    show nana1 1e 2a 3a regular2 at u32 as nana
    with dissolve
    n "What about soft drinks?"
    show nana1 1e 2a 3a regular2 at d32 as nana
    show marta2 1d 2b 3d regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d31 as sima
    show nana1 1a 2a 3a regular2 at d32 as nana
    show marta2 1e 2a 3d regular2 at u33 as marta
    with dissolve
    m "It's not food."
    show nana1 1a 2a 3a regular2 at u32 as nana
    show marta2 1e 2a 3d regular2 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3d regular1 at d33 as marta
    show nana1 1e 2a 3a regular2 at u32 as nana
    with dissolve
    n "What about cakes then?"
    show nana1 1e 2a 3a regular2 at d32 as nana
    $ renpy.pause(.2, hard=True)
    show nana1 1g 2c 3c blush regular1 at d32 as nana
    show marta2 1g 2c 3d blush regular1 at d33 as marta
    show sima2 1g 2b 3d blush regular2 at d31 as sima
    with dissolve
    $ renpy.pause(.3, hard=True)
    "Winning by unanimous decision!"
    show nana1 1g 2c 3c blush regular1 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1d 2c 3c noblush regular1 at u32 as nana
    show marta2 1g 2a 3a noblush regular1 at d33 as marta
    show sima3a 1g 2a 3a noblush at d31 as sima
    with dissolve
    n "Hey, let's make a perfect cake!"
    show nana1 1d 2c 3c noblush regular1 at d32 as nana
    show marta2 1g 2a 3a noblush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular1 at d32 as nana
    show marta2 1e 2b 3a regular1 at u33 as marta
    with dissolve
    m "We don't have any ingredients..."
    show marta2 1e 2b 3a regular1 at d33 as marta
    show sima3a 1g 2a 3a noblush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d32 as nana
    show marta2 1f 2b 3a regular1 at d33 as marta
    show sima2 1d 2a 3a regular1 at u31 as sima
    with dissolve
    s "Let's go buy some, we have our budget."
    show sima2 1d 2a 3a regular1 at d31 as sima
    show nana1 1a 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima
    show marta2 1a 2b 3a regular1 at d33 as marta
    show nana3 1d 2a 3b blush at u32 as nana
    with dissolve
    n "I already know what the perfect cake looks and tastes like!"
    show marta2 1a 2b 3a regular1 at u33 as marta
    show nana3 1d 2a 3b blush at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1g 2a 3b blush at d32 as nana
    show marta2 1b 2a 3a regular2 at u33 as marta
    with dissolve
    m "So do I!"
    show marta2 1b 2a 3a regular2 at d33 as marta
    show sima2 1a 2a 3a regular2 at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d33 as marta
    show sima3b 1d 2a 3d blush at u31 as sima
    show nana3 1g 2a 3d noblush at d32 as nana
    with dissolve
    s "I know that as well!"
    show sima3b 1d 2a 3d blush at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3b 1g 2a 3d noblush at d31 as sima with dissolve
    p "Looks like we're going to have a heated discussion..."
    show sima3b 1g 2a 3d noblush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1d 2a 3b at u31 as sima with dissolve
    s "Hm... Not if you're the one who makes the cake, [player_name]!"
    show sima1 1d 2a 3b at d31 as sima
    show nana3 1g 2a 3d noblush at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima1 1e 2a 3a at d31 as sima
    show nana3 1e 2a 3d at u32 as nana
    with dissolve
    n "Great idea! If anything, you're the one to blame!"
    show nana3 1e 2a 3d at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1g 2a 3a at d32 as nana with dissolve
    p "But I can't read your minds..."
    show marta2 1g 2a 3a regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1e 2a 3a regular1 at u33 as marta with dissolve
    m "Well, then it means you have to test your luck!"
    show marta3 1e 2a 3a regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d33 as marta with dissolve
    p "Alright, last question..."
    p "How am I supposed to get the ingredients?"
    show marta2 1f 2b 3a regular1 at d33 as marta with dissolve
    p "And even if I manage to do it..."
    show nana2 1a 2b 3a at d32 as nana
    show sima1 1a 2b 3a at d31 as sima
    with dissolve
    p "We have no kitchen or anything like this here."
    show sima1 1a 2b 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1c 2b 3a regular2 at u31 as sima with dissolve
    s "Oh dear."
    show sima2 1c 2b 3a regular2 at d31 as sima
    show marta2 1f 2b 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2b 3a regular2 at d31 as sima
    show marta1 1e 2b 3d at u33 as marta
    with dissolve
    m "Why do you ruin our dream, [player_name]?"
    show marta1 1e 2b 3d at d33 as marta
    show nana2 1a 2b 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta1 1a 2b 3d at d33 as marta
    show nana3 1e 2a 3a at u32 as nana
    with dissolve
    n "A dream, you say..."
    show nana1 1e 2a 3a regular2 at u32 as nana
    show marta2 1a 2a 3a regular1 at d33 as marta
    show sima3a 1g 2a 3a at d31 as sima
    with dissolve
    n "Let's try closing our eyes again, but this time we won't be meditating."
    show nana1 1e 2c 3c regular2 at u32 as nana
    show marta2 1c 2c 3a regular1 at d33 as marta
    show sima3a 1c 2c 3a at d31 as sima
    with dissolve
    n "No, we'll use the power of visualization!"
    show nana1 1d 2c 3a regular1 at u32 as nana
    show marta2 1a 2c 3a regular1 at d33 as marta
    show sima3a 1a 2c 3a at d31 as sima
    with dissolve
    n "If we visualize a cake... It will get attracted to us!"
    show sima1 1c 2d 3b at d31 as sima
    show marta3 1a 2b 3b blush regular1 at d33 as marta
    show nana1 1c 2d 3b regular2 at u32 as nana
    with dissolve
    n "Behold, [player_name]!"
    stop music fadeout 1.5
    jump cake_game
label tea_after:
    scene black with fade
    $ renpy.pause(1, hard=True)
    show cg_all_2_2 as tea
    with fade
    $ persistent.unlock_cg_all_2_2 = 1
    "In the end, our combined visualization powers were still not enough."
    "The cake was a lie."
    call drinking_tea from _call_drinking_tea
    show cg_all_1_3 as tea with dissolve
    "Well..."
    show cg_all_1_2 as tea with dissolve
    "As they say, \"Time you enjoy wasting is not wasted time.\""
    scene black with fade
    if books_skip == 1:
        jump street_ermy

    python:
        am_tp  = acm_p + am_p
    python:
        as_tp = acs_p + as_p
    python:
        an_tp = acn_p + an_p

    if as_tp > am_tp:
        if as_tp > an_tp:
            jump street_sima
        elif as_tp < an_tp:
            jump street_nana
        else:
            jump street_ermy
    elif am_tp > as_tp:
        if am_tp > an_tp:
            jump street_marta
        elif am_tp < an_tp:
            jump street_nana
        else:
            jump street_ermy
    elif am_tp == as_tp:
        if an_tp > am_tp:
            if an_tp > as_tp:
                jump street_nana
            else:
                jump street_ermy
        else:
            jump street_ermy
    else:
        jump street_ermy

label street_nana:
    $ g_p_1 = 1
    scene jp_classroom_night with fade
    "I realized I forgot my notes in the classroom."
    "I was on my way out when I stumbled across Nana."
    call after_club_nana from _call_after_club_nana
    show nana1_redtint 1e 2a 3a regular2 at u11 as nana with dissolve
    n "Are you heading off to your home?"
    show nana1_redtint 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Yeah."
    show nana3_redtint 1e 2a 3b at u11 as nana with dissolve
    n "Mind if I tag along?"
    show nana3_redtint 1g 2a 3b at u11 as nana with dissolve
    p "I don't!"
    show nana3_redtint 1d 2a 3a at u11 as nana with dissolve
    n "Surprised?"
    show nana3_redtint 1g 2a 3a at u11 as nana with dissolve
    p "Well, you've never kept me company before..."
    show nana3_redtint 1b 2a 3d at u11 as nana with dissolve
    n "It's because our classes just started, silly."
    show nana1_redtint 1e 2a 3a regular2 at u11 as nana with dissolve
    n "Also, you picked my favorite book!"
    show nana1_redtint 1b 2a 3a regular2 at u11 as nana with dissolve
    n "Shall we go or do you prefer to stay here?"
    stop music fadeout 1.5
    scene black with fade
    $ renpy.pause(1, hard=True)
    play music "music/way_back_day1.ogg"fadein 1.5
    scene street with fade
    "Evening already! Time sure flies..."
    "We walk in silence, and it feels a bit awkward."
    "I decide to start a conversation, but play it safe."
    show nana1_dark 1a 2a 3a regular2 at di11 as nana with dissolve
    p "Hey, Nana..."
    show nana1_dark 1c 2a 3a regular2 at u11 as nana
    n "Yes?"
    show nana1_dark 1a 2b 3a regular2 at u11 as nana with dissolve
    p "You know, I admire your outlook on life."
    show nana1_dark 1f 2b 3a regular2 at u11 as nana with dissolve
    p "The way you see things may be unusual, but it's honest and clever."
    p "I can relate to what you said in class today."
    show nana1_dark 1c 2a 3d regular2 at u11 as nana with dissolve
    n "Thanks."
    show nana1_dark 1f 2a 3d regular2 at u11 as nana with dissolve
    "And... that's it, a one word reply?"
    "Maybe she doesn't like small talk... Alright!"
    p "So clever that now when I look at you, I can't help but notice..."
    p "Notice another layer below your surface of fun and cutesy."
    show nana3_dark 1b 2c 3d blush at u11 as nana with dissolve
    n "Wow, so deep..."
    show nana3_dark 1d 2a 3d noblush at u11 as nana with dissolve
    n "Getting straight to a personal matter, aren't we?"
    hide nana
    show cg_nana_7_1 as nana1
    with fade
    $ persistent.unlock_cg_nana_7_1 = 1
    n "Just teasing you! It's okay..."
    n "See, chitchat feels like sandpaper to me."
    n "And the surface you just described... You know, it's very convenient to have one."
    n "It makes life a whole lot easier, [player_name]."
    n "People perceive me as a nice, innocent girl, especially because I look... pretty young."
    n "You know what? It's great."
    n "I can simply play dumb when I need to, and it's enough to get out of everything."
    show cg_nana_7_2 as nana1 with dissolve
    n "Who'd blame me if I make a face like {i}this{/i}?"
    show cg_nana_7_1 as nana1 with dissolve
    p "Y-yeah, I understand..."
    p "Well, what does the real Nana look like?"
    n "I'm trying to figure this one myself, [player_name], don't know {i}yet{/i}. Time will tell."
    n "One thing I know for sure is that unexpected cleverness throws people off."
    hide nana1
    show nana1_dark 1a 2a 3a regular2 noblush at ui11 as nana
    hide cg_nana_7_1
    with fade
    p "What do you mean?"
    show nana3_dark 1d 2b 3d noblush at u11 as nana with dissolve
    n "My friends don't ask for my advice anymore... They used to, you know."
    show nana3_dark 1a 2a 3d at u11 as nana with dissolve
    p "Why?"
    show nana3_dark 1e 2a 3d at u11 as nana with dissolve
    n "Well, they expect this..."
    show nana1date_dark 1e 2c 3a regular1 blush at u11 as nana with dissolve
    n "\"Take it easy! You can make it! I will be rooting for you, alright?\""
    show nana1date_dark 1g 2c 3a regular1 blush at u11 as nana with dissolve
    p "Wow, now I know what causes global warming."
    show nana1_dark 1d 2a 3b regular2 noblush at u11 as nana with dissolve
    n "Haha!"
    show nana3_dark 1d 2a 3a at u11 as nana with dissolve
    n "Anyway, I think you see the point."
    show nana2_dark 1c 2b 3d at u11 as nana with dissolve
    n "And when I actually try to help..."
    show nana2date_dark 1d 2b 3c regular at u11 as nana with dissolve
    n "\"How cold and rude. I thought you were my friend.\""
    show nana2_dark 1f 2a 3a at u11 as nana with dissolve
    p "You know what? I'd listen to your advice, Nana."
    show nana3_dark 1a 2a 3d at u11 as nana with dissolve
    p "Especially if it went together with you rooting for me."
    show nana3_dark 1e 2a 3d at u11 as nana with dissolve
    n "I see..."
    show nana1_dark 1d 2a 3a regular1 at u11 as nana with dissolve
    n "By the way, I actually enjoy cute things, I really do."
    show nana3_dark 1e 2a 3a at u11 as nana with dissolve
    n "They make everything tolerable."
    show nana3_dark 1g 2a 3a at u11 as nana with dissolve
    p "Nana, what do you look for in people?"
    show nana3_dark 1c 2a 3a at u11 as nana with dissolve
    n "Fun. I thought I told you..."
    show nana3_dark 1a 2b 3a at u11 as nana with dissolve
    p "Is that all? I don't buy it."
    show nana2_dark 1c 2a 3d at u11 as nana with dissolve
    n "Alright, much more than that, but..."
    show nana2_dark 1d 2a 3a at u11 as nana with dissolve
    n "I am tired of being disappointed in people."
    show nana2_dark 1b 2a 3d at u11 as nana with dissolve
    n "Over and over again they turn out to be boring and predictable."
    show nana2_dark 1d 2a 3d at u11 as nana with dissolve
    n "It's painful, so... I've just stopped expecting anything."
    show nana2_dark 1c 2a 3a at u11 as nana with dissolve
    n "Fun is my safe bet."
    show nana2_dark 1e 2c 3c at u11 as nana with dissolve
    $ renpy.pause(1, hard=True)
    show nana3_dark 1g 2a 3a at u11 as nana with dissolve
    p "Well, I hope someone exceeds your expectations very soon!"
    show nana3_dark 1b 2a 3d at u11 as nana with dissolve
    n "Okay, I'll keep an eye on you!"
    show nana3_dark 1g 2a 3d at u11 as nana with dissolve
    p "On me?"
    show nana1_dark 1e 2a 3a regular2 at u11 as nana with dissolve
    n "Alright, [player_name], I need to take the subway now."
    show nana1_dark 1d 2a 3d blush regular2 at u11 as nana with dissolve
    n "It was nice talking to you! I mean it..."
    show nana3_dark 1d 2a 3d at u11 as nana with dissolve
    n "See you tomorrow!"
    hide nana with dissolve
    $ renpy.pause(1, hard=True)
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            scene ru_classroom_day with fade
            jump beauty
    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            jump catgirl_extra5
    jump street_end
label street_sima:
    $ g_p_1 = 3
    scene jp_classroom_night with fade
    "I realized I forgot my notes in the classroom."
    "I was on my way out when I stumbled across Sima."
    show sima2_redtint 1c 2a 3a regular2 at u11 as sima with dissolve
    s "Hoped you enjoyed the club today..."
    show sima2_redtint 1e 2a 3a regular2 at u11 as sima with dissolve
    p "It was... memorable!"
    show sima3a_redtint 1d 2a 3d at u11 as sima with dissolve
    s "By the way, I'm glad you picked \"Crime and Punishment\" today!"
    show sima3a_redtint 1a 2a 3d at u11 as sima with dissolve
    p "It would've been a crime not to do so."
    show sima3a_redtint 1g 2a 3a at u11 as sima with dissolve
    p "What are you doing here?"
    show sima1_redtint 1d 2a 3d at u11 as sima with dissolve
    s "I wanted to write a report about our meeting, but I'm too tired."
    show sima1_redtint 1c 2a 3b at u11 as sima with dissolve
    s "I think I'll just head home."
    show sima1_redtint 1a 2a 3a at u11 as sima with dissolve
    p "Where to?"
    "Turned out our we live near each other."
    show sima3a_redtint 1c 2a 3a at u11 as sima with dissolve
    s "I wonder if you qualify for a boy next door, [player_name]..."
    show sima3a_redtint 1g 2c 3a at u11 as sima with dissolve
    p "The only way to tell is for me to keep you company."
    show sima3a_redtint 1e 2a 3b at u11 as sima with dissolve
    s "Sure, why not?"
    show sima3a_redtint 1a 2a 3a at u11 as sima with dissolve
    p "Wow!"
    "Somehow, I said it out loud."
    show sima3a_redtint 1e 2a 3d at u11 as sima with dissolve
    s "What's so surprising?"
    show sima3a_redtint 1g 2a 3d at u11 as sima with dissolve
    p "Never thought you'd accept..."
    show sima2_redtint 1d 2c 3a regular1 at u11 as sima with dissolve
    s "I am curious to hear why, [player_name]."
    show sima2_redtint 1e 2a 3d regular2 at u11 as sima with dissolve
    s "See, now we even have a topic to discuss!"
    call after_club_sima from _call_after_club_sima
    stop music fadeout 1.5
    scene black with fade
    $ renpy.pause(1, hard=True)
    play music "music/way_back_day1.ogg"fadein 1.5
    scene street with fade
    "It's evening already. Time sure flies..."
    show sima1_dark 1c 2a 3a at u11 as sima with dissolve
    s "So? What's so surprising about us walking home together?"
    show sima1_dark 1a 2a 3a at u11 as sima with dissolve
    p "Oh, it's... well..."
    p "Like I told you, I never thought you'd accept."
    show sima1_dark 1a 2d 3b blush at u11 as sima with dissolve
    p "You seem a bit distant and resorted, that's why..."
    show sima2_dark 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Hey, that's not true. Maybe it seems like that because of the way I behave..."
    show sima1_dark 1c 2d 3a blush at u11 as sima with dissolve
    s "And yes, it takes me some time to open up, but it's only normal."
    show cg_sima_1_2 as sima1 with fade
    $ persistent.unlock_cg_sima_1_1 = 1
    s "I always mind my manners."
    p "Don't you think it can lead people away?"
    show cg_sima_1_1 as sima1 with dissolve
    s "Not really... why?"
    p "Let's say you run into someone who wears the same outfit as you..."
    show cg_sima_1_2 as sima1 with dissolve
    s "Oh my, [player_name], you picked the worst example for a girl."
    show cg_sima_1_3 as sima1 with dissolve
    s "In that case, I'd try to cross the street."
    p "I just wanted to say a lot of people won't have enough courage to approach you."
    p "Who knows, maybe one of them could've became your friend?"
    p "Instead, they would simply think you're not interested."
    show cg_sima_1_1 as sima1 with dissolve
    s "[player_name], don't get me started about that, okay?"
    p "Did I say something wrong?"
    s "No, it's just... well, that's a different story. Maybe I'll tell you later."
    hide sima1
    show sima1_dark 1a 2a 3a blush at u11 as sima
    with fade
    "I always thought Sima's been very popular throughout her life, but..."
    "Somehow, her words make me less confident about it."
    show sima1_dark 1c 2a 3d noblush at u11 as sima with dissolve
    s "Anyway, real friends are so rare that I'm unlikely to find them in the streets."
    show sima1_dark 1a 2a 3a  at u11 as sima with dissolve
    p "It's worth the try, I think, because a friend can stay with your forever."
    show sima1_dark 1d 2b 3b at u11 as sima with dissolve
    s "I'm afraid my friendships don't last, [player_name]..."
    show sima1_dark 1a 2b 3a at u11 as sima with dissolve
    p "What happens?"
    show sima1_dark 1c 2d 3d at u11 as sima with dissolve
    s "I tend to think that people are good friends while you're even."
    show sima1_dark 1d 2b 3b at u11 as sima with dissolve
    s "However, as soon as you start doing better..."
    show sima1_dark 1d 2a 3a at u11 as sima with dissolve
    s "They think you're out of their league, and become increasingly distant."
    show sima3a_dark 1d 2a 3a at u11 as sima with dissolve
    s "Don't know whether they're envious or just feeling uncomfortable."
    show sima3a_dark 1a 2a 3a at u11 as sima with dissolve
    p "I think I know what you're talking about..."
    show sima3a_dark 1d 2b 3a at u11 as sima with dissolve
    s "But what you probably don't know is that I come from a wealthy, noble family."
    show sima2_dark 1c 2a 3a regular1 at u11 as sima with dissolve
    s "Trust me, it makes things even worse."
    show sima2_dark 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Something tells me you'd never make a big deal out of it."
    show sima2_dark 1d 2c 3a regular1 at u11 as sima with dissolve
    s "Exactly! Still, my social status alone is enough for people to alienate me."
    show sima2_dark 1c 2b 3b regular1 at u11 as sima with dissolve
    s "Money ruins friendships."
    show sima2_dark 1d 2d 3a regular2 at u11 as sima with dissolve
    s "What's even worse, \"friends\" often become leaches."
    show sima1_dark 1d 2d 3a at u11 as sima with dissolve
    s "When I'm not able to help them, they're all like..."
    show sima1_dark 1d 2d 3b at u11 as sima with dissolve
    s "\"But it means nothing to you! What a scrooge...\""
    show sima1_dark 1a 2d 3a at u11 as sima with dissolve
    p "Have you tried looking for someone within your social circle?"
    show sima1_dark 1d 2d 3b at u11 as sima with dissolve
    s "I can't deal with rich kids. Oh dear, this crowd..."
    show sima2_dark 1d 2c 3a regular1 at u11 as sima with dissolve
    s "Today I chose \"Crime and Punishment\", but in fact I should've gone with \"Vanity Fair\"."
    show sima2_dark 1a 2c 3a regular2 at u11 as sima with dissolve
    p "Hey, I wouldn't mind being your friend."
    show sima2_dark 1c 2c 3d regular2 at u11 as sima with dissolve
    s "What for?"
    show sima2_dark 1a 2c 3c blush regular2 at u11 as sima with dissolve
    p "I don't think there should be a reason."
    s "..."
    show sima2_dark 1a 2b 3b  regular2 at u11 as sima with dissolve
    "She whispers something."
    show sima2_dark 1a 2a 3a  regular2 at u11 as sima with dissolve
    p "What did you say?"
    show sima2_dark 1d 2a 3a  regular1 at u11 as sima with dissolve
    s "I said we'll see!"
    show sima2_dark 1c 2a 3a regular2 at u11 as sima with dissolve
    s "And now it's time for me to go, [player_name]."
    show sima3a_dark 1c 2a 3d at u11 as sima with dissolve
    s "I enjoyed the discussion. You know, if we talk about first impression..."
    show sima3a_dark 1d 2a 3a at u11 as sima with dissolve
    s "You certainly seem different from others."
    show sima3a_dark 1e 2a 3a at u11 as sima with dissolve
    s "Question is, will you make this impression last?"
    show sima2_dark 1e 2a 3d regular2 at u11 as sima with dissolve
    s "See you tomorrow!"
    show sima2_dark 1a 2a 3d regular2 at d11 as sima with dissolve
    $ renpy.pause(.5, hard=True)
    hide sima with dissolve
    $ renpy.pause(2, hard=True)
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            scene ru_classroom_day with fade
            jump future
    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            jump catgirl_extra5
    jump street_end
label street_marta:
    $ g_p_1 = 2
    scene jp_classroom_night with fade
    "I realized I forgot my notes in the classroom."
    "I was on my way home when I stumbled across Marta."
    call after_club_marta from _call_after_club_marta
    show marta3_redtint 1g 2a 3b regular1 at u11 as marta with dissolve
    m "Our club was weird but fun, don't you agree?"
    show marta3_redtint 1e 2a 3a regular1 at u11 as marta with dissolve
    m "By the, to think that you like \"The Catcher in the Rye\"..."
    show marta2_redtint 1b 2a 3b regular2 at u11 as marta with dissolve
    m "Not bad, not bad!"
    show marta2_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Thanks! I am heading off to home, you?"
    show marta3_redtint 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Same."
    show marta3_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Where do you live?"
    "Turns out we reside close to each other."
    p "Mind if I keep you company?"
    show marta2_redtint 1d 2a 3c regular1 blush at u11 as marta with dissolve
    m "..."
    show marta2_redtint 1b 2a 3a regular1 blush at u11 as marta with dissolve
    m "Sure, let's go."
    stop music fadeout 1.5
    scene black with fade
    $ renpy.pause(1, hard=True)
    play music "music/way_back_day1.ogg"fadein 1.5
    scene street
    show marta2_dark 1g 2a 3a regular1 noblush at u11 as marta
    with fade
    $ renpy.pause(1, hard=True)
    p "I thought you'd hesitate, to be honest."
    show marta2_dark 1d 2a 3a regular1 at u11 as marta with dissolve
    m "Hesitate about what?"
    p "Going home together."
    show marta3_dark 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Is it a big deal for you, [player_name]?"
    show marta3_dark 1g 2a 3a regular1 at u11 as marta with dissolve
    p "No, it's just..."
    show marta3_dark 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Just picking on you."
    show marta3_dark 1ee 2a 3a regular2 blush at u11 as marta with dissolve
    m "\"It's not like I want you to invite me...\""
    show marta3_dark 1g 2a 3a regular1 noblush at u11 as marta with dissolve
    m "Did you expect this, [player_name]?"
    show marta2_dark 1b 2a 3a regular2 at u11 as marta with dissolve
    m "Don't make me laugh!"
    show marta2_dark 1g 2a 3a regular1 at u11 as marta with dissolve
    p "I'd be happy to make you laugh though..."
    show marta2_dark 1c 2c 3c blush regular1 at u11 as marta with dissolve
    m "..."
    "She blushes a little. It looks surprisingly cute."
    p "Marta, I really enjoyed your speech today."
    show marta2_dark 1b 2a 3a noblush regular1 at u11 as marta with dissolve
    m "Thanks, I put quite some effort in preparation."
    show marta2_dark 1a 2a 3a regular1 at u11 as marta with dissolve
    p "I bet you worked hard! By the way, what motivates you? Like, in life?"
    show marta2_dark 1d 2a 3a regular2 at u11 as marta with dissolve
    m "It's a bit hard to explain..."
    show marta2_dark 1c 2b 3a regular1 at u11 as marta with dissolve
    m "Promise not to laugh?"
    show marta2_dark 1a 2b 3a regular1 at u11 as marta with dissolve
    p "Would a pinky promise do?"
    show marta3_dark 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Deal! You see, [player_name]..."
    show marta3_dark 1g 2b 3b regular1 at u11 as marta with dissolve
    m "For me, there's no motivation in the usual sense of this word."
    show cg_marta_3_5 as marta1 with fade
    $ persistent.unlock_cg_marta_3_2 = 1
    m "I simply can't afford to waste countless hours I've invested in studying for nothing."
    m "If I'd stop now and just... chill, what was all the hard work for?"
    show cg_marta_3_4 as marta1 with dissolve
    m "I mean, I might've been slacking for all this time instead... having fun, you know."
    p "So you plan to have fun later on?"
    show cg_marta_3_3 as marta1 with dissolve
    m "True, until I have enough money racked up for everything I want."
    m "I sacrifice today for a good, grass-fed tomorrow."
    show cg_marta_3_6 as marta1 with dissolve
    m "Does this pass as a motivation?"
    p "I think so, but..."
    p "What motivated you in the very beginning then?"
    show cg_marta_3_3 as marta1 with dissolve
    m "I was lacking."
    p "Lacking of what?"
    m "Lacking {i}in{/i} everything."
    show cg_marta_3_4 as marta1 with dissolve
    m "You know, some people are naturally gifted... I was naturally mediocre."
    show cg_marta_3_2 as marta1 with dissolve
    m "Jack of all trades, master of none."
    m "I realized it wouldn't get me far."
    show cg_marta_3_1 as marta1 with dissolve
    m "So I decided to become the best by putting more effort."
    m "Well, here I am. Turns out being mediocre is enough in this day and age."
    show marta1_dark 1a 2b 3b at u11 as marta
    hide marta1
    with fade
    p "You think too low of yourself."
    show marta1_dark 1g 2b 3d at u11 as marta with dissolve
    p "Your \"mediocre\" is the end goal for other people."
    show marta2_dark 1e 2a 3a regular2 at u11 as marta with dissolve
    m "I compare myself only to my previous self. Oh, and to those who are better."
    show marta2_dark 1d 2a 3a regular1 at u11 as marta with dissolve
    m "You won't progress otherwise, [player_name]."
    show marta2_dark 1a 2c 3a regular1 at u11 as marta with dissolve
    p "That's why you spend a lot of time with Sima, right?"
    show marta2_dark 1f 2b 3d regular1 at u11 as marta with dissolve
    p "Well, if you keep up the pace, the victory will be yours, no doubt."
    show marta2_dark 1f 2d 3d regular1 at u11 as marta with dissolve
    m "..."
    "Although I complimented her, Marta's visibly annoyed."
    show marta2_dark 1d 2d 3d regular1 blush at u11 as marta with dissolve
    m "What has that to do with Sima? I don't compare myself to her."
    show marta2_dark 1e 2d 3c regular2 blush at u11 as marta with dissolve
    m "No way I'm doing this!"
    show marta2_dark 1b 2b 3a regular1 blush at u11 as marta with dissolve
    m "However... what you said about my victory was really pleasant, [player_name]."
    show marta2_dark 1d 2a 3a regular1 noblush at u11 as marta with dissolve
    m "Look, I don't have much time left now, but..."
    show marta3_dark 1e 2a 3a regular1 at u11 as marta with dissolve
    m "I enjoyed your company!"
    show marta3_dark 1ee 2a 3b regular2 at u11 as marta with dissolve
    m "Keep saying pleasant things to me tomorrow, okay?"
    show marta2_dark 1b 2a 3a regular2 at u11 as marta with dissolve
    m "It's an order!"
    show marta2_dark 1g 2a 3a regular1 at d11 as marta with dissolve
    $ renpy.pause(1, hard=True)
    hide marta with dissolve
    "She says good-bye and leaves."
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            scene ru_classroom_day with fade:
            jump success
    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            jump catgirl_extra5
    jump street_end
label street_ermy:
    $ g_p_1 = 4
    play music "music/way_back_day1.ogg" fadeout 1.5 fadein 1.5
    scene street with fade
    "I'm on my way home. Evening already! Time sure flies..."
    "Suddenly, I see Ermy nearby the convenience store."
    show ermy1_dark 1d 2a 3a pose1 at u11 as ermy
    e "Hey, what's up?"
    show ermy1_dark 1b 2a 3a pose2 at u11 as ermy with dissolve
    e "How was the club?"
    show ermy1_dark 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "It was alright, I guess..."
    show ermy1_dark 1h 2a 3c pose2 at u11 as ermy with dissolve
    e "Look, maybe you could take me in, after all... I promise to do my best!"
    show ermy1_dark 1f 2a 3a pose2 at u11 as ermy with dissolve
    p "I'm okay with this, but I think the girls don't want to..."
    show ermy1_dark 1f 2b 3a pose2 at u11 as ermy with dissolve
    p "We still have plenty of time on our hands, just keep asking."
    show ermy1_dark 1c 2b 3a pose2 at u11 as ermy with dissolve
    e "What should I do to raise my chances of being accepted?"
    show ermy1_dark 1f 2b 3a pose2 at u11 as ermy with dissolve
    p "I have an idea... Promise you won't get mad?"
    show ermy1_dark 1e 2c 3a pose2 at u11 as ermy with dissolve
    e "Of course not, I'd really appreciate it."
    show ermy1_dark 1g 2a 3a pose2 at u11 as ermy with dissolve
    p "Look, Ermy, you're a nice guy."
    show ermy1_dark 1f 2a 3a pose2 at u11 as ermy with dissolve
    p "Problem is, nice guys aren't popular."
    show ermy1_dark 1e 2b 3a pose2 at u11 as ermy with dissolve
    p "Maybe you should change your game a bit."
    show ermy1_dark 1d 2b 3b pose1 at u11 as ermy with dissolve
    e "Hm... If only I knew how!"
    show ermy1_dark 1a 2a 3a pose1 at u11 as ermy with dissolve
    p "I'll be honest with you, it's easier said than done."
    show ermy1_dark 1a 2c 3a pose2 at u11 as ermy with dissolve
    p "I'm acting high and mighty now, but if I were to go on a date with one of the girls..."
    p "Man, not sure I wouldn't act like an idiot."
    show ermy1_dark 1c 2c 3c pose2 at u11 as ermy with dissolve
    e "Wow, really? You look pretty confident."
    show ermy1_dark 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "Exactly, it's all about the looks."
    show ermy1_dark 1a 2a 3a pose1 at u11 as ermy with dissolve
    p "Why don't you work on how people perceive you?"
    show ermy1_dark 1g 2d 3a pose1 at u11 as ermy with dissolve
    e "I'll give it a shot. By the way..."
    show ermy1_dark 1d 2a 3a pose2 at u11 as ermy with dissolve
    e "Who's the best girl here?"
    show ermy1_dark 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "I don't really know. They're all cute here, Ermy."
    show ermy1_dark 1b 2c 3b blush pose1 at u11 as ermy with dissolve
    e "True that!"
    show ermy1_dark 1d 2c 3d pose1 at u11 as ermy with dissolve
    e "Hey, I think girls from another class like me, by the way."
    show ermy1_dark 1g 2c 3b noblush pose2 at u11 as ermy with dissolve
    p "Why?"
    show ermy1_dark 1c 2c 3c pose2 at u11 as ermy with dissolve
    e "I look at them from time to time..."
    show ermy1_dark 1d 2a 3c pose1 at u11 as ermy with dissolve
    e "And today like two girls returned my look."
    show ermy1_dark 1g 2a 3c blush pose1 at u11 as ermy with dissolve
    e "See? It's a hint, [player_name]."
    show ermy1_dark 1g 2a 3b noblush pose1 at u11 as ermy with dissolve
    p "..."
    show ermy1_dark 1d 2a 3d noblush pose2 at u11 as ermy with dissolve
    e "You think it sounds cheesy, don't you?"
    show ermy1_dark 1c 2b 3d pose2 at u11 as ermy with dissolve
    e "C'mon, I know you do."
    show ermy1_dark 1c 2b 3b pose1 at u11 as ermy with dissolve
    e "Between us, I also know I don't stand a chance in this school."
    show ermy1_dark 1c 2b 3d pose2 at u11 as ermy with dissolve
    e "One accidental look is the most intimate thing I can expect from a girl here..."
    show ermy1_dark 1a 2b 3a pose2 at u11 as ermy with dissolve
    p "Hey, what's wrong with you? You're doing fine!"
    show ermy1_dark 1d 2b 3d pose2 at u11 as ermy with dissolve
    e "I appreciate your effort, but you're a bad liar."
    show ermy1_dark 1a 2b 3d pose2 at u11 as ermy with dissolve
    p "Ermy, seriously, go get some rest."
    show ermy1_dark 1c 2a 3a pose2 at u11 as ermy with dissolve
    e "Maybe you're right..."
    show ermy1_dark 1g 2a 3a pose2 at u11 as ermy with dissolve
    e "I'll start with buying some snacks at this store! See you tomorrow!"
    show ermy1_dark 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "See you, Ermy."
    show ermy1_dark 1a 2a 3a pose2 at d11 as ermy with dissolve
    hide ermy with dissolve
    $ renpy.pause(1, hard=True)
    show ermy1_dark 1d 2a 3a pose1 at u11 as ermy with dissolve
    e "Oh, by the way, [player_name]!"
    show ermy1_dark 1a 2a 3a pose1 at u11 as ermy with dissolve
    p "What's that?"
    show ermy1_dark 1b 2b 3a pose2 at u11 as ermy with dissolve
    e "Please, don't forget to play my game! It's important!"
    show ermy1_dark 1a 2a 3a pose2 at d11 as ermy with dissolve
    $ renpy.pause(1, hard=True)
    hide ermy with dissolve
label street_end:
    scene black with fade
    "Ten minutes' walk, and then tea and slippers!"
    stop music fadeout 2
    $ renpy.pause(2, hard=True)
    jump sweet_home_d1
return

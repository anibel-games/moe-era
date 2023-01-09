label day3:
    play sound [ "<silence 1>", "sound/samenote.ogg" ] loop
    $ renpy.pause(6.0, hard=True)
    init python:
        renpy.music.register_channel("rain", "rain")
    "This sound is just sooo repetitive..."
    $ renpy.pause(1.0, hard=True)
    stop sound
    scene music_room_rain_animation with eye_open
    $ renpy.music.set_volume(0.5, 0, channel='rain')
    $ renpy.music.play('sound/rain.ogg', channel='sound', loop=True)
    show sima1close_rain 1d 2d 3b at u11 as sima
    s "So that's what you think of my piano skills, [player_name]!"
    show sima2close_rain 1e 2c 3a regular2 at u11 as sima with dissolve
    s "Just kidding! Welcome back."
    show sima2close_rain 1c 2a 3a regular2 at u11 as sima with dissolve
    s "I started playing the same note right after you dozed off."
    show sima3aclose_rain 1c 2c 3d at u11 as sima with dissolve
    s "Turns out you're quite a light sleeper."
    show sima3aclose_rain 1d 2a 3a at u11 as sima with dissolve
    s "Anyway, our class starts in a few, so you better get yourself together."
    show sima3aclose_rain 1a 2a 3a at u11 as sima with dissolve
    p "Oh, jeez. Thanks for waking me up... You know, I'm always sleepy on a rainy day."
    show sima2close_rain 1e 2a 3b regular1 at u11 as sima with dissolve
    s "You're welcome!"
    show sima2close_rain 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Hey, can you play something for me? Right now, before everyone comes in?"
    show sima3aclose_rain 1c 2b 3d blush at u11 as sima with dissolve
    s "Oh! Um... I'm not that good at piano, you see."
    show sima3aclose_rain 1a 2b 3d blush at u11 as sima with dissolve
    p "Good enough for me, I assure you."
    show sima3aclose_rain 1d 2b 3a blush at u11 as sima with dissolve
    s "Well, if you insist... Just don't expect much, okay?"
    scene melody
    with fade
    show melody1
    play music "music/sima_theme1.ogg"
    $ renpy.pause(2, hard=True)
    "She starts playing a simple yet elegant melody."
    s "How do you like it?"
    p "Somehow, that's what I thought you'd play."
    s "[player_name], I don't think it counts as an answer!"
    s "Hey, you don't think I can only play melodies this easy, do you?"
    s "Here we go..."
    stop music fadeout 1
    hide melody1 with dissolve
    $ renpy.pause(1, hard=True)
    show melody2
    play music "music/sima_theme2.ogg"
    $ renpy.pause(2, hard=True)
    "She switches to a more complicated piece."
    s "My goodness, I make way too many mistakes..."
    p "Really? I can't hear a single one, I swear."
    s "[player_name], you're flattering me."
    $ renpy.pause(1.0, hard=True)
    $ renpy.music.play("<from 0 to 4>sound/en_bell.ogg", channel='sound', loop=False)
    stop music fadeout 2
    $ renpy.pause(1.0, hard=True)
    hide melody2 with dissolve
    $ renpy.pause(1.0, hard=True)
    stop sound fadeout 2
    s "And now... the interlude!"
    $ renpy.pause(1.0, hard=True)
    scene music_room_rain_animation
    show teya2_rain 1a 2a 3a regularhand3 at u11 as teya
    with fade
    show teya2_rain 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "Okay, class."
    show teya2_rain 1b 2a 3b regularhand1 at u11 as teya with dissolve
    t "On a rainy day like this, music is a necessity for me."
    show teya2_rain 1d 2a 3a regularhand2 at u11 as teya with dissolve
    t "Let's finish early today, you need to get ready for the career day."
    show teya2_rain 1b 2a 3b regularhand1 at u11 as teya with dissolve
    t "Oh, and it's Friday, you know!"
    show teya2_rain 1e 2c 3a regularhand2 at u11 as teya with dissolve
    t "I'm scared of people who try hard on Friday."
    show teya2_rain 1e 2c 3a regularhand2 at d11 as teya
    $ renpy.pause(0.001, hard=True)
    show teya2_rain 1a 2a 3d regularhand4 at d11 as teya
    show sima2_rain 1d 2a 3a regular2 at u31 as sima
    with dissolve
    s "What are we going to discuss today?"
    hide sima with dissolve
    show teya2_rain 1a 2a 3d regularhand4 at u11 as teya
    $ renpy.pause(0.001, hard=True)
    show teya2_rain 1e 2a 3a regularhand1 at u11 as teya with dissolve
    t "I intended to cover a few basics on music theory, but..."
    show teya1_rain 1c 2a 3b at u11 as teya with dissolve
    t "Between us, music isn't about theory."
    show teya2_rain 1e 2c 3a regularhand2 at u11 as teya with dissolve
    t "I think a few notes is all you need to create a memorable melody."
    show teya1_rain 1c 2a 3a at u11 as teya with dissolve
    t "You know why? Because music influences your mood."
    show teya1_rain 1e 2b 3b at u11 as teya with dissolve
    t "Cheerful and mellow, gloomy and melancholic, music can be very differeny."
    show teya1_rain 1e 2b 3b at d21 as teya
    $ renpy.pause(.25, hard=True)
    show ermy1_rain pose2 1a 2a 3a at u22 as ermy
    $ renpy.pause(.001, hard=True)
    show teya1_rain 1b 2a 3a at d21 as teya
    show ermy1_rain pose2 1d 2a 3a at u22 as ermy
    with dissolve
    e "That's why I always tell people I don't have a favorite band."
    show ermy1_rain pose2 1g 2a 3b at u22 as ermy with dissolve
    e "Everything goes as long as the mood is right."
    show ermy1_rain pose2 1g 2a 3b at d22 as ermy
    show teya1_rain 1b 2a 3a at u21 as teya
    $ renpy.pause(.001, hard=True)
    show ermy1_rain pose2 1g 2a 3b at d22 as ermy
    show teya3_rain 1c 2a 3a at u21 as teya
    with dissolve
    t "People probably compliment your taste in music, Ermy."
    show ermy1_rain pose2 1g 2a 3b at u22 as ermy
    show teya3_rain 1c 2a 3a at d21 as teya
    $ renpy.pause(.001, hard=True)
    show teya3_rain 1a 2a 3a at d21 as teya
    show ermy1_rain pose2 1b 2c 3a blush at u22 as ermy
    with dissolve
    e "Maybe, but they hide it well."
    show teya1_rain 1b 2a 3a at d21 as teya
    show ermy1_rain pose2 1d 2a 3a noblush at u22 as ermy
    with dissolve
    e "By the way, sometimes it feels like the music {i}controls{/i} me."
    show teya1_rain 1b 2a 3a at u21 as teya
    show ermy1_rain pose2 1d 2a 3a noblush at d22 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1_rain pose2 1e 2a 3a at d22 as ermy
    show teya2_rain 1e 2c 3a regularhand2 at u21 as teya
    with dissolve
    t "Frequency and volume of a sound have enormous impact on humans."
    show teya2_rain 1c 2d 3c regularhand2 at u21 as teya with dissolve
    t "In fact, music can act as a weapon of mass destruction."
    show teya3_rain 1c 2a 3b at u21 as teya
    show ermy1_rain pose2 1a 2a 3a at d22 as ermy
    with dissolve
    t "Anyway, let's get back on track..."
    show teya2_rain 1e 2a 3a regularhand1 at u21 as teya with dissolve
    t "Your task for today is to enjoy some music! How cool is that, huh?"
    show teya1_rain 1e 2a 3a at u21 as teya
    show ermy1_rain pose2 1g 2a 3a at d22 as ermy
    with dissolve
    t "Ermy, I've heard you're really good at piano."
    show teya1_rain 1e 2a 3a at d21 as teya
    show ermy1_rain pose2 1g 2a 3a at u22 as ermy
    $ renpy.pause(.001, hard=True)
    show teya1_rain 1b 2a 3a at d21 as teya
    show ermy1_rain pose1 1e 2a 3b blush at u22 as ermy
    with dissolve
    e "T-thanks, y-you too..."
    show teya1_rain 1b 2a 3a at u21 as teya
    show ermy1_rain pose1 1e 2a 3b blush at d22 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1_rain pose2 1a 2a 3a blush at d22 as ermy
    show teya1_rain 1c 2a 3b at u21 as teya
    with dissolve
    t "Would you be so kind to play something for us?"
    show teya3_rain 1c 2a 3b at u21 as teya with dissolve
    t "Oh, and... today we discuss music theory, remember?"
    show teya3_rain 1c 2a 3b at d21 as teya
    show ermy1_rain pose2 1a 2a 3a blush at u22 as ermy
    $ renpy.pause(.001, hard=True)
    show teya3_rain 1a 2a 3a at d21 as teya
    show ermy1_rain pose2 1e 2a 3c blush at u22 as ermy
    with dissolve
    e "Anything specific you want me to play?"
    show teya3_rain 1a 2a 3a at u21 as teya
    show ermy1_rain pose2 1e 2a 3c blush at d22 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1_rain pose2 1a 2a 3a blush at d22 as ermy
    show teya2_rain 1e 2a 3a regularhand2 at u21 as teya
    with dissolve
    t "No, it's up to you!"
    show ermy1_rain pose2 1a 2a 3a blush at u22 as ermy
    show teya2_rain 1e 2a 3a regularhand2 at d21 as teya
    $ renpy.pause(.001, hard=True)
    show teya2_rain 1d 2a 3a regularhand4 at d21 as teya
    show ermy1_rain pose1 1d 2a 3a noblush at u22 as ermy
    with dissolve
    e "Alright. You can count on me!"
    scene melody with fade
    "Ermy gets ready, his fingers twitching over the keyboard like he's already playing."
label schumann:
    play music "sound/schumann.ogg"
    show melody3
    $ renpy.pause(3.0, hard=True)
    show sima2d3_rain 1e 2a 3d regular2 as sima with dissolve:
        xalign .75
        yalign .15
    s "Oh, Ermy..."
    show sima2d3_rain 1e 2c 3a regular2 as sima with dissolve:
        xalign .75
        yalign .15
    s "You like Schumann!"
    show sima2d3_rain 1d 2c 3c blush regular1 as sima with dissolve:
        xalign .75
        yalign .15
    s "\"Fantasiestücke, Des Abends\" is marvellous!"
    show sima3bd3_rain 1d 2b 3d as sima with dissolve:
        xalign .75
        yalign .15
    s "And... a rainy day suits it so well."
    show sima3ad3_rain 1c 2b 3d noblush as sima with dissolve:
        xalign .75
        yalign .15
    s "It's sad to know that my favorite composer had a tragic life."
    show sima3ad3_rain 1d 2a 3a as sima with dissolve:
        xalign .75
        yalign .15
    s "Born in 1810 in Germany, he intended to pursue a career as a virtuoso pianist."
    show sima3ad3_rain 1e 2a 3b as sima with dissolve:
        xalign .75
        yalign .15
    s "However, a hand injury destroyed his plans and made Schumann switch to composing."
    show sima3ad3_rain 1c 2a 3a as sima with dissolve:
        xalign .75
        yalign .15
    s "Who knows, maybe he would've never created this masterpiece if not for that accident."
    show sima2d3_rain 1c 2b 3b regular2 as sima with dissolve:
        xalign .75
        yalign .15
    s "Schumann suffered from a mental disorder and died at an asylum when he was only 46."
    show sima2d3_rain 1e 2b 3a regular2 as sima with dissolve:
        xalign .75
        yalign .15
    s "It's relieving to think that his music will stay with us forever."
    show sima3bd3_rain 1e 2a 3a as sima with dissolve:
        xalign .75
        yalign .15
    s "Just listen..."
    show sima3bd3_rain 1g 2a 3a as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(1.0, hard=True)
    menu:
        "Stay a while and listen.":
            jump schumann_listen
        "Move on to the next track.":
            jump satie
label schumann_listen:
    show screen sch_next
    $ renpy.pause(2.0, hard=True)
    show sima3bd3_rain 1g 2a 3b noblush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima3bd3_rain 1e 2a 3a blush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima2d3_rain 1e 2a 3a regular2 noblush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima2d3_rain 1g 2a 3b regular2 blush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima3bd3_rain 1e 2a 3a blush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima3bd3_rain 1a 2a 3a noblush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima2d3_rain 1e 2a 3a regular2 noblush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(4.0, hard=True)
    show sima2d3_rain 1g 2a 3b regular2 blush as sima with dissolve:
        xalign .75
        yalign .15
    $ renpy.pause(2.0, hard=True)
    jump schumann_listen
label satie:
    hide screen sch_next
    scene melody with fade
    play music "sound/satie.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(2.0, hard=True)
    show melody3
    $ renpy.pause(3.0, hard=True)
    show marta2d3_rain 1c 2c 3a regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "Wow!"
    show marta2d3_rain 1b 2c 3a blush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "Ermy, to think that you..."
    show marta2d3_rain 1b 2c 3c blush regular2 as marta with dissolve:
        xalign .8
        yalign .05
    m "To think that you also like Eric Satie..."
    show marta3d3_rain 1e 2a 3a noblush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "His \"Gymnopedie No. 1\" is fantastic!"
    show marta3d3_rain 1d 2a 3a regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "I listen to it on repeat while studying."
    show marta2d3_rain 1b 2a 3a regular2 as marta with dissolve:
        xalign .8
        yalign .05
    m "He was born in Honfleur, France, back in 1866."
    show marta2d3_rain 1g 2b 3b regular1 blush as marta with dissolve:
        xalign .8
        yalign .05
    m "Ah, beautiful Normandy... I want to visit it again when flowers blossom."
    show marta3d3_rain 1e 2a 3a regular1 noblush as marta with dissolve:
        xalign .8
        yalign .05
    m "Do you know the way Satie preferred to introduce himself?"
    show marta3d3_rain 1ee 2a 3a regular2 as marta with dissolve:
        xalign .8
        yalign .05
    m "He referred to himself as a \"gymnopedist\" instead of \"musician\"."
    show marta3d3_rain 1gg 2a 3b regular2 as marta with dissolve:
        xalign .8
        yalign .05
    m "It's because he was once called \"clumsy but subtle technician\" by critics."
    show marta2d3_rain 1d 2b 3a regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "Satie died at the age of 59, years of heavy drinking took its toll."
    show marta2d3_rain 1e 2b 3d regular2 as marta with dissolve:
        xalign .8
        yalign .05
    m "I guess alcohol has the killer talent for killing talents."
    show marta3d3_rain 1g 2a 3a regular1 as marta with dissolve:
        xalign .8
        yalign .05
    m "Anyway, just listen..."
    $ renpy.pause(2.0, hard=True)
    menu:
        "Stay a while and listen.":
            jump satie_listen
        "Move on to the next track.":
            jump chopin
label satie_listen:
    show screen sat_next
    show marta3d3_rain 1b 2a 3a noblush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta3d3_rain 1d 2b 3a blush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta2d3_rain 1b 2a 3b noblush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta2d3_rain 1a 2a 3a blush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta3d3_rain 1b 2a 3a noblush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta3d3_rain 1d 2b 3a blush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta2d3_rain 1b 2a 3b noblush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    show marta2d3_rain 1a 2a 3a blush regular1 as marta with dissolve:
        xalign .8
        yalign .05
    $ renpy.pause(4.0, hard=True)
    jump satie_listen
label chopin:
    hide screen sat_next
    scene melody with fade
    play music "sound/chopin.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(3.0, hard=True)
    show melody3
    $ renpy.pause(2.0, hard=True)
    show nana1d3_rain 1a 2c 3c blush regular1 as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(.1, hard=True)
    show nana1d3_rain 1e 2c 3c blush regular1 as nana:
        xalign .8
        yalign -.1
        linear .2 yalign -.05
        linear .2 yalign -.1
    n "Chopin!!!"
    show nana1d3_rain 1e 2c 3c blush regular1 as nana:
        xalign .8
        yalign -.1
        linear .2 yalign -.05
        linear .2 yalign -.1
    n "It's Chopin!!!"
    show nana3d3_rain 1b 2a 3a as nana with dissolve:
        xalign .8
        yalign -.1
    n "Ermy, you're better than I thought!"
    show nana1d3_rain 1d 2a 3b regular2 as nana with dissolve:
        xalign .8
        yalign -.1
    n "It's his \"Op. 9, No. 1 in B flat minor\"."
    show nana1d3_rain 1d 2a 3a regular1 as nana with dissolve:
        xalign .8
        yalign -.1
    n "It's a real masterpiece!"
    show nana3d3_rain 1c 2a 3a as nana with dissolve:
        xalign .8
        yalign -.1
    n "Frederick Chopin was a Polish composer born in 1810."
    show nana1d3_rain 1e 2a 3d regular1 as nana with dissolve:
        xalign .8
        yalign -.1
    n "Yes, the same as Schumann! What a year... By the way, Schumann admired Chopin."
    show nana3d3_rain 1c 2b 3a as nana with dissolve:
        xalign .8
        yalign -.1
    n "Coincidentally, Chopin also died really early, at the age of 39."
    show nana3d3_rain 1d 2a 3b as nana with dissolve:
        xalign .8
        yalign -.1
    n "He settled in Paris at the age of 21. I wish I lived there back then!"
    show nana1d3_rain 1d 2c 3a regular2 as nana with dissolve:
        xalign .8
        yalign -.1
    n "Chopin supported himself by giving piano lessons, aside from composing."
    show nana1d3_rain 1e 2c 3c regular1 blush as nana with dissolve:
        xalign .8
        yalign -.1
    n "I'd trade week worth of my lunch money for just one lesson of his!"
    show nana3d3_rain 1d 2b 3d blush as nana with dissolve:
        xalign .8
        yalign -.1
    n "Alright, maybe a week is too much... Whatever, just listen."
    show nana3d3_rain 1g 2b 3d blush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(2.0, hard=True)
    menu:
        "Stay a while and listen.":
            jump chopin_listen
        "Move on.":
            jump ermy_piano_end
label chopin_listen:
    show screen cpn_next
    $ renpy.pause(2.0, hard=True)
    show nana3d3_rain 1g 2b 3d blush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana3d3_rain 1b 2a 3a noblush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana1d3_rain 1g 2a 3a regular2 noblush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana1d3_rain 1g 2a 3d regular2 blush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana3d3_rain 1g 2b 3d blush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana3d3_rain 1b 2a 3a noblush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana1d3_rain 1g 2a 3a regular2 noblush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(4.0, hard=True)
    show nana1d3_rain 1g 2a 3d regular2 blush as nana with dissolve:
        xalign .8
        yalign -.1
    $ renpy.pause(2.0, hard=True)
    jump chopin_listen
label ermy_piano_end:
    hide screen cpn_next
    scene black with fade
    stop rain fadeout 2
    $ renpy.pause(2.0, hard=True)
    play music "music/classes_day3.ogg" fadeout 2 fadein 2
    scene music_room with dissolve
    "The rain stopped, and it's getting sunny now."
    show teya2 1b 2a 3d regularhand1 blush at u11 as teya
    t "That was magnificient, Ermy! Thank you so much!"
    show teya2 1c 2a 3a regularhand3 noblush at u11 as teya with dissolve
    t "By the way, [player_name], you didn't say a word... anything wrong?"
    show teya2 1c 2a 3a regularhand3 noblush at d21 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d21 as teya
    show sima2 1d 2a 3b regular1 at u22 as sima
    with dissolve
    s "To compensate for this, you're now obliged to play us something!"
    show teya2 1a 2a 3a regularhand3 at d31 as teya
    show sima2 1d 2a 3b regular1 at d33 as sima
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d31 as teya
    show sima2 1a 2a 3a regular2 at d33 as sima
    show marta2 1e 2a 3a regular2 at u32 as marta
    m "Yeah, [player_name], you do this now!"
    show teya2 1a 2a 3a regularhand3 at d41 as teya
    show sima2 1a 2a 3a regular2 at d44 as sima
    show marta2 1e 2a 3a regular2 at d42 as marta
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d41 as teya
    show marta2 1g 2a 3a regular1 at d42 as marta
    show nana1 1e 2c 3a regular1 at u43 as nana
    show sima2 1a 2a 3a regular2 at d44 as sima
    n "Yes, yes! I too want to hear him playing!"
    show nana1 1e 2c 3a regular1 at d43 as nana
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand4 at d41 as teya
    show sima2 1a 2b 3a regular2 at d44 as sima
    show nana1 1a 2b 3a regular2 at d43 as nana
    show marta2 1a 2b 3a regular1 at d42 as marta
    with dissolve
    p "Hold on, hold on, I don't know how to play the piano..."
    show sima2 1a 2b 3a regular2 at u44 as sima
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand4 at d41 as teya
    show nana1 1a 2b 3a regular2 at d43 as nana
    show marta2 1a 2b 3a regular1 at d42 as marta
    show sima2 1d 2a 3a regular2 at u44 as sima
    s "I've heard that music is about improvisation."
    show sima2 1d 2a 3a regular2 at d44 as sima
    show teya2 1a 2a 3a regularhand4 at u41 as teya
    $ renpy.pause(.001, hard=True)
    show sima2 1e 2a 3a regular2 at d44 as sima
    show marta2 1g 2c 3a at d42 as marta
    show nana1 1g 2a 3a regular2 at d43 as nana
    show teya2 1e 2c 3d regularhand1 at u41 as teya
    with dissolve
    t "My, sounds like an interesting exercise!"
    show teya2 1e 2a 3b regularhand2 at u41 as teya with dissolve
    t "Everyone, why don't you tell [player_name] what you enjoy in music?"
    show teya2 1e 2a 3b regularhand2 at d41 as teya
    show marta2 1g 2c 3a at u42 as marta
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d41 as teya
    show marta2 1c 2c 3a at u42 as marta
    with dissolve
    m "Like, broadly speaking?"
    show teya2 1a 2a 3a regularhand3 at u41 as teya
    show marta2 1c 2c 3a at d42 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a at d42 as marta
    show teya2 1e 2c 3a regularhand2 at u41 as teya
    with dissolve
    t "Exactly. Based on this information, he will actually improvise."
    show teya3 1a 2a 3b at u41 as teya with dissolve
    t "Go easy on him, okay?"
    show teya3 1a 2a 3b at d41 as teya
    $ renpy.pause(.001, hard=True)
    show teya1 1a 2a 3a at d41 as teya
    show sima2 1a 2a 3a regular2 at d44 as sima
    with dissolve
    p "Hey, I'm afraid it won't help much. Once again, I can't play!"
    show teya1 1a 2a 3a at u41 as teya
    $ renpy.pause(.001, hard=True)
    show teya1 1c 2a 3a at u41 as teya with dissolve
    t "Well then, [player_name], use the first octave only!"
    show teya1 1c 2a 3b at u41 as teya with dissolve
    t "Trust me, even pressing just one key at a time will do the trick."
    show teya2 1e 2a 3a regularhand2 at u41 as teya with dissolve
    t "I'm sure we'll like your melody."
    show teya2 1e 2a 3a regularhand2 at d41 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d41 as teya with dissolve
    p "Where's the first octave?"
    show teya2 1a 2a 3a regularhand3 at u41 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2a 3b regularhand2 at u41 as teya with dissolve
    t "Ermy's going to show you. Right, Ermy, my dear?"
    show teya2 1e 2a 3a regularhand2 at u41 as teya with dissolve
    t "Alright, class, time to tell [player_name] what kind of music you like!"
    hide teya with dissolve
    show marta2 1c 2a 3a at d31 as marta
    show nana1 1g 2a 3a regular2 at d32 as nana
    show sima2 1e 2a 3a regular2 at d33 as sima
    $ renpy.pause(.25, hard=True)
    show nana1 1g 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3a regular1 at u32 as nana with dissolve
    n "I'll go first!"
    show nana1 1e 2c 3a regular1 at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular1 at d32 as nana with dissolve
    p "What do you like, Nana?"
    show nana1 1a 2a 3a regular1 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2d 3a regular2 at u32 as nana with dissolve
    n "Let me think.. hm, you know what? I like seven different genres!"
    show nana1 1e 2d 3a blush regular2 at u32 as nana with dissolve
    n "If I were to pick the first one..."
    show nana1 1e 2c 3c noblush regular1 at u32 as nana with dissolve
    n "I like progressive rock, where a five-string guitar often meets classical instruments."
    show nana1 1c 2c 3a regular1 at u32 as nana with dissolve
    n "My three favorite bands are \"Yes\", \"King Crimson\" and \"Wishbone Ash\"."
    show nana3 1e 2a 3a at u32 as nana with dissolve
    n "The name of the genre is often shortened to just four letters, \"prog\"."
    show nana3 1e 2a 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3a at d32 as nana with dissolve
    "How am I supposed to handle this information?"
    show marta2 1c 2a 3a at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 at u31 as marta with dissolve
    m "Well, as Nana already mentioned rock, I'll go ahead and jump to my second favorite genre."
    show marta3 1g 2a 3a regular1 at u31 as marta with dissolve
    m "I began to enjoy hip-hop music about two years ago."
    show marta2 1e 2a 3a regular2 at u31 as marta with dissolve
    m "First and foremost, it's all about the beat, the rhythm."
    show marta2 1d 2a 3b regular1 at u31 as marta with dissolve
    m "I always prefer alternative or abstract hip-hop to the mainstream one."
    show marta3 1g 2a 3a regular1 at u31 as marta with dissolve
    m "MF Doom, Madlib, \"A Tribe Called Quest\", \"The Pharcyde\", \"Wu-Tang Clan\", it's my top five."
    show marta3 1g 2a 3a regular1 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d31 as marta with dissolve
    "This is no better..."
    show sima2 1e 2a 3a regular2 at u33 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1e 2a 3b regular1 at u33 as sima with dissolve
    s "Classical music is my love at the first sight."
    show sima2 1c 2a 3a regular1 at u33 as sima with dissolve
    s "Debussy, Borodin and Schumann are my three favorite composers."
    show sima2 1e 2a 3a regular2 at u33 as sima with dissolve
    s "Do you know which genre comes second in terms of complexity?"
    show sima3a 1d 2c 3b at u33 as sima with dissolve
    s "Two ways to name it, jungle and d'n'b."
    show sima3a 1c 2a 3d at u33 as sima with dissolve
    s "Don't believe me? Listen to \"Source Direct\", Dub One or B-Key, these three will blow your mind."
    show sima3a 1c 2a 3d at d33 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3d at d33 as sima with dissolve
    "I feel a clear lack of sanity in this room."
    hide nana
    hide marta
    hide sima
    with dissolve
    show teya1 1c 2a 3a at u11 as teya with dissolve
    t "It's time, [player_name]! Ermy, don't forget to help him out."
    hide teya with dissolve
    jump pianogame
label piano_win_nana:
    scene music_room with fade
    show nana1 1d 2c 3a regular2 blush at u11 as nana
    $achievement.grant("mensaclub")
    init:
        $achievement.register("mensaclub")
        $achievement.sync()
    $achievement.sync()
    n "I like it! Sounds fun!"
    jump piano_end
label piano_win_sima:
    scene music_room with fade
    show sima3b 1e 2a 3a blush at u11 as sima
    $achievement.grant("mensaclub")
    init:
        $achievement.register("mensaclub")
        $achievement.sync()
    $achievement.sync()
    s "I like it!"
    jump piano_end
label piano_win_marta:
    scene music_room with fade
    show marta3 1e 2a 3a blush at u11 as marta
    $achievement.grant("mensaclub")
    init:
        $achievement.register("mensaclub")
        $achievement.sync()
    $achievement.sync()
    m "Hey, that's pretty cool!"
    jump piano_end
label piano_fail:
    scene music_room with fade
    show ermy1 1b 2a 3b  pose1 at u11 as ermy
    e "Sounds great!"
    jump piano_end
label piano_end:
    play music "music/classes_day3.ogg" fadeout 1.5 fadein 1.5
    hide nana
    hide marta
    hide sima
    hide ermy
    with dissolve
    show teya2 1a 2a 3a regularhand4 at u11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1b 2a 3a regularhand2 at u11 as teya with dissolve
    t "Very well, how about we end our class here, on a major note, so to speak?"
    show teya2 1e 2a 3a regularhand3 at u11 as teya with dissolve
    t "I need to take something from the staffroom right now..."
    show teya2 1d 2a 3a regularhand3 at u11 as teya with dissolve
    t "You guys wait here."
    show teya3 1c 2a 3b at u11 as teya with dissolve
    t "As it's far from break time, please don't be too loud."
    hide teya with dissolve
    $ renpy.pause(0.2, hard=True)
    show marta2 1a 2a 3a regular1 at u11 as marta
    show marta2 1d 2a 3a regular1 at u11 as marta with dissolve
    m "Well, let's start packing up."
    show marta2 1d 2a 3a regular1 at d31 as marta
    $ renpy.pause(0.25, hard=True)
    show ermy1 1a 2d 3a pose2 at u33 as ermy
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3a regular1 at d31 as marta
    show ermy1 1h 2d 3a pose2 at u33 as ermy
    e "You guys..."
    show ermy1 1h 2d 3c pose2 at u33 as ermy
    with dissolve
    e "You didn't even ask {i}me{/i} about my favorite music!"
    show ermy1 1h 2d 3c pose2 at d33 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1 1f 2d 3a pose2 at d33 as ermy
    show marta2 1f 2a 3a regular1 at d31 as marta
    show sima1 1d 2d 3d at u32 as sima
    with dissolve
    s "But I do remember you said that everything goes if it has the right mood."
    show sima1 1d 2d 3d at d32 as sima
    show ermy1 1f 2d 3a pose2 at u33 as ermy
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3d at d32 as sima
    show ermy1 1h 2d 3a pose1 blush at u33 as ermy
    with dissolve
    e "Yeah, true that, but..."
    show ermy1 1d 2c 3a pose2 blush at u33 as ermy
    show sima1 1a 2a 3a at d32 as sima
    show marta2 1a 2a 3a regular1 at d31 as marta
    with dissolve
    e "One exception to this rule is \"The Smiths\"!"
    show ermy1 1d 2c 3a pose1 blush at u33 as ermy with dissolve
    e "I really like them."
    show ermy1 1e 2c 3a pose2 blush at d44 as ermy
    show sima1 1a 2a 3a at d43 as sima
    show marta2 1a 2a 3a regular1 at d41 as marta
    $ renpy.pause(.2, hard=True)
    show nana1 1a 2a 3d regular2 at u42 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2a 3d regular2 at u42 as nana with dissolve
    n "Who doesn't?"
    show nana1 1e 2a 3d regular2 at d42 as nana
    show marta2 1a 2a 3a regular1 at u41 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3d regular2 at d42 as nana
    show marta2 1b 2a 3a regular2 at u41 as marta
    with dissolve
    m "Try \"Igginbottom\", they played somewhat similar music before it became mainstream."
    show marta2 1b 2a 3a regular2 at d41 as marta
    show ermy1 1e 2c 3a pose2 blush at u44 as ermy
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d41 as marta
    show ermy1 1b 2c 3c pose2 blush at u44 as ermy
    with dissolve
    e "I will!"
    show ermy1 1b 2a 3a pose1 noblush at u44 as ermy with dissolve
    e "By the way, we only discussed music today, but..."
    show ermy1 1c 2a 3a pose2 noblush at u44 as ermy with dissolve
    e "Movies are equally important!"
    show ermy1 1c 2a 3a pose2 noblush at d44 as ermy
    show sima1 1a 2a 3a at u43 as sima
    $ renpy.pause(.001, hard=True)
    show ermy1 1g 2a 3a pose2 noblush at d44 as ermy
    show sima2 1d 2a 3b regular1 at u43 as sima
    show nana1 1a 2a 3a regular2 at d42 as nana
    with dissolve
    s "I enjoy \"The Night of the Hunter\", \"It's a Wonderful Life\" and \"Paper Moon\"."
    show sima2 1d 2a 3b regular1 at d43 as sima
    show nana1 1a 2a 3a regular2 at u42 as nana
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d43 as sima
    show nana1 1e 2a 3d regular2 at u42 as nana
    show ermy1 1a 2a 3a pose2 at d44 as ermy
    with dissolve
    n "I bet these movies are way too old!"
    show sima2 1a 2a 3a regular2 at u43 as sima
    show nana1 1e 2a 3d regular2 at d42 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3d regular2 at d42 as nana
    show sima1 1d 2d 3d at u43 as sima
    show ermy1 1f 2a 3d pose2 at d44 as ermy
    with dissolve
    s "Time only makes them better, Nana. They age like wine."
    show sima1 1d 2d 3d at d43 as sima
    show marta2 1a 2a 3a regular1 at u41 as marta
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3d at d43 as sima
    show marta2 1b 2a 3b regular2 at u41 as marta
    show ermy1 1f 2b 3d pose2 at d44 as ermy
    with dissolve
    m "I wish we all did."
    hide ermy with dissolve
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3b regular2 at d31 as marta
    show nana1 1a 2a 3d regular2 at u32 as nana
    show sima1 1a 2d 3d at d33 as sima
    $ renpy.pause(.3, hard=True)
    show sima1 1a 2b 3a at d33 as sima
    show marta2 1f 2a 3a regular1 at d31 as marta
    show nana1 1c 2a 3d regular2 at u32 as nana
    with dissolve
    n "Pff."

    call before_expo from _call_before_expo

    hide sima
    hide marta
    hide nana
    with dissolve
    show teya2 1a 2a 3a regularhand3 at u11 as teya
    $ renpy.pause(.3, hard=True)
    show teya2 1e 2a 3a regularhand3 at u11 as teya with dissolve
    t "Class, let's go. Once again, please don't be loud."
    scene hallway1_en with fade
    show teya2 1c 2c 3a regularhand3 at u11 as teya with dissolve
    t "Where's Ermy?"
    show teya2 1a 2a 3a regularhand3 at d22 as teya
    $ renpy.pause(.2, hard=True)
    show nana1 1e 2a 3d regular2 at u21 as nana
    with dissolve
    n "He's still packing up."
    show nana1 1e 2a 3d regular2 at d21 as nana
    show teya2 1a 2a 3a regularhand3 at u22 as teya
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3d regular2 at d21 as nana
    show teya1 1c 2a 3b at u22 as teya
    with dissolve
    t "Just a quick reminder before we go..."
    show nana1 1a 2c 3c regular2 at d21 as nana
    show teya2 1e 2a 3a regularhand2 at u22 as teya
    with dissolve
    t "Girls, you're in charge of the handouts."
    show nana1 1a 2b 3c regular2 blush at d21 as nana
    show teya2 1e 2a 3b regularhand2 at u22 as teya
    with dissolve
    t "I hope they're ready... We don't want to disappoint our guests, right?"
    show nana2 1a 2a 3a at d21 as nana
    show teya1 1e 2a 3d at u22 as teya
    with dissolve
    t "Right, Nana?"
    show nana2 1f 2b 3d blush at d21 as nana
    show teya1 1e 2c 3a at u22 as teya
    with dissolve
    t "Are {i}you{/i} ready? Might I ask where are your handouts?"
    show nana2 1f 2b 3d blush at u21 as nana
    show teya1 1e 2c 3a at d22 as teya
    $ renpy.pause(.001, hard=True)
    show teya1 1a 2c 3a at d22 as teya
    show nana2 1d 2b 3b at u21 as nana
    with dissolve
    n "I... well, I forgot to prepare mine."
    show teya1 1a 2c 3a at u22 as teya
    show nana2 1d 2b 3b at d21 as nana
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2b 3b at d21 as nana
    show teya1 1e 2d 3c at u22 as teya
    with dissolve
    t "\"Mine\"? I'd say you've totally bombed it."
    show nana2 1f 2b 3b blush at d21 as nana
    show teya1 1c 2a 3b at u22 as teya
    with dissolve
    t "Consider yourself lucky that I don't give grades today."
    show teya2 1e 2a 3a regularhand4 at u22 as teya
    show nana2 1f 2b 3a blush at d21 as nana
    with dissolve
    t "By the way, I also participate! My booth is called \"Grown-up life horrors\"."
    show teya2 1b 2b 3b regularhand4 at u22 as teya
    show nana1 1g 2a 3a noblush regular2 at d21 as nana
    with dissolve
    t "It's hors concours, of course. As you know, we promote diversity..."
    show teya2 1b 2c 3a regularhand2 at u22 as teya with dissolve
    t "Inflexible generalities are diversity's worst enemy. Come and laugh at it with me!"
    scene black with fade
    "As the girls are still setting up, I decide to go check on Teya's booth."
    play music "music/career_day.ogg" fadeout 1.5 fadein 1.5
    scene teya_booth1
    show teya2 1a 2d 3a regularhand3 at u33 as teya
    with fade
    "Teya has two displays set up in her space. The first one resembles a corporate world, I guess."
    show teya2 1b 2d 3a regularhand3 at u33 as teya with dissolve
    t "Welcome, [player_name]!"
    jump teya_booth
label teya_booth:
    show teya1 1e 2d 3a at u33 as teya with dissolve
    t "So! Let me walk you through a mock interview for a prestigious job."
    show teya1 1a 2d 3a at u33 as teya with dissolve
    p "What kind of a job is this?"
    show teya1 1e 2b 3b at u33 as teya with dissolve
    t "Um... Doesn't matter, [player_name], let's just say it's a Fortune 500 company."
    show teya1 1a 2b 3b at u33 as teya with dissolve
    t "Fortune 500 is the world's 500 largest companies."
    show teya2 1b 2d 3a regularhand2 at u33 as teya with dissolve
    t "Every fresh graduate dreams to have his first job at a company like this!"
    p "They say now it's more trendy to join startups..."
    show teya3 1b 2a 3a at u33 as teya with dissolve
    t "They say a lot until it's time to pay off education loans."
    show teya3 1a 2a 3a at u33 as teya with dissolve
    p "Well, what're you going to ask me about?"
    show teya2 1e 2d 3d regularhand2 at u33 as teya with dissolve
    t "Not so fast, [player_name]! First, prove yourself worthy of reaching the interview stage."
    show teya1 1e 2d 3a at u33 as teya with dissolve
    t "Let me have a look at your curriculum vitae as well as cover letter."
    show teya1 1a 2d 3a at u33 as teya with dissolve
    p "Uh, what? What are you talking about?"
    show teya1 1e 2d 3b at u33 as teya with dissolve
    t "Next, please!"
    show teya1 1a 2d 3b at u33 as teya with dissolve
    p "..."
    show teya2 1b 2a 3a regularhand3 at u33 as teya with dissolve
    t "Alright, I'm just kidding. Ready for the interview?"
    show teya2 1a 2a 3a regularhand4 at u33 as teya with dissolve
    p "I'm ready."
    show teya2 1e 2d 3a regularhand2 at u33 as teya with dissolve
    t "For starters, let me ask you one simple question."
    show teya2 1c 2a 3a regularhand4 at u33 as teya with dissolve
    t "Where do you see yourself in 10 years?"
    show teya2 1a 2d 3d regularhand3 at u33 as teya with dissolve
    p "In 10 years? Well, I don't know... it's impossible to predict, I guess."
    show teya2 1a 2c 3c regularhand3 at u33 as teya with dissolve
    p "Why 10 though, not 7 or 12?"
    show teya1 1c 2b 3b at u33 as teya with dissolve
    t "Sorry, but we're looking for candidates with a clear long-term vision of their goals."
    show teya1 1e 2b 3a at u33 as teya with dissolve
    t "Tell me about the time you demonstrated yourself as a valuable team-player."
    show teya1 1b 2d 3a at u33 as teya with dissolve
    p "..."
    show teya1 1e 2d 3a at u33 as teya with dissolve
    t "Also, what are your development areas?"
    show teya1 1b 2d 3a at u33 as teya with dissolve
    p "Uh, I need to develop everything, I think. I'm still in school, after all."
    show teya1 1c 2b 3b at u33 as teya with dissolve
    t "Thank you for your time and interest in our company. We'll call you back!"
    show teya1 1a 2a 3a at u33 as teya with dissolve
    p "This display looks a bit strange, by the way."
    show teya3 1d 2b 3b at u33 as teya with dissolve
    t "Production department messed up."
    show teya2 1d 2a 3a regularhand3 at u33 as teya with dissolve
    t "[player_name], let's move on, maybe it's not your piece of the cake."
    show teya_booth2 behind teya with dissolve
    show teya2 1a 2a 3a regularhand4 at u11 as teya
    "Teya directs my attention to another display just next to her."
    show teya2 1d 2a 3d regularhand1 at u11 as teya with dissolve
    t "You know, on a second thought, it's not always about paychecks and big names."
    show teya2 1e 2c 3a regularhand2 at u11 as teya with dissolve
    t "Take this awesome startup, for instance."
    show teya2 1c 2a 3a regularhand4 at u11 as teya with dissolve
    t "By the way, feel free to take a bite..."
    show teya2 1e 2a 3b regularhand2 at u11 as teya with dissolve
    t "I have some fresh-baked gluten-free cookies with me!"
    show teya1 1e 2c 3b at u11 as teya with dissolve
    t "Fresh like a hip coworking place at Bay Area."
    show teya1 1b 2c 3a at u11 as teya with dissolve
    p "Where's the application form and all?"
    show teya2 1e 2c 3a regularhand4 at u11 as teya with dissolve
    t "What're you talking about?"
    show teya2 1c 2a 3a regularhand2 at u11 as teya with dissolve
    t "Startups look for people who can think outside the box."
    show teya2 1b 2a 3d regularhand1 blush at u11 as teya with dissolve
    t "Just tell me why you want to join the family."
    show teya2 1a 2a 3a regularhand1 at u11 as teya with dissolve
    p "Family?"
    show teya2 1b 2c 3c regularhand2 at u11 as teya with dissolve
    t "It's all about the mindset, [player_name]."
    show teya2 1e 2a 3a regularhand4 noblush at u11 as teya with dissolve
    t "At the startup scene, people often see themselves as family members rather than colleagues."
    show teya2 1a 2a 3a regularhand4 at u11 as teya with dissolve
    p "What's the startup portrayed here about?"
    show teya3 1d 2b 3b at u11 as teya with dissolve
    t "Oh, it's irrelevant! All that matters is that they are sure to {i}disrupt{/i} the market."
    show teya3 1b 2c 3c blush at u11 as teya with dissolve
    t "But if you insist... So, it's a mobile app that connects taxi drivers with passengers."
    show teya3 1c 2a 3b at u11 as teya with dissolve
    t "Innovative, huh?"
    show teya1 1a 2d 3a noblush at u11 as teya with dissolve
    p "Wait, but isn't it the same as any other taxi app on the market?"
    show teya1 1c 2c 3b at u11 as teya with dissolve
    t "Ha! Here, the {i}mission{/i} is different."
    show teya1 1e 2c 3b at u11 as teya with dissolve
    t "The mission is to connect people! We encourage our users to learn more about each other during a ride..."
    show teya2 1e 2c 3c regularhand2 at u11 as teya with dissolve
    t "Nothing helps to build diversity and inclusion better than a taxi ride."
    show teya2 1b 2a 3b regularhand1 blush at u11 as teya with dissolve
    t "We need friendship, friendship is magic."
    show teya2 1a 2c 3c regularhand4 at u11 as teya with dissolve
    p "I see there's even a stock chart."
    show teya3 1e 2c 3c at u11 as teya with dissolve
    t "Yes, as you can see, the price is about to skyrocket! Just look at the forecast."
    show teya3 1b 2c 3c noblush at u11 as teya with dissolve
    p "Seems legitimate!"
    show teya2 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "Was it fun, [player_name]?"
    show teya2 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "I have mixed feelings..."
    show teya2 1b 2a 3b regularhand1 blush at u11 as teya with dissolve
    t "Hence the \"Grown-up Life Horrors\"!"
    show teya2 1c 2a 3a regularhand2 noblush at u11 as teya with dissolve
    t "A grown-up life is all about mixed feelings."
    show teya2 1e 2a 3a regularhand3 noblush at u11 as teya with dissolve
    t "Actually, the purpose of my booth is to show you how stereotypes work."
    show teya2 1c 2a 3c regularhand4 at u11 as teya with dissolve
    t "In real life, both corporate and startup worlds have a lot to offer."
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "We live in time where you can do whatever you want..."
    show teya2 1c 2c 3a regularhand1 at u11 as teya with dissolve
    t "Moreover, you can even get paid for it!"
    show teya1 1c 2a 3b at u11 as teya with dissolve
    t "Anyway, [player_name]..."
    show teya1 1c 2a 3a at u11 as teya with dissolve
    t "Who're you going to help with the handouts?"
    show teya1 1a 2a 3a at u11 as teya with dissolve
    menu:
        "Nana":
            jump nanas_booth
        "Sima":
            jump simas_booth
        "Marta":
            jump martas_booth
        "Everyone":
            jump everyones_booth
label nanas_booth:
    if bhn_p == 2:
        $ cn_p = 3
        scene black with fade
        "A promise is a promise, so I helped Nana."
        call flyers_nana from _call_flyers_nana
        scene black with fade
        "We returned to our class after that."
        jump after_expo
    else:
        scene black with fade
        "I decided to change my mind and help Nana."
        "She was really suprised..."
        call flyers_nana from _call_flyers_nana_1
        scene black with fade
        "We returned to our class after that."
        jump after_expo
label martas_booth:
    if bhm_p == 2:
        $ cm_p = 3
        scene black with fade
        "A promise is a promise, so I helped Marta."
        call flyers_marta from _call_flyers_marta
        scene black with fade
        "We returned to our class after that."
        jump after_expo
    else:
        scene black with fade
        "I decided to change my mind and help Marta."
        "She was really suprised..."
        call flyers_marta from _call_flyers_marta_1
        scene black with fade
        "We returned to our class after that."
        jump after_expo
label simas_booth:
    if bhs_p == 2:
        $ cs_p = 3
        scene black with fade
        "A promise is a promise, so I helped Sima."
        call flyers_sima from _call_flyers_sima
        scene black with fade
        "We returned to our class after that."
        jump after_expo
    else:
        scene black with fade
        "I decided to change my mind and help Sima."
        "She was really suprised..."
        call flyers_sima from _call_flyers_sima_1
        scene black with fade
        "We returned to our class after that."
        jump after_expo
label everyones_booth:
    if bhe_p == 1:
        scene black with fade
        "A promise is a promise, so I tried to help everyone."
        "It didn't work that well, to be honest, but..."
        jump after_expo
    else:
        scene black with fade
        "I decided to change my mind and help everyone."
        "Everyone disliked that."
        "We returned to our class after the expo was over."
        jump after_expo
label after_expo:
    scene music_room
    show nana1 1a 2a 3a regular2 at d43 as nana
    show teya2 1a 2a 3a regularhand4 at d44 as teya
    show sima2 1a 2a 3a regular2 at d41 as sima
    show marta2 1a 2a 3a regular1 at d42 as marta
    with fade
    show nana1 1a 2a 3a regular2 at u43 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1d 2a 3a regular1 at u43 as nana with dissolve
    n "I think we did well! Why don't we celebrate?"
    show nana1 1e 2a 3c regular1 at u43 as nana with dissolve
    n "Let's go to \"Doorsia\"!"
    show nana1 1e 2a 3c regular1 at d43 as nana
    show marta2 1a 2a 3a regular1 at u42 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3d regular2 at d43 as nana
    show marta2 1e 2b 3a blush regular1 at u42 as marta
    with dissolve
    m "I'm afraid it's way too expensive for me..."
    show nana1 1a 2a 3d regular2 at u43 as nana
    show marta2 1e 2b 3a blush regular1 at d42 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2b 3a blush regular1 at d42 as marta
    show nana3 1d 2a 3d at u43 as nana
    with dissolve
    n "Marta, I have this voucher, remember?"
    show marta2 1a 2b 3a blush regular1 at u42 as marta
    show nana3 1d 2a 3d at d43 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3d at d43 as nana
    show marta2 1b 2a 3a noblush regular1 at u42 as marta
    with dissolve
    m "Oh, that's right, I completely forgot about it... Cool, I want to go!"
    show marta2 1b 2a 3a noblush regular1 at d42 as marta
    show sima2 1a 2a 3a regular2 at u41 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d42 as marta
    show sima2 1e 2a 3b regular1 at u41 as sima
    with dissolve
    s "I'd be happy to join you!"
    show marta2 1a 2a 3a regular1 at u42 as marta
    show sima2 1e 2a 3b regular1 at d41 as sima
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular1 at d41 as sima
    show marta2 1e 2a 3a regular2 at u42 as marta
    with dissolve
    m "Wait! The voucher is valid {i}for two{/i}, and there's five of us."
    show marta2 1e 2a 3a regular2 at d42 as marta
    show teya2 1a 2a 3a regularhand4 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d42 as marta
    show teya1 1c 2a 3b at u44 as teya
    with dissolve
    t "The rest is on the house."
    show teya1 1c 2a 3b at d44 as teya
    show nana3 1a 2a 3d at u43 as nana
    $ renpy.pause(.001, hard=True)
    show teya1 1b 2a 3a at d44 as teya
    show nana1 1b 2a 3a regular1 at u43 as nana
    with dissolve
    n "Yay!"
    show nana1 1b 2a 3a regular1 at d43 as nana
    show sima2 1a 2a 3a regular1 at u41 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular1 at d43 as nana
    show sima2 1c 2a 3a regular2 at u41 as sima
    with dissolve
    s "This is very generous of yours!"
    show sima2 1c 2a 3a regular2 at d41 as sima
    show marta2 1a 2a 3a regular1 at u42 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d41 as sima
    show marta3 1e 2a 3b regular1 at u42 as marta
    with dissolve
    m "You're the best!"
    show marta3 1e 2a 3b regular1 at d42 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1b 2a 3a regular1 at d42 as marta with dissolve
    p "Thank you so much!"
    show teya1 1b 2a 3a at u44 as teya
    $ renpy.pause(.001, hard=True)
    show teya1 1c 2a 3b at u44 as teya with dissolve
    t "The pleasure is all mine."
    show teya2 1e 2a 3a regularhand3 at u44 as teya with dissolve
    t "By the way, Ermy's still nowhere to be seen, huh..."
    show teya2 1d 2a 3b regularhand4 at u44 as teya with dissolve
    t "Well, I'll send him a text. Let's go!"
    play music "music/cafe_music.ogg" fadeout 1 fadein 1
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    scene cafe
    show marta2 1d 2c 3c regular1 blush at d41 as marta
    show nana1 1g 2a 3a regular2 blush at d42 as nana
    show sima2 1e 2a 3a regular2 at d43 as sima
    show teya2 1b 2a 3d regularhand1 at d44 as teya
    with fade
    show teya2 1b 2a 3d regularhand1 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2a 3a regularhand1 at u44 as teya with dissolve
    t "Everyone, order what you like."
    show black with fade
    "Whoa, everything is pricey here."
    show sima3a 1g 2a 3a at d43 as sima
    show marta3 1g 2a 3a at d41 as marta
    show nana2 1a 2a 3a at d42 as nana
    show teya2 1a 2a 3a regularhand4 at d44 as teya
    hide black with fade
    show nana2 1a 2a 3a at u42 as nana
    $ renpy.pause(.001, hard=True)
    show nana2 1d 2a 3a at u42 as nana with dissolve
    n "Say... we won't discuss school stuff, right? Right?"
    show nana2 1d 2a 3a at d42 as nana
    show teya2 1a 2a 3a regularhand4 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at d42 as nana
    show teya2 1e 2a 3b blush regularhand1 at u44 as teya
    with dissolve
    t "Do I look that boring? Feel free to talk about anything you want."
    show teya2 1e 2a 3b blush regularhand1 at d44 as teya
    show marta3 1g 2a 3a at u41 as marta
    $ renpy.pause(.001, hard=True)
    show teya2 1b 2a 3a noblush regularhand3 at d44 as teya
    show marta3 1e 2a 3a at u41 as marta
    with dissolve
    m "Why don't we talk about you then?"
    show teya2 1b 2a 3a noblush regularhand3 at u44 as teya
    show marta3 1e 2a 3a at d41 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a at d41 as marta
    show teya2 1e 2c 3c blush regularhand1 at u44 as teya
    with dissolve
    t "About {i}me{/i}? Do I look that interesting?"
    show teya2 1e 2c 3c blush regularhand1 at d44 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1d 2c 3c blush regularhand1 at d44 as teya with dissolve
    "She seems geniunly surprised."
    show sima3a 1g 2a 3a at u43 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2c 3d at u43 as sima with dissolve
    s "Well, we know little about you, so I second Marta's idea."
    show sima3a 1d 2c 3d at d43 as sima
    show marta3 1g 2a 3a at u41 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3d at d43 as sima
    show marta3 1e 2c 3b blush at u41 as marta
    with dissolve
    m "Yeah... Like, what do you love? What do you hate? Tell us!"
    show marta3 1e 2c 3b blush at d41 as marta
    show nana1 1g 2a 3a regular2 at u42 as nana
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a noblush at d41 as marta
    show nana1 1c 2c 3a regular1 at u42 as nana
    with dissolve
    n "Don't forget to mention your favorite food."
    show nana1 1c 2c 3a regular1 at d42 as nana
    show teya2 1d 2c 3c blush regularhand1 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at d42 as nana
    show teya2 1e 2b 3b regularhand2 at u44 as teya
    with dissolve
    t "Alright!"
    show teya2 1e 2a 3a regularhand4 at u44 as teya with dissolve
    t "I'm indifferent to food. The only thing that bothers me is staying in shape."
    show teya2 1e 2a 3a noblush regularhand3 at u44 as teya with dissolve
    t "And, believe it or not, I love and hate the same thing."
    show teya2 1e 2a 3a noblush regularhand3 at d44 as teya
    show marta3 1g 2a 3a noblush at u41 as marta
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a noblush regularhand3 at d44 as teya
    show marta2 1e 2a 3a regular2 at u41 as marta
    with dissolve
    m "Money?"
    show marta2 1e 2a 3a regular2 at d41 as marta
    show sima3a 1g 2a 3d at u43 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d41 as marta
    show sima3a 1d 2c 3a at u43 as sima
    with dissolve
    s "Knowledge?"
    show sima3a 1g 2a 3d at d43 as sima
    show nana1 1g 2a 3a regular2 at u42 as nana
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2c 3a at d43 as sima
    show nana1 1e 2a 3c regular1 at u42 as nana
    with dissolve
    n "People?"
    show nana1 1e 2a 3c regular1 at d42 as nana
    show teya2 1a 2a 3a noblush regularhand3 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d42 as nana
    show teya2 1e 2a 3a regularhand2 at u44 as teya
    with dissolve
    t "Not even close! I love and hate... time."
    show teya2 1e 2a 3a regularhand2 at d44 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand4 at d44 as teya with dissolve
    p "I'm curious to know why."
    show teya2 1a 2a 3a regularhand4 at u44 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1c 2a 3a regularhand2 at u44 as teya with dissolve
    t "Say, we're having great time now, and I fully enjoy it."
    show teya2 1d 2a 3b regularhand1 blush at u44 as teya with dissolve
    t "But... it can't stay like this forever, regardless of what I do."
    show teya2 1e 2a 3a regularhand2 noblush at u44 as teya with dissolve
    t "At the same time, a bad day seems endless. How is this fair?"
    show teya2 1c 2b 3a regularhand3 noblush at u44 as teya with dissolve
    t "Oh, and time is a mercyless judge when you're getting older."
    show teya2 1e 2a 3a regularhand4 at u44 as teya with dissolve
    t "Ironically enough, you only start to value time when it's too late."
    show teya2 1d 2a 3b regularhand4 at u44 as teya with dissolve
    t "You can love time, but time will never love you back."
    show teya2 1d 2a 3b regularhand4 at d44 as teya
    show sima3a 1a 2c 3a at u43 as sima
    $ renpy.pause(.001, hard=True)
    show teya2 1b 2a 3a regularhand4 at d44 as teya
    show sima1 1c 2b 3d at u43 as sima
    with dissolve
    s "I guess it would be nice to have all the time in the world..."
    show teya2 1b 2a 3a regularhand4 at u44 as teya
    show sima1 1c 2b 3d at d43 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3d at d43 as sima
    show teya2 1e 2a 3a regularhand2 at u44 as teya
    with dissolve
    t "I don't think so. It would devalue the sense of achievement."
    show teya1 1e 2a 3a at u44 as teya with dissolve
    t "\"It was well worth the time spent.\""
    show teya1 1d 2a 3a at u44 as teya with dissolve
    t "\"Only one year until I graduate and start living large.\""
    show teya1 1c 2a 3b at u44 as teya with dissolve
    t "Time forces you to do something."
    show teya1 1c 2a 3b at d44 as teya
    show nana1 1a 2a 3a regular2 at u42 as nana
    $ renpy.pause(.001, hard=True)
    show teya1 1b 2a 3a at d44 as teya
    show nana3 1c 2a 3d at u42 as nana
    with dissolve
    n "I don't feel like it, to be honest."
    show teya1 1b 2a 3a at u44 as teya
    show nana3 1c 2a 3d at d42 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2b 3d at d42 as nana
    show teya2 1d 2a 3b regularhand1 at u44 as teya with dissolve
    t "Simply because it's still early morning for you, Nana."
    show teya2 1d 2a 3b regularhand1 at d44 as teya
    show sima1 1a 2b 3d at u43 as sima
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3d regularhand3 at d44 as teya
    show sima3a 1c 2a 3d at u43 as sima
    with dissolve
    s "Don't you contradict yourself with what you said?"
    show teya2 1a 2a 3d regularhand3 at u44 as teya
    show sima3a 1c 2a 3d at d43 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3d at d43 as sima
    show teya2 1e 2a 3a regularhand2 at u44 as teya
    with dissolve
    t "Contradict, you say? My, a very suitable word indeed, Sima."
    show teya2 1c 2a 3a regularhand3 at u44 as teya with dissolve
    t "Time is contradictory. That's why I love and hate it in parallel."
    scene black with fade
    "Our waiter finally arrives... I think they should work faster at a place like this."
    "He certainly took his time."
    python:
        cm_tp  = cm_p
    python:
        cs_tp = cs_p
    python:
        cn_tp = cn_p

    if cs_tp > cm_tp:
        if cs_tp > cn_tp:
            scene cafe with fade
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump sima_invite
        elif cs_tp < cn_tp:
            scene cafe with fade
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump nana_invite
        else:
            jump ermy_invite
    elif cm_tp > cs_tp:
        if cm_tp > cn_tp:
            scene cafe with fade
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump marta_invite
        elif cm_tp < cn_tp:
            scene cafe with fade
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump nana_invite
        else:
            jump ermy_invite
    elif cm_tp == cs_tp:
        if cn_tp == 0:
            jump ermy_invite
        else:
            scene cafe with fade
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump nana_invite
    else:
        jump ermy_invite

label nana_invite:
    $ g_p_3 = 1
    show nana1close 1g 2a 3a regular2 at u11 as nana
    "The first one to come back is Nana."
    p "Hey there! Where are the others?"
    show nana1close 1d 2a 3a regular2 at u11 as nana with dissolve
    n "Being slow as always."
    show nana3close 1e 2a 3d at u11 as nana with dissolve
    n "Well, I don't mind, it's a good excuse to spend more time here."
    show nana3close 1c 2a 3b blush at u11 as nana with dissolve
    n "I never return to the same place twice, but I'm ready to make an exception!"
    show nana3close 1g 2a 3b blush at u11 as nana with dissolve
    p "I bet it's a trending date spot, perfect for making an impression..."
    show nana3close 1e 2c 3d noblush at u11 as nana with dissolve
    n "Maybe you're right, [player_name]..."
    show nana3close 1d 2c 3d blush at u11 as nana with dissolve
    n "But I can't be sure unless I see for myself."
    show nana3close 1b 2c 3d at u11 as nana with dissolve
    p "Hope you won't be stalking anyone."
    show nana1close 1c 2a 3a regular2 at u11 as nana with dissolve
    n "Anyone but {i}myself{/i}."
    show nana1close 1g 2a 3a regular2 at u11 as nana with dissolve
    "She's looking right at me."
    "Wait, maybe that means..."
    p "You want to return here... like, with someone?"
    show nana1close 1c 2c 3a regular2 at u11 as nana with dissolve
    n "Why not?"
    show nana1close 1g 2c 3a regular2 at u11 as nana with dissolve
    "Still staring."
    "I wonder what I should reply..."
    show nana3close 1b 2c 3a noblush at u11 as nana with dissolve
    n "You're the one paying, though!"
    show nana3close 1a 2c 3a noblush at u11 as nana with dissolve
    "What? I haven't even said anything!"
    show nana3close 1e 2a 3b at u11 as nana with dissolve
    n "\"I should be the one making the invitation!\""
    show nana3close 1d 2a 3d at u11 as nana with dissolve
    n "That's what you think, right?"
    show nana1close 1d 2a 3a regular2 at u11 as nana with dissolve
    n "Sorry, I hate waiting, it's too boring."
    show nana1close 1c 2a 3d regular2 at u11 as nana with dissolve
    n "From another side, it {i}actually{/i} feels weird unless you do it."
    show nana1close 1c 2a 3a blush regular2 at u11 as nana with dissolve
    n "So, do you want me to come along or not?"
    show nana1close 1e 2a 3a blush regular1 at u11 as nana with dissolve
    n "If you want to come here again, of course."
    show nana1close 1a 2a 3a blush regular1 at u11 as nana with dissolve
    "She acts indifferently, but I feel like it's all made up."
    "Nana must be very, very nervous right now."
    show nana1close 1b 2c 3a blush regular1 at u11 as nana with dissolve
    p "I do."
    show nana1close 1b 2a 3a blush regular2 at u11 as nana with dissolve
    "She says nothing, only smiles brightly."
    show nana1close 1a 2a 3a blush regular2 at u11 as nana with dissolve
    p "Let's go tomorrow?"
    show nana3close 1d 2a 3d noblush at u11 as nana with dissolve
    n "I'm not sure about tomorrow. Need to check my plans."
    show nana3close 1a 2c 3c blush at u11 as nana with dissolve
    p "Alright, next weekend also works if you're busy."
    n "..."
    show nana3close 1e 2c 3b at u11 as nana with dissolve
    n "On a second thought, I can reschedule something..."
    show nana3close 1a 2c 3b at u11 as nana with dissolve
    p "Huh?"
    show nana1close 1e 2c 3c regular2 at u11 as nana with dissolve
    n "At 2 p.m. tomorrow... We meet here!"
    show nana1close 1a 2c 3c regular2 at u11 as nana with dissolve
    p "Deal!"
    show nana1close 1g 2c 3c regular2 noblush at u11 as nana with dissolve
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump date_nana
    if new_game1_sima_set == 1:
        scene black with fade
        $ renpy.pause(1, hard=True)
        jump date_nana
    jump sweet_home_d3
label marta_invite:
    $ g_p_3 = 2
    show marta2close 1a 2a 3a regular1 at u11 as marta
    "The first one to come back is Marta."
    p "Welcome back! Where are the others?"
    show marta2close 1b 2a 3a regular1 at u11 as marta with dissolve
    m "Nana's too busy admiring Sima's hair."
    show marta2close 1b 2a 3a regular2 at u11 as marta with dissolve
    m "Pretty cool place, right?"
    show marta2close 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Yes, I enjoyed it."
    show marta3close 1e 2a 3a regular1 blush at u11 as marta with dissolve
    m "I wish I could return."
    show marta3close 1f 2c 3a regular1 at u11 as marta with dissolve
    p "Definitely. Shame it's so expensive."
    show marta3close 1f 2d 3a regular1 at u11 as marta with dissolve
    m "..."
    p "Hey, why are you looking at me like this?"
    show marta1close 1d 2d 3a blush at u11 as marta with dissolve
    m "Nevermind. What takes them so long? These girls..."
    show marta1close 1f 2d 3a at u11 as marta with dissolve
    "Marta's annoyed. Could it be she expected me to... No, no way."
    p "Hey, um..."
    show marta1close 1e 2d 3a at u11 as marta with dissolve
    m "What?"
    show marta1close 1f 2d 3a at u11 as marta with dissolve
    p "See, if we both want to return, why don't we do it together?"
    show marta2close 1e 2c 3a regular2 noblush at u11 as marta with dissolve
    m "Me? With you? It'd look like a date, you know!"
    show marta2close 1a 2c 3a regular2 noblush at u11 as marta with dissolve
    p "I know."
    show marta2close 1d 2d 3d regular1 noblush at u11 as marta with dissolve
    m "Sorry, no."
    "Rejected, point blank."
    show marta2close 1d 2c 3a regular1 blush at u11 as marta with dissolve
    m "Why couldn't you..."
    show marta2close 1d 2c 3c regular1 at u11 as marta with dissolve
    "She probably intended to say it to herself."
    p "Why couldn't I what?"
    show marta2close 1e 2c 3c regular1 at u11 as marta with dissolve
    m "Why couldn't you invite me before!!!"
    show marta2close 1f 2c 3c regular1 at u11 as marta with dissolve
    p "What? But you just flat out rejected me!"
    show marta3close 1c 2d 3c regular1 blush at u11 as marta with dissolve
    m "It's because I was ashamed!"
    show marta3close 1c 2d 3b regular1 at u11 as marta with dissolve
    m "I had to give you a hint that I wanted to return here!"
    show marta3close 1d 2d 3c regular1 at u11 as marta with dissolve
    m "So, in fact, it's like {i}I{/i} invited you along!"
    show marta3close 1f 2b 3a regular1 at u11 as marta with dissolve
    "God, what's going on in her head?"
    "However, that implies I have another try."
    p "Uh... Well, let's start all over again."
    show marta2close 1f 2d 3a regular1 at u11 as marta with dissolve
    p "Welcome back! Where are the others?"
    m "..."
    show marta2close 1e 2d 3a regular2 at u11 as marta with dissolve
    m "Nana's still checking out Sima's hair."
    show marta2close 1d 2d 3a regular2 at u11 as marta with dissolve
    p "And this is a pretty cool place!"
    show marta2close 1b 2d 3a regular2 at u11 as marta with dissolve
    m "No doubt. I'd return any time!"
    show marta2close 1f 2c 3c regular1 at u11 as marta with dissolve
    p "Me too! Shame it's so..."
    p "Sorry, just kidding."
    p "Let's return here together!"
    show marta2close 1d 2c 3c regular1 at u11 as marta with dissolve
    m "O-okay..."
    "She blushes a bit."
    p "Will tomorrow do?"
    show marta2close 1e 2c 3c regular1 at u11 as marta with dissolve
    m "Sure!"
    show marta2close 1d 2c 3c regular1 at u11 as marta with dissolve
    m "Oh!"
    p "What's wrong?"
    show marta1close 1d 2b 3a at u11 as marta with dissolve
    m "I agreed for tomorrow straight away. It's bad..."
    p "Fine with me."
    show marta2close 1e 2d 3a regular2 at u11 as marta with dissolve
    m "But I set the time! It's 2 p.m. sharp!"
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump date_marta
    if new_game1_marta_set == 1:
        scene black with fade
        $ renpy.pause(1, hard=True)
        jump date_marta
    jump sweet_home_d3
label sima_invite:
    $ g_p_3 = 3
    show sima2close 1a 2a 3a regular2 at u11 as sima
    "The first one to come back is Sima."
    p "Welcome back! Where are the others?"
    show sima2close 1d 2a 3a regular2 at u11 as sima with dissolve
    s "Still there. They told me to come first... I have no idea why."
    show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
    p "It's an awesome place, right?"
    show sima2close 1e 2c 3a regular2 at u11 as sima with dissolve
    s "It sure is. My second time here and it only gets better."
    show sima2close 1a 2c 3a regular2 at u11 as sima with dissolve
    p "Oh, so you've been here before..."
    show sima3aclose 1g 2a 3b at u11 as sima with dissolve
    s "I coudln't help it. Nana's voucher looked way too exciting."
    p "Why didn't you tell us?"
    show sima3aclose 1d 2a 3a at u11 as sima with dissolve
    s "Well, it's an expensive place, so I tried to be considerate."
    show sima3aclose 1a 2a 3a at u11 as sima with dissolve
    p "That's very nice of you."
    p "I want to return here, doubt I can afford myself a dinner though..."
    show sima3bclose 1d 2a 3b blush at u11 as sima with dissolve
    s "I'd rather have another one of their delicious cakes."
    show sima3bclose 1a 2a 3b blush at u11 as sima with dissolve
    p "Back then, did you go alone or with your family?"
    show sima3aclose 1d 2a 3d noblush at u11 as sima with dissolve
    s "Alone. My family's in another country, silly."
    show sima3aclose 1g 2a 3d at u11 as sima with dissolve
    p "Right, I'm being stupid."
    show sima3aclose 1c 2c 3d at u11 as sima with dissolve
    s "Is it just me or you want to tell me something?"
    show sima3aclose 1a 2c 3d at u11 as sima with dissolve
    p "Well... I don't know where to begin."
    show sima3aclose 1e 2a 3d at u11 as sima with dissolve
    s "Anywhere will do."
    show sima3aclose 1a 2a 3d at u11 as sima with dissolve
    p "So, I'd really like to return here, but I don't want to go alone."
    show sima1close 1d 2a 3d at u11 as sima with dissolve
    s "Why don't you take Ermy? The guy seems a bit lonely."
    show sima1close 1a 2a 3d at u11 as sima with dissolve
    "Oh my. This sounds like a polite rejection."
    p "I probably should..."
    show sima1close 1e 2c 3a at u11 as sima with dissolve
    s "That's not what you expected of me to say."
    show sima1close 1c 2a 3b at u11 as sima with dissolve
    s "It means you {i}did{/i} want to tell me something."
    show sima1close 1a 2a 3a at u11 as sima with dissolve
    p "See, I thought it would be cool to return here... with a girl."
    show sima3aclose 1c 2a 3a at u11 as sima with dissolve
    s "How romantic. Who could that girl be?"
    show sima3aclose 1a 2a 3a at u11 as sima with dissolve
    p "You."
    show sima3aclose 1c 2c 3c at u11 as sima with dissolve
    s "Me?"
    show sima3bclose 1e 2a 3b blush at u11 as sima with dissolve
    s "You want to invite me along?"
    show sima3aclose 1g 2a 3a at u11 as sima with dissolve
    s "Oh my..."
    show sima3aclose 1a 2a 3a noblush at u11 as sima with dissolve
    p "Forget it, I know you're not interested..."
    show sima3aclose 1a 2d 3a at u11 as sima with dissolve
    p "You probably have a waitlist of other guys and all..."
    show sima3aclose 1a 2d 3d at u11 as sima with dissolve
    p "So stupid of me."
    s "..."
    show sima1close 1d 2b 3d at u11 as sima with dissolve
    s "You're only stupid because you managed to get it all wrong."
    show sima1close 1c 2b 3a blush at u11 as sima with dissolve
    s "I'll repeat it for the first and last time, [player_name]..."
    show sima1close 1d 2b 3a blush at u11 as sima with dissolve
    s "Do you want to invite me along to come here?"
    show sima1close 1a 2b 3a at u11 as sima with dissolve
    p "I... I do."
    show sima1close 1c 2a 3b at u11 as sima with dissolve
    s "I accept."
    show sima1close 1g 2a 3b at u11 as sima with dissolve
    p "What???"
    show sima2close 1e 2a 3a regular2 at u11 as sima with dissolve
    s "Between us..."
    show sima2close 1d 2c 3a regular1 at u11 as sima with dissolve
    s "This is my first invitation."
    show sima3bclose 1c 2b 3a blush at u11 as sima with dissolve
    s "P-please be gentle, okay?"
    p "You're kidding me!"
    show sima2close 1d 2a 3a regular1 noblush at u11 as sima with dissolve
    s "I'm not."
    show sima2close 1e 2b 3a regular2 at u11 as sima with dissolve
    s "That dinner I had here... I didn't go alone because I wanted to, you know."
    "Oh boy, oh boy, oh boy..."
    show sima2close 1d 2a 3a regular2 blush at u11 as sima with dissolve
    p "H-how about we go tomorrow?"
    show sima2close 1e 2a 3a regular2 at u11 as sima with dissolve
    s "Sure. I'm looking forward to it!"
    show sima3aclose 1e 2a 3a blush at u11 as sima with dissolve
    p "Would 2 p.m. work for you?"
    s "Sure!"
    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump date_sima
    if new_game1_sima_set == 1:
        scene black with fade
        $ renpy.pause(1, hard=True)
        jump date_sima
    jump sweet_home_d3
label ermy_invite:
    $ g_p_3 = 4
    play music "music/road_home_day1.ogg" fadeout 1.5 fadein 1.5
    scene music_room_night with fade
    "Girls went home after we left the cafe."
    "My phone charger is nowhere to be found..."
    "This class is no exception."
    "It's Saturday tomorrow, huh..."
    "Shame I have nothing planned for the weekend."
    "I wish I could go back to that cafe with one of the girls."
    "Well, they'd probably reject me anyway."
    show ermy1_dark 1e 2a 3a pose2 at u11 as ermy
    e "You're here."
    p "Jeez, Ermy, you scared me!"
    p "What're you doing here? Where have you been?"
    show ermy1_dark 1c 2a 3d pose2 at u11 as ermy with dissolve
    e "Does it really matter?"
    show ermy1_dark 1e 2a 3d pose2 at u11 as ermy with dissolve
    p "Yes, of course! We tried to find you, but to no avail."
    show ermy1_dark 1h 2c 3a pose2 at u11 as ermy with dissolve
    e "Tried so hard that no one even bothered to check the classroom?"
    show ermy1_dark 1f 2c 3a pose2 at u11 as ermy with dissolve
    p "Trust me, that's exactly what we did!"
    show ermy1_dark 1h 2c 3d pose2 at u11 as ermy with dissolve
    e "Oh! Well, maybe I was somewhere around..."
    show ermy1_dark 1h 2c 3c pose2 at u11 as ermy with dissolve
    e "Anyway, the fact that you left without me follows the trend."
    show ermy1_dark 1a 2c 3c pose2 at u11 as ermy with dissolve
    p "The trend?"
    show ermy1_dark 1c 2b 3a pose2 at u11 as ermy with dissolve
    e "I played for you this whole morning, but..."
    show ermy1_dark 1e 2d 3a pose2 at u11 as ermy with dissolve
    e "No one asked me if I want to relax and listen to the music, [player_name]."
    show ermy1_dark 1d 2a 3a pose2 at u11 as ermy with dissolve
    e "No one cares about me."
    show ermy1_dark 1f 2c 3c pose2 at u11 as ermy with dissolve
    p "Hey, it's not like that."
    show ermy1_dark 1c 2b 3d pose2 at u11 as ermy with dissolve
    e "But it is."
    show ermy1_dark 1c 2b 3d pose1 at u11 as ermy with dissolve
    e "When I say something, you guys always look so annoyed..."
    show ermy1_dark 1e 2b 3d pose1 at u11 as ermy with dissolve
    e "And about today..."
    show ermy1_dark 1h 2d 3d pose2 at u11 as ermy with dissolve
    e "How much time have you spent searching for me? Two, three minutes?"
    show ermy1_dark 1e 2d 3d pose1 at u11 as ermy with dissolve
    e "I'm just saying you wouldn't even notice if I disappeared."
    show ermy1_dark 1g 2b 3b pose2 at u11 as ermy with dissolve
    e "Sometimes I think it would've been for the better."
    show ermy1_dark 1f 2b 3d pose2 at u11 as ermy with dissolve
    p "Hey, cut it out. How long do you plan to stay here? Let's get going."
    p "I'll treat you to a soda or something. Let's go, man."
    show ermy1_dark 1c 2b 3d pose1 at u11 as ermy with dissolve
    e "Whatever..."
    show ermy1_dark 1e 2b 3a pose1 at u11 as ermy with dissolve
    e "By the way, how was the cafe?"
    p "Oh, awesome. It's a perfect place for a date."
    show ermy1_dark 1d 2b 3a pose1 at u11 as ermy with dissolve
    e "Did you invite Sima, Nana or Marta along?"
    show ermy1_dark 1a 2b 3a pose2 at u11 as ermy with dissolve
    p "Nope. Couldn't do it."
    show ermy1_dark 1g 2a 3a pose2 at u11 as ermy with dissolve
    e "I think you had a chance."
    p "Maybe..."
    show ermy1_dark 1c 2a 3d pose2 at u11 as ermy with dissolve
    e "I wonder how some guys just ask a girl out like it's not a big deal..."
    show ermy1_dark 1f 2a 3d pose2 at u11 as ermy with dissolve
    "Maybe I should cheer Ermy up... hey, I have an idea!"
    show ermy1_dark 1a 2c 3a pose2 at u11 as ermy with dissolve
    p "Ermy, why don't we go to \"Doorsia\" tomorrow?"
    p "I mean, screw girls, just us two. Let's eat something and talk."
    show ermy1_dark 1a 2c 3a pose2 blush at u11 as ermy with dissolve
    e "..."
    show ermy1_dark 1c 2c 3d pose2 blush at u11 as ermy with dissolve
    e "You really want to hang out with me?"
    show ermy1_dark 1c 2b 3a pose2 noblush at u11 as ermy with dissolve
    e "I don't want you to invite me out of pity."
    show ermy1_dark 1f 2b 3a pose2 noblush at u11 as ermy with dissolve
    p "Ermy, do you want to go or not?"
    show ermy1_dark 1a 2c 3a pose2 at u11 as ermy with dissolve
    "He lightens up."
    show ermy1_dark 1b 2c 3a pose2 blush at u11 as ermy with dissolve
    e "See you tomorrow!"
    jump sweet_home_d3
return

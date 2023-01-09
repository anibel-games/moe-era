label day2:
    $ renpy.pause(2, hard=True)
    show ru_street_static with fade
    call street_before_d2 from _call_street_before_d2
    scene black with fade
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    m "Watch out, [player_name]!"
    $ renpy.music.set_volume(1, 0, channel = "sound")
    $ renpy.music.set_volume(1, 0, channel = "music")
    play sound "sound/faceball.ogg"
    play music "music/gym_theme.ogg"
    scene ball with sshake
    "Ouch!!!"
    "The ball hits me right in the face."
    "It hurts! It really hurts!"
    scene gym
    show cg_marta_2_4 as marta
    with fade
    $ persistent.unlock_cg_marta_2_5 = 1
    m "Hey! Pass me the ball!"
    show cg_marta_2_5 as marta with dissolve
    "Warming up? With Marta it gets {i}hot{/i} in no time."
    "Yeah, hot..."
    "What was I talking about again?"
    show cg_marta_2_3 as marta with dissolve
    m "[player_name], it's not the best moment for day-dreaming."
    show cg_marta_2_4 as marta with dissolve
    m "Are you going to play or not?"
    show cg_marta_2_5 as marta with dissolve
    "I have a weird sensation in my nose."
    show cg_marta_2_3 as marta with dissolve
    m "Jeez, [player_name]... you're bleeding!"
    show cg_marta_2_5 as marta with dissolve
    "Well, at least my nosebleed is backed by science."
    p "I'm okay, don't worry."
    show cg_marta_2_3 as marta with dissolve
    m "You sure about that? See if you should visit a doctor."
    m "We're going to start the game now, but feel free to join us later on."
    window hide
    scene black with fade
    "I went to the locker room to fix my bloody nose."
    $ renpy.pause(.5, hard=True)
    scene gym with fade
    window show
    "It's nothing serious, yet I don't rush myself to go back."
    "Today we play volleyball, and I lack dexterity to be good at it."
    "Maybe it makes more sense to be a spectator today."
    show cg_all_3_s with dissolve
    "Boy, was I right!"
    "Sima is a strong, independent player."
    show cg_all_3_n with dissolve
    "Nana, despite her short stature, shows them hoops."
    "I wonder what vertical she has."
    show cg_all_3_m with dissolve
    $ persistent.unlock_cg_all_3 = 1
    "And Marta... She has that ass{w=1}ured, I'm talking about winning."
    "She got game."
    "The view is well worth being a benchwarmer."
    "{i}Now{/i} I can see myself as an avid volleyball fan."
    "It has a steep learning curve, hands down. {i}A lot{/i} of curves even..."
    "This sport is great."
    s "Watch out, [player_name]!!!"
    hide cg_all_3_s
    hide cg_all_3_n
    hide cg_all_3_m
    play sound "sound/faceball.ogg"
    scene ball with sshake
    p "Ouch!!!"
    scene gym with fade
    "This is getting old."
    "On my way to the locker room I see Ermy arguing with the teacher."
    show ermy1 pose1 blush 1h 2b 3a at u11 as ermy
    e "I can't do it! Look, I have a note from my doctor..."
    show ermy1 pose1 blush 1f 2b 3a at d11 as ermy
    "Ermy's still in his uniform. I guess he tried to skip the lesson, but was busted."
    peteacher "I can't recognize {i}a single word{/i} written here..."
    peteacher "Why don't you just tell me what kind of disease you have?"
    show ermy1 pose1 blush 1h 2b 3a at u11 as ermy
    e "Hey, this information is private..."
    show ermy1 pose1 blush 1f 2c 3c at d11 as ermy
    peteacher "That's right, private! Ten pull-ups, {i}now{/i}!"
    "Our teacher is a former navy seal."
    show ermy1 pose1 blush 1e 2b 3d at d11 as ermy with dissolve
    n "Go Ermy!"
    show ermy1 pose2 blush 1e 2b 3a at d11 as ermy with dissolve
    s "Ten pull-ups and you can join our club!"
    "The girls, having stopped playing, try to cheer Ermy."
    show ermy1 pose2 noblush 1c 2d 3c at ui11 as ermy with dissolve:
        pause 2.5
        linear 3.0 xalign -2.0
    e "Alright! Everybody, watch me doing this!{w=1} Onwards!!!"
    scene gym with sshake
    "He falls down after a lame attempt to do the very first pull-up."
    n "What a beautiful descent."
    s "Ermy, are you alright?"
    peteacher "Lights out, kids!"
    stop music fadeout 2
    scene black with fade
    $ renpy.pause(2, hard=True)
    scene ru_classroom_day
    show shade_bottom
    with fade
    play music "music/jazzy_school.ogg" fadein 1.5 fadeout 1.5
    "Putting physical education right before math is outright evil."
    "For some reason, I see our class in a new light today."
    "My brain must've evaporated with the sweat."
    show teya2 1a 2a 3a regularhand1 at u11 as teya behind shade_bottom
    $ renpy.pause(.3, hard=True)
    show teya2 1e 2a 3a regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "Good day, everyone."
    show teya2 1e 2a 3b regularhand4 at u11 as teya behind shade_bottom with dissolve
    t "Today I'll spend the whole class standing right next to you."
    show teya1 1c 2a 3b at u11 as teya behind shade_bottom with dissolve
    t "Remember, we're a small but diverse group of friends!"
    show teya2 1e 2a 3a regularhand2 at u11 as teya behind shade_bottom with dissolve
    t "On that note, let's start our math class!"
    show teya2 1b 2a 3b regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "As you may know, even rules of the universe are defined using mathematics."
    show teya2 1b 2a 3b regularhand1 at d21 as teya behind shade_bottom
    $ renpy.pause(.3, hard=True)
    show teya2 1a 2a 3a regularhand4 at d21 as teya behind shade_bottom
    show nana2 1d 2d 3d at u22 as nana behind shade_bottom
    with dissolve
    n "I feel it every time I count the money in my wallet."
    show teya2 1a 2a 3a regularhand4 at d31 as teya behind shade_bottom
    show nana2 1a 2d 3d at d33 as nana behind shade_bottom
    $ renpy.pause(.3, hard=True)
    show marta3 1e 2a 3a regular1 at u32 as marta behind shade_bottom
    with dissolve
    m "Two important Education Majors also depend on your aptitude to math."
    show nana1 1a 2a 3a regular2 at d33 as nana behind shade_bottom
    show marta2 1b 2a 3a regular1 at u32 as marta behind shade_bottom
    with dissolve
    m "I'm talking about STEM and Liberal Arts degree majors. "
    show nana1 1a 2a 3a regular2 at u33 as nana behind shade_bottom
    show marta2 1b 2a 3a regular1 at d32 as marta behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1c 2a 3a regular2 at u33 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    with dissolve
    n "STEM? What's that?"
    show teya2 1e 2a 3a regularhand2 at u31 as teya behind shade_bottom
    show nana1 1c 2a 3a regular2 at d33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d33 as nana behind shade_bottom
    show teya2 1e 2a 3a regularhand2 at u31 as teya behind shade_bottom
    with dissolve
    t "Short for science, technology, engineering and math, Nana."
    show nana1 1a 2a 3a regular2 at u33 as nana behind shade_bottom
    show teya2 1e 2a 3a regularhand2 at d31 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand4 at d31 as teya behind shade_bottom
    show nana1 1d 2a 3a regular2 at u33 as nana behind shade_bottom
    with dissolve
    n "I see... what's better, a STEM degree or a Liberal Arts degree?"
    show nana1 1d 2a 3a regular2 at d33 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at u32 as marta behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d33 as nana behind shade_bottom
    show marta2 1e 2a 3a regular1 at u32 as marta behind shade_bottom
    with dissolve
    m "STEM" #fixed in None
    show teya1 1a 2a 3a at d41 as teya behind shade_bottom
    show nana3 1a 2a 3a at d44 as nana behind shade_bottom
    show marta2 1a 2a 3a regular1 at d43 as marta behind shade_bottom
    $ renpy.pause(.3, hard=True)
    show sima1 1d 2d 3a regular at u42 as sima behind shade_bottom
    with dissolve
    s "Why do you think STEM is superior, Marta?"
    show marta2 1a 2a 3a regular1 at u43 as marta behind shade_bottom
    show sima1 1d 2d 3a regular at d42 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3a regular at d42 as sima behind shade_bottom
    show marta3 1e 2a 3a regular1 at u43 as marta behind shade_bottom
    with dissolve
    m "Well, take a look around..."
    show marta2 1e 2a 3a regular2 at u43 as marta behind shade_bottom
    show nana3 1a 2a 3d at d44 as nana behind shade_bottom
    show teya1 1b 2a 3a at d41 as teya behind shade_bottom
    with dissolve
    m "It's all predicted by scientists, calculated by mathematicians, built by engineers."
    show marta2 1e 2a 3a regular2 at d43 as marta behind shade_bottom
    show sima1 1a 2d 3a regular at u42 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d43 as marta behind shade_bottom
    show sima1 1d 2d 3a regular at u42 as sima behind shade_bottom
    with dissolve
    s "Maybe, but then you need to make it beautiful!"
    show sima1 1d 2d 3a regular at d42 as sima behind shade_bottom
    show teya1 1b 2a 3a at u41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2a 3a regularhand4 noblush at u41 as teya behind shade_bottom
    show marta3 1a 2a 3a regular1 at d43 as marta behind shade_bottom
    show sima2 1a 2a 3a regular2 at d42 as sima behind shade_bottom
    with dissolve
    t "Sadly, we only have that much time, so let's move on, class."
    show teya1 1c 2a 3b at u41 as teya behind shade_bottom
    show marta3 1b 2a 3a regular1 at d43 as marta behind shade_bottom
    with dissolve
    t "Just as yesterday, you had to prepare a short speech..."
    show teya2 1e 2a 3a regularhand2 at u41 as teya behind shade_bottom
    show sima2 1e 2a 3a regular2 at d42 as sima behind shade_bottom
    with dissolve
    t "This time, it's about real-life applications of math."
    show teya2 1e 2a 3a regularhand1 at u41 as teya behind shade_bottom
    show nana1 1b 2a 3a regular1 at d44 as nana behind shade_bottom
    with dissolve
    t "Talk about a field where math's used in, and how you find it amusing."
    show teya2 1e 2a 3a regularhand1 at d41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya1 1b 2a 3a at d41 as teya behind shade_bottom
    show nana1 1a 2a 3a regular2 at d44 as nana behind shade_bottom
    with dissolve
    "I wonder what everyone else finds amusing..."
    jump choice_d2
label choice_d2:
    show teya1 1b 2a 3a at u41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya3 1c 2a 3b at u41 as teya behind shade_bottom with dissolve
    t "They say history repeats itself. Well, guess what..."
    show teya2 1e 2a 3a regularhand3 at u41 as teya behind shade_bottom with dissolve
    t "My shortlist has three topics, and we only have time to cover two of them."
    if books_skip == 0:
        show teya2 1e 2a 3a regularhand4 at u41 as teya behind shade_bottom with dissolve
        t "[player_name], please help me one more time."
        show teya2 1e 2a 3a regularhand4 at d41 as teya behind shade_bottom
        $ renpy.pause(.001, hard=True)
    else:
        show teya3 1c 2a 3d at u41 as teya behind shade_bottom with dissolve
        t "[player_name], I hope today you'll find something relevant to your interests."
        show teya2 1e 2a 3a regularhand2 at u41 as teya behind shade_bottom with dissolve
        t "Yes, I want to ask you to make the choice again."
        show teya2 1e 2a 3a regularhand2 at d41 as teya behind shade_bottom
        $ renpy.pause(.001, hard=True)
    show teya2 1d 2a 3a regularhand3 at d41 as teya behind shade_bottom with dissolve
    "Here we go again."
    menu:
        "Math and beauty.":
            $ bn_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump beauty
        "Math and the future.":
            $ bs_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump future
        "Math and success.":
            $ bm_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump success
        "I don't like any of these topics.":
            jump math_is_boring
label math_is_boring:
    p "I agree that history repeats itself."
    p "None of these topics seem interesting to me."
    show teya2 1d 2c 3d regularhand3 at d41 as teya behind shade_bottom
    show marta2 1d 2d 3d at d43 as marta behind shade_bottom
    show nana1 1f 2b 3a regular2 at d44 as nana behind shade_bottom
    show sima1 1a 2d 3d at d42 as sima behind shade_bottom
    with dissolve
    p "Maybe someone else should make a choice?"
    show teya2 1d 2c 3d regularhand3 at u41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1d 2c 3d regularhand3 at u41 as teya behind shade_bottom with dissolve
    t "Well, what if I told you..."
    show teya2 1c 2a 3d blush regularhand1 behind shade_bottom at u41 as teya
    show marta2 1d 2a 3a at d43 as marta behind shade_bottom
    show nana1 1a 2b 3a regular2 at d44 as nana behind shade_bottom
    show sima1 1a 2a 3a at d42 as sima behind shade_bottom
    with dissolve
    t "What if I told you that numbers can be sexy?"
    show teya2 1e 2d 3a noblush regularhand2 at u41 as teya behind shade_bottom with dissolve
    t "You know what a prime number is, right?"
    show teya2 1e 2d 3a noblush regularhand2 at d41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2d 3a regularhand4 at d41 as teya behind shade_bottom with dissolve
    p "Like, uh... eleven?"
    p "You can't form a prime number by multiplying two natural numbers."
    show teya2 1a 2d 3a regularhand4 at u41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2d 3a regularhand2 at u41 as teya behind shade_bottom with dissolve
    t "That's correct. Now, some prime numbers are called {i}sexy primes{/i}?"
    show teya2 1e 2d 3a regularhand2 at d41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1b 2d 3a regularhand4 at d41 as teya behind shade_bottom with dissolve
    p "Oh wow..."
    show teya2 1b 2d 3a regularhand4 at u41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2d 3a regularhand2 at u41 as teya behind shade_bottom with dissolve
    t "Ready to change your mind now?"
    show teya2 1e 2d 3a regularhand2 at d41 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand3 at d41 as teya behind shade_bottom with dissolve
    menu:
        "Yes.":
            jump math_is_fine
        "No. Sorry, I think I'll pass.":
            $ math_skip = 1

            $achievement.grant("TLDR")
            init:
                $achievement.register("TLDR")
                $achievement.sync()
            $achievement.sync()

            jump math_sucks
label math_is_fine:
    menu:
        "Math and beauty.":
            $ bn_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump beauty
        "Math and the future.":
            $ bs_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump future
        "Math and success.":
            $ bm_p = 2
            $ math_chosen = 1
            play music "music/math1_day2.ogg" fadeout 1 fadein 1
            jump success
label math_sucks:
    hide sima
    hide marta
    hide nana
    with dissolve
    show teya2 1a 2a 3a regularhand3 behind shade_bottom at u11 as teya
    $ renpy.pause(.25, hard=True)
    show teya1 1c 2a 3b at u11 as teya behind shade_bottom with dissolve
    t "Well, it's your right. Ermy, will you be my knight in shining armor?"
    show teya1 1c 2a 3b at d22 as teya behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show teya1 1a 2a 3a at d22 as teya behind shade_bottom
    show ermy1 1b 2a 3a pose1 at u21 as ermy behind shade_bottom
    with dissolve
    e "At your service!"
    scene black with eye_shut
    $ renpy.pause(2, hard=True)
    scene ru_classroom_day
    show shade_bottom
    with eye_open
    play music "music/math2_day2.ogg" fadeout 1 fadein 1
    jump math_lessonp2
label beauty:
    p "Beauty? Are you sure it's connected with math?"
    hide teya
    hide marta
    hide sima
    with dissolve
    show nana1 1a 2a 3a regular2 at u11 as nana behind shade_bottom
    $ renpy.pause(.3, hard=True)
    show nana1 1e 2c 3c regular1 at u11 as nana behind shade_bottom with dissolve
    n "Great choice, [player_name]!"
    show nana1 1c 2a 3c regular2 at u11 as nana behind shade_bottom with dissolve
    n "Have you ever heard about the Golden Ratio?"
    show nana1 1d 2a 3a regular2 at u11 as nana behind shade_bottom with dissolve
    n "It's been known for ages. You know, for a countless number of days..."
    show nana1_runight 1g 2a 3b regular2 at u11 as nana behind shade_bottom
    show ru_classroom_night behind nana
    with dissolve
    n "And nights..."
    show nana1 1d 2a 3a regular2 at u11 as nana behind shade_bottom
    hide ru_classroom_night behind nana
    with dissolve
    n "And days..."
    show nana1_runight 1g 2a 3b regular2 at u11 as nana behind shade_bottom
    show ru_classroom_night behind nana
    with dissolve
    n "And nights again."
    hide ru_classroom_night behind nana
    show nana3 1e 2a 3a at u11 as nana behind shade_bottom
    with dissolve
    n "It's pretty simple..."
    hide nana
    show cg_barashek
    with fade
    pause
    $ persistent.unlock_cg_barashek = 1
    n "Our attraction to the human body increases if it's symmetrical and in proportion."
    n "Same goes for the face. We're more likely to, um, like proportional ones."
    n "Although it's a well-known rule..."
    n "A lot of artists still fail to apply it to their works."
    n "The Golden Ratio is 1.618:1."
    n "Human attractiveness is not the only field where it is used, by the way."
    n "The Golden Ratio provides a sense of balance and equilibrium in architecture."
    n "However, there's no rule without an exception..."
    n "The ratio for the length of the miniskirt, exposed thighs and the over-knee part of socks is 4:1:2.5."
    n "It's called..."
    show nana1 1f 2d 3a regular2 at d11 as nana behind shade_bottom
    hide cg_barashek
    with fade
    show nana1 1f 2d 3a regular2 at u11 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2d 3b regular1 at u11 as nana behind shade_bottom with dissolve
    n "Hey, what are you looking at?"
    show nana1 1f 2d 3a regular2 at d22 as nana behind shade_bottom
    $ renpy.pause(0.25, hard=True)
    show sima3a 1c 2a 3a at u21 as sima behind shade_bottom with dissolve
    s "The Golden Ratio rule's based on Fibonacci numbers, right?"
    show sima3a 1c 2a 3a at d21 as sima behind shade_bottom
    show nana1 1f 2d 3a regular2 at u22 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima3a 1g 2a 3d at d21 as sima behind shade_bottom
    show nana3 1d 2a 3a at u22 as nana behind shade_bottom
    with dissolve
    n "Who cares... was that Fibonacci guy symmetrical?"
    show sima3a 1g 2a 3d at d31 as sima behind shade_bottom
    show nana3 1g 2a 3a at d33 as nana behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show marta2 1b 2a 3a regular2 at u32 as marta behind shade_bottom with dissolve
    m "I think that mathematical beauty is an elegant way to prove your theory."
    show marta2 1b 2a 3a regular2 at d32 as marta behind shade_bottom
    show nana3 1g 2a 3a at u33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2a 3a regular1 at d32 as marta behind shade_bottom
    show sima3a 1c 2c 3a at d31 as sima behind shade_bottom
    show nana1 1c 2d 3a regular2 at u33 as nana behind shade_bottom
    with dissolve
    n "In your case, it's the boredom theory..."
    show marta2 1f 2a 3d regular1 at d32 as marta behind shade_bottom
    show sima3a 1g 2a 3a at d31 as sima behind shade_bottom
    show nana1 1d 2a 3c regular1 at u33 as nana behind shade_bottom
    with dissolve
    n "Math is the ultimate power!"
    show marta2 1a 2a 3a regular1 at d42 as marta behind shade_bottom
    show sima3a 1a 2a 3a at d41 as sima behind shade_bottom
    show nana1 1g 2a 3a regular2 at d43 as nana behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show teya3 1c 2b 3a blush at u44 as teya behind shade_bottom with dissolve
    t "Nana, thank you. Well done... I guess."
    hide nana
    hide sima
    hide marta
    with dissolve
    show teya2 1a 2a 3a regularhand4 noblush at u11 as teya behind shade_bottom
    show teya2 1e 2a 3a regularhand2 noblush at u11 as teya behind shade_bottom with dissolve
    t "I believe in the Golden Ratio, but..."
    show teya3 1c 2a 3d  noblush at u11 as teya behind shade_bottom with dissolve
    t "Don't forget that looks can be deceiving, alright?"
    show teya2 1e 2a 3b regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "It's much more important to see what's inside."
    show teya2 1a 2a 3a regularhand3 at u22 as teya behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show ermy1 1h 2d 3d pose2 at u21 as ermy behind shade_bottom with dissolve
    e "Everyone wants to be friends with beautiful people! It's not fair!"
    show ermy1 1h 2d 3d pose2 at d21 as ermy behind shade_bottom
    show teya2 1a 2a 3a regularhand3 at u22 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 1f 2d 3d pose2 at d21 as ermy behind shade_bottom
    show teya1 1e 2a 3a at u22 as teya behind shade_bottom
    with dissolve
    t "Life is unfair!{w=1} Deal with it." #fixed in None
    hide ermy with dissolve
    show teya1 1e 2a 3a at u11 as teya behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show teya2 1e 2a 3a regularhand2 noblush at u11 as teya behind shade_bottom with dissolve
    t "Use this fact to your own benefit."
    show teya2 1a 2a 3a regularhand4 at u11 as teya behind shade_bottom with dissolve

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump day2_road_home_nana

    if nana_plusset == True:
        $ new_game1_nana_set = 1
        $ renpy.pause(1, hard=True)
        jump day2_road_home_nana

    if math_chosen == 1:
        call math_intermission from _call_math_intermission
    if math_chosen == 1:
        menu:
            "Math and the future.":
                $ bs_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump future
            "Math and success.":
                $ bm_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump success
    else:
        jump math_lessonp2
label success:
    hide nana
    hide sima
    hide teya
    with dissolve
    show marta3 1b 2a 3a regular1 at d11 as marta behind shade_bottom
    p "Success and math? Is it about your personal finance?"
    show marta3 1b 2a 3a regular1 at u11 as marta behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3a regular2 at u11 as marta behind shade_bottom with dissolve
    m "Great choice, [player_name]."
    show marta3 1e 2a 3a regular1 at u11 as marta behind shade_bottom with dissolve
    m "Do you guys want to be successful, earning a lot of money?"
    show marta3 1e 2a 3a regular1 at d21 as marta behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show nana1 1e 2c 3c regular1 at u22 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at d21 as marta behind shade_bottom
    with dissolve
    n "Yes!!!"
    show nana1 1e 2c 3c regular1 at d33 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show nana1 1a 2a 3a regular2 at d33  as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    show sima3a 1d 2d 3a at u31 as sima behind shade_bottom
    with dissolve
    s "I don't value material possessions that much... but you have my interest."
    show marta3 1g 2a 3a regular1 at u32 as marta behind shade_bottom
    show sima3a 1d 2d 3a at d31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2c 3a at d31 as sima behind shade_bottom
    show marta2 1e 2a 3a regular1 at u32 as marta behind shade_bottom
    show nana1 1g 2c 3a regular1 at d33 as nana behind shade_bottom
    with dissolve
    m "It's all possible if you're good at math."
    show marta2 1b 2a 3a regular2 at u32 as marta behind shade_bottom
    show sima1 1a 2a 3d at d31 as sima behind shade_bottom
    show nana1 1b 2c 3a regular1 at d33 as nana behind shade_bottom
    with dissolve
    m "Take gambling mathematics, for example."
    show marta3 1e 2a 3a regular1 at u32 as marta behind shade_bottom
    show sima1 1a 2a 3a at d31 as sima behind shade_bottom
    show nana1 1g 2a 3a regular2 at d33 as nana behind shade_bottom
    with dissolve
    m "Let's imagine we're in, say, Las Vegas... and it's evening now."
    show ru_classroom_night behind sima, nana, marta
    show marta2_runight 1b 2a 3a regular2 at u11 as marta
    show sima3a_runight 1a 2a 3a at d31 as sima
    show nana1_runight 1g 2a 3a regular2 at d33 as nana
    with dissolve
    m "Gambling mathematics can be included in game theory."
    show marta3_runight 1g 2a 3b regular1 at u11 as marta
    show nana1_runight 1f 2a 3d regular2 at d33 as nana
    with dissolve
    m "It's all about {i}probability{/i} of an event to occur."
    show marta2_runight 1b 2a 3a regular1 at u32 as marta with dissolve
    m "Let me give you an example..."
    show cg_marta_1_1 behind shade_bottom with fade
    $ persistent.unlock_cg_marta_1_1 = 1
    m "Imagine yourself near a roulette table."
    m "It has two zeroes and 36 numbers, 18 red and 18 black."
    m "If you bet any amount of money on red, your chance to win is 18/38, right?"
    m "However, if you lose, it's 20/38 chance."
    m "20 is superior to 18. Therefore, odds are not in your favour."
    m "It's very simple yet it's the reason casinos exist."
    m "If you think I forgot about luck..."
    m "Luck is called \"standard deviation\" here."
    m "It's an expectation of a range of your earnings after a couple of rounds."
    m "That range is increasingly negative. The more you play, the more you lose."
    m "Players also come up with various betting systems, such as martingale..."
    m "If you double the bet after every loss, the first win recovers everything."
    m "So... if you're good at math, it can get you rich!"
    hide cg_marta_1_1
    show marta2_runight 1g 2a 3a regular1 at d32 as marta
    show nana1_runight 1a 2c 3a regular1 at d33 as nana
    with fade
    show nana1_runight 1a 2c 3a regular1 at u33 as nana
    $ renpy.pause(.001, hard=True)
    show nana1_runight 1e 2c 3a regular1 at u33 as nana with dissolve
    n "Predicting things... just how exciting could it be?"
    show nana1_runight 1e 2c 3a regular1 at d33 as nana
    show marta2_runight 1g 2a 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show nana1_runight 1a 2a 3a regular1 at d33 as nana
    show marta2_runight 1b 2a 3a regular2 at u32 as marta
    with dissolve
    m "Told you!"
    show nana1_runight 1a 2a 3a regular1 at u33 as nana
    show marta2_runight 1b 2a 3a regular2 at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1a 2a 3a regular2 at d32 as marta
    show nana1_runight 1c 2a 3a regular2 at u33 as nana
    show sima3a_runight 1g 2a 3b at d31 as sima
    with dissolve
    n "But... If what you said is true, how come you're not rich?"
    show marta2_runight 1a 2a 3a regular2 at u32 as marta
    show nana1_runight 1c 2a 3a regular2 at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana1_runight 1f 2a 3a regular2 at d33 as nana
    show marta2_runight 1b 2c 3b blush regular1 at u32 as marta
    show sima2_runight 1a 2a 3a regular2 at d31 as sima
    with dissolve
    m "Hey, I can't even play yet!"
    show marta2_runight 1b 2c 3b blush regular1 at d32 as marta
    show sima2_runight 1a 2a 3a regular2 at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1g 2a 3a noblush regular1 at d32 as marta
    show sima1_runight 1d 2a 3a at u31 as sima
    show nana1_runight 1f 2b 3a regular2 at d33 as nana
    with dissolve
    s "If you listened carefully, you'd notice that chance of losing stacks over time."
    show sima1_runight 1d 2a 3b at u31 as sima
    show marta2_runight 1a 2a 3a regular1 at d32 as marta
    with dissolve
    s "And it's very hard to stop, due to the nature of gambling."
    show sima1_runight 1c 2a 3a at u31 as sima
    show nana3_runight 1a 2a 3d at d33 as nana
    with dissolve
    s "However, I've heard that you can also use game theory on stock market."
    show sima1_runight 1c 2a 3a at d31 as sima
    show marta2_runight 1a 2a 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show sima1_runight 1a 2a 3a at d31 as sima
    show marta2_runight 1b 2a 3a regular2 at u32 as marta
    with dissolve
    m "That's right! Stock traders from the biggest banks use it."
    show marta2_runight 1b 2a 3a regular2 at d32 as marta
    show nana3_runight 1a 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1a 2a 3a regular1 at d32 as marta
    show nana3_runight 1c 2a 3a at u33 as nana
    with dissolve
    n "So... they're, like, employed at the bank, right?"
    show marta2_runight 1a 2a 3a regular1 at u32 as marta
    show nana3_runight 1c 2a 3a at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana3_runight 1c 2a 3a at d33 as nana
    show marta2_runight 1b 2a 3a regular2 at u32 as marta
    with dissolve
    m "So what of it?"
    show nana3_runight 1c 2a 3a at u33 as nana
    show marta2_runight 1b 2a 3a regular2 at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1a 2c 3a regular1 at d32 as marta
    show nana3_runight 1c 2a 3a at u33 as nana
    show sima1_runight 1g 2a 3b at d31 as sima
    with dissolve
    n "Why don't they quit their jobs and trade on their own?"
    show nana3_runight 1e 2a 3a at u33 as nana
    show sima1_runight 1g 2a 3a at d31 as sima
    show marta2_runight 1f 2c 3d regular1 at d32 as marta
    with dissolve
    n "I mean, if that game theory really works!"
    show marta2_runight 1f 2c 3d regular1 at u32 as marta
    show nana3_runight 1e 2a 3a at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana3_runight 1a 2a 3a at d33 as nana
    show marta3_runight 1e 2a 3a regular1 at u32 as marta
    with dissolve
    m "Well, maybe you can't predict everything..."
    show marta3_runight 1gg 2c 3b regular2 blush at u32 as marta
    show sima1_runight 1e 2b 3d blush at d31 as sima
    with dissolve
    m "Like... what bra size you're going to be, Nana."
    show marta3_runight 1gg 2c 3b regular2 blush at d32 as marta
    show nana3_runight 1a 2a 3a at u33 as nana
    $ renpy.pause(.001, hard=True)
    show marta3_runight 1gg 2c 3b regular2 at d32 as marta
    show nana3_runight 1c 2a 3a at ui33 as nana:
        alpha 1
        zoom 1
        ypos 1244
        pause 1.7
        linear .25 alpha 0
    with dissolve
    show nana1_runight 1e 2c 3c regular2 at ui33 as nana2:
        alpha 0
        zoom 1
        ypos 1250
        pause 1
        linear .25 alpha 1
    n "Ha! So you admit...{w=1} Hey!!!"
    show nana1_runight 1f 2c 3c blush regular2 at ui33 as nana
    show marta3_runight 1gg 2c 3a regular2 at d32 as marta
    hide nana2
    with dissolve
    n "What did you just ask???"
    show sima1_runight 1e 2b 3d blush at u31 as sima
    show nana1_runight 1f 2c 3c blush regular2 at d33 as nana
    $ renpy.pause(.001, hard=True)
    show nana1_runight 1f 2c 3c blush regular2 at d33 as nana
    show sima1_runight 1e 2b 3d blush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana1_runight 1f 2c 3c blush regular2 at d33 as nana
    show sima3b_runight blush 1d 2b 3b at u31 as sima
    show marta3_runight 1g 2c 3b regular1 at d32 as marta
    with dissolve
    s "Hahaha!"
    hide ru_classroom_night
    hide nana
    hide sima
    hide marta
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show teya2 1a 2a 3a regularhand1 at u11 as teya behind shade_bottom with dissolve
    show teya2 1c 2a 3a regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "Marta, thanks! Well done."
    show teya3 1c 2a 3b at u11 as teya behind shade_bottom with dissolve
    t "I believe in game theory, but..."
    show teya2 1e 2a 3a regularhand2 at u11 as teya behind shade_bottom with dissolve
    t "Our world is a bit illogical. Things tend to happen just {i}because{/i}."
    show teya2 blush 1c 2a 3a regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "Who knows, maybe that's what makes our world beautiful."

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump day2_road_home_marta

    if marta_plusset == True:
        scene black with fade
        $ renpy.pause(1, hard=True)
        $ new_game1_marta_set = 1
        jump day2_road_home_marta

    if math_chosen == 1:
        call math_intermission from _call_math_intermission_1
    if math_chosen == 1:
        menu:
            "Math and the future.":
                $ bs_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump future
            "Math and beauty.":
                $ bn_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump beauty
    else:
        jump math_lessonp2
label future:
    hide nana
    hide marta
    hide teya
    with dissolve
    show sima2 1e 2a 3a regular2 at d11 as sima behind shade_bottom
    p "Mathematics and the future... sounds exciting!"
    show sima2 1e 2a 3a regular2 at u11 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima2 1d 2a 3b regular1 at u11 as sima behind shade_bottom with dissolve
    s "A very interesting topic, indeed. Glad you picked it!"
    show sima2 1c 2a 3a regular2 at u11 as sima behind shade_bottom with dissolve
    s "Have you ever heard about..."
    show sima2 1d 2c 3c regular1 at u11 as sima behind shade_bottom with dissolve
    s "Big Data?"
    show sima2 1d 2c 3c regular1 at d21 as sima behind shade_bottom
    $ renpy.pause(.2, hard=True)
    show sima2 1a 2a 3a regular2 at d21 as sima behind shade_bottom
    show nana1 1c 2c 3c regular1 at u22 as nana behind shade_bottom
    with dissolve
    n "Is it something like rocket science?"
    show sima2 1a 2a 3a regular2 at u21 as sima behind shade_bottom
    show nana1 1c 2c 3c regular1 at d22 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2c 3c regular2 at d22 as nana behind shade_bottom
    show sima2 1c 2a 3b regular2 at u21 as sima behind shade_bottom
    with dissolve
    s "Not quite..."
    show nana1 1a 2c 3c regular2 at u22 as nana behind shade_bottom
    show sima2 1c 2a 3b regular2 at d21 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima2 1g 2a 3a regular2 at d21 as sima behind shade_bottom
    show nana1 1d 2a 3a regular1 at u22 as nana behind shade_bottom
    with dissolve
    n "Big Data. Machine Learning..."
    show nana1 1a 2a 3a regular2 at d33 as nana behind shade_bottom
    show sima2 1g 2a 3a regular2 at d31 as sima behind shade_bottom
    $ renpy.pause(.2, hard=True)
    show marta3 1ee 2a 3b regular2 blush at u32 as marta behind shade_bottom with dissolve
    m "Enough to make a startup, Nana!"
    show marta3 1ee 2a 3b regular2 blush at d32 as marta behind shade_bottom
    show sima2 1g 2a 3a regular2 at u31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show marta3 1b 2a 3a regular1 noblush at d32 as marta behind shade_bottom
    show sima2 1c 2a 3a regular1 at u31 as sima behind shade_bottom
    show nana3 1a 2a 3d at d33 as nana behind shade_bottom
    with dissolve
    s "Joke as much as you want, but it's the future."
    show the_future behind shade_bottom with dissolve
    s "The future!"
    hide the_future
    show cg_sima_2_3 as sima1 behind shade_bottom
    with fade
    pause
    show cg_sima_2_4 as sima1 with dissolve
    $ persistent.unlock_cg_sima_2_4 = 1
    s "Big Data is like a new galaxy."
    s "It's detailed down to the lowest level possible in the target set..."
    show cg_sima_2_3 as sima1 with dissolve
    s "For example, you analyze store sales down to every single customer."
    show cg_sima_2_2 as sima1 with dissolve
    s "Of course, it's {i}a lot{/i} of data, hence the word \"Big\"."
    s "Why do we need it at all? Well, imagine you went shopping."
    show cg_sima_2_1 as sima1 with dissolve
    s "Here you are, standing near a shelf with a lot of goods on it."
    show cg_sima_2_4 as sima1 with dissolve
    s "Do you think these items are placed randomly?"
    show cg_sima_2_3 as sima1 with dissolve
    s "No, Big Data is their new order."
    s "First, you analyze purchasing history of each customer..."
    show cg_sima_2_2 as sima1 with dissolve
    s "When you put it together, you see the most and the least popular items."
    s "Based on that, you can review what you sell, the {i}assortment{/i}."
    show cg_sima_2_1 as sima1 with dissolve
    s "All what's left is to \n re-arrange the shelf accordingly."
    show cg_sima_2_2 as sima1 with dissolve
    s "Do you know where they place the top-sellers?"
    show cg_sima_2_4 as sima1 with dissolve
    s "At your eye level, in the middle of the shelf."
    show cg_sima_2_2 as sima1 with dissolve
    s "Expensive goods are put on the upper shelves, \"above\" everything."
    s "The cheapest items are usually at the lowest level."
    hide sima1
    show sima1 1e 2a 3a at d31 as sima behind shade_bottom
    show nana3 1a 2a 3d at d33 as nana behind shade_bottom
    show marta3 1a 2a 3a regular1 at d32 as marta behind shade_bottom
    with fade
    show nana3 1a 2a 3d at u33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana3 1d 2a 3a at u33 as nana behind shade_bottom with dissolve
    n "Why can't we rely on common sense instead of Big Data?"
    show nana3 1d 2a 3a at d33 as nana behind shade_bottom
    show sima1 1e 2a 3a at u31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at d33 as nana behind shade_bottom
    show sima2 1e 2a 3b regular1 at u31 as sima behind shade_bottom
    with dissolve
    s "Relying on common sense means relying on people."
    show marta2 1a 2a 3a regular1 at d32 as marta behind shade_bottom
    show sima2 1c 2a 3d regular2 at u31 as sima behind shade_bottom
    show nana3 1a 2a 3d at d33 as nana behind shade_bottom
    with dissolve
    s "And people tend to make mistakes, Nana."
    show sima3a 1d 2a 3d at u31 as sima behind shade_bottom
    show nana3 1f 2a 3d at d33 as nana behind shade_bottom
    with dissolve
    s "Without Big Data, your predictions lack..."
    show sima2 1d 2a 3a regular1 at u31 as sima behind shade_bottom
    show nana3 1a 2d 3c at d33 as nana behind shade_bottom
    with dissolve
    s "Quality!"
    show sima2 1d 2a 3a regular1 at d31 as sima behind shade_bottom
    show nana3 1a 2d 3c at u33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima behind shade_bottom
    show nana3 1c 2a 3d at u33 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    with dissolve
    n "Even if I'm the best store manager on planet Earth?"
    show nana3 1c 2a 3d at d33 as nana behind shade_bottom
    show marta3 1g 2a 3a regular1 at u32 as marta behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3a at d33 as nana behind shade_bottom
    show marta2 1e 2a 3a regular2 at u32 as marta behind shade_bottom
    with dissolve
    m "What if you have to run one hundred stores in different countries?"
    show marta2 1e 2a 3a regular2 at d32 as marta behind shade_bottom
    show sima2 1a 2a 3a regular2 at u31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3a regular1 at d32 as marta behind shade_bottom
    show sima2 1c 2a 3b regular1 at u31 as sima behind shade_bottom
    with dissolve
    s "Marta's right on the money."
    show sima2 1c 2a 3b regular1 at d31 as sima behind shade_bottom
    show nana3 1a 2a 3a at u33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2a 3a regular2 at d31 as sima behind shade_bottom
    show marta3 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    show nana1 1d 2a 3a regular1 at u33 as nana behind shade_bottom
    with dissolve
    n "Then I'd hire one hundred managers, the best of the best!"
    show sima2 1a 2a 3a regular2 at u31 as sima behind shade_bottom
    show nana1 1d 2a 3a regular1 at d33 as nana behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2a 3a regular1 at d33 as nana behind shade_bottom
    show sima2 1e 2a 3d regular2 at u31 as sima behind shade_bottom
    show marta3 1a 2a 3a regular1 at d32 as marta behind shade_bottom
    with dissolve
    s "The money comes into question again, Nana."
    show nana1 1f 2a 3a regular1 at u33 as nana behind shade_bottom
    show sima2 1e 2a 3d regular2 at d31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima2 1e 2a 3d regular2 at d31 as sima behind shade_bottom
    show nana1 1d 2a 3a regular1 at u33 as nana behind shade_bottom
    with dissolve
    n "The money, you say..."
    show nana1 1c 2d 3a regular2 at u33 as nana behind shade_bottom
    show sima3a 1a 2a 3d at d31 as sima behind shade_bottom
    show marta3 1a 2c 3a regular1 at d32 as marta behind shade_bottom
    with dissolve
    n "Alright. Challenge accepted!"
    show nana1 1e 2d 3c regular1 at u33 as nana behind shade_bottom
    show sima3a 1d 2a 3d at d31 as sima behind shade_bottom
    with dissolve
    n "My people versus your Big Data."
    show nana1 1d 2c 3c regular1 at u33 as nana behind shade_bottom
    show sima2 1a 2a 3c blush regular2 at d31 as sima behind shade_bottom
    show marta3 1gg 2c 3b blush regular2 at d32 as marta behind shade_bottom
    with dissolve
    n "Give me a few months and I'll be taking showers of gold."
    show nana1 1d 2c 3c regular1 at d33 as nana behind shade_bottom
    show sima2 1a 2a 3c blush regular2 at u31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2c 3a regular2 blush at d33 as nana behind shade_bottom
    show sima1 1c 2b 3c at u31 as sima behind shade_bottom
    show marta3 1g 2c 3a blush regular1 at d32 as marta behind shade_bottom
    with dissolve
    s "Excuse me?"
    show nana1 1f 2c 3a regular2 blush at u33 as nana behind shade_bottom
    show sima1 1c 2b 3c at d31 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3c at d31 as sima behind shade_bottom
    show nana1 1e 2d 3b regular1 blush at u33 as nana behind shade_bottom
    show marta2 1g 2c 3a noblush regular1 at d32 as marta behind shade_bottom
    with dissolve
    n "What I mean is I'll get more revenue thanks to my people."
    show sima1 1a 2b 3a noblush at d31 as sima behind shade_bottom
    show nana2 1d 2d 3a blush at u33 as nana behind shade_bottom
    show marta2 1g 2a 3a regular1 at d32 as marta behind shade_bottom
    with dissolve
    n "Your Big Data is nothing but another buzzword."
    show nana2 1d 2d 3a blush at d33 as nana behind shade_bottom
    show marta2 1g 2a 3a regular1 at u32 as marta behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2d 3a blush at d33 as nana behind shade_bottom
    show marta3 1ee 2a 3b regular2 blush at u32 as marta behind shade_bottom
    show sima1 1g 2a 3a at d31 as sima behind shade_bottom
    with dissolve
    m "I'd rather take bets on who out of you two goes bankrupt first."
    hide marta
    hide sima
    hide nana
    with dissolve
    show teya3 1a 2a 3a at u11 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya3 1d 2a 3b at u11 as teya behind shade_bottom with dissolve
    t "Okay, class."
    show teya2 1e 2a 3a regularhand3 at u11 as teya behind shade_bottom with dissolve
    t "Sima, thanks, well done."
    show teya2 1b 2a 3a regularhand4 at u11 as teya behind shade_bottom with dissolve
    t "I think that the future will be driven by data."
    show teya2 1e 2a 3a regularhand1 at u11 as teya behind shade_bottom with dissolve
    t "But... maybe it's better to go to the future step by step."

    if sima_plusset == True:
        scene black with fade
        $ renpy.pause(1, hard=True)
        $ new_game1_sima_set = 1
        jump day2_road_home_sima

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump day2_road_home_sima

    if math_chosen == 1:
        call math_intermission from _call_math_intermission_2
    if math_chosen == 1:
        menu:
            "Math and success.":
                $ bm_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump success
            "Math and beauty.":
                $ bn_p = 1
                $ math_chosen = 2
                play music "music/math2_day2.ogg" fadeout 1 fadein 1
                jump beauty
    else:
        jump math_lessonp2
label math_intermission:
    show teya2 1b 2a 3a regularhand1 noblush at u11 as teya behind shade_bottom with dissolve
    t "Let's have a short break."
    show teya2 1c 2a 3a regularhand2 at u11 as teya behind shade_bottom with dissolve
    t "Everything is good in moderation."
    show teya2 1a 2a 3a regularhand4 at d21 as teya behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show ermy1 pose1 1e 2a 3a at u22 as ermy behind shade_bottom with dissolve
    e "Uh, I, well..."
    show ermy1 pose2 1d 2a 3a at u22 as ermy behind shade_bottom with dissolve
    e "Inspired by that music box from yesterday..."
    show ermy1 pose1 1d 2a 3b blush at u22 as ermy behind shade_bottom with dissolve
    e "I made a music video yesterday!"
    show ermy1 pose2 1c 2c 3a at u22 as ermy behind shade_bottom with dissolve
    e "Or rather, it's my mixtape with simple visuals."
    show teya2 1a 2a 3a regularhand4 at u21 as teya behind shade_bottom
    show ermy1 pose2 1c 2c 3a at d22 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose2 1a 2a 3a noblush at d22 as ermy behind shade_bottom
    show teya3 1c 2a 3a  at u21 as teya behind shade_bottom
    with dissolve
    t "I don't really know what a mixtape is, but..."
    show teya2 1e 2a 3b regularhand1 at u21 as teya behind shade_bottom with dissolve
    t "Put it on!"
    show teya2 1e 2a 3b regularhand1 at d21 as teya behind shade_bottom
    show ermy1 pose2 1a 2a 3a noblush at u22 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1a 2a 3a regularhand4 at d21 as teya behind shade_bottom
    show ermy1 pose2 1d 2a 3b at u22 as ermy behind shade_bottom
    with dissolve
    e "Alright."
    show ermy1 pose1 1e 2c 3a at u22 as ermy behind shade_bottom with dissolve
    e "It can look unusual though, so..."
    show ermy1 pose1 1e 2c 3a at d22 as ermy behind shade_bottom
    show teya2 1a 2a 3a regularhand4 at u21 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose2 1a 2a 3a at d22 as ermy behind shade_bottom
    show teya2 1e 2a 3b regularhand1 at u21 as teya behind shade_bottom
    with dissolve
    t "Don't worry, it's a risk-free environment here, Ermy."
    stop music fadeout 2
    scene black with fade
    $ renpy.pause(2, hard=True)
    play music "music/broken_things.ogg" noloop
    $ renpy.movie_cutscene("images/movies/ermywave.mkv",stop_music=False,loops=0, delay=109.5)
    play music "music/math1_day2.ogg" fadein 1.5 fadeout 1.5
    show black with fade
    $ renpy.pause(.5, hard=True)
    scene ru_classroom_day
    show shade_bottom
    with fade
    call ermy_wave_reaction from _call_ermy_wave_reaction
    hide ermy
    hide sima
    hide nana
    with dissolve
    show teya2 1a 2a 3a regularhand4 at u11 as teya behind shade_bottom
    $ renpy.pause(0.25, hard=True)
    show teya2 1e 2a 3a regularhand2 at u11 as teya behind shade_bottom with dissolve
    t "Everyone, calm down."
    show teya2 1c 2a 3b regularhand2 at u11 as teya behind shade_bottom with dissolve
    t "Ermy tried to express himself! Well done, Ermy!"
    show teya2 1e 2a 3a regularhand3 at u11 as teya behind shade_bottom with dissolve
    t "On that note, let's move on."
    show teya2 1a 2a 3a regularhand3 at u11 as teya behind shade_bottom with dissolve
    return
label math_lessonp2:
    stop music fadeout 6
    show teya3 1c 2b 3b at u11 as teya behind shade_bottom with dissolve
    t "I guess that's it for today!"
    scene black with fade
    play music "music/streets.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(1, hard=True)
    scene hallway1_ru
    show hallway1
    with fade
    "Break time..."
    hide hallway1 with dissolve
    "This hallway feels somewhat dodgy."
    "I see Ermy approaching me."
    show ermy1 1d 2a 3a pose2 at u11 as ermy
    e "Hey, man! What's up?"
    show ermy1 1c 2a 3d pose1 at u11 as ermy with dissolve
    e "Who're you going to help tomorrow?"
    show ermy1 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "Um, what're you talking about?"
    show ermy1 1b 2c 3a pose2 at u11 as ermy with dissolve
    e "C'mon, our career day, of course!"
    show ermy1 1b 2c 3a pose2 at d11 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1 1a 2a 3a pose2 at d11 as ermy with dissolve
    "Oh, right, I've heard it's a regular event at this school."
    "It helps to plan a track of education you need to land a specific job."
    "Sima, Nana and Marta will be distributing handouts..."
    "Teya asked me and Ermy to pair up with them."
    p "Honestly, I haven't thought about it..."
    show ermy1 1a 2a 3a pose2 at u11 as ermy
    $ renpy.pause(.001, hard=True)
    show ermy1 1c 2a 3a pose2 at u11 as ermy with dissolve
    e "When do you plan to make up your mind?"
    show ermy1 1a 2a 3a pose2 at u11 as ermy with dissolve
    p "Why's that so important to you?"
    show ermy1 1e 2a 3a pose2 blush at u11 as ermy with dissolve
    e "Well... What if we approach the same girl?"
    show ermy1 1c 2b 3d pose1 at u11 as ermy with dissolve
    e "I'm afraid I know her second pick."
    show ermy1 1e 2b 3a pose1 at u11 as ermy with dissolve
    e "Let me know, alright?"
    scene hallway1_ru with fade
    "I notice Sima, Nana and Marta walking down the hallway."
    "They probably think they talk among themselves..."
    "However, I can hear almost every word."
    show sima2 1a 2a 3a regular2 at d31 as sima
    show nana1 1a 2a 3a regular2 at d32 as nana
    show marta2 1a 2a 3a regular1 at d33 as marta
    with fade
    $ renpy.pause(.5, hard=True)
    show ermy1_boring 1f 2b 3d pose1 blush at di41 as ermy behind sima,marta,nana with dissolve
    show marta2 1a 2a 3a regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3a regular1 at u33 as marta with dissolve
    m "So... who's going to help you with handouts?"
    show marta2 1e 2a 3a regular1 at d33 as marta
    show nana1 1a 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d33 as marta
    show sima3a 1a 2a 3a at d31 as sima
    show nana2 1d 2d 3b at u32 as nana
    with dissolve
    show ermy1_boring 1f 2b 3d pose2 blush at di43 as ermy behind sima,marta,nana with dissolve
    n "No idea."
    show sima3a 1a 2a 3a at u31 as sima
    show nana2 1d 2d 3b at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2d 3b at d32 as nana
    show sima3a 1d 2a 3a at u31 as sima
    show marta2 1f 2a 3a regular1 at d33 as marta
    with dissolve
    show ermy1_boring 1e 2b 3a pose2 blush at di42 as ermy behind sima,marta,nana with dissolve
    s "Do you have your handouts ready, Nana?"
    show nana2 1f 2d 3b at u32 as nana
    show sima3a 1d 2a 3a at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d31 as sima
    show nana2 1d 2d 3b at u32 as nana
    show marta2 1a 2b 3a regular1 at d33 as marta
    with dissolve
    show ermy1_boring 1a 2b 3a pose1 blush at di41 as ermy behind sima,marta,nana with dissolve
    n "No idea."
    show nana2 1d 2d 3b at d32 as nana
    show marta2 1a 2b 3a regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2d 3b at d32 as nana
    show marta2 1b 2c 3d regular1 at u33 as marta
    with dissolve
    show ermy1_boring 1f 2b 3d pose2 blush at di43 as ermy behind sima,marta,nana with dissolve
    m "What about you, Sima? Anyone on mind?"
    show marta2 1b 2c 3d regular1 at d33 as marta
    show sima3a 1a 2a 3a at u31 as sima
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3d regular1 at d33 as marta
    show sima3a 1d 2a 3d at u31 as sima
    with dissolve
    show ermy1_boring 1f 2b 3d pose1 blush at di42 as ermy behind sima,marta,nana with dissolve
    s "Still up for discussion, I'm afraid."
    show sima3a 1e 2a 3d at u31 as sima
    show nana2 1a 2d 3d at d32 as nana
    with dissolve
    hide ermy with dissolve
    s "Why don't we ask [player_name] to help one of us?"
    show sima3a 1e 2a 3d at d31 as sima
    show marta2 1d 2a 3d regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a 1a 2a 3a at d31 as sima
    show marta2 1e 2a 3a regular2 at u33 as marta
    show nana2 1g 2d 3a at d32 as nana
    with dissolve
    m "Why don't {i}you{/i} ask him then?"
    show sima3a 1a 2a 3a at u31 as sima
    show marta2 1e 2a 3a regular2 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d33 as marta
    show sima3a 1c 2a 3d blush at u31 as sima
    with dissolve
    s "It feels awkward..."
    show marta2 1a 2a 3a regular1 at u33 as marta
    show sima3a 1c 2a 3d blush at d31 as sima
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2a 3d noblush at d31 as sima
    show marta2 1c 2a 3d regular1 at u33 as marta
    with dissolve
    m "Yeah, that's what I'm talking about..."
    show marta2 1d 2a 3d regular2 at u33 as marta
    show sima1 1a 2a 3b at d31 as sima
    with dissolve
    m "He should make the move first."
    show marta2 1d 2a 3d regular2 at d33 as marta
    show nana2 1g 2d 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2a 3d regular1 at d33 as marta
    show nana3 1a 2d 3d at u32 as nana
    show sima1 1a 2a 3a at d31 as sima
    with dissolve
    n "Hm..."
    show marta2 1c 2c 3c blush regular1 at d33 as marta
    show sima2 1a 2c 3c blush regular2 at d31 as sima
    show nana3 1e 2c 3a at u32 as nana
    with dissolve
    n "[player_name], [player_name]! Got a minute?"
    show sima2 1a 2c 3c blush regular2 at u31 as sima
    show nana3 1e 2c 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2c 3b at d32 as nana
    show sima2 1d 2c 3c blush regular2 at u31 as sima
    with dissolve
    s "Nana!"
    show sima2 1d 2c 3c blush regular2 at d31 as sima
    show marta2 1c 2c 3c blush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2d 3c blush at d31 as sima
    show marta2 1e 2c 3c blush regular1 at u33 as marta
    show nana3 1b 2a 3a at d32 as nana
    with dissolve
    m "Stop!"
    show marta2 1e 2c 3c blush regular1 at d33 as marta
    show nana3 1b 2a 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2c 3c blush regular1 at d33 as marta
    show nana3 1e 2c 3a at u32 as nana
    with dissolve
    n "Tee-hee!"
    show nana3 1e 2c 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2c 3a at d32 as nana with dissolve
    "Maybe it's better to play it dumb."
    show sima2 1a 2a 3c blush at d31 as sima
    show nana3 1b 2c 3b at d32 as nana
    with dissolve
    p "Hey, what's happening?"
    "I can feel the tension in the air."
    show nana3 1b 2c 3b at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2c 3a at u32 as nana with dissolve
    n "Hey, [player_name]! We need to ask you something..."
    show nana3 1e 2c 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2c 3a at d32 as nana with dissolve
    p "Sure, what's that?"
    show nana3 1b 2c 3a at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2c 3a at u32 as nana with dissolve
    n "Sima, you go ahead and ask."
    show nana3 1e 2c 3a at d32 as nana
    show sima2 1a 2a 3c blush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2c 3a at d32 as nana
    show sima1 1c 2c 3c blush at u31 as sima
    with dissolve
    s "Oh... right, sure. Sure..."
    show nana3 1g 2a 3a at d32 as nana
    show sima1 1g 2c 3c blush at u31 as sima
    with dissolve
    s "Um..."
    show sima1 1c 2c 3c blush at u31 as sima
    show marta1 1f 2b 3a blush at d33 as marta
    with dissolve
    s "Say, do you plan to..."
    show sima1 1e 2b 3c blush at u31 as sima
    show marta1 1f 2b 3c blush at d33 as marta
    show nana1 1f 2a 3d regular2 at d32 as nana
    with dissolve
    s "Do you plan to travel around the world?"
    show sima1 1e 2b 3c blush at d31 as sima
    show marta1 1f 2b 3c blush at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima1 1e 2b 3c blush at d31 as sima
    show nana2 1f 2d 3d  at d32 as nana
    show marta2 1b 2c 3c blush regular1 at u33 as marta
    with dissolve
    m "Yeah! Which country would you like to visit first?"
    show marta2 1g 2c 3c blush regular1 at u33 as marta with dissolve
    "Wait, what?"
    show marta2 1b 2b 3c blush regular1 at u33 as marta
    show sima1 1a 2a 3c blush at d31 as sima
    with dissolve
    m "For example, I always wanted to visit Liechtenstein!"
    show marta2 1b 2b 3c blush regular1 at d33 as marta
    show nana2 1f 2d 3d  at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2b 3c blush regular1 at d33 as marta
    show nana2 1d 2a 3a at u32 as nana
    with dissolve
    n "How do you spell it?"
    show nana2 1d 2a 3a at d32 as nana
    show sima1 1a 2a 3c blush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3d at d32 as nana
    show sima2 1c 2b 3c regular1 blush at u31 as sima
    with dissolve
    s "And I'd like to visit China. It's a very vibrant country."
    show sima2 1c 2b 3c regular1 blush at d31 as sima
    show marta2 1g 2b 3c blush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1a 2b 3c regular2 blush at d31 as sima
    show marta2 1b 2b 3c blush regular1 at u33 as marta
    with dissolve
    m "Yeah, they also have rich cultural heritage. I enjoy the works of Sun Tzu."
    show marta2 1b 2b 3c blush regular1 at d33 as marta
    show nana3 1a 2a 3d at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2b 3c blush regular1 at d33 as marta
    show nana3 1e 2a 3a at u32 as nana
    with dissolve
    n "Sun is always nice. However..."
    show nana3 1c 2a 3b at u32 as nana
    show marta1 1f 2b 3b blush at d33 as marta
    show sima1 1a 2b 3a blush at d31 as sima
    with dissolve
    n "I am pretty sure [player_name] realized you're making this up."
    show nana3 1b 2a 3d at u32 as nana
    show marta1 1a 2b 3b blush at d33 as marta
    with dissolve
    n "The truth is, [player_name], we want you to choose one of us..."
    show nana3 1b 2a 3d at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1b 2a 3d at d32 as nana
    show marta1 1a 2c 3c blush at d33 as marta
    show sima1 1a 2d 3c blush at d31 as sima
    with dissolve
    p "What?"
    show marta1 1a 2c 3c blush at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2b 3b blush regular1 at u33 as marta with dissolve
    m "Nana!"
    show sima1 1a 2d 3c blush at u31 as sima
    show marta2 1e 2b 3b blush regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2b 3d blush regular1 at d33 as marta
    show sima1 1d 2d 3d blush at u31 as sima
    with dissolve
    s "You're being inappropriate!"
    show sima1 1d 2d 3d blush at d31 as sima
    show nana3 1b 2a 3d at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2d 3d blush at d31 as sima
    show nana3 1e 2c 3b at u32 as nana
    with dissolve
    n "Oh my, this is so funny... Alright, let's cut it short."
    show nana1 1e 2a 3a at u32 as nana with dissolve
    n "[player_name], we need you to help us with printouts tomorrow!"
    show nana1 1e 2a 3a regular2 at u32 as nana with dissolve
    n "Question is, who exactly will you help?"
    show nana1 1d 2a 3a blush regular2 at u32 as nana with dissolve
    n "I mean... You want to lend us a hand, right?"
    show nana1 1d 2a 3a blush regular2 at d32 as nana
    show sima1 1d 2d 3d blush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a at d32 as nana
    show sima3b 1e 2b 3a blush at u31 as sima
    with dissolve
    s "Right?"
    show sima3b 1e 2b 3a blush at d31 as sima
    show marta2 1f 2b 3d blush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show sima3b 1e 2b 3a blush at d31 as sima
    show marta3 1g 2b 3a blush regular1 at u33 as marta
    with dissolve
    m "Right?"
    show marta3 1g 2b 3a blush regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2b 3a blush regular1 at d33 as marta with dissolve
    "Tough choice."
    menu:
        "Help Sima":
            $ bhs_p = 2
            jump pick_sima
        "Help Marta":
            $ bhm_p = 2
            jump pick_marta
        "Help Nana":
            $ bhn_p = 2
            jump pick_nana
        "Try to help everyone":
            $ bhe_p = 1
            jump not_yet
label pick_sima:
    show sima3a 1e 2c 3a blush at d31 as sima
    show nana2 1a 2d 3b noblush at d32 as nana
    show marta2 1f 2b 3d noblush regular1 at d33 as marta
    with dissolve
    p "I'd like to help Sima."
    show sima3a 1e 2c 3a blush at u31 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2c 3a blush at u31 as sima
    show nana2 1a 2d 3a noblush at d32 as nana
    with dissolve
    s "So nice of you, [player_name]!"
    show sima3b 1e 2a 3a blush at u31 as sima
    show nana2 1a 2d 3a noblush at d32 as nana
    with dissolve
    s "I promise it won't be bothersome."
    show sima3b 1e 2a 3a blush at d31 as sima
    show sima3b 1g 2a 3a blush at d31 as sima with dissolve
    $ renpy.pause(0.5, hard=True)
    jump day2_road_check
label pick_nana:
    show nana1 1g 2c 3c blush at d32 as nana
    show sima1 1a 2b 3d noblush at d31 as sima
    show marta2 1f 2b 3d noblush regular1 at d33 as marta
    with dissolve
    p "I'd like to help Nana."
    show nana1 1g 2c 3c blush at u32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3c blush regular1 at u32 as nana
    show sima1 1a 2b 3d noblush at d31 as sima
    show marta2 1f 2b 3d noblush regular1 at d33 as marta
    with dissolve
    n "We'll have fun, I guarantee it!"
    show nana1 1e 2c 3c blush regular1 at d32 as nana
    show nana1 1a 2c 3a blush regular1 at d32 as nana with dissolve
    $ renpy.pause(0.5, hard=True)
    jump day2_road_check
label pick_marta:
    show nana2 1a 2d 3b noblush at d32 as nana
    show sima1 1a 2b 3d noblush at d31 as sima
    show marta3 1d 2c 3c blush regular1 at d33 as marta
    with dissolve
    p "I'd like to help Marta."
    show marta3 1d 2c 3c blush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1c 2c 3c blush regular1 at u33 as marta
    show sima1 1a 2b 3d noblush at d31 as sima
    show nana2 1a 2d 3a noblush at d32 as nana
    with dissolve
    m "So glad you... I mean... hey, don't you dare go letting me down!"
    show marta3 1c 2c 3c blush regular1 at d33 as marta
    show marta3 1b 2c 3c blush regular1 at d33 as marta with dissolve
    $ renpy.pause(0.5, hard=True)
    jump day2_road_check
label not_yet:
    p "Hey, I'll manage to find time to help each of you."
    "It's a safe bet, I think."
    show marta3 1g 2b 3a blush regular1 at u33 as marta
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2d 3b noblush at d32 as nana
    show sima1 1a 2b 3d noblush at d31 as sima
    show marta2 1c 2b 3d noblush regular1 at u33 as marta
    with dissolve
    m "No need to help me, I'll be just fine."
    show sima1 1a 2b 3d noblush at u31 as sima
    show marta2 1c 2b 3d noblush regular1 at d33 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2b 3d noblush regular1 at d33 as marta
    show sima1 1e 2b 3d noblush at u31 as sima
    with dissolve
    s "Same here."
    show sima1 1e 2b 3d noblush at d31 as sima
    show nana2 1f 2d 3b noblush at u32 as nana
    $ renpy.pause(.001, hard=True)
    show sima1 1a 2b 3d noblush at d31 as sima
    show nana2 1d 2d 3b noblush at u32 as nana
    with dissolve
    n "How boring..."
    show nana2 1d 2d 3b noblush at d32 as nana
    show nana2 1a 2d 3b noblush at d32 as nana with dissolve
    $ renpy.pause(0.5, hard=True)
    jump day2_road_check

label day2_road_check:
    if math_skip == 1:
        jump day2_road_home_not_yet
    if bhe_p == 1:
        jump day2_road_home_not_yet
    python:
        bm_tp  = bhm_p + bm_p
    python:
        bs_tp = bhs_p + bs_p
    python:
        bn_tp = bhn_p + bn_p

    if bs_tp > bm_tp:
        if bs_tp > bn_tp:
            jump day2_road_home_sima
        elif bs_tp < bn_tp:
            jump day2_road_home_nana
        else:
            jump day2_road_home_not_yet
    elif bm_tp > bs_tp:
        if bm_tp > bn_tp:
            jump day2_road_home_marta
        elif bm_tp < bn_tp:
            jump day2_road_home_nana
        else:
            jump day2_road_home_not_yet
    elif bm_tp == bs_tp:
        if bn_tp > bm_tp:
            if bn_tp > bs_tp:
                jump day2_road_home_nana
            else:
                jump day2_road_home_not_yet
        else:
            jump day2_road_home_not_yet
    else:
        jump day2_road_home_not_yet

label day2_road_home:
    scene black with fade
    play music "music/Russia_night_theme.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(2, hard=True)
    scene street_ru with fade
    "The rest of the day passed by really quick."
    "We don't have any after school activities, and I'm on my way home."
    "Someone pats me on the shoulder."
    return
label day2_road_home_marta:
    $ g_p_2 = 2
    if persistent.game_done1 == None:
        call after_help_teya from _call_after_help_teya
    call after_help_marta from _call_after_help_marta
    call day2_road_home from _call_day2_road_home
    show marta3 1e 2a 3a noblush regular1 at u11 as marta
    m "Hey! What're you looking at?"
    show marta3 1d 2a 3a blush regular1 at u11 as marta with dissolve
    p "Your eyes only."
    show marta3 1b 2a 3a regular1 at u11 as marta with dissolve
    p "So... Excited about the career day tomorrow?"
    show marta2 1b 2a 3a regular2 noblush at u11 as marta with dissolve
    m "I just hope it's going to be helpful for my future!"
    show marta2 1g 2a 3a regular1 at u11 as marta with dissolve
    p "I see. By the way, what do you plan to do?"
    show marta2 1c 2c 3a regular1 blush at u11 as marta with dissolve
    m "Huh?"
    p "I mean, what are your plans for the future?"
    show marta2 1b 2a 3a regular1 noblush at u11 as marta with dissolve
    m "Hm... I can foresee myself getting a bachelor degree."
    show marta2 1d 2a 3a regular1 at u11 as marta with dissolve
    p "C'mon, you know what I mean... What about after you graduate?"
    show marta2 1e 2a 3a regular2 at u11 as marta with dissolve
    m "I'm going to land one of the most prestigious entry-level jobs."
    show marta2 1a 2a 3a regular2 at u11 as marta with dissolve
    p "What kind of a job is that?"
    show marta3 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Either investment banking or consulting."
    show marta3 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Right, I've heard it's very exciting to work there."
    show marta2 1e 2a 3a regular1 at u11 as marta with dissolve
    m "For me, it's just a nice launch pad to six figures."
    show marta2 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Is it possible to withstand long hours with that approach?"
    show marta2 1b 2a 3d regular1 at u11 as marta with dissolve
    m "Eventually, I'll get used to it."
    show marta2 1c 2b 3a regular2 at u11 as marta with dissolve
    m "After all, hard work is what I'm really good at..."
    show marta1 1b 2b 3d at u11 as marta with dissolve
    m "Yeah... really good."
    show marta1 1d 2b 3b at u11 as marta with dissolve
    p "Hey, did I ask anything wrong?"
    show marta1 1g 2b 3d at u11 as marta with dissolve
    m "..."
    show marta2 1b 2b 3d regular1 at u11 as marta with dissolve
    m "No, it's just... I really don't like to lie."
    show marta2 1c 2b 3d regular1 at u11 as marta with dissolve
    m "And right now I'm lying not only to you, but also to myself."
    show marta1 1c 2b 3b regular1 at u11 as marta with dissolve
    m "I don't want an office job at all, be it the six or zero figures one."
    show marta1 1e 2b 3a regular1 at u11 as marta with dissolve
    m "It's brutally boring, and I'll be working with mediocre people."
    show marta1 1f 2b 3d regular1 at u11 as marta with dissolve
    p "Mediocre? The jobs you just mentioned are for the very best..."
    show marta2 1d 2b 3d regular1 at u11 as marta with dissolve
    m "The very best of those who can only work for someone else."
    show marta2 1e 2a 3a regular2 at u11 as marta with dissolve
    m "Truly outstanding people play by their own rules."
    show marta2 1f 2a 3a regular1 at u11 as marta with dissolve
    p "Well then, why go for..."
    show marta2 1b 2b 3d regular1 at u11 as marta with dissolve
    m "You don't understand, huh? You clearly don't, do you..."
    show marta2 1d 2b 3a regular1 at u11 as marta with dissolve
    m "A corporate job is the only option for me as I'm not special."
    show marta2 1f 2b 3d regular1 at u11 as marta with dissolve
    p "Hey, don't be self-loathing."
    show marta2 1e 2d 3a regular1 at u11 as marta with dissolve
    m "I'm only being honest... I hate how \"everyone is special\" nowadays."
    show marta2 1e 2d 3a regular2 blush at u11 as marta with dissolve
    m "Why? Why do they tell that to kids? It only makes them suffer..."
    show marta2 1f 2d 3a regular1 at u11 as marta with dissolve
    p "Well, {i}because{/i} they're kids... To support them."
    show marta2 1e 2d 3a regular2 at u11 as marta with dissolve
    m "Then it should be \"do your best\" instead of \"you're special\"."
    show marta2 1d 2d 3c regular1 at u11 as marta with dissolve
    m "If you only excel at studying, and teachers assure you of bright future ahead..."
    show marta2 1e 2d 3a regular2 at u11 as marta with dissolve
    m "It only means you're nothing special, just like them. Just like me..."
    show marta1 1b 2b 3d regular1 at u11 as marta with dissolve
    m "I'm a queen of mediocrity."
    show marta1 1c 2b 3b regular1 at u11 as marta with dissolve
    m "You won't believe how jealous I am of someone with raw, natural talent."
    show marta1 1d 2d 3d regular1 at u11 as marta with dissolve
    m "It's the only way to be number one."
    show marta1 1a 2b 3d regular1 at u11 as marta with dissolve
    p "I see where you're going, but raw talent is a waste if not honed."
    p "And talented people are often lazy, so if you work more, you can catch up!"
    show marta2 1d 2b 3d regular1 at u11 as marta with dissolve
    m "Only if there's enough time."
    show marta2 1b 2b 3a regular1 at u11 as marta with dissolve
    m "Sadly, I'm already behind... I hate it, I really do!"
    show marta2 1f 2b 3a regular1 at u11 as marta with dissolve
    p "You're kidding me."
    show marta2 1c 2b 3d regular1 at u11 as marta with dissolve
    m "I'm afraid not."
    show marta2 1d 2b 3a regular2 at u11 as marta with dissolve
    m "Say, if I wanted to go into figure skating..."
    show marta2 1a 2b 3a regular2 at u11 as marta with dissolve
    p "Isn't this a bit of an extreme example?"
    show marta2 1e 2b 3a regular1 at u11 as marta with dissolve
    m "Okay, let's talk about drawing. I always wanted to be good at it."
    show marta2 1d 2b 3a regular2 at u11 as marta with dissolve
    m "If I start now, in two years I'll be pretty decent..."
    show marta1 1b 2a 3b at u11 as marta with dissolve
    m "But those who started ten years ago will be presented in art galleries."
    show marta1 1d 2a 3a at u11 as marta with dissolve
    m "But the punchline is..."
    show marta3 1d 2a 3a at u11 as marta with dissolve
    m "These art galleries would {i}always{/i} be named after someone with raw talent."
    show marta2 1f 2b 3a regular1 at u11 as marta with dissolve
    p "Trust me, you still have enough time, Marta!"
    show marta2 1e 2d 3a regular2 at u11 as marta with dissolve
    m "Maybe, but I really need to make up my mind and concentrate on... something."
    show marta1 1b 2b 3d regular1 at u11 as marta with dissolve
    m "\"Something\"... Screw it, I have zero idea about what I want to do!"
    show marta1 1f 2b 3b regular1 at u11 as marta with dissolve
    p "Well, have you tried discussing it with your parents?"
    show marta1 1e 2d 3c regular1 at u11 as marta with dissolve
    m "I despise them."
    show marta1 1f 2d 3a regular1 at u11 as marta with dissolve
    p "Why?"
    show marta1 1e 2d 3a regular1 at u11 as marta with dissolve
    m "My father settled down and tried to drag me along."
    show marta2 1e 2d 3c regular1 at u11 as marta with dissolve
    m "I asked countless times to get me into arts, dancing, whatever..."
    show marta2 1c 2d 3a regular2 at u11 as marta with dissolve
    m "You know, just to try it out and see if it's my thing."
    show marta2 1e 2d 3d regular1 at u11 as marta with dissolve
    m "He always told me I should forget this nonsense and study hard."
    show marta1 1d 2d 3a regular1 at u11 as marta with dissolve
    m "To live a decent life, he said..."
    show marta1 1d 2d 3b regular1 at u11 as marta with dissolve
    m "And my mother... I don't even know her well. But that's another story."
    show marta1 1f 2d 3d regular1 at u11 as marta with dissolve
    p "I don't know what to say..."
    show marta1 1d 2a 3d regular1 at u11 as marta with dissolve
    m "Well, excuse me for this rant."
    show marta3 1g 2a 3a regular1 at u11 as marta with dissolve
    m "Actually, thanks for listening. I feel a bit better now!"
    show marta3 1e 2c 3c blush regular1 at u11 as marta with dissolve
    m "Hey, why are you looking at me like that, [player_name]?"
    show marta3 1gg 2a 3b blush regular2 at u11 as marta with dissolve
    m "Don't think I opened up or anything."
    show marta3 1b 2a 3a blush regular1 at u11 as marta with dissolve
    p "I just go over what you said, Marta."
    show marta2 1b 2a 3a noblush regular1 at u11 as marta with dissolve
    m "Really? Well then, take your time!"
    show marta2 1b 2a 3a regular2 at u11 as marta with dissolve
    m "You're walking painfully slow anyway."
    show marta3 1e 2a 3a regular1 blush at u11 as marta with dissolve
    m "See you tomorrow!"
    show marta2 1c 2a 3d regular1 blush at u11 as marta with dissolve
    m "I... I'll be glad to see you tomorrow..."
    hide marta with dissolve

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            call flyers_marta from _call_flyers_marta_2
            play music "music/cafe_music.ogg" fadeout 1 fadein 1
            scene black with fade
            $ renpy.pause(1, hard=True)
            scene cafe
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump marta_invite

    if marta_plusset == True:
        scene black with fade
        call flyers_marta from _call_flyers_marta_3
        play music "music/cafe_music.ogg" fadeout 1 fadein 1
        scene black with fade
        $ renpy.pause(1.0, hard=True)
        scene cafe
        "We're about to get going."
        "In fact, Teya already left us."
        "I am waiting for the girls to return from the bathroom."
        jump marta_invite
    jump day2_end
label day2_road_home_nana:
    $ g_p_2 = 1
    if persistent.game_done1 == None:
        call after_help_teya from _call_after_help_teya_1
    call after_help_nana from _call_after_help_nana
    call day2_road_home from _call_day2_road_home_1
    show nana1 1a 2a 3a regular2 at di11 as nana with dissolve
    "It's Nana."
    "She says nothing, just standing around."
    "..."
    "Not being fond of staring contests, I decide to say something first."
    p "Hey, how're you?"
    show nana1 1f 2a 3d regular2 at d11 as nana with dissolve
    n "..."
    p "Ready for the..."
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "Career day tomorrow? Sure I am!"
    show nana1 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Is there..."
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "Anything wrong? No, it's alright, thanks for asking!"
    show nana1 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Nana, you're acting strange."
    show nana1 1f 2a 3d regular2 at d11 as nana with dissolve
    n "..."
    show nana2 1d 2b 3d at u11 as nana with dissolve
    n "I'm sorry... You have nothing to do with it."
    show nana2 1f 2b 3d at u11 as nana with dissolve
    p "What happened?"
    show nana2 1d 2b 3d at u11 as nana with dissolve
    n "Don't think you'll understand, [player_name]."
    show nana2 1g 2b 3d at u11 as nana with dissolve
    p "Can't say unless I give it a try."
    show nana2 1d 2a 3a at u11 as nana with dissolve
    n "Well, if you insist..."
    show nana1 1e 2d 3c regular1 blush at u11 as nana with dissolve
    n "I can't take it anymore... People are so scripted!"
    show nana1 1f 2d 3c regular2 at u11 as nana with dissolve
    p "Scripted? Predictable, you mean?"
    show nana1 1d 2d 3c regular2 at u11 as nana with dissolve
    n "Yes, to put it mildly..."
    show nana1 1f 2a 3a regular2 noblush at u11 as nana with dissolve
    n "Have you ever played a role-playing game, [player_name]?"
    show nana1 1g 2a 3d regular2 at u11 as nana with dissolve
    p "Um..."
    show nana1 1b 2c 3b regular1 blush at u11 as nana with dissolve
    n "Hey, not {i}that{/i} kind of a game, you silly!"
    show nana3 1e 2c 3d noblush at u11 as nana with dissolve
    n "A computer game where you have a few main characters, a side cast..."
    show nana3 1b 2a 3a at u11 as nana with dissolve
    n "And then a lot of non-playable characters to enrich the game lore."
    show nana3 1c 2b 3d at u11 as nana with dissolve
    n "Your interaction with the latter is limited to just a couple of phrases..."
    show nana3 1e 2a 3a at u11 as nana with dissolve
    n "It's because they're usually scripted only to serve a certain game purpose."
    show nana3 1b 2a 3d at u11 as nana with dissolve
    n "Guess what, it seems that our life is no different."
    show nana3 1g 2a 3d at u11 as nana with dissolve
    p "What do you mean?"
    show nana1 1e 2a 3d regular2 at u11 as nana with dissolve
    n "I think eighty percent of people, if not more, are non-playable characters."
    show nana1 1g 2a 3d regular2 at u11 as nana with dissolve
    p "C'mon, it's not true..."
    show nana1 1c 2b 3a regular2 at u11 as nana with dissolve
    n "Maybe I'm wrong, but then tell me... why are they so shallow?"
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "Try to throw in an unconventional reply when chatting to these people..."
    show nana2 1d 2b 3a at u11 as nana with dissolve
    n "Next thing you know, there's that particularly blank expression in their eyes."
    show nana2 1c 2b 3d at u11 as nana with dissolve
    n "You broke the script, and they're not programmed to handle that."
    show nana2 1f 2b 3d at u11 as nana with dissolve
    p "Oh wow, Nana... At least now it's clear why you were silent in the beginning."
    show nana2 1c 2b 3a at u11 as nana with dissolve
    n "\"Ready for the career day tomorrow?\""
    show nana3 1d 2a 3a at u11 as nana with dissolve
    n "If I say yes, would you be delighted? If I say no, would you offer immediate help?"
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "I doubt it. Truth is, only expected a reply that'd abide by the script."
    show nana1 1f 2b 3d regular2 at u11 as nana with dissolve
    n "Something you could reply to with \"Oh, I see\" and all."
    show nana1 1a 2a 3d regular2 at u11 as nana with dissolve
    p "Well, how do you expect me to communicate?"
    show nana1 1e 2d 3a regular1 blush at u11 as nana with dissolve
    n "I'd expect anyone, you included, to keep silent if there's nothing to say."
    show nana1 1f 2d 3a regular2 at u11 as nana with dissolve
    n "People just can't shut up, and you know why?"
    show nana1 1d 2d 3c regular2 at u11 as nana with dissolve
    n "Because they're afraid to start thinking instead of talking."
    show nana2 1d 2b 3d noblush at u11 as nana with dissolve
    n "Thinking process can lead to a rather unpleasant self-realization..."
    show nana2 1d 2a 3a at u11 as nana with dissolve
    n "That is, how shallow you are. This kills the non-playable character."
    show nana2 1f 2b 3d at u11 as nana with dissolve
    p "What's so bad about discussing something conventional... like hobbies?"
    show nana2 1d 2a 3a at u11 as nana with dissolve
    n "Nothing, but then it goes down the same alley."
    show nana3 1e 2a 3a at u11 as nana with dissolve
    n "Music? No one knows anything outside the top charts."
    show nana3 1b 2a 3d at u11 as nana with dissolve
    n "Movies? Same, people only watch what's trending today."
    show nana2 1b 2b 3a at u11 as nana with dissolve
    n "\"Trending\" is the keyword here."
    show nana2 1c 2b 3d at u11 as nana with dissolve
    n "Non-playable characters don't have hobbies, they follow the trend."
    show nana2 1a 2b 3d at u11 as nana with dissolve
    p "Now that you mention it... Internet subculture is going mainstream..."
    show nana1 1d 2d 3a regular2 at u11 as nana with dissolve
    n "We're the meme generation, [player_name]."
    show nana1 1e 2a 3d regular1 at u11 as nana with dissolve
    n "It's even worse when they start enjoying {i}my{/i} hobbies."
    show nana1 1f 2a 3a regular2 at u11 as nana with dissolve
    p "What're you into?"
    show nana3 1c 2a 3a at u11 as nana with dissolve
    n "Swimming, for instance."
    show nana3 1a 2a 3a at u11 as nana with dissolve
    p "So what if swimming becomes the next hot topic?"
    show nana3 1c 2d 3d at u11 as nana with dissolve
    n "Then my local pool will be crowded with people who can't swim at all."
    show nana2 1b 2b 3b at u11 as nana with dissolve
    n "They don't even want to learn, they're here because everyone else is."
    show nana2 1d 2b 3d at u11 as nana with dissolve
    n "I'd close that pool for being too shallow."
    show nana2 1a 2b 3a at u11 as nana with dissolve
    p "Jeez, Nana, isn't it a bit too much?"
    p "You're simply calling the majority of people fools."
    show nana3 1d 2a 3d at u11 as nana with dissolve
    n "I've never ever called them like that."
    show nana3 1c 2a 3d at u11 as nana with dissolve
    n "In a way, they are the smarter ones, as they fit in seamlessly."
    show nana1 1e 2b 3d regular2 at u11 as nana with dissolve
    n "While I... I just stand out like a sore thumb."
    show nana1 1f 2c 3a regular2 at u11 as nana with dissolve
    n "..."
    show nana1 1f 2b 3a regular2 blush at u11 as nana with dissolve
    n "My, I've actually gone a bit too far."
    show nana1 1c 2b 3a regular2 at u11 as nana with dissolve
    n "Please don't take what I said close to heart, alright?"
    show nana2 1c 2b 3b at u11 as nana with dissolve
    n "I'm a bit ashamed of this confession."
    show nana2 1f 2b 3a at u11 as nana with dissolve
    p "Well, sorry for scripted replies, I guess."
    show nana1 1d 2c 3a regular2 noblush at u11 as nana with dissolve
    n "You're not like that."
    show nana3 1c 2a 3a at u11 as nana with dissolve
    n "I'm even thinking... You know, it's just a maybe!"
    show nana3 1b 2c 3d at u11 as nana with dissolve
    n "Maybe my life gets less boring every time I talk to you."
    show nana1 1d 2a 3a regular1 at u11 as nana with dissolve
    n "You made me light up a bit. Thanks!"
    show nana1 1b 2a 3a regular2 blush at u11 as nana with dissolve
    n "Looking forward to see you tomorrow!"
    hide nana with dissolve

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            call flyers_nana from _call_flyers_nana_2
            play music "music/cafe_music.ogg" fadeout 1 fadein 1
            scene black with fade
            $ renpy.pause(1, hard=True)
            scene cafe
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump nana_invite

    if nana_plusset == True:
        scene black with fade
        call flyers_nana from _call_flyers_nana_3
        play music "music/cafe_music.ogg" fadeout 1 fadein 1
        scene black with fade
        $ renpy.pause(1.0, hard=True)
        scene cafe
        "We're about to get going."
        "In fact, Teya already left us."
        "I am waiting for the girls to return from the bathroom."
        jump nana_invite
    jump day2_end
label day2_road_home_sima:
    $ g_p_2 = 3
    if persistent.game_done1 == None:
        call after_help_teya from _call_after_help_teya_2
    call after_help_sima from _call_after_help_sima
    call day2_road_home from _call_day2_road_home_2
    "It's Sima."
    show sima2 1c 2a 3a regular2 at u11 as sima with dissolve
    s "Hi, [player_name]."
    show sima2 1e 2a 3a regular2 at u11 as sima with dissolve
    s "From a distance, it looks like you don't know where to go."
    show sima2 1g 2a 3a regular2 at u11 as sima with dissolve
    p "Doesn't matter as long as you keep me company."
    show sima2 1e 2b 3d regular2 blush at u11 as sima with dissolve
    s "Oh..."
    show sima2 1d 2a 3a regular1 blush at u11 as sima with dissolve
    s "How's your week going, [player_name]?"
    show sima2 1a 2a 3a regular1 noblush at u11 as sima with dissolve
    p "Going great! Just a little bit tired..."
    show sima2 1d 2a 3b regular1 at u11 as sima with dissolve
    s "Get some rest so you'll be ready for career day."
    show sima2 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Excited about it?"
    show sima3a 1c 2a 3d at u11 as sima with dissolve
    s "I am! I am..."
    show sima3a 1a 2a 3a at u11 as sima with dissolve
    s "..."
    p "Did I say something wrong?"
    show sima3a 1c 2a 3d at u11 as sima with dissolve
    s "Nothing at all! It's just... you see..."
    show sima3a 1d 2d 3a at u11 as sima with dissolve
    s "I'm in a constant fear of missing out."
    show sima3a 1a 2d 3a at u11 as sima with dissolve
    p "What do you mean?"
    show sima1 1c 2b 3b at u11 as sima with dissolve
    s "I always think I should've been busy with something else."
    show sima3a 1d 2b 3d at u11 as sima with dissolve
    s "Maybe I should've gone to another school?"
    show sima3a 1d 2b 3a at u11 as sima with dissolve
    s "A few years ago I declined an invitation for a movie audition..."
    show sima3a 1c 2d 3d at u11 as sima with dissolve
    s "What if I missed the opportunity of a lifetime?"
    show sima1 1c 2b 3a at u11 as sima with dissolve
    s "Tomorrow won't be any different."
    show sima1 1a 2b 3b at u11 as sima with dissolve
    s "I know it probably sounds laughable..."
    p "Is there anything to laugh about?"
    show sima2 1e 2b 3d regular2 at u11 as sima with dissolve
    s "Trust me, there is, simply because..."
    show sima2 1c 2b 3a regular1 at u11 as sima with dissolve
    s "\"Nothing matters very much, and few things matter at all.\""
    show sima2 1a 2b 3d regular2 at u11 as sima with dissolve
    p "Care to explain?"
    show sima2 1e 2a 3d regular2 at u11 as sima with dissolve
    s "Well, it's a long story... Maybe next time, [player_name]."
    show sima3a 1d 2d 3a at u11 as sima with dissolve
    s "By the way, I'm a root of that fear for some. Funny, isn't it?"
    show sima3a 1a 2d 3a at u11 as sima with dissolve
    p "What do you mean?"
    show sima3a 1e 2b 3d at u11 as sima with dissolve
    s "Others often think they miss out on something {i}I{/i} do."
    show sima2 1d 2a 3a regular1 at u11 as sima with dissolve
    s "If I stay late studying, so that the next day I have dark circles under my eyes..."
    show sima2 1c 2a 3b regular2 at u11 as sima with dissolve
    s "Other girls would gossip about me spending the whole night out."
    show sima2 1d 2a 3a regular1 at u11 as sima with dissolve
    s "If they invite me somewhere, and I'm busy, they think that I simply reject them."
    show sima2 1c 2d 3a regular2 at u11 as sima with dissolve
    s "That I have something better to do."
    show sima2 1d 2b 3a regular2 at u11 as sima with dissolve
    s "See why is it so amusing?"
    show sima2 1a 2b 3b regular2 at u11 as sima with dissolve
    s "They're envious about missing out on something they imagine I'm doing..."
    show sima2 1c 2b 3d regular2 at u11 as sima with dissolve
    s "Something that doesn't even exist."
    show sima2 1c 2b 3a regular2 at u11 as sima with dissolve
    s "They also say they can't understand me... that I look reserved."
    show sima2 1d 2d 3a regular1 blush at u11 as sima with dissolve
    s "In the end, they stop approaching me altogether... I'm not reserved!"
    show sima2 1d 2d 3c regular1 blush at u11 as sima with dissolve
    s "It's simply my everyday expression! I'm sorry, you know!"
    show sima2 1d 2d 3b regular1 blush at u11 as sima with dissolve
    s "Sorry that I don't look like your average cheerleader..."
    show sima2 1a 2d 3a regular1 blush at u11 as sima with dissolve
    p "Wow... I mean, I'd think you're very popular if we just met..."
    show sima1 1d 2b 3d blush at u11 as sima with dissolve
    s "That's exactly what everyone assumes, [player_name]."
    show sima1 1d 2b 3b blush at u11 as sima with dissolve
    s "Oh well, it only means I should treasure those who see the real me."
    show sima1 1a 2a 3a blush at u11 as sima with dissolve
    p "I'd be happy to learn more about the real you, Sima."
    show sima1 1e 2a 3b blush at u11 as sima with dissolve
    s "Is that so?"
    show sima1 1c 2a 3a blush at u11 as sima with dissolve
    s "What if you simply lose the interest after a while?"
    show sima1 1e 2b 3a blush at u11 as sima with dissolve
    s "What if you find me pretty boring?"
    show sima1 1d 2a 3a noblush at u11 as sima with dissolve
    s "It'd be painful, [player_name]."
    show sima1 1c 2a 3b noblush at u11 as sima with dissolve
    s "I hate losing people after I grow accustomed to them."
    show sima1 1a 2a 3a blush at u11 as sima with dissolve
    p "I'd never do something like this."
    p "But if you think I should stay away, just let me know."
    show sima2 1c 2c 3a regular2 at u11 as sima with dissolve
    s "I can't... I'd be missing out!"
    show sima2 1d 2b 3b regular2 at u11 as sima with dissolve
    s "Oh my, I making a fool out of myself..."
    show sima2 1c 2a 3a regular2 at u11 as sima with dissolve
    s "D-do you mean what you said about willing to know me better?"
    show sima2 1a 2a 3a regular2 at u11 as sima with dissolve
    p "I do."
    show sima3a 1d 2a 3a at u11 as sima with dissolve
    s "Well, time will show if it's true..."
    show sima3b 1e 2a 3a noblush at u11 as sima with dissolve
    s "I look forward to seeing you tomorrow!"
    show sima3b 1e 2a 3b at u11 as sima with dissolve
    p "Whoa, did you really say this?"
    show sima2 1e 2c 3b regular1 at u11 as sima with dissolve
    s "So what if I did?"
    show sima2 1d 2c 3a regular1 at u11 as sima with dissolve
    s "It's one of the better sides of being a girl..."
    show sima3b 1e 2c 3a at u11 as sima with dissolve
    s "I can say a lot, but then pretend it means nothing!"
    show sima3a 1d 2a 3a at u11 as sima with dissolve
    s "On that note... It's time for me to go. See you!"
    hide sima with dissolve

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            call flyers_sima from _call_flyers_sima_2
            play music "music/cafe_music.ogg" fadeout 1 fadein 1
            scene black with fade
            $ renpy.pause(1, hard=True)
            scene cafe
            "We're about to get going."
            "In fact, Teya already left us."
            "I am waiting for the girls to return from the bathroom."
            jump sima_invite

    if sima_plusset == True:
        scene black with fade
        call flyers_sima from _call_flyers_sima_3
        play music "music/cafe_music.ogg" fadeout 1 fadein 1
        scene black with fade
        $ renpy.pause(1.0, hard=True)
        scene cafe
        "We're about to get going."
        "In fact, Teya already left us."
        "I am waiting for the girls to return from the bathroom."
        jump sima_invite
    jump day2_end
label day2_road_home_not_yet:
    $ g_p_2 = 4
    call after_help_teya from _call_after_help_teya_3
    call after_help_ermy from _call_after_help_ermy
    call day2_road_home from _call_day2_road_home_3
    "It's Ermy."
    show ermy1 pose2 1d 2a 3a at u11 as ermy
    e "Hey, what's up?"
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "Nothing much, going home."
    show ermy1 pose2 1b 2c 3c at u11 as ermy with dissolve
    e "I am envious!"
    show ermy1 pose2 1e 2a 3a at u11 as ermy with dissolve
    p "Why?"
    show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
    e "Three girls asked you to help them tomorrow!"
    show ermy1 pose2 1c 2c 3c at u11 as ermy with dissolve
    e "That's right, three... at the same time!"
    show ermy1 pose2 1e 2a 3a at u11 as ermy with dissolve
    p "Well, it's not like they asked me out."
    show ermy1 pose1 1c 2b 3d at d11 as ermy with dissolve
    e "Still, you'll have fun tomorrow, while I..."
    show ermy1 pose2 1a 2a 3d at d11 as ermy with dissolve
    p "Cheer up, Ermy, it's such a small thing... Don't bother."
    show ermy1 pose2 1c 2b 3d at d11 as ermy with dissolve
    e "It's small, but it follows a clear pattern..."
    show ermy1 pose2 1a 2b 3d at d11 as ermy with dissolve
    p "What're you talking about?"
    show ermy1 pose2 1c 2b 3d at d11 as ermy with dissolve
    e "I don't play the main role even in my own life."
    show ermy1 pose2 1c 2b 3a at d11 as ermy with dissolve
    e "I feel like I just observe things happen...."
    show ermy1 pose2 1f 2b 3d at d11 as ermy with dissolve
    p "Ermy, c'mon, we're in high school... Wait till you grow up."
    show ermy1 pose2 1e 2b 3a at d11 as ermy with dissolve
    e "Every morning I ask myself why..."
    show ermy1 pose2 1e 2b 3b at d11 as ermy with dissolve
    e "Why? Why am I here?"
    show ermy1 pose2 1g 2b 3d at d11 as ermy with dissolve
    e "You know what? I never come up with a decent reason."
    show ermy1 pose2 1h 2a 3d at d11 as ermy with dissolve
    e "I don't know whether I'm alive or still sleeping."
    show ermy1 pose2 1h 2b 3c at d11 as ermy with dissolve
    e "I don't really feel anything."
    show ermy1 pose2 1f 2b 3d at d11 as ermy with dissolve
    p "Ermy, are you serious?"
    show ermy1 pose2 1g 2b 3d at d11 as ermy with dissolve
    e "Trust me, I am."
    show ermy1 pose2 1g 2b 3b at d11 as ermy with dissolve
    e "I act and look foolish way too often, but I can't help it..."
    show ermy1 pose2 1e 2b 3a at d11 as ermy with dissolve
    e "Something feels off for me. I can't concentrate on a single thing."
    show ermy1 pose2 1c 2b 3a at d11 as ermy with dissolve
    e "Regardless of what I do, I feel tired in an hour."
    show ermy1 pose2 1e 2a 3a at d11 as ermy with dissolve
    e "It's like I flow down the river, and the current gets stronger every day."
    show ermy1 pose2 1c 2b 3d at d11 as ermy with dissolve
    e "But... I don't know where to swim. I can't swim, for starters."
    show ermy1 pose1 1h 2b 3a at d11 as ermy with dissolve
    e "Lately, the only thing I can do is play games... oh, and watch videos."
    show ermy1 pose1 1f 2b 3b at d11 as ermy with dissolve
    e "But even that doesn't spark joy."
    show ermy1 pose2 1h 2d 3a at d11 as ermy with dissolve
    e "I can't really get indulged in it, and I hate myself for killing time."
    show ermy1 pose2 1a 2b 3a at d11 as ermy with dissolve
    p "..."
    p "Well, if it's true..."
    p "Please don't take as an insult or anything like this, okay?"
    p "Maybe you should visit a doctor? Just saying..."
    show ermy1 pose2 1h 2d 3d at u11 as ermy with dissolve
    e "A doctor? What for? So he could give some pills to feel happy?"
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "Unlike others, I'm well aware that it doesn't solve the problem at all."
    show ermy1 pose2 1f 2d 3d at u11 as ermy with dissolve
    p "Still, think about it. Also... It will get better, trust me."
    show ermy1 pose2 1c 2d 3d at u11 as ermy with dissolve
    e "Yeah, sure.... it will. I'll definitely {i}settle{/i} for something."
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "Screw that."
    hide ermy with dissolve
    "He leaves without saying good-bye."
    jump day2_end
label day2_end:
    "Alright, time to go home."
    scene black with fade
    stop music fadeout 2
    $ renpy.pause(2, hard=True)
    jump sweet_home_d2
return

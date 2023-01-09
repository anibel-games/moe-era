label intro:
    stop music fadeout 2
    $ s_name = "Sima"
    $ m_name = "Marta"
    $ n_name = "Nana"
    $ t_name = "Teya"
    if persistent.game_done2 == True:
        $ game_restarted2 = 1
        $ c_name = "Tyche"
        $ e_name = "Ermy"
        scene black with fade
        $ renpy.pause(2, hard=True)
        jump catgirl_extra9
    if persistent.game_done1 == True:
        $ game_restarted1 = 1
        $ c_name = "Tyche"
        $ e_name = "Ermy"
        scene black with fade
        $ renpy.pause(2, hard=True)
        jump new_game_plus1
    $ e_name = "???"
    $ c_name = "???"
    scene black
    $ renpy.pause(4, hard=True)
    show arch_nonf with eye_open
    $ renpy.pause(1.2, hard=True)
    scene black with eye_shut
    $ renpy.pause(.4, hard=True)
    scene arch_nonf with eye_open_fast
    $ renpy.pause(0.2, hard=True)
    scene black with eye_shut_fast
    $ renpy.pause(0.2, hard=True)
    scene arch_nonf with eye_open_fast
    $ renpy.pause(0.2, hard=True)
    scene black with eye_shut_fast
    $ renpy.pause(1.5, hard=True)
    play music "music/newIntro.ogg"
    $ renpy.pause(0.35, hard=True)
    scene arch_intro_p
    show teya_intro_whoops1 as teya:
        xpos -25
    with flash
    t "Whooops!"
    show teya_intro_whoops2 as teya with dissolve:
        xpos -25
    t "Now I've got your attention!"
    show teya2 1b 2a 3a regularhand1 at ui11 as teya with dissolve
    $ renpy.pause(0.3, hard=True)
    show teya3 1c 2a 3a at u11 as teya with dissolve
    t "Human attention span is way too short, so..."
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Let's get straight to the point!"
    show teya2 1b 2a 3a regularhand4 at u11 as teya with dissolve
    t "You see, [player_name], they say that..."
    scene cg_teya_intro_you_see with fade
    window hide
    $renpy.transition(dissolve)
    show screen scr_intro_you_see
    $ renpy.pause(4, hard=True)
    pause
    $renpy.transition(dissolve)
    scene cg_teya_intro_you_not with dissolve
    hide screen scr_intro_you_see
    show screen scr_intro_but_you
    $ renpy.pause(2, hard=True)
    pause
    $renpy.transition(dissolve)
    hide screen scr_intro_but_you
    scene arch_intro_p
    show teya2 1b 2a 3a regularhand1 at u11 as teya
    with fade
    $ renpy.pause(1, hard=True)
    scene arch_intro_t_m:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    window show
    scene arch_intro_b
    show marta3 1a 2c 3a regular1 blush at ui11 as marta
    with dissolve
    show marta3 1e 2c 3a regular1 at u11 as marta with dissolve
    m "Yeah, [player_name], why don't you tell us..."
    show marta2 1b 2b 3a regular2 at u11 as marta with dissolve
    m "What's your life about?"
    show marta3 1g 2b 3b regular1 at u11 as marta with dissolve
    m "I'm {i}so{/i} excited to learn all about it!"
    show marta1 1g 2a 3b at u11 as marta with dissolve
    m "My, sounds so... {w}phony.{w=1}{nw}"
    show marta1 1g 2a 3d at u11 as marta with dissolve
    show cg_marta_phony with fade
    window hide
    show screen scr_marta_phony
    $ renpy.pause(4, hard=True)
    pause
    hide screen scr_marta_phony
    hide cg_marta_phony
    with fade
    window show
    show marta1 1b 2a 3b at u11 as marta with dissolve
    m "I'm such a horrible actor..."
    show marta1 1g 2a 3b at u11 as marta with dissolve
    $ renpy.pause(.3, hard=True)
    scene arch_intro_m_s:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_o
    show sima2 1e 2a 3a regular1 at ui11 as sima
    with dissolve
    show sima2 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Hey, I thought we decided to get straight to the point!"
    show sima2 1e 2b 3a regular2 at u11 as sima with dissolve
    s "[player_name], we {i}really{/i} need your help."
    show sima3a 1c 2b 3a at u11 as sima with dissolve
    s "Trust me, it's not a trivial issue..."
    scene arch_empty
    show cg_the
    show sima2fullscale 1a 2a 3a regular2 as sima behind cg_the:
        xpos 750
        yalign .2
    with fade
    show sima2fullscale 1c 2a 3a regular2 as sima behind cg_the with dissolve:
        xpos 750
        yalign .2
        alpha 1
        pause 2.8
        linear .5 alpha 0
    show sima2fullscale 1e 2a 3d regular2 as sima2 behind cg_the:
        xpos 750
        yalign .2
        alpha 0
        pause 1.8
        linear .5 alpha 1
    s "Look, [player_name]... {w=2}this is the story of your life."
    show sima2fullscale 1e 2b 3a regular2 as sima2 behind cg_the with dissolve:
        xpos 750
        yalign .2
    s "It appears to be a little... {w=1.5}too empty, don't you think so?"
    scene arch_intro_o
    hide sima2
    show sima1 1c 2b 3a at u11 as sima
    with fade
    s "The thing is, we've allegedly lost its content."
    show sima1 1d 2b 3b at u11 as sima with dissolve
    s "We have too many lives on our hands..."
    show sima2 1c 2a 3a regular2 at u11 as sima with dissolve
    s "I used the word \"allegedly\" on purpose."
    show sima3a 1d 2a 3d at u11 as sima with dissolve
    s "See, there's another possible explanation for that gaping void."
    show sima3a 1e 2a 3b blush at u11 as sima with dissolve
    s "If your life is meaningless, there's nothing to write about!"
    show sima3b 1e 2c 3d blush at u11 as sima with dissolve
    s "But I'm sure that's not the case with you. Right?"
    scene cg_sima_right with fade
    show screen scr_sima_right1
    pause
    hide screen scr_sima_right1
    scene arch_intro_o
    show sima3b 1e 2c 3d blush at u11 as sima
    with fade
    $ renpy.pause(1, hard=True)
    scene arch_intro_s_n:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_g
    show nana3 1a 2a 3d at ui11 as nana
    with dissolve
    show nana3 1e 2a 3d at u11 as nana with dissolve
    n "C'mon, of course it's not true."
    show nana2 1d 2b 3b at u11 as nana with dissolve
    n "Let's admit it, we're to blame. Luckily, everything can be fixed."
    show nana2 1c 2b 3d at u11 as nana with dissolve
    n "You could just tell us what your life is about."
    hide nana
    show nana2 1c 2b 3d at ui11 as nana2:
        ypos 1250
        alpha 1
        pause 1.4
        linear 0.5 alpha 0
    show nana2 1b 2a 3a at ui11 as nana1:
        ypos 1250
        alpha 0
        pause 1.0
        linear 0.5 alpha 1
    show arch_intro_p_baw behind nana1,nana2:
        alpha 0
        pause 1
        linear 0.8 alpha 1
    n "But how would we know...{w=1.5} if you're telling the {i}truth{/i}?"
    hide nana1
    hide nana2
    show nana2 1b 2a 3a at ui11 as nana
    $ renpy.pause(.01, hard=True)
    hide arch_intro_p_baw
    show nana1 1d 2a 3d regular2 at u11 as nana
    with dissolve
    n "Instead, I think it's better to observe you for a while."
    show nana1 1e 2b 3a regular1 at u11 as nana with dissolve
    n "That'll be the best way to fill in the blanks, don't you think?"
    show nana1 1a 2b 3a regular1 at u11 as nana with dissolve
    scene arch_intro_n_t:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_p
    show teya2 1a 2a 3a regularhand3 at ui11 as teya
    with dissolve
    show teya2 1e 2a 3a regularhand3 at u11 as teya with dissolve
    t "Don't worry, [player_name], we won't bother you for too long."
    show teya3 1d 2a 3b at u11 as teya with dissolve
    t "Oh, and no alternate realities or time travel! We need you to be the real you."
    show teya1 1c 2a 3a at u11 as teya with dissolve
    t "That's why we'll conduct the observation in your natural habitat."
    show teya3 1b 2b 3b blush at u11 as teya with dissolve
    t "Sounds a bit rude, I admit, but you get the point."
    show teya2 1c 2a 3a regularhand2 noblush at u11 as teya with dissolve
    t "Just be yourself, [player_name]!"
    show teya2 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "A few days is all we need to get the story of your life back."
    show teya1 1c 2a 3b at u11 as teya with dissolve
    t "I'll do my best to make these days magical, you hear?"
    show teya2 1e 2a 3a regularhand1 blush at u11 as teya with dissolve
    t "You're guaranteed to create happy memories that will last a lifetime!"
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Have fun! Just remember..."
    show teya2 1b 2a 3b blush regularhand1 at u11 as teya with dissolve
    t "Life is about..."
    scene arch_intro_p_baw
    show teya2_baw 1b 2a 3b blush regularhand1 at ui11 as teya
    with dissolve
    $ renpy.pause(.3, hard=True)
    c "Choices!"
    stop music fadeout 2
    scene black with eye_shut
    $ renpy.pause(1, hard=True)
    show jp_classroom_matrix_animation with eye_open:
        size (1920, 1080)
        alpha .2
    scene black with eye_shut
    $ renpy.pause(0.5, hard=True)
    play music "music/japan_night_theme.ogg" fadein 3
    scene jp_classroom_matrix_animation with eye_open:
        size (1920, 1080)
    $ renpy.pause(2.0, hard=True)
    c "Psst, [player_name]!"
    c "Can you hear me?"
    c "Not sure what happened, but I'm kind of stuck here..."
    c "Come and see for yourself!"
    show right_here:
        alpha 0
        linear .5 alpha 1
        linear .5 alpha 0
    c "Here! I'm right here!"
    show right_here:
        alpha 0
        linear .5 alpha 1
        linear .5 alpha 0
    c "The whiteboard, [player_name]!"
    stop sound fadeout 5.0
    scene whiteboard:
        size (1920, 1080)
    show cat1t:
        xalign 0.01
        yalign 0.45
    with fade
    catgirl_text 'Hello, mortal!'
    catgirl_text 'Or should I keep referring to you by name?'
    catgirl_text 'Sorry I look like this. Can\'t do anything...'
    catgirl_text 'Well, at least I can change the vibe a bit!'
    scene whiteboard3:
        size (1920, 1080)
    show cat1:
        xalign 0.01
        yalign 0.45
    play sound "sound/finger_snap.ogg"
    play music "music/catgirl.ogg"
    catgirl_text 'Yes, much better now.'
    catgirl_text 'By the way, I’m a living human girl!'
    catgirl_text 'Don’t believe me?'
    catgirl_text 'Fine! I\'ll prove it!'
    hide cat1
    show cat1t:
        xalign 0.01
        yalign 0.45
        linear 1 alpha 0.3
        pause 0.5
        linear 2 alpha 0.5
        pause 2.5
        linear 2 alpha 0.3
        repeat
    with dissolve
    $ renpy.pause(1, hard=True)
    show cat2 with dissolve:
        xalign 0.35
        yalign 0.25
    catgirl_text 'See, I walk on my two feet just fine!'
    catgirl_text 'You have no other choice but to admit it...'
    catgirl_text 'I\'m a real human being!'
    catgirl_text 'Maybe you\'re confused about my tail and cat ears, though...'
    catgirl_text 'Well, I\'m just lucky enough to have things like that.'
    catgirl_text 'I\'m a lucky girl.'
    catgirl_text 'Do you believe in luck, [player_name]?'
    show cat2t with dissolve:
        xalign 0.35
        yalign 0.25
        linear 1 alpha 0.3
        pause 1
        linear 1.5 alpha 0.5
        pause 1
        linear 1 alpha 0.3
        repeat
    hide cat2
    with dissolve
    $ renpy.pause(1, hard=True)
    show cat3 with dissolve:
        xalign 0.69
        yalign 0.4
    catgirl_text 'I hope you do... luck is crucial!'
    catgirl_text 'See, your life is about the choices you make.'
    catgirl_text 'Guess what, to make a good one...'
    catgirl_text 'You need luck!'
    catgirl_text 'Which reminds me, I have plenty of luck to share with you!'
    catgirl_text 'From now on, every time you stand at the crossroads...'
    catgirl_text 'Just look around and you may see me!'
    catgirl_text 'Well, maybe not {i}every{/i} time, I do need to sleep, ya know.'
    show cat3t:
        zoom 1
        xalign 0.69
        yalign 0.4
        linear 2 alpha 0.3
        pause 0.5
        linear 1 alpha 0.5
        pause 0.5
        linear 1 alpha 0.3
        repeat
    hide cat3
    with dissolve
    $ renpy.pause(2, hard=True)
    show cat4 as cat4 with dissolve:
        xpos 1250
        yalign 0.2
    catgirl_text 'Actually, I feel like taking a nap right now.'
    catgirl_text 'You\'re going to have a memorable time this week.'
    catgirl_text 'Who knows, maybe it\'s a beginning of a new era!'
    catgirl_text 'Please enjoy it, okay?'
    catgirl_text 'Okay, here goes...'
    show cat4t as cat4 with dissolve:
        zoom 1
        xpos 1250
        yalign 0.2
    stop music fadeout 3
    $ renpy.pause(2, hard=True)
    scene black with fade
    $ renpy.pause(1, hard=True)
    jump backrooms_d1
return

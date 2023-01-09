label day4:
    scene black with fade
    $ renpy.pause(2, hard=True)
    jump d4_wake_up
label d4_wake_up:
    scene room_v1 with eye_open
    show noise:
        alpha 0.05
        linear .3 alpha 0
    "I woke up with a slight headache."
    show noise:
        alpha 0.05
        linear .3 alpha 0
    "It's like I had a fever yesterday..."
    "Well, who cares about yesterday? {i}Today{/i} is the day!"

    if g_p_3 == 4:
        scene black with fade
        stop music fadeout 1.5
        $ renpy.pause(2, hard=True)
        jump date_ermy

    if g_p_3 == 1:
        if g_p_2 == 1:
            if g_p_1 == 1:
                scene black with fade
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump date_nana
            else:
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump fake_date_nana
        else:
            stop music fadeout 1.5
            $ renpy.pause(2, hard=True)
            jump fake_date_nana

    if g_p_3 == 2:
        if g_p_2 == 2:
            if g_p_1 == 2:
                scene black with fade
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump date_marta
            else:
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump fake_date_marta
        else:
            stop music fadeout 1.5
            $ renpy.pause(2, hard=True)
            jump fake_date_marta

    if g_p_3 == 3:
        if g_p_2 == 3:
            if g_p_1 == 3:
                scene black with fade
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump date_sima
            else:
                stop music fadeout 1.5
                $ renpy.pause(2, hard=True)
                jump fake_date_sima
        else:
            stop music fadeout 1.5
            $ renpy.pause(2, hard=True)
            jump fake_date_sima
label fake_date_sima:
    play sound "sound/phone.ogg"
    $ renpy.pause(1, hard=True)
    "Whoa, an incoming call."
    play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
    show sima2 1e 2a 3a regular2 at u11 as sima:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Hi, [player_name]! How are you today?"
    show sima2 1a 2a 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "Feeling like a million bucks, and you?"
    show sima2 1c 2b 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "All good!"
    show sima2 1e 2b 3d regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Look, you haven't left your place yet, have you?"
    show sima2 1a 2b 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "No, but don't worry, I'll be on time!"
    p "There's no way I'm going to make you wait."
    show sima1 1a 2b 3a at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "..."
    show sima1 1c 2b 3a at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "Um, [player_name], you see... I hate to say this..."
    show sima1 1c 2b 3b blush at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "I won't be able to make it today. Sorry! I'm really sorry!"
    show sima1 1a 2b 3b noblush at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    p "I... I see."
    show sima1 1a 2b 3a at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    p "I mean, stuff like this happens, right? Haha..."
    show sima1 1d 2b 3d at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "I'm sorry!"
    show sima1 1a 2b 3d at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    p "Hey, it's fine. Let's meet tomorrow!"
    show sima3a 1c 2b 3d at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "I'm afraid my whole weekend is booked..."
    show sima3a 1a 2b 3d at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "How about next week?"
    show sima3a 1d 2a 3d at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Sounds fine!"
    show sima3a 1a 2a 3d at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "Then... next Saturday?"
    show sima3a 1e 2a 3b at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Let's talk on Friday, okay? You know how hectic a week can be."
    show sima3a 1a 2a 3b at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "Yeah..."
    show sima2 1d 2a 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "You're so nice!"
    show sima2 1a 2a 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    "\"Nice\"..."
    p "By the way, what happened? Need my help?"
    show sima2 1a 2a 3a blush regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "..."
    show sima2 1e 2a 3a blush regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "I'll be fine, but thanks for asking."
    show sima1 1d 2b 3a noblush at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "See, a childhood friend of mine decided to visit the city."
    show sima1 1e 2a 3a blush at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "His name is Chad. I haven't seen him for years!"
    show sima3a 1e 2a 3b noblush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "He's a junior at one of the Ivy League schools."  #Fixed in None
    show sima3b 1e 2a 3b blush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Chad must've grown up, as he mentioned playing basketball there..."
    show sima3a 1c 2a 3a blush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Duke! I think he's at Duke."
    show sima3a 1a 2a 3a noblush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "..."
    p "Well, have fun!"
    p "I'm sure it's going to be a great weekend for you."
    show sima1 1d 2a 3a noblush at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "Thanks! You have some fun too, okay?"
    show sima1 1d 2a 3b at u11 as sima with dissolve:
        xalign -.08
        ypos 1800
        zoom 1.1
    s "I promise to find some time next weekend!"
    show sima2 1e 2a 3b regular1 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Being together with my new friend is top priority."
    show sima2 1a 2a 3a regular1 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "F-friend?"
    show sima2 1d 2a 3a regular2 at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Yes! Let's be friends, [player_name]!"
    show sima3a 1e 2a 3a blush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "See? I'm not ashamed of saying it first!"
    show sima3a 1a 2a 3a blush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    p "But... I..."
    show sima3a 1e 2a 3a noblush at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "I really need to run now."
    show sima3a 1e 2a 3b at u11 as sima with dissolve:
        xalign -.03
        ypos 1800
        zoom 1.1
    s "Drop me a message tomorrow, okay?"
    p "Bye."
    hide sima with dissolve

    $achievement.grant("Friendzone")
    init:
        $achievement.register("Friendzone")
        $achievement.sync()
    $achievement.sync()

    "She hangs up."
    jump failed_date
label date_sima:
    play music "music/admit.ogg"
    $ renpy.pause(1.0, hard=True)
    scene cafe with fade
    $ renpy.pause(2.0, hard=True)
    show sima2close 1e 2c 3a fancy2 at u11 as sima
    "Sima arrives five minutes late."
    "Something tells me it was carefully planned."
    "I make a visible effort to concentrate on her eyes."
    show sima2close 1c 2a 3a fancy2 at u11 as sima with dissolve
    s "How are you, [player_name]?"
    show sima2close 1e 2a 3d fancy1 at u11 as sima with dissolve
    s "Hello?"
    show sima2close 1g 2a 3a fancy1 at u11 as sima with dissolve
    p "Oh!"
    show sima2close 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "Hi... I'm doing great!"
    show sima2close 1e 2a 3d fancy1 at u11 as sima with dissolve
    s "Glad to hear it."
    show sima3aclose 1e 2a 3a fancy at u11 as sima with dissolve
    s "Well, shall we take a seat?"
    scene cg_sima_4_1
    $ persistent.unlock_cg_sima_4_1= 1
    with fade
    "We've got a decent table, and relief washes over me in an awesome wave."
    show cg_sima_4_2 as sima with dissolve
    s "We had such a lovely time here yesterday."
    p "Yeah..."
    show cg_sima_4_1 as sima with dissolve
    s "Shame we didn't try their best dessert!"
    p "Which one?"
    s "It's obvious from the first glance."
    p "From the first glance, you say..."
    s "Give it a try."
    "I show Sima my selection."
    s "What do you know, [player_name], it's on your list!"
    show cg_sima_4_2 as sima with dissolve
    s "You know what I'm going to ask you next, don't you?"
    p "Which one..."
    show cg_sima_4_1 as sima with dissolve
    s "Is the best one!"
    menu:
        "\"Peach Passion\", chocolate peach cake.":
            jump dessert_choice_wrong_sima
        "\"Strawberry Delight\", strawberry shortcake.":
            jump dessert_choice_wrong_sima
        "\"Cherry D'Or\", cherry mille-feuille.":
            jump dessert_choice_right_sima
label dessert_choice_wrong_sima:
    s "This is my second favorite, [player_name]!"
    jump date_main_sima_p1
label dessert_choice_right_sima:
    s "Correct... Am I this easy to read?"
    show cg_sima_4_2 as sima with dissolve
    s "Well, it's just the first chapter!"
    show cg_sima_4_1 as sima with dissolve
    jump date_main_sima_p1
label date_main_sima_p1:
    "I pick something for myself, and we're all set."
    s "Do you feel the same, [player_name]?"
    p "Excited?"
    s "Nervous."
    p "Pretty close."
    s "Yeah, maybe... I'm very nervous, you know."
    s "See, I'm not that good at small talk... people often think I'm boring."
    menu:
        "Really? I can't believe it.":
            play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
            scene cafe
            show sima1date 1a 2d 3a fancy at u11 as sima
            with fade
            jump date_main_sima_p1a
        "These people are not your people then.":
            jump date_main_sima_p1b
label date_main_sima_p1a:
    s "..."
    show sima1date 1d 2d 3a fancy at u11 as sima with dissolve
    s "Seems like you didn't listen to what I said a few days ago."
    show sima3adate 1c 2a 3d fancy at u11 as sima with dissolve
    s "Anyway, I'm curious to know, [player_name]..."
    show sima3adate 1d 2a 3a fancy at u11 as sima with dissolve
    s "{i}Why{/i} do you think it's hard to believe in what I said?"
    show sima3adate 1a 2a 3a fancy at u11 as sima with dissolve
    menu:
        "Because you look so... perfect!":
            jump date_main_sima_p1_bad_end
        "Because I underestimated how silly people can be.":
            scene cg_sima_4_1 with fade
            play music "music/admit.ogg" fadein 1.5 fadeout 2
            jump date_main_sima_p1b
label date_main_sima_p1_bad_end:
    show sima3a 1e 2d 3d fancy at u11 as sima with dissolve
    s "Perfect? Well... thanks, [player_name]."
    show sima3a 1a 2d 3d fancy at u11 as sima with dissolve
    p "I take it quite some people said these words before..."
    show sima1 1c 2d 3d fancy at u11 as sima with dissolve
    s "Do you know what they have in common?"
    show sima1 1a 2d 3d fancy at u11 as sima with dissolve
    p "What?"
    show sima1 1d 2d 3a fancy at u11 as sima with dissolve
    s "They're not my people."
    jump sima_date_fail
label date_main_sima_p1b:
    s "Maybe you're right..."
    s "Hey, [player_name]!"
    s "Tell me something."
    p "Anything you want to know."
    show cg_sima_4_2 as sima with dissolve
    s "No, silly, tell me {i}something{/i}."
    show cg_sima_4_1 as sima with dissolve
    p "Something, you say..."
    p "Honestly, nothing comes up on my mind."
    s "Why? Is it because of me?"
    p "I think so."
    s "..."
    p "Nothing comes to mind because I only think of you."
    s "Oh..."
    show cg_sima_4_2 as sima with dissolve
    s "You're flattering me, [player_name]."
    p "Sorry, I..."
    show cg_sima_4_1 as sima with dissolve
    s "I didn't say stop."
    s "Um... is there something special about me?"
    menu:
        "Your beauty.":
            play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
            scene cafe
            show sima3adate 1c 2a 3a fancy at u11 as sima
            with fade
            jump date_main_sima_p2a
        "Your self-control.":
            scene cafe
            show sima2date 1e 2a 3a fancy1 at u11 as sima
            with fade
            jump date_main_sima_p2b
label date_main_sima_p2a:
    s "I see."
    show sima3adate 1a 2a 3a fancy at u11 as sima with dissolve
    p "Did I say anything wrong?"
    show sima3adate 1e 2a 3b fancy at u11 as sima with dissolve
    s "No, of course not. I appreciate your words."
    show sima3adate 1c 2b 3a fancy at u11 as sima with dissolve
    s "I just wonder if there's anything else..."
    menu:
        "Everything!":
            jump date_main_sima_p2_bad_end
        "You're so... strong and independent.":
            play music "music/admit.ogg" fadein 2 fadeout 2
            show sima2date 1e 2a 3a fancy1 at u11 as sima with dissolve
            jump date_main_sima_p2b
label date_main_sima_p2_bad_end:
    show sima1 1d 2a 3d fancy at u11 as sima with dissolve
    s "Everything?"
    show sima1 1d 2d 3b fancy at u11 as sima with dissolve
    s "Everything, but nothing in particular, I guess."
    show sima1 1a 2d 3b fancy at u11 as sima with dissolve
    p "I mean it!"
    show sima1 1d 2d 3a fancy at u11 as sima with dissolve
    s "Okay."
    show sima1 1a 2d 3a fancy at u11 as sima with dissolve
    p "Really, it's a whole list of things explaining what's great about you."
    show sima1 1d 2d 3d fancy at u11 as sima with dissolve
    s "You're also on my list now, I think."
    show sima1 1d 2d 3a fancy at u11 as sima with dissolve
    s "The list of people who're not my people."
    jump sima_date_fail
label date_main_sima_p2b:
    s "Oh, thank you!"
    show sima2date 1a 2a 3a fancy1 at u11 as sima with dissolve
    p "What's the secret?"
    show sima2date 1e 2a 3b fancy1 at u11 as sima with dissolve
    s "It's simple."
    show sima3adate 1e 2a 3a fancy at u11 as sima with dissolve
    s "Few things matter, [player_name]."
    p "I don't buy it... What about our exams, career plans and all?"
    show sima3adate 1c 2a 3d fancy at u11 as sima with dissolve
    s "And all {i}temporary{/i} and silly things."
    show sima2date 1e 2a 3a fancy1 at u11 as sima with dissolve
    s "In five years you're going to look back and laugh..."
    show sima2date 1e 2a 3d fancy2 at u11 as sima with dissolve
    s "Trust me, our problems are nothing serious."
    p "And what {i}is{/i} serious enough for you?"
    show sima3adate 1c 2a 3d fancy at u11 as sima with dissolve
    s "Hm, let me think..."
    show sima3adate 1d 2a 3d fancy at u11 as sima with dissolve
    s "Say, having nothing to eat or nowhere to sleep."
    show sima3adate 1d 2a 3a fancy at u11 as sima with dissolve
    s "Death of someone precious to you."
    show sima3adate 1e 2a 3d fancy at u11 as sima with dissolve
    s "Now, career plans, you say..."
    show sima3adate 1e 2a 3a fancy at u11 as sima with dissolve
    s "Even if you don't get a prestigious job, so what of it?"
    show sima2date 1e 2a 3d fancy2 at u11 as sima with dissolve
    s "Less people going to say you're doing great?"
    show sima2date 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "It's not about people, it's about money."
    p "Money gives you freedom."
    show sima2date 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "I'd be lying if I said it's not true."
    show sima2date 1e 2a 3d fancy1 at u11 as sima with dissolve
    s "However, freedom costs little, [player_name]."
    show sima2date 1e 2a 3a fancy1 at u11 as sima with dissolve
    s "Having a good lifestyle isn't expensive at all."
    menu:
        "Not expensive for those who have the money.":
            play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
            jump date_main_sima_p3a
        "But is it really \"nice enough\"?":
            play music "music/admit.ogg" fadein 2 fadeout 2
            jump date_main_sima_p3b
label date_main_sima_p3a:
    show sima1date 1d 2b 3b fancy at u11 as sima with dissolve
    s "I see."
    show sima1date 1c 2b 3a fancy at u11 as sima with dissolve
    s "You mean that the rich considers everything inexpensive, right?"
    show sima2date 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "It's easier to say you don't need much on an empty stomach."
    show sima2date 1d 2d 3a fancy1 at u11 as sima with dissolve
    s "Makes sense, [player_name], after all, I'm from a rich family."
    show sima2date 1a 2d 3a fancy1 at u11 as sima with dissolve
    p "That's not what I was trying to say."
    menu:
        "I'm just saying that the rich have a privilege...":
            jump date_main_sima_p3_bad_end
        "I'm just saying that it's hard to define the \"nice enough\" thing.":
            play music "music/admit.ogg" fadein 2 fadeout 2
            jump date_main_sima_p3b
label date_main_sima_p3_bad_end:
    show sima2 1d 2d 3a fancy1 at u11 as sima with dissolve
    s "Let me tell you something..."
    show sima2 1d 2d 3c blush fancy1 at u11 as sima with dissolve
    s "It's a not a privilege, it's \"noblesse oblige\"."
    show sima2 1a 2d 3c fancy1 at u11 as sima with dissolve
    p "What do you mean?"
    show sima2 1d 2d 3c fancy1 at u11 as sima with dissolve
    s "You're supposed to own a lot of things when you're rich..."
    show sima1 1c 2b 3b fancy at u11 as sima with dissolve
    s "At a certain point, they \"end up owning you\", like in that movie."
    show sima1 1d 2d 3c fancy at u11 as sima with dissolve
    s "For example, imagine you have more money than you can spend."
    show sima1 1c 2d 3d fancy at u11 as sima with dissolve
    s "Where do you think you store an amount that high?"
    show sima1 1a 2d 3d fancy at u11 as sima with dissolve
    p "Like, in a bank?"
    show sima1 1c 2b 3d fancy at u11 as sima with dissolve
    s "Then you're not the one who owns the money."
    show sima1 1a 2b 3d fancy at u11 as sima with dissolve
    p "What about buying real estate and whatnot?"
    show sima1 1d 2a 3d fancy at u11 as sima with dissolve
    s "It only means being less and less liquid."
    show sima1 1a 2a 3d fancy at u11 as sima with dissolve
    p "Liquid?"
    show sima1 1d 2a 3a fancy at u11 as sima with dissolve
    s "Yes, a lot of money on paper but nothing in cash."
    show sima1 1c 2b 3d fancy at u11 as sima with dissolve
    s "However, I see why a lot of people don't get it."
    show sima1 1d 2b 3d fancy at u11 as sima with dissolve
    s "You never know unless you get rich."
    show sima1 1a 2b 3d fancy at u11 as sima with dissolve
    p "Or die trying."
    show sima1 1c 2d 3d fancy at u11 as sima with dissolve
    s "Do you know what all these people have in common?"
    show sima1 1a 2d 3d fancy at u11 as sima with dissolve
    p "What?"
    show sima1 1d 2d 3d fancy at u11 as sima with dissolve
    s "They're not my people, [player_name]."
    jump sima_date_fail
label date_main_sima_p3b:
    play music "music/relax_theme.ogg" fadein 2 fadeout 2
    show sima2date 1c 2a 3a fancy2 at u11 as sima with dissolve
    s "Hm..."
    show sima2date 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "A good lifestyle means, like..."
    p "I don't know, having a personal yacht, I guess."
    show sima2date 1d 2a 3b fancy1 at u11 as sima with dissolve
    s "But you don't really need it. It's a common misunderstanding."
    show sima2date 1e 2a 3a fancy1 at u11 as sima with dissolve
    s "See, money makes drastic improvements in your life only for so long."
    show sima3adate 1c 2a 3d fancy at u11 as sima with dissolve
    s "Say, a pair of shoes worth one hundred dollars is likely to be good enough."
    show sima3adate 1d 2a 3a fancy at u11 as sima with dissolve
    s "Then you get yourself another one, this time worth two thousand..."
    show sima3adate 1a 2a 3a fancy at u11 as sima with dissolve
    p "I guess it's even better!"
    show sima3adate 1c 2a 3d fancy at u11 as sima with dissolve
    s "Right, but usually not twenty times more."
    show sima3adate 1e 2a 3a fancy at u11 as sima with dissolve
    s "A dinner at a three-star Michelin restaurant is good..."
    show sima3adate 1c 2b 3d fancy at u11 as sima with dissolve
    s "But is worth the extra price compared to your favorite cafe?"
    show sima3adate 1e 2b 3d fancy at u11 as sima with dissolve
    s "I'm not even talking about a dinner with your family."
    show sima1date 1c 2a 3a fancy at u11 as sima with dissolve
    s "At some point, everything becomes good enough, not worth the extra money."
    show sima1date 1e 2a 3b fancy at u11 as sima with dissolve
    s "Sadly, you can only learn it from your own experience."
    show sima1date 1c 2a 3d fancy at u11 as sima with dissolve
    s "That's why the rich often say money isn't everything..."
    s "And the poor hate them for that."
    show sima2date 1d 2a 3b fancy1 at u11 as sima with dissolve
    s "Let's learn to enjoy the little things, [player_name]!"
    show sima3bdate 1d 2a 3b fancy at u11 as sima with dissolve
    s "How about we start from our desserts?"
    show black with fade
    "We'll take our time."
    scene cg_sima_4_1 with fade
    p "Hey, do you like art?"
    s "Yeah, why?"
    p "There's an exhibition nearby, I heard it's quite good..."
    s "You want to go?"
    p "Only if you keep me company."
    s "I'm afraid I have to leave soon..."
    s "..."
    show cg_sima_4_2 as sima with dissolve
    s "Haha! The face you made was priceless."
    show cg_sima_4_1 as sima with dissolve
    s "I'll go with you, [player_name]!"
    scene black with fade
    "The exhibition is right across the corner, so we decide to take a walk."
    scene cg_sima_6_1 with fade
    $ persistent.unlock_cg_sima_6_2 = 1
    "The wind's picking up."
    "Wow..."
    "With her hair like that, Sima looks a valkyrie."
    "Sounds a bit cheesy, but who cares..."
    s "What?"
    p "N-nothing!"
    show cg_sima_6_2 as sima with dissolve
    s "My hair is probably a mess..."
    s "Why won't this wind stop?"
    "Maybe because it listens to my prayers."
    "Let it be not the mere breeze, but a mighty gale."
    jump date_exhibition_sima
label date_exhibition_sima:
    scene date_expo with fade
    "This is the showstopper, I guess. We admire it for a while."
    show sima2close 1e 2a 3a fancy2 at u11 as sima
    s "I'm glad you invited me here, [player_name]."
    show sima2close 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "Honestly, I was surprised."
    show sima2close 1a 2a 3a fancy1 at u11 as sima with dissolve
    p "Why?"
    show sima3aclose 1c 2a 3d fancy at u11 as sima with dissolve
    s "How should I put it..."
    show sima3aclose 1c 2a 3a fancy at u11 as sima with dissolve
    s "Say, do you visit places like this often... with other girls?"
    p "Um... yeah, well... from time to time."
    show sima3aclose 1d 2c 3c fancy at u11 as sima with dissolve
    s "Oh! I see..."
    show sima3aclose 1c 2b 3d fancy at u11 as sima with dissolve
    s "Just so you know, no one has invited me before."
    p "They don't know what they've missed, Sima."
    show sima3aclose 1e 2a 3a blush fancy at u11 as sima with dissolve
    "She says nothing. But..."
    show sima2close 1e 2a 3d blush fancy2 at ui11 as sima with dissolve:
        ypos 1370
        pause 1
        linear 1 zoom 1.1 ypos 1500
    "She moves closer to me."
    show sima2close 1e 2a 3d blush fancy2 at ui11 as sima:
        zoom 1.1
        ypos 1500
        linear 1 zoom 1.2 ypos 1600
    "{i}Much{/i} closer."
    show sima2close 1c 2a 3a blush fancy2 at ui11 as sima with dissolve:
        zoom 1.2
        ypos 1600
    s "D-do you think this picture is beautiful?"
    show sima2close 1a 2a 3a blush fancy2 at ui11 as sima with dissolve:
        zoom 1.2
        ypos 1600
    p "Not as beautiful as something else I see right now."
    p "Actually, it's not \"something\"... it's \"someone\"."
    show sima2close 1e 2a 3d blush fancy2 at ui11 as sima with dissolve:
        zoom 1.2
        ypos 1600
    s "W-who are you talking about?"
    show sima2close 1a 2a 3a blush fancy2 at ui11 as sima with dissolve:
        zoom 1.2
        ypos 1600
    p "You."
    hide sima
    show sima2close 1a 2a 3a blush fancy2 at ui11 as simax:
        alpha 1
        zoom 1.2
        ypos 1590
        linear 1 zoom 1.3 ypos 1700
    show sima2close 1c 2a 3b blush fancy2 at ui11 as sima:
        zoom 1.3
        ypos 1700
        alpha 0
        pause 1
        linear .5 alpha 1
    s "{w=1.8}Wait a second, [player_name]..."
    hide simax
    show sima2close 1c 2a 3b blush fancy2 at ui11 as sima:
        zoom 1.3
        ypos 1700
        linear 1 zoom 1 ypos 1370
    $ renpy.pause(1.1, hard=True)
    show sima3aclose 1a 2a 3b blush fancy at u11 as sima with dissolve
    "Oh no!"
    show sima3bclose 1a 2a 3b blush fancy at u11 as sima with dissolve
    "I know that voice."
    show sima3bclose 1e 2a 3d blush fancy at u11 as sima with dissolve
    "I'm afraid I also know what comes next... rejection."
    show sima3bclose 1a 2a 3a blush fancy at u11 as sima with dissolve
    p "That's it, huh?"
    show sima2close 1d 2c 3c blush fancy2 at u11 as sima with dissolve
    s "What? What do you mean?"
    show sima2close 1a 2c 3a blush fancy2 at u11 as sima with dissolve
    p "C'mon, that \"wait a second\" is a rejection, flat out."
    show sima2close 1e 2a 3a blush fancy1 at u11 as sima with dissolve
    s "Do you know why I asked you to wait?"
    show sima3bclose 1d 2d 3b blush fancy at u11 as sima with dissolve
    s "Simply because I wanted to cherish this moment."
    show sima3bclose 1a 2a 3a blush fancy at u11 as sima with dissolve
    s "..."
    show sima3bclose 1c 2b 3d blush fancy at u11 as sima with dissolve
    s "Can we go for a walk? The air is stale here."
    show sima3bclose 1a 2b 3d blush fancy at u11 as sima with dissolve
    p "Sure..."
    scene black with fade
    "We leave the exhibition."
    "I need to clarify a few things here, but..."
    "Before that, I have to deal with this rain."
    p "Um, my umbrella is good for two."
    play music "music/succeed.ogg" fadein 2 fadeout 2
    scene cg_sima_7_1_back
    show rain1 at arain1
    show rain2 at arain2
    show cg_sima_7_3 as sima
    $ persistent.unlock_cg_sima_7_1 = 1
    show rain3 at arain3
    with fade
    "She leans under my umbrella and..."
    "She's so close!"
    s "Do you like it when it rains?"
    p "T-the air is fresh."
    s "I like the sound of raindrops."
    show cg_sima_7_1 as sima with dissolve
    s "Hey, [player_name]..."
    p "Yes?"
    s "Don't even think about taking your words back."
    p "I won't. But... it's a bit tough for me right now."
    s "What do you mean?"
    p "Do you... do you feel what I feel?"
    s "What do you mean?"
    s "Haha, that face of yours again."
    show cg_sima_7_3 as sima with dissolve
    s "..."
    show cg_sima_7_1 as sima with dissolve
    s "I do."
    p "Doesn't sound too convincing when you only say it once."
    s "[player_name], don't ever make a girl repeat it."
    p "You can say something new then..."
    s "I like it when it rains."
    s "I like you when it rains."
    "She's dangerously close now."
    s "Hey..."
    show cg_sima_7_3 as sima with dissolve
    s "Promise you'll never take what you said back?"
    p "I promise."
    show cg_sima_7_1 as sima with dissolve
    s "You better be honest, [player_name]."
    s "Otherwise I'll kill you. But only after..."
    s "Only after we kiss."
    $ s_date_finished = 1

    $achievement.grant("LargerThanLife")
    init:
        $achievement.register("LargerThanLife")
        $achievement.sync()
    $achievement.sync()

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            $ new_game2_sima_done = 1
            jump wb2

    if new_game1_sima_set == 1:
        $ new_game1_sima_done = 1
        scene black with fade
        $ renpy.pause(2, hard=True)
        jump wb1
    jump date_end
label sima_date_fail:
    scene black with fade
    "We finish our desserts in awkward silence."
    "Sima gives me nothing but one-word replies."
    "I guess only good manners stop her from leaving right now."
    "Having asked for the bill, I catch a relieved look on her face."
    scene cafe with fade
    show sima2 1d 2a 3a fancy1 at u11 as sima
    s "Thanks for today, [player_name]! I enjoyed my time here."
    show sima2 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "The pleasure is all mine!"
    p "Hey, let's take a short walk!"
    show sima1 1e 2b 3a fancy at u11 as sima with dissolve
    s "Sorry, [player_name], I'm afraid I need to go home right now."
    show sima1 1e 2b 3b fancy at u11 as sima with dissolve
    s "I really need to catch up on my studies."
    p "I'll walk you home then!"
    show sima1 1d 2a 3c fancy at u11 as sima with dissolve
    s "I don't want to bother you..."
    show sima1 1a 2a 3c fancy at u11 as sima with dissolve
    p "You're not bothering me at all!"
    show sima1 1d 2a 3a fancy at u11 as sima with dissolve
    s "Really, it's fine. See you on Monday, [player_name]!"
    show sima1 1a 2a 3a fancy at u11 as sima with dissolve
    p "See you..."
    hide sima with dissolve
    "Sima leaves in a hurry."
    jump failed_date
label fake_date_marta:
    play sound "sound/phone.ogg"
    $ renpy.pause(1, hard=True)
    "Whoa, an incoming call."
    "It's Marta."
    play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
    show marta2 1b 2a 3a regular2 noblush at u11 as marta:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "What's up, [player_name]."
    show marta2 1g 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "Hi! About to leave my place."
    show marta2 1c 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "This early?"
    show marta2 1a 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "I don't want to be running late."
    show marta2 1b 2a 3b regular2 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Yeah, you'd better not to."
    show marta2 1c 2b 3a regular1 blush at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "..."
    show marta1 1c 2b 3b at u11 as marta with dissolve:
        xalign -.14
        ypos 1760
        zoom 1.1
    m "So, [player_name], um, about today..."
    show marta1 1e 2b 3a at u11 as marta with dissolve:
        xalign -.14
        ypos 1760
        zoom 1.1
    m "I can't make it. Sorry!"
    show marta1 1f 2b 3b at u11 as marta with dissolve:
        xalign -.14
        ypos 1760
        zoom 1.1
    p "Oh..."
    p "What's wrong?"
    show marta1 1e 2a 3a at u11 as marta with dissolve:
        xalign -.14
        ypos 1760
        zoom 1.1
    m "Nothing, it's just..."
    show marta1 1b 2a 3a at u11 as marta with dissolve:
        xalign -.14
        ypos 1760
        zoom 1.1
    m "Turns out someone really special for me is in town."
    show marta2 1e 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Professor Chadwick has been my mentor since like forever."
    show marta3 1gg 2a 3b regular2 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "He messaged me out of the blue yesterday."
    show marta3 1d 2b 3a noblush regular1 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "I said I'm busy, I really did, but..."
    show marta3 1a 2b 3a regular1 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    p "Look, it's okay."
    p "Just don't tell me you guys are meeting at \"Doorsia\"."
    show marta2 1d 2c 3c regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "No way! We're meeting at his hotel. He wants to discuss my future."
    show marta2 1e 2b 3d regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "You know how important it is to me, right?"
    show marta2 1e 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Professor Chadwick has connections with all Ivy League schools."
    show marta2 1a 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "So... discussing the future at his hotel room, huh."
    show marta2 1e 2d 3a regular2 blush at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Hey, who said anything about the room? What're you getting at?"
    show marta2 1f 2d 3a regular1 noblush at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "N-nothing, I just asked."
    show marta2 1c 2b 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Alright then."
    show marta2 1a 2b 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "Um, how about we meet on Sunday?"
    show marta2 1b 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Sunday funday..."
    show marta3 1e 2a 3a regular1 blush at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "Sorry, I'm afraid I can't. Next week?"
    p "Alright!"
    show marta2 1b 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "It's a deal then!"
    show marta2 1d 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "Yeah..."
    show marta2 1b 2d 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Hey, [player_name], don't be upset!"
    show marta2 1d 2d 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "Nah, I'm not. It's fine."
    show marta3 1dd 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "You know what? It's so nice to have a friend like you..."
    p "F-friend?"
    show marta3 1e 2a 3b regular1 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "I know you didn't expect this."
    show marta2 1b 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Usually I'd act like it's not a big deal at all, but..."
    show marta2 1b 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "This time I have enough courage to say it first!"
    show marta2 1g 2a 3d regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "\"Let's be friends, [player_name]!\""
    p "..."
    show marta2 1e 2b 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    m "Hey, what's wrong?"
    show marta2 1a 2b 3a regular1 at u11 as marta with dissolve:
        xalign -.12
        ypos 1760
        zoom 1.1
    p "N-nothing."
    show marta3 1gg 2a 3a regular2 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "Think about where you want to go with your friend next week then!"
    show marta3 1e 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    m "Look, I really have to run. Take care, okay?"
    show marta3 1g 2a 3a regular1 at u11 as marta with dissolve:
        xalign -.08
        ypos 1760
        zoom 1.1
    p "O-okay..."
    hide marta with dissolve

    $achievement.grant("Friendzone")
    init:
        $achievement.register("Friendzone")
        $achievement.sync()
    $achievement.sync()

    "She hangs up."
    jump failed_date
label date_marta:
    play music "music/admit.ogg"
    $ renpy.pause(1, hard=True)
    scene cafe
    show marta2close 1a 2a 3d fancy1 at u11 as marta
    with fade
    "Marta arrived strictly on time."
    show marta2close 1a 2a 3a fancy1 at u11 as marta with dissolve
    "The dress she wears today makes me see her in a new light."
    p "Hi! How're ya doin'?"
    show marta3close 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "F-fine..."
    show marta3close 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "You look totally different today!"
    show marta3close 1g 2a 3a fancy1 blush  at u11 as marta with dissolve
    "She blushes a little."
    show marta2close 1b 2c 3a fancy1 at u11 as marta with dissolve
    m "Is it any good?"
    show marta2close 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "..."
    show marta2close 1g 2a 3b fancy1 at u11 as marta with dissolve
    p "It's awesome! Alright, let's take a seat."
    scene black with fade
    "The waiter leads us to the table."
    show cg_marta_4_1 with fade
    $ persistent.unlock_cg_marta_4_1 = 1
    "Here I am, pretending to look at the menu."
    "The truth is, it's only an excuse for stealing a glance at Marta."
    "And... I think she's playing the same game!"
    p "Found anything you like?"
    show cg_marta_4_2 as marta with dissolve
    m "W-what did you say?"
    show cg_marta_4_1 as marta with dissolve
    p "Desserts here look good."
    m "And taste even better. Remember that one from yesterday?"
    p "Yeah... Which one are you going to try today?"
    show cg_marta_4_2 as marta with dissolve
    m "Hm..."
    show cg_marta_4_1 as marta with dissolve
    m "This menu is annoying!"
    p "Why?"
    m "It's too extensive."
    p "Just pick the first one that looks decent."
    show cg_marta_4_2 as marta with dissolve
    m "Hey, it's important! How can't you understand?"
    show cg_marta_4_1 as marta with dissolve
    m "You! You help me to decide."
    menu:
        "\"Peach Passion\", chocolate peach cake.":
            jump dessert_choice_right_marta
        "\"Strawberry Delight\", strawberry shortcake.":
            jump dessert_choice_wrong_marta
        "\"Cherry D'Or\", cherry mille-feuille.":
            jump dessert_choice_wrong_marta
label dessert_choice_right_marta:
    m "Wow, it's the one I was thinking about!"
    p "I just knew it, somehow."
    m "Cool."
    show cg_marta_4_2 as marta with dissolve
    m "Don't act like you can read my mind or anything though!"
    show cg_marta_4_1 as marta with dissolve
    jump date_main_marta_p1
label dessert_choice_wrong_marta:
    show cg_marta_4_2 as marta with dissolve
    m "Hm... maybe."
    show cg_marta_4_1 as marta with dissolve
    m "On second thought... I'll go with something else, I think."
    jump date_main_marta_p1
label date_main_marta_p1:
    "Now that we're done with our orders, I better get the conversation going."
    menu:
        "Hey, tell me about your hobbies.":
            play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
            $ story_told = 1
            scene cafe
            show marta2date 1c 2b 3d fancy1 at u11 as marta
            with fade
            jump date_main_marta_p1a
        "So, how did you like this week?":
            scene cafe
            show marta3date 1g 2a 3b noblush fancy1 at u11 as marta
            with fade
            jump date_main_marta_p1bb
label date_main_marta_p1a:
    m "My hobbies?"
    show marta2date 1d 2a 3a fancy1 at u11 as marta with dissolve
    m "Working hard, I guess."
    show marta2date 1d 2b 3a fancy2 at u11 as marta with dissolve
    m "I can't really waste my time on anything else right now."
    show marta2date 1c 2b 3a fancy1 at u11 as marta with dissolve
    m "I mean, I aim high in life."
    show marta1date 1c 2b 3a fancy at u11 as marta with dissolve
    m "And... it's too late for me to get a hobby anyway."
    show marta2date 1d 2b 3b fancy1 at u11 as marta with dissolve
    m "I should've started ages ago."
    show marta2date 1a 2b 3a fancy1 at u11 as marta with dissolve
    p "Like, as a kid?"
    show marta2date 1e 2b 3a fancy1 at u11 as marta with dissolve
    m "Yeah, but back then... Well, never mind."
    show marta1date 1f 2b 3b fancy at u11 as marta with dissolve
    p "Tell me about it."
    show marta2date 1d 2a 3a fancy2 at u11 as marta with dissolve
    m "Well, why not?"
label marta_story:
    show marta2date 1d 2a 3d fancy1 at u11 as marta with dissolve
    m "I come from a family that once was very rich."
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "I was a very privileged kid, you know. Fancy clothes, big house..."
    show marta2date 1d 2a 3a fancy2 at u11 as marta with dissolve
    m "My dad worked as an investment banker."
    show marta2date 1d 2b 3d fancy1 at u11 as marta with dissolve
    m "He just laughed at anything I tried to do as a hobby."
    show marta2date 1e 2d 3d fancy2 at u11 as marta with dissolve
    m "He was like, \"Don't waste your time on this stupid stuff\"."
    show marta2date 1c 2a 3d fancy1 at u11 as marta with dissolve
    m "Over time, I just stopped trying to do anything."
    show marta2date 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "Anything but studying. It was the only legitimate activity."
    show marta1date 1e 2a 3a fancy at u11 as marta with dissolve
    m "Anyway... remember that famous mortgage crisis?"
    show marta1date 1a 2a 3a fancy at u11 as marta with dissolve
    p "Yeah. Your dad lost his job, I guess?"
    show marta2date 1d 2a 3d fancy1 at u11 as marta with dissolve
    m "He was among the first bunch to be thrown under the bus."
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "He had a lot of savings, but he invested them all in some shady deals..."
    show marta2date 1e 2d 3a fancy2 at u11 as marta with dissolve
    m "Saying that the market's going to recover in no time. He went broke."
    show marta2date 1f 2b 3a fancy1 at u11 as marta with dissolve
    p "I imagine it was a big hit for him."
    show marta2date 1e 2c 3a fancy2 at u11 as marta with dissolve
    m "You bet!"
    show marta1date 1b 2b 3b fancy at u11 as marta with dissolve
    m "And my mother... she was too used to a glamorous life."
    show marta1date 1e 2b 3a fancy at u11 as marta with dissolve
    m "Her last words were, directed to my father..."
    show marta2date 1e 2d 3a fancy1 at u11 as marta with dissolve
    m "\"You're not the man I used to love anymore.\""
    show marta2date 1d 2b 3d fancy1 at u11 as marta with dissolve
    m "My rich friends suddenly grew distant. Oh well."
    show marta2date 1b 2b 3a fancy1 at u11 as marta with dissolve
    m "From that moment, I could only rely on my hard work."
    show marta2date 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "Well, here I am."
    show marta2date 1a 2a 3a fancy1 at u11 as marta with dissolve
    if story_told == 1:
        jump date_main_marta_p1aa
    if story_told == 0:
        jump marta_story_told
label date_main_marta_p1aa:
    p "Yeah. I understood why you don't have time for hobbies..."
    show marta2date 1e 2a 3a fancy2 at u11 as marta with dissolve
    m "There's another thing..."
    show marta2date 1b 2b 3d fancy1 at u11 as marta with dissolve
    m "I don't think I have a talent for anything."
    show marta2date 1e 2d 3a fancy2  blush at u11 as marta with dissolve
    m "What's the point in doing something if you can't be the best?"
    show marta3date 1g 2b 3a fancy1 at u11 as marta with dissolve
    m "Oh well, at least I can study."
    menu:
        "Maybe you should lower your expectations.":
            jump date_main_marta_p1_bad_end
        "Studying here is sure special.":
            play music "music/admit.ogg" fadein 2 fadeout 2
            show marta2date 1c 2c 3c fancy1 at u11 as marta with dissolve
            jump date_main_marta_p1bb
label date_main_marta_p1_bad_end:
    show marta2 1c 2c 3c fancy1 at u11 as marta with dissolve
    m "..."
    show marta2 1e 2d 3c fancy2 at u11 as marta with dissolve
    m "Never. Never ever..."
    show marta2 1e 2d 3a fancy2 noblush at u11 as marta with dissolve
    m "I expect only the best from myself and those around me."
    show marta2 1f 2d 3a fancy1 at u11 as marta with dissolve
    p "Everyone is different, don't you think so?"
    show marta2 1c 2a 3d fancy1 at u11 as marta with dissolve
    m "But I don't need everyone, I only need the best."
    show marta2 1f 2d 3d fancy1 at u11 as marta with dissolve
    p "What if someone simply can't keep up with your pace?"
    show marta2 1e 2d 3a fancy2 at u11 as marta with dissolve
    m "Then they're not my type, simple as that. Okay, let's move on."
    jump marta_date_fail
label date_main_marta_p1bb:
    m "Oh yea! It's been a hectic week, but that's what I expect of this place."
    show marta3date 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "I definitely enjoy it here."
    show marta3date 1g 2a 3a fancy1 at u11 as marta with dissolve
    p "What do you enjoy the most?"
    jump date_main_marta_p1b
label date_main_marta_p1b:
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "Hm... probably the people."
    show marta2date 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "They're really something!"
    show marta2date 1b 2a 3d fancy2 at u11 as marta with dissolve
    m "Take Nana for example... I can't really understand here."
    show marta2date 1c 2a 3d fancy1 at u11 as marta with dissolve
    m "It scares me a bit, but... it also gets me excited."
    show marta2date 1e 2c 3a fancy1 at u11 as marta with dissolve
    m "She's much smarter than she wants us to believe."
    show marta2date 1c 2c 3d fancy1 at u11 as marta with dissolve
    m "Also, Nana looks annoyed way too often... Why, I wonder?"
    show marta2date 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "Sima is a different story."
    show marta2date 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "A different story with a similar beginning, that is."
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "Sima comes from a rich family..."
    if story_told == 0:
        jump marta_story
    if story_told == 1:
        jump marta_story_told
label marta_story_told:
    show marta2date 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Both Sima and I were raised with one thought carved in our minds."
    show marta2date 1e 2c 3a fancy2 at u11 as marta with dissolve
    m "\"I am the best.\""
    show marta2date 1f 2b 3a fancy1 at u11 as marta with dissolve
    m "..."
    p "Is there anything wrong with that?"
    show marta2date 1c 2b 3a blush fancy1 at u11 as marta with dissolve
    m "Well..."
    show marta2date 1d 2b 3a fancy2 at u11 as marta with dissolve
    m "You know, there's only {i}one{/i} winner."
    show marta1date 1e 2a 3b fancy at u11 as marta with dissolve
    m "And... Sima's better in every aspect, simple as that."
    show marta2date 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "I don't stand a chance against her."
    show marta3date 1ff 2b 3a fancy2 at u11 as marta with dissolve
    m "I'm sure she has a bright future, while I..."
    show marta2date 1e 2d 3d fancy1 at u11 as marta with dissolve
    m "While I'll be stuck in my office cage. It's not fair!"
    show marta2date 1e 2c 3c fancy2 at u11 as marta with dissolve
    m "Oh, and her looks!"
    show marta2date 1f 2a 3a fancy1 at u11 as marta with dissolve
    m "..."
    menu:
        "Enough about Sima! Everyone is different.":
            play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
            jump date_main_marta_p2a
        "Enough about Sima! I only want to talk about you.":
            play music "music/relax_theme.ogg" fadein 2 fadeout 2
            jump date_main_marta_p2bb
label date_main_marta_p2a:
    show marta2date 1e 2d 3a fancy1 at u11 as marta with dissolve
    m "So you mean I can't be compared with her?"
    show marta2date 1e 2d 3c fancy1 at u11 as marta with dissolve
    m "Thanks for opening my eyes, [player_name]!"
    show marta2date 1f 2d 3a fancy1 at u11 as marta with dissolve
    p "I just wanted to say that both of you have great personalities!"
    show marta2date 1f 2a 3c fancy1 at u11 as marta with dissolve
    m "..."
    show marta1date 1d 2d 3b fancy at u11 as marta with dissolve
    m "Look, [player_name], let me tell you something."
    show marta1date 1e 2d 3a fancy at u11 as marta with dissolve
    m "Never tell a girl that she has a great personality."
    show marta1date 1d 2d 3a fancy at u11 as marta with dissolve
    m "Especially when you're on a date...{w=1.5} oh!"
    show marta1date 1c 2a 3b blush fancy at u11 as marta with dissolve
    m "Disregard what I just said."
    show marta1date 1a 2a 3b noblush fancy at u11 as marta with dissolve
    p "But I don't want to compare your looks, it's inappropriate, after all."
    show marta1date 1c 2a 3d fancy at u11 as marta with dissolve
    m "Yeah, \"inappropriate\"."
    show marta2date 1e 2d 3c fancy2 at u11 as marta with dissolve
    m "Just say it out loud! Say that she's better!"
    show marta2date 1f 2d 3c fancy2 at u11 as marta with dissolve
    menu:
        "You're the best.":
            play music "music/relax_theme.ogg" fadein 2 fadeout 2
            jump date_main_marta_p2aa
        "I value what's inside.":
            jump date_main_marta_p2_bad_end
label date_main_marta_p2aa:
    show marta2date 1c 2c 3c fancy2 at u11 as marta with dissolve
    m "..."
    show marta3date 1gg 2a 3b fancy2 at u11 as marta with dissolve
    m "Hahaha..."
    show marta3date 1g 2a 3a fancy1 at u11 as marta with dissolve
    m "Oh my."
    show marta3date 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Hey. I want to hear more!"
    jump date_main_marta_p2bb
label date_main_marta_p2_bad_end:
    show marta2 1e 2d 3a fancy1 at u11 as marta with dissolve
    m "So you think I'm ugly. Great!"
    show marta2 1f 2d 3a fancy1 at u11 as marta with dissolve
    p "Wait..."
    show marta2 1e 2d 3a fancy2 at u11 as marta with dissolve
    m "No, the wait is over, [player_name]."
    jump marta_date_fail
label date_main_marta_p2b:
    show marta3date 1ee 2c 3a fancy2 at u11 as marta with dissolve
    m "I'm the best, huh?"
    show marta3date 1a 2c 3a fancy1 at u11 as marta with dissolve
    p "That's right."
    show marta2date 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "I know it, but, um, w-what exactly is so special about me?"
    jump date_main_marta_p2bbb
label date_main_marta_p2bb:
    show marta2date 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "But, um, w-what exactly is so special about me?"
    jump date_main_marta_p2bbb
label date_main_marta_p2bbb:
    show marta2date 1a 2b 3a fancy1 at u11 as marta with dissolve
    p "Well, it's..."
    show marta2date 1e 2a 3a fancy2 at u11 as marta with dissolve
    m "No, wait! D-don't spoil it, okay? I want to guess..."
    show marta2date 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "Even if you guess it, I'll always come up with a new reason."
    show marta2date 1c 2c 3c blush fancy1 at u11 as marta with dissolve
    m "..."
    show marta2date 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "You know what?"
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "I just thought..."
    show marta3date 1e 2a 3b fancy1 at u11 as marta with dissolve
    m "I don't know why, but... I feel safe with you."
    show marta3date 1g 2a 3a fancy1 at u11 as marta with dissolve
    m "H-has a girl ever said something like this to you?"
    show marta3date 1a 2a 3a noblush fancy1 at u11 as marta with dissolve
    p "Um, yeah, a few times, I think."
    show marta3date 1ee 2a 3b noblush fancy2 at u11 as marta with dissolve
    m "I'm glad to be the first one."
    show marta3date 1d 2a 3a blush fancy1 at u11 as marta with dissolve
    m "It makes me happy..."
    show marta3date 1ee 2a 3b noblush fancy2 at u11 as marta with dissolve
    m "Well, maybe!"
    show marta2date 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "Just maybe? Well, I want to make sure."
    p "Hey, what else makes you happy?"
    show marta2date 1c 2c 3a fancy1 at u11 as marta with dissolve
    m "Um, I..."
    show marta2date 1e 2c 3c fancy2 at u11 as marta with dissolve
    m "By the way, it's a secret, you hear?"
    show marta2date 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "Ahem!"
    show marta3date 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "I'm happy when I'm on the road."
    show marta3date 1d 2a 3b fancy1 at u11 as marta with dissolve
    m "I have everything ahead of me, nothing behind me."
    show marta2date 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "I see something new, I {i}become{/i} something new."
    show marta2date 1d 2a 3a fancy1 at u11 as marta with dissolve
    m "Also... I like getting ill."
    show marta2date 1e 2a 3a fancy2 at u11 as marta with dissolve
    m "Only if it's nothing serious, of course."
    show marta2date 1c 2a 3d fancy1 at u11 as marta with dissolve
    m "I stay in a bed for a day to... stop for a while."
    show marta2date 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "You know, watch some movies, play games..."
    show marta2date 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "Can't you do it any other time?"
    show marta2date 1g 2b 3d fancy1 at u11 as marta with dissolve
    m "I can, but I'd feel guilty."
    show marta2date 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "..."
    show marta2date 1b 2c 3a fancy1 at u11 as marta with dissolve
    m "Hey, do you like art?"
    show marta2date 1g 2a 3a fancy1 at u11 as marta with dissolve
    p "Yeah, why?"
    show marta2date 1e 2c 3a blush fancy2 at u11 as marta with dissolve
    m "I'm dying to see an expo nearby. Let's go!"
    show marta2date 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "Sure!"
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene cg_marta_5_3 with fade
    $ persistent.unlock_cg_marta_5_3 = 1
    "Her hand is warm and soft."
    "But man, is the grip tight!"
    "I wish the time would go slower."
    "On and on, on and on, on and on..."
    p "Hey, Marta!"
    scene cg_marta_5_2 as marta with dissolve
    m "That's my name."
    scene cg_marta_5_3 as marta with dissolve
    p "What's that expo about?"
    m "Does it matter?"
    p "No."
    scene cg_marta_5_2 as marta with dissolve
    m "That's correct."
    scene cg_marta_5_3 as marta with dissolve
    m "Anyway, it's about landscape art, and..."
    m "One painting there is out of this world. Also, it feels familiar."
    m "You know, like I've been there before."
    scene black with fade
    $ renpy.pause(2, hard=True)
    scene date_expo with fade
    "The painting is pretty cool."
    "More importantly, Marta took my hand again..."
    "I think I adore landscape art."
    show marta2close 1e 2d 3a blush fancy2 at u11 as marta with dissolve
    m "Hey, it's not like I invited you here because I didn't want to leave..."
    show marta2close 1d 2a 3a fancy2 at u11 as marta with dissolve
    p "If anything, it's me who wanted to stay."
    show marta2close 1c 2a 3c fancy1 at u11 as marta with dissolve
    m "..."
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "I also want to stay with you for a little while longer."
    show marta3close 1g 2b 3a fancy1 at u11 as marta with dissolve
    m "Just a little, tiny bit!"
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "[player_name]..."
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "Do you know how to really appreciate a painting?"
    show marta2close 1g 2a 3a fancy2 at u11 as marta with dissolve
    p "You tell me."
    show marta2close 1c 2a 3d fancy1 at u11 as marta with dissolve
    m "Close your eyes, make the image appear in your mind..."
    show marta2close 1d 2c 3a fancy2 at u11 as marta with dissolve
    m "Stay like that for five seconds with your eyes closed, no cheating!"
    show marta3close 1g 2a 3a fancy1 at u11 as marta with dissolve
    m "Open your eyes, and you'll see the painting in a new light."
    show marta3close 1e 2c 3c fancy1 at u11 as marta with dissolve
    m "Go ahead, t-try it!"
    show marta3close 1b 2a 3a fancy1 at u11 as marta with dissolve
    p "Alright!"
    play music "music/succeed.ogg" fadein 2 fadeout 2
    scene black with fade
    "I close my eyes."
    m "Now, count to five! Promise not to open your eyes before that!"
    p "One..."
    p "Two..."
    p "Three..."
    p "Four..."
    "The room just got warmer for no reason."
    p "Five."
    show cg_marta_6_a as marta
    with fade
    $ renpy.pause(6.0, hard=True)
    "..."
    "She's... she's so close!"
    show cg_marta_6_b as marta with dissolve
    "The way she stands... does it mean... can I?"
    show cg_marta_6_b as marta:
        linear 1 zoom 1.1
    $ renpy.pause(1.0, hard=True)
    $ persistent.unlock_cg_marta_6_1 = 1
    "I move my face closer..."
    show cg_marta_6_b as marta:
        zoom 1.1
        linear 1 zoom 1.2
    $ renpy.pause(1.0, hard=True)
    "And closer..."
    show cg_marta_6_b as marta:
        zoom 1.2 ypos 1080
        linear 1 zoom 1.3 ypos 1100
    $ renpy.pause(1.0, hard=True)
    "And closer..."
    show cg_marta_6_b as marta:
        zoom 1.3 ypos 1100
        linear 1 zoom 1.4 ypos 1100
    $ renpy.pause(1.0, hard=True)
    "And closer..."
    scene black with fade
    "Then our worlds collide."
    $ m_date_finished = 1

    $achievement.grant("Openspace")
    init:
        $achievement.register("Openspace")
        $achievement.sync()
    $achievement.sync()

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            $ new_game2_marta_done = 1
            jump wb2

    if new_game1_marta_set == 1:
        scene black with fade
        $ renpy.pause(2, hard=True)
        $ new_game1_marta_done = 1
        jump wb1
    jump date_end
label marta_date_fail:
    show marta2 1f 2d 3d fancy1 at u11 as marta with dissolve
    p "Alright, let's change the topic!"
    show marta2 1c 2d 3d fancy1 at u11 as marta with dissolve
    m "Don't bother."
    show marta2 1f 2d 3d fancy1 at u11 as marta with dissolve
    p "What's wrong?"
    show marta2 1f 2a 3a fancy1 at u11 as marta with dissolve
    "She says nothing."
    $ renpy.pause(1.0, hard=True)
    play sound "<from 0 to 3>sound/ringtone.ogg"
    $ renpy.pause(2.0, hard=True)
    show marta2 1d 2a 3a fancy1 at u11 as marta with dissolve
    m "[player_name], I need to take this call, alright?"
    show marta2 1f 2a 3a fancy1 at u11 as marta with dissolve
    p "Sure, go ahead."
    hide marta with dissolve
    show marta2 1f 2a 3d fancy1 at u11 as marta with dissolve
    "She comes back in a few."
    show marta2 1c 2a 3a fancy1 at u11 as marta with dissolve
    m "Um... [player_name], I have to go."
    show marta2 1f 2a 3a fancy1 at u11 as marta with dissolve
    p "Right now?"
    show marta2 1e 2d 3a fancy2 at u11 as marta with dissolve
    m "Yeah. I'm sorry, it's something urgent."
    show marta2 1c 2d 3a fancy1 at u11 as marta with dissolve
    p "Need my help?"
    show marta2 1e 2d 3d fancy2 at u11 as marta with dissolve
    m "No, thanks. See you on Monday!"
    show marta2 1c 2d 3d fancy1 at u11 as marta with dissolve
    p "S-see you."
    hide marta with dissolve
    "I ask for the bill and leave."
    jump failed_date
label fake_date_nana:
    play music "music/admit.ogg"
    $ renpy.pause(1, hard=True)
    scene cafe with fade
    "\"Doorsia\" again."
    "I'm 10 minutes early. Should I browse the menu?"
    "No, wait! I better hit the restroom. What if my hair's messed up?"
    scene black with fade
    $ renpy.pause(2, hard=True)
    scene cafe_table with fade
    "Nana should arrive anytime soon."
    "I think it's okay for a girl to be slightly late."
    "After all, she wants to look good!"
    "Wait, I'm talking about Nana... Anyway!"
    "Do {i}I{/i} look good enough?"
    play sound "sound/phone.ogg"
    $ renpy.pause(1, hard=True)
    "My phone vibrates. One new message!"
    "Can't believe Nana's considerate enough to let me know she's late!"
    play music "music/unlucky_beat.ogg" fadein 2 fadeout 2
    "\"Sorry, I don't feel well. Need to stay home. See you on Monday!\""
    "What? Why didn't she call me this morning?"
    "Wait, what if she's been trying to get herself together all this time?"
    "You know, just to spend time with me?"
    "Oh my... I decide to call Nana myself."
    $ renpy.pause(2, hard=True)
    "She doesn't pick the phone."
    "I gave Nana a few more calls, but to no avail. Weird..."
    "One last call..."
    "Click! I got through."
    $ chad_name = "???"
    chad "Bro, stop calling, seriously."
    p "Who's that?"
    chad "Doesn't matter."
    p "Where's Nana!"
    chad "How much are you paying for this information?"
    show nana1 1e 2d 3a regular2 at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "Chad! Give me my phone, now!"
    $ chad_name = "Chad"
    hide nana with dissolve
    chad "Oh well. So long, bro."
    show nana1 1d 2a 3d regular2 at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "[player_name]?"
    show nana1 1a 2a 3d regular2 at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    p "Nana, what's happening? Are you okay? That message of yours..."
    show nana3 1e 2a 3d  at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "Yeah, I feel horrible today... on my way to see a doctor."
    show nana3 1a 2a 3a  at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    p "Who's that guy who picked up your phone?"
    show nana3 1c 2a 3a  at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "He's a new neighbor of mine. We just met yesterday."
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "Chad has a car, and he said he'd give me a lift!"
    show nana1 1e 2c 3c blush regular1 at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "You should see his car, it moves {i}so{/i} fast!"
    hide nana with dissolve
    chad "Yep. Still got the moves."
    show nana3 1d 2a 3a noblush at u11 as nana with dissolve:
        xalign -.05
        ypos 1670
        zoom 1.2
    n "Thanks for calling, anyway! See you soon!"
    hide nana with dissolve

    $achievement.grant("Friendzone")
    init:
        $achievement.register("Friendzone")
        $achievement.sync()
    $achievement.sync()

    "She hangs up."
    jump failed_date
label date_nana:
    play music "music/admit.ogg"
    $ renpy.pause(1, hard=True)
    scene cafe with fade
    "Nana was terribly late."
    $ renpy.pause(1, hard=True)
    show nana1close 1d 2a 3a fancy2 at u11 as nana with dissolve
    n "Hi, [player_name]!"
    show nana1close 1d 2a 3b fancy1 at u11 as nana with dissolve
    n "I want a dessert!"
    show nana1close 1g 2a 3a fancy1 at u11 as nana with dissolve
    "No \"sorry for being late\", as expected."
    scene cg_nana_3_1 with fade
    $ persistent.unlock_cg_nana_3_1 = 1
    n "I want to order every single dessert here."
    n "Every single one!"
    show cg_nana_3_2 as nana with dissolve
    p "Will it fit?"
    show cg_nana_3_3 as nana with dissolve
    n "Now that you say it..."
    p "Just pick the best one."
    show cg_nana_3_1 as nana with dissolve
    n "Impossible. All their desserts are the best."
    show cg_nana_3_2 as nana with dissolve
    n "Choose one for me if you know better..."
    menu:
        "\"Peach Passion\", chocolate peach cake.":
            jump dessert_choice_wrong_nana
        "\"Strawberry Delight\", strawberry shortcake.":
            jump dessert_choice_right_nana
        "\"Cherry D'Or\", cherry mille-feuille.":
            jump dessert_choice_wrong_nana
label dessert_choice_right_nana:
    show cg_nana_3_1 as nana with dissolve
    n "Wow! That's what I wanted!"
    n "Honestly, I was sure you'd guess wrong."
    show cg_nana_3_3 as nana with dissolve
    p "So there {i}was{/i} something you wanted the most."
    n "Of course... strawberries! It's a no-brainer."
    show cg_nana_3_2 as nana with dissolve
    n "Name one thing which is cuter than a strawberry. Oh wait, you can't."
    show cg_nana_3_2 as nana with dissolve
    n "Hey, I'll share one strawberry with you."
    n "But only one!"
    jump date_main_nana_p1
label dessert_choice_wrong_nana:
    show cg_nana_3_1 as nana with dissolve
    n "You failed!"
    n "It's obvious that strawberries are cuter than cherries and peaches."
    show cg_nana_3_3 as nana with dissolve
    n "I'll have a strawberry shortcake."
    p "Well, I did my best."
    n "I appreciate the effort, [player_name]."
    show cg_nana_3_2 as nana with dissolve
    n "As a reward, you're allowed to eat one strawberry from my cake."
    show cg_nana_3_3 as nana with dissolve
    n "But only one!"
    jump date_main_nana_p1
label date_main_nana_p1:
    scene cafe
    show nana3date 1a 2a 3a fancy at u11 as nana
    with fade
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Alright, [player_name]!"
    show nana3date 1c 2a 3d fancy at u11 as nana with dissolve
    n "Right now, you're probably trying to come up with an interesting topic..."
    show nana1date 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "Let me help you with that!"
    show nana1date 1a 2a 3a fancy2 at u11 as nana with dissolve
    p "O-okay..."
    show nana3date 1e 2a 3a fancy at u11 as nana with dissolve
    n "Say... what do you think a good date is?"
    menu:
        "Hm... doesn't matter as long as it's fun.":
            jump date_main_nana_p1a
        "When you get to know each other a little bit.":
            play music "music/unlucky_beat.ogg" fadeout 2 fadein 2
            jump date_main_nana_p1b
label date_main_nana_p1a:
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Spot on!"
    show nana3date 1c 2a 3d fancy at u11 as nana with dissolve
    n "But what {i}is{/i} fun about?"
    show nana3date 1b 2a 3d fancy at u11 as nana with dissolve
    p "Fun things are fun, that's all I know."
    show nana3date 1e 2a 3a fancy at u11 as nana with dissolve
    n "Okay, I'll tell you."
    show nana1date 1b 2a 3a fancy2 at u11 as nana with dissolve
    n "Fun is about being spontaneous and easy-going!"
    show nana1date 1d 2a 3a fancy1 at u11 as nana with dissolve
    n "Few things are worse than long term planning."
    show nana1date 1g 2a 3a fancy1 at u11 as nana with dissolve
    p "What's so bad about it?"
    show nana3date 1e 2a 3a fancy at u11 as nana with dissolve
    n "It's useless! Nothing in life goes as planned."
    show nana3date 1e 2a 3d fancy at u11 as nana with dissolve
    n "Trying to stick to a plan turns you into a non-playable character."
    show nana1date 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "That's how you miss an opportunity of a lifetime."
    show black with fade
    $ renpy.pause(.1, hard=True)
    jump date_main_nana_p2
label date_main_nana_p1b:
    show nana2date 1d 2b 3d fancy at u11 as nana with dissolve
    n "Meh, what a boring reply."
    show nana2date 1c 2a 3a fancy at u11 as nana with dissolve
    n "Would you like to learn about my blood type? Or what I had for breakfast?"
    show nana2date 1c 2b 3d fancy at u11 as nana with dissolve
    n "It makes no difference and you'll forget about it anyway."
    show nana2date 1f 2b 3d fancy at u11 as nana with dissolve
    p "So you don't want to talk about yourself..."
    show nana2date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Actions speak louder than words."
    show nana2date 1f 2a 3a fancy at u11 as nana with dissolve
    p "Okay, I have something else to discuss."
    show nana1date 1d 2a 3a fancy1 at u11 as nana with dissolve
    n "Surprise me!"
    show nana1date 1a 2a 3a fancy1 at u11 as nana with dissolve
    menu:
        "Ermy makes a video game, and I'm the only one who knows about it.":
            jump date_main_nana_bad_end
        "What should I do in order to kiss you?":
            play music "music/admit.ogg" fadeout 2 fadein 2
            jump date_main_nana_p1aa
label date_main_nana_bad_end:
    show nana1 1e 2d 3d fancy2 at u11 as nana with dissolve
    n "Are you kidding me?"
    show nana1 1f 2d 3d fancy2 at u11 as nana with dissolve
    p "Wait until you hear what the game's about."
    show nana2 1c 2b 3d fancy at u11 as nana with dissolve
    n "I don't know Ermy well, but..."
    show nana2 1d 2b 3d fancy at u11 as nana with dissolve
    n "Something tells me he would like you to keep it between you two."
    show nana1 1e 2d 3d fancy2 at u11 as nana with dissolve
    n "Do you know how to keep a secret, [player_name]?"
    show nana1 1f 2d 3d fancy2 at u11 as nana with dissolve
    p "Alright, alright, let's change the topic again..."
    show nana1 1a 2d 3a fancy2 at u11 as nana with dissolve
    p "You'll like the next one."
    show nana1 1f 2d 3a fancy2 at u11 as nana with dissolve
    n "..."
    show nana1 1e 2a 3a fancy2 at u11 as nana with dissolve
    n "Look, it only shows you don't really have anything to discuss."
    show nana1 1f 2a 3a fancy2 at u11 as nana with dissolve
    p "Why?"
    show nana2 1c 2b 3d fancy at u11 as nana with dissolve
    n "Because."
    jump nana_date_fail
label date_main_nana_p1aa:
    show nana1date 1a 2c 3c fancy2 blush at u11 as nana with dissolve
    $ renpy.pause(.7, hard=True)
    show nana1date 1d 2c 3a fancy2 blush at u11 as nana with dissolve
    n "Okay, now I'm surprised!"
    show nana3date 1c 2c 3d fancy noblush at u11 as nana with dissolve
    n "Not sure about myself though, but..."
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Let's talk about any other girl, alright?"
    show nana3date 1d 2c 3a fancy at u11 as nana with dissolve
    n "Tell me, [player_name], how does one go about kissing a lady?"
    show nana3date 1b 2a 3a fancy at u11 as nana with dissolve
    p "Well, by making her develop a feeling, for starters..."
    show nana3date 1c 2a 3d fancy at u11 as nana with dissolve
    n "But how? That's the question!"
    show nana3date 1a 2a 3d fancy at u11 as nana with dissolve
    p "What do you mean? I'll show her that I like her."
    show nana3date 1b 2a 3d fancy at u11 as nana with dissolve
    n "Another one bites the dust."
    show nana1date 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "Never show a girl that you like her, [player_name]."
    show nana1date 1b 2a 3d fancy2 at u11 as nana with dissolve
    n "Otherwise she'll lose the interest in no time."
    p "I don't get it..."
    show nana3date 1b 2a 3b fancy at u11 as nana with dissolve
    n "You should be a man of mistery."
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "As soon as you start being predictable, it's game over."
    show nana3date 1g 2a 3a fancy at u11 as nana with dissolve
    p "How am I supposed to act then?"
    show nana3date 1b 2a 3d fancy at u11 as nana with dissolve
    n "Act like she's not the only one around."
    show nana3date 1a 2a 3b fancy at u11 as nana with dissolve
    p "What if she's the only one?"
    show nana3date 1e 2a 3a fancy at u11 as nana with dissolve
    n "Then you don't see the other fish in the sea."
    show nana1date 1d 2c 3a fancy1 at u11 as nana with dissolve
    n "Anyway, just become a busy, interesting person."
    show nana1date 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "You'll have no time to worry about girls that way. Guess what..."
    show nana1date 1b 2c 3b fancy1 at u11 as nana with dissolve
    n "They now pay attention."
    show nana1date 1g 2c 3a fancy2 at u11 as nana with dissolve
    p "So... to kiss you, I should act indifferent?"
    show nana3date 1c 2c 3c fancy blush  at u11 as nana with dissolve
    n "Me? Why me, [player_name]."
    show nana3date 1b 2a 3d fancy noblush at u11 as nana with dissolve
    n "We should exchange love letters and all if you want to kiss me."
    p "..."
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Just kidding."
    show nana1date 1e 2a 3a fancy2 at u11 as nana with dissolve
    n "I never discuss stuff like this on empty stomach, [player_name]."
    show nana3date 1b 2a 3d fancy at u11 as nana with dissolve
    n "Let's postpone it until we're done with our cakes."
    jump date_main_nana_p2
label date_main_nana_p2:
    scene cg_nana_3_4 with fade
    n "Wooow! Look at this!"
    n "It's a shortcake!"
    n "And it's awesome!"
    p "You promised to share one strawberry with me."
    show cg_nana_3_5 as nana with dissolve
    n "Did I? Well, a promise is a promise."
    p "Okay, which one should I take?"
    n "{i}You{/i}? No way! What if your fork is dirty and contagious?"
    p "Hey, I take care of myself."
    n "I'm talking about the fork."
    show cg_nana_3_6 as nana with dissolve
    n "Well, there's no other way but..."
    n "[player_name], [player_name]!"
    show cg_nana_5_1 as nana with dissolve
    $ persistent.unlock_cg_nana_5_1 = 1
    n "Say \"Aaaahhh\"."
    n "\"Aaaahhh.\""
    n "\"Aaaahhh!\""
    "How should I eat in a romantic way?"
    n "[player_name]..."
    p "Yeah?"
    n "Why do you make your lips like this? You look like a duck."
    n "\"Aaaahhh.\""
    show black with fade
    $ renpy.pause(.1, hard=True)
    scene cafe
    show nana1date 1b 2a 3b fancy1 at ui11 as nana behind black
    with fade
    p "It was tasty."
    show nana1date 1d 2a 3a fancy1 at u11 as nana with dissolve
    n "Yeah, they know what they're doing here."
    show nana1date 1b 2a 3a fancy2 at u11 as nana with dissolve
    p "It's because you gave it to me."
    show nana1date 1b 2a 3a blush fancy2 at u11 as nana with dissolve
    n "..."
    show nana1date 1d 2a 3d noblush fancy1 at u11 as nana with dissolve
    n "Oh you."
    show nana3date 1b 2a 3a fancy at u11 as nana with dissolve
    p "Want me to order something else for you?"
    show nana3date 1e 2a 3d fancy at u11 as nana with dissolve
    n "No thanks, then you won't be asking how to kiss me anymore."
    show nana3date 1d 2a 3a fancy at u11 as nana with dissolve
    n "Well, jokes aside, I'd really prefer you to know me better and all."
    show nana3date 1b 2a 3d fancy at u11 as nana with dissolve
    n "I probably contradict myself..."
    p "No, it's okay."
    show nana3date 1d 2c 3a fancy at u11 as nana with dissolve
    n "Do you believe me?"
    show nana3date 1b 2c 3a fancy at u11 as nana with dissolve
    p "Yeah, why?"
    show nana1date 1d 2a 3a fancy1 at u11 as nana with dissolve
    n "I'm lying!"
    show nana1date 1d 2d 3d fancy2 at u11 as nana with dissolve
    n "A girl decides if she could kiss you the first minute you two meet."
    show nana1date 1b 2d 3d fancy2 at u11 as nana with dissolve
    p "You're kidding me."
    show nana1date 1d 2a 3a fancy2 at u11 as nana with dissolve
    n "I wish."
    show nana1date 1b 2a 3a fancy2 at u11 as nana with dissolve
    menu:
        "Regardless of that, I actually want to know you better.":
            play music "music/unlucky_beat.ogg" fadeout 2 fadein 2
            jump date_main_nana_p2a
        "Does it mean you already know whether or not you could kiss me?":
            play music "music/relax_theme.ogg" fadeout 2 fadein 2
            jump date_main_nana_p2b
label date_main_nana_p2a:
    show nana1date 1c 2a 3d fancy2 at u11 as nana with dissolve
    n "Don't you listen to what I'm saying {i}at all{/i}?"
    show nana1date 1f 2a 3d fancy2 at u11 as nana with dissolve
    p "Well, it's important to me."
    show nana3date 1c 2a 3a fancy at u11 as nana with dissolve
    n "I'll tell you next time."
    show nana3date 1a 2a 3a fancy at u11 as nana with dissolve
    menu:
        "Why not now?":
            jump date_main_nana_p2_bad_end
        "Okay, next time!":
            play music "music/relax_theme.ogg" fadeout 2 fadein 2
            jump date_main_nana_p2aa
label date_main_nana_p2_bad_end:
    show nana2 1d 2b 3d fancy at u11 as nana with dissolve
    n "Sorry, I don't feel like it."
    show nana2 1a 2b 3d fancy at u11 as nana with dissolve
    p "What's wrong?"
    show nana2 1c 2b 3a fancy at u11 as nana with dissolve
    n "Nothing. Sorry I don't go by the script."
    show nana3 1d 2b 3a fancy at u11 as nana with dissolve
    n "Can I order another tart?"
    show nana3 1a 2b 3d fancy at u11 as nana with dissolve
    p "Sure!"
    jump nana_date_fail
label date_main_nana_p2aa:
    p "And this time, tell me about that first minute..."
    p "Does it mean you also know whether or not you could kiss me?"
    jump date_main_nana_p2b
label date_main_nana_p2b:
    show nana1date 1d 2c 3a fancy1 at u11 as nana with dissolve
    n "Of course, I already know."
    show nana1date 1b 2c 3a fancy1 at u11 as nana with dissolve
    p "And..."
    show nana3date 1d 2c 3b fancy at u11 as nana with dissolve
    n "Ha, no way I'm telling you."
    show nana3date 1b 2c 3a fancy at u11 as nana with dissolve
    n "By the way, what do we do next?"
    p "How about going for walk?"
    show nana1date 1d 2b 3a fancy1 at u11 as nana with dissolve
    n "Let's do it! Also..."
    show nana1date 1c 2a 3a fancy2 blush at u11 as nana with dissolve
    n "Promise you take me here again, [player_name]."
    scene black with fade
    "Next second Nana changes her mind, and now we're going to an expo."
    n "Art stuff."
    scene date_expo with fade
    n "Look, a painting!"
    n "Check out this fusion of ancient and relatively modern..."
    show nana1close 1d 2c 3c fancy1 at u11 as nana with dissolve
    n "[player_name], [player_name]..."
    show nana3close 1d 2a 3d noblush fancy at u11 as nana with dissolve
    n "What's your biggest fear?"
    show nana3close 1b 2a 3d fancy at u11 as nana with dissolve
    p "Living a meaningless life."
    show nana1close 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "Then we have something in common."
    show nana1close 1g 2a 3a fancy2 at u11 as nana with dissolve
    "She says nothing for a few seconds..."
    show nana1close 1g 2a 3a fancy2 at ui11 as nana:
        ypos 1410
        linear .7 zoom 1.1 ypos 1480
    "And then she silently stands much closer."
    show nana2close 1d 2b 3d fancy blush at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "That fear... It's because of my family."
    show nana2close 1d 2b 3b fancy at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "My mom and dad are very conservative, so my life was predefined."
    show nana2close 1c 2b 3d fancy at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "Good education, steady job, happy marriage, kids, growing old..."
    show nana1close 1e 2d 3c fancy1 at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "Thanks, but no thanks."
    show nana1close 1c 2b 3a fancy2 at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "I don't blame them though... They're non-playable characters."
    show nana1close 1f 2b 3a fancy2 at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    p "Hey, go easy on your parents. They're family, after all."
    show nana3close 1d 2c 3d fancy noblush at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "You know what's funny?"
    show nana3close 1c 2b 3d fancy at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "Sometimes I see a light in their eyes when they do something fun."
    show nana2close 1c 2b 3b fancy at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "It only lasts for a while, then they're back to their programmings."
    show nana1close 1d 2a 3a fancy2 at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    n "Hey, I want some fresh air."
    show nana1close 1g 2a 3b blush fancy2 at ui11 as nana with dissolve:
        zoom 1.1
        ypos 1480
    p "Sure!"
    scene black with fade
    play music "music/succeed.ogg" fadeout 2 fadein 2
    "We move to a small park nearby."
    n "Hey, [player_name], you're pretty tall, you know."
    n "I wonder if come closer... would the difference make me look funny?"
    p "There's only one way to find out!"
    scene cg_nana_6_1 with fade
    $ persistent.unlock_cg_nana_6_1 = 1
    "Next thing I know we're standing like this."
    "Her gentle body is so close!"
    n "[player_name]..."
    n "I told you that fun is about the only thing I need..."
    n "Well, you know what?"
    n "Maybe you're my type of fun, [player_name]."
    n "Oh, it probably sounds so cheesy..."
    n "I... I don't know what to say right now..."
    p "Well then... why don't we just stay like this for a while?"
    p "Comfortable silence is rare."
    p "Just like you..."
    pause
    scene cg_nana_9_1 with fade
    n "Hey, [player_name], look!"
    show cg_nana_9_2 as nana with dissolve
    n "Who's tall now, huh?"
    show cg_nana_9_1 as nana with dissolve
    n "How does it make you feel?"
    p "Inferior."
    show cg_nana_9_2 as nana with dissolve
    n "Ha!"
    show cg_nana_9_1 as nana with dissolve
    p "Watch me, watch me now!"
    n "Let me get closer to you so you can see it well enough!"
    show cg_nana_9_1 as nana:
        linear 1 xalign .6 yalign .4 zoom 1.2
    n "W-well enough..."
    show cg_nana_9_4 as nana with dissolve
    n "Yeah..."
    show cg_nana_9_4 as nana:
        linear 1 xalign .6 yalign .4 zoom 1.3
    "Her face gets closer and closer."
    show cg_nana_9_4 as nana:
        linear 1 xalign .6 yalign .4 zoom 1.4
    "So close. So close."
    show cg_nana_9_1 as nana with dissolve
    n "You know, on the other hand..."
    n "When I'm with you, [player_name]..."
    show cg_nana_9_6 as nana with dissolve
    $ persistent.unlock_cg_nana_9_6 = 1
    n "I don't mind feeling weak."
    show cg_nana_9_6 as nana:
        linear 1 xalign .6 yalign .4 zoom 1.5
    "I want to give a reply, but..."
    show cg_nana_9_4 as nana with dissolve
    show cg_nana_9_4 as nana:
        linear 1 xalign .6 yalign .4 zoom 1.6
    "Words suddenly become meaningless."
    $ n_date_finished = 1

    $achievement.grant("Maincharacter")
    init:
        $achievement.register("Maincharacter")
        $achievement.sync()
    $achievement.sync()

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            $ new_game2_nana_done = 1
            jump wb2

    if new_game1_nana_set == 1:
        scene black with fade
        $ renpy.pause(2, hard=True)
        $ new_game1_nana_done = 1
        jump wb1
    jump date_end
label nana_date_fail:
    scene black with fade
    "Nana orders another dessert."
    "She doesn't talk much, giving me one-word replies."
    "Meanwhile, I excuse myself to the restroom."
    "I need to step it up."
    "Question is, what can I do?"
    scene cafe_table with fade
    "When I return to my table, Nana is nowhere to be found."
    "Probably went to the restroom as well."
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene cafe_table with fade
    "Well, it's not the case."
    "I try to call Nana but she doesn't pick up the phone."
    "The only thing left for me is to ask for the bill."
    jump failed_date
label date_ermy:
    play music "music/disko_jester.ogg" fadeout 1.5 fadein 1.5
    scene cafe_kawa with fade
    show ermy1 pose2 1a 2a 3a at u11 as ermy
    "Ermy was right on time."
    "However, the cafe was full, so we moved to the next one around the corner."
    "Turns out it's also pretty upscale, as expected of this hip district."
    show ermy1 pose1 1c 2b 3a at u11 as ermy with dissolve
    e "I should've put on my \"going-out\" shirt..."
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    "We make our orders."
    show ermy1 pose2 1e 2a 3d at u11 as ermy with dissolve
    e "So... What do you think about my game?"
    if ermy_game_finished_d2 == 1:
        jump date_main_ermy_p0a
    else:
        jump date_main_ermy_p0b
label date_main_ermy_p0b:
    "Jeez, I totally forgot about it."
    p "Uh, well, it's okay..."
    show ermy1 pose2 1d 2a 3a at u11 as ermy with dissolve
    e "Okay? What do you mean by that?"
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "It's decent, Ermy."
    show ermy1 pose2 1f 2a 3d at u11 as ermy with dissolve
    e "Hm..."
    show ermy1 pose2 1e 2d 3d at u11 as ermy with dissolve
    e "I don't buy it."
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "You haven't played my game!"
    show ermy1 pose2 1f 2d 3c at u11 as ermy with dissolve
    p "C'mon, it's not true. It was a promise."
    show ermy1 pose1 1d 2a 3a at u11 as ermy with dissolve
    e "Very well, thanks for playing!"
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "You're welcome."
    show ermy1 pose2 1d 2a 3a at u11 as ermy with dissolve
    e "How did you like the plot?"
    show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
    p "It got me hooked!"
    show ermy1 pose2 1b 2c 3d at u11 as ermy with dissolve
    e "What's your favorite part then?"
    show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
    p "Um, like, I don't really have one... the plot's balanced, you know."
    show ermy1 pose2 1c 2c 3d at u11 as ermy with dissolve
    e "Who's your favorite character?"
    show ermy1 pose2 1f 2a 3d at u11 as ermy with dissolve
    p "They're all great. I especially like that girl, what's her name..."
    show ermy1 pose2 1c 2b 3d at u11 as ermy with dissolve
    e "I hope you appreciated that one male character as well."
    show ermy1 pose2 1e 2b 3a at u11 as ermy with dissolve
    e "The old guy who's an army general..."
    show ermy1 pose2 1f 2d 3c at u11 as ermy with dissolve
    p "Yeah, he rocks!"
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "He would if he existed... I'm leaving."

    $achievement.grant("Nogames")
    init:
        $achievement.register("Nogames")
        $achievement.sync()
    $achievement.sync()

    jump ermy_date_fail
label date_main_ermy_p0a:
    p "I think you need to step it up."
    show ermy1 pose1 1h 2a 3b at u11 as ermy with dissolve
    e "{i}Computer{/i} game, [player_name]!"
    show ermy1 pose1 1a 2a 3a at u11 as ermy with dissolve
    p "Just messing with you. Well... Do you want an honest answer?"
    show ermy1 pose2 1g 2a 3b at u11 as ermy with dissolve
    e "Of course. Give me a review!"
    menu:
        "Give a positive review.":
            jump date_main_ermy_p1a
        "Give a negative review.":
            jump date_main_ermy_p1b
label date_main_ermy_p1b:
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "Look, honestly... I wanted to compliment you, but..."
    show ermy1 pose2 1f 2c 3c at u11 as ermy with dissolve
    p "The game's really weak."
    show ermy1 pose2 1c 2c 3c at u11 as ermy with dissolve
    e "Why?"
    show ermy1 pose2 1f 2a 3a at u11 as ermy with dissolve
    p "First of all, the setting is messed up."
    show ermy1 pose2 1f 2b 3d at u11 as ermy with dissolve
    p "Second, the characters don't feel real."
    show ermy1 pose1 1c 2b 3a at u11 as ermy with dissolve
    e "Because it's a game, [player_name]."
    show ermy1 pose1 1f 2b 3a at u11 as ermy with dissolve
    p "Still, it feels kind of fake."
    show ermy1 pose2 1f 2b 3a at u11 as ermy with dissolve
    p "Next, your writing style could use some polishing."
    show ermy1 pose2 1f 2d 3d at u11 as ermy with dissolve
    p "If you think about it, half of the text is... omittable."
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "I don't agree."
    show ermy1 pose2 1e 2d 3d at u11 as ermy with dissolve
    e "I did my research... You know what?"
    show ermy1 pose2 1g 2c 3b at u11 as ermy with dissolve
    e "People value the script length."
    show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
    p "If so, then all games would be filled to the brim with nonsense..."
    p "Just to build up the length. I'm sure it's not what happens."
    show ermy1 pose1 1c 2b 3d blush at u11 as ermy with dissolve
    e "I need the length to make my writing look {i}solid{/i}, you know."
    show ermy1 pose1 1e 2b 3d at u11 as ermy with dissolve
    p "Ermy, try watching old \"Pink Panther\" animated shorts."
    p "Words are optional."
    show ermy1 pose2 1d 2a 3a at u11 as ermy with dissolve
    e "Hey, I can't afford the animation, it's too expensive."
    show ermy1 pose1 1c 2a 3d at u11 as ermy with dissolve
    e "All I can do is to describe a thing."
    show ermy1 pose2 1d 2a 3b at u11 as ermy with dissolve
    e "At least it should look fancy!"
    show ermy1 pose2 1h 2d 3a at u11 as ermy with dissolve
    e "Also, it's very easy to criticize."
    show ermy1 pose2 1d 2d 3c at u11 as ermy with dissolve
    e "Try writing something on your own... then we talk!"
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "As for now... I'm leaving!"
    jump ermy_date_fail

label date_main_ermy_p1a:
    menu:
        "Compliment the graphics.":
            show ermy1 pose2 1g 2c 3a at u11 as ermy with dissolve
            p "The graphics are awesome."
            show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
            p "By the way, main characters remind me of our class."
            show ermy1 pose1 1d 2a 3c at u11 as ermy with dissolve
            e "Ha, w-what a coincidence!"
            jump date_main_ermy_p1aa
        "Compliment the plot.":
            show ermy1 pose2 1g 2c 3a at u11 as ermy with dissolve
            p "The girls are nice, but what they do is even better."
            show ermy1 pose2 1g 2a 3c at u11 as ermy with dissolve
            p "I really like the plot, Ermy. There should be an answer though!"
            show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
            p "Don't you end it with cliffhanger."
            show ermy1 pose1 1d 2a 3b at u11 as ermy with dissolve
            e "Well, it's only because I don't know the answer myself."
            jump date_main_ermy_p1ab

label date_main_ermy_p1aa:
    jump date_main_ermy_p2
label date_main_ermy_p1ab:
    jump date_main_ermy_p2
label date_main_ermy_p2:
    show ermy1 pose2 1g 2a 3a at u11 as ermy with dissolve
    p "Best of luck with the game. Hope my friendly feedback helps."
    show ermy1 pose1 1e 2a 3d at u11 as ermy with dissolve
    e "Friendly feedback, huh..."
    show ermy1 pose1 1c 2a 3a at u11 as ermy with dissolve
    e "Do you believe in friendship?"
    show ermy1 pose1 1e 2a 3a at u11 as ermy with dissolve
    p "Sure, why?"
    show ermy1 pose1 1e 2b 3a blush at u11 as ermy with dissolve
    e "I've never had any friends, that's why."
    show ermy1 pose2 1f 2b 3a at u11 as ermy with dissolve
    p "Have you actually tried looking for one?"
    show ermy1 pose2 1d 2a 3d noblush at u11 as ermy with dissolve
    e "C'mon, [player_name], I'm not that stupid."
    show ermy1 pose2 1c 2a 3d at u11 as ermy with dissolve
    e "Actually, turns out it's really easy to {i}find{/i} friends."
    show ermy1 pose2 1f 2a 3d at u11 as ermy with dissolve
    p "I think I've lost you here, Ermy."
    show ermy1 pose2 1c 2a 3d at u11 as ermy with dissolve
    e "People like to be friends with you if they can feel superior."
    show ermy1 pose2 1b 2c 3a at u11 as ermy with dissolve
    e "See the point? I'm the perfect fit."
    show ermy1 pose2 1g 2c 3a at u11 as ermy with dissolve
    p "I wouldn't call it friendship, to be honest..."
    show ermy1 pose1 1c 2a 3a at u11 as ermy with dissolve
    e "That's why I said I've never had any friends."
    show ermy1 pose1 1e 2a 3a at u11 as ermy with dissolve
    p "What about, like, normal people? Those who just want to hang out?"
    show ermy1 pose2 1c 2b 3a at u11 as ermy with dissolve
    e "It goes smooth for some time, but then, all of a sudden, I'm alone again."
    show ermy1 pose2 1e 2b 3d at u11 as ermy with dissolve
    e "It's like they {i}need{/i} something from me, but... what exactly?"
    show ermy1 pose2 1f 2b 3d at u11 as ermy with dissolve
    p "Don't you think they want you to give back?"
    show ermy1 pose2 1d 2a 3a at u11 as ermy with dissolve
    e "Give back? What's that?"
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "You said some people want to have you as a friend to feel superior..."
    p "That's what you give back to them, your inferiority, that is."
    show ermy1 pose1 1e 2b 3d at u11 as ermy with dissolve
    e "Oh... Makes sense, I think..."
    show ermy1 pose2 1e 2b 3d at u11 as ermy with dissolve
    p "It's more complicated with the others."
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "If you're better, you give them excitement."
    p "I mean, being friends with someone popular is pretty cool, right?"
    show ermy1 pose2 1e 2a 3d at u11 as ermy with dissolve
    e "What if you're even?"
    show ermy1 pose2 1a 2a 3d at u11 as ermy with dissolve
    p "Then you give back attention. Everyday calls, texts...."
    show ermy1 pose1 1c 2b 3c at u11 as ermy with dissolve
    e "Jeez... I can't handle it!"
    show ermy1 pose2 1h 2a 3c at u11 as ermy with dissolve
    e "It's way too tiresome!"
    show ermy1 pose1 1d 2b 3a at u11 as ermy with dissolve
    e "I simply need someone who can understand me..."
    show ermy1 pose1 1e 2b 3b at u11 as ermy with dissolve
    e "Someone who won't ask for anything in return."
    show ermy1 pose1 1g 2b 3a at u11 as ermy with dissolve
    p "I wouldn't call it friendship either."
    show ermy1 pose2 1c 2c 3a at u11 as ermy with dissolve
    e "Why?"
    show ermy1 pose2 1a 2c 3a at u11 as ermy with dissolve
    p "Because it's charity."
    show ermy1 pose1 1c 2a 3d at u11 as ermy with dissolve
    e "But I need my own personal space!"
    show ermy1 pose1 1e 2a 3d at u11 as ermy with dissolve
    p "No one takes it away."
    p "Just being genuinely interested in your friend's life is enough."
    show ermy1 pose1 1b 2a 3b blush at u11 as ermy with dissolve
    e "Hmm... maybe I should get a couple of {i}female{/i} friends then."
    show ermy1 pose1 1d 2a 3a noblush at u11 as ermy with dissolve
    e "Do you believe in friendship between men and women, [player_name]?"
    menu:
        "I do.":
            play music "music/relax_theme.ogg" fadein 2 fadeout 2
            $ ido = 1
            jump date_main_ermy_p2a
        "I don't.":
            play music "music/relax_theme.ogg" fadein 2 fadeout 2
            jump date_main_ermy_p2b
label date_main_ermy_p2a:
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "Of course. I never objectify women."
    show ermy1 pose2 1b 2a 3a at u11 as ermy with dissolve
    e "Cool! How many female friends do you have?"
    show ermy1 pose2 1a 2a 3a at u11 as ermy with dissolve
    p "Uhh... well, zero at the moment, but I had quite a few in the past."
    show ermy1 pose1 1d 2a 3a at u11 as ermy with dissolve
    e "What happened?"
    show ermy1 pose1 1a 2a 3d at u11 as ermy with dissolve
    p "You see, I... I kind of started to like them..."
    show ermy1 pose2 1h 2a 3d at u11 as ermy with dissolve
    e "Wait a second, that means friendship was never your real intention."
    show ermy1 pose2 1a 2a 3d at u11 as ermy with dissolve
    p "Nah, it's a coincidence."
    jump date_main_ermy_p3
label date_main_ermy_p2b:
    show ermy1 pose2 1a 2c 3c at u11 as ermy with dissolve
    p "I only believe in a friend zone."
    show ermy1 pose1 1e 2b 3d at u11 as ermy with dissolve
    e "Hey, it's only a starting point!"
    show ermy1 pose1 1e 2b 3d at u11 as ermy with dissolve
    e "You win her over time, building trust and all..."
    show ermy1 pose1 1d 2c 3a at u11 as ermy with dissolve
    e "You know what they say?\n \"I wish I had a boyfriend like you.\""
    show ermy1 pose2 1c 2c 3c at u11 as ermy with dissolve
    e "Girls are just unlucky to run into bad guys instead of {i}me{/i}."
    show ermy1 pose2 1a 2a 3d at u11 as ermy with dissolve
    p "Maybe the bad guys are actually {i}good{/i} at giving emotions."
    show ermy1 pose2 1f 2b 3d at u11 as ermy with dissolve
    p "And you? You're a safe haven, Ermy."
    show ermy1 pose2 1h 2c 3c at u11 as ermy with dissolve
    e "It doesn't make sense!"
    show ermy1 pose2 1d 2c 3c at u11 as ermy with dissolve
    e "Bad guys always dump girls first. Why date someone who brings suffering?"
    show ermy1 pose2 1f 2c 3a at u11 as ermy with dissolve
    p "I'm not sure myself."
    show ermy1 pose1 1d 2c 3c at u11 as ermy with dissolve
    e "Wait, [player_name]!"
    show ermy1 pose1 1c 2b 3a at u11 as ermy with dissolve
    e "Suffering is an emotion."
    show ermy1 pose2 1b 2a 3b blush at u11 as ermy with dissolve
    e "But... I will find my princess, just you wait!"
    show ermy1 pose2 1a 2a 3a noblush at u11 as ermy with dissolve
    p "Let's hope that the princess is in another castle."
    jump date_main_ermy_p3
label date_main_ermy_p3:
    show ermy1 pose2 1a 2a 3a noblush at u11 as ermy with dissolve
    p "By the way, about the real reason why I invited you here..."
    show ermy1 pose2 1a 2c 3a noblush at u11 as ermy with dissolve
    p "I want to help you."
    show ermy1 pose2 1f 2b 3a noblush at u11 as ermy with dissolve
    p "You've been in low spirits lately..."
    show ermy1 pose2 1e 2b 3d at u11 as ermy with dissolve
    e "I have a depression as you may've guessed."
    p "A self-diagnosed one, I presume?"
    show ermy1 pose2 1h 2c 3c at u11 as ermy with dissolve
    e "So what of it? Whatever I'm doing, I don't enjoy it."
    show ermy1 pose2 1c 2b 3d at u11 as ermy with dissolve
    e "I can't concentrate, I feel horrible, I..."
    show ermy1 pose2 1e 2b 3d at u11 as ermy with dissolve
    p "At least you're able to concentrate on yourself."
    show ermy1 pose2 1a 2b 3d at u11 as ermy with dissolve
    p "Why don't you focus on your grades for today?"
    show ermy1 pose2 1c 2b 3a at u11 as ermy with dissolve
    e "You know what my father likes to say, [player_name]?"
    show ermy1 pose2 1b 2a 3b at u11 as ermy with dissolve
    e "\"Don't be sad. Tomorrow will be worse.\""
    show ermy1 pose2 1g 2b 3a at u11 as ermy with dissolve
    p "Seriously, get yourself together, work hard and thank me later."
    p "How else do you plan to get a nice job?"
    show ermy1 pose2 1b 2d 3d at u11 as ermy with dissolve
    e "\"Nice job\"... You're kidding me!"
    show ermy1 pose2 1h 2d 3a at u11 as ermy with dissolve
    e "I was born too late to explore the Earth and too early to explore the Galaxy."
    show ermy1 pose2 1h 2a 3a at u11 as ermy with dissolve
    e "I'm the middle child who doesn't really have a place."
    show ermy1 pose2 1h 2c 3a at u11 as ermy with dissolve
    e "All good jobs are already taken."
    show ermy1 pose2 1c 2b 3b at u11 as ermy with dissolve
    e "Unless you have connections, you won't get anywhere."
    show ermy1 pose2 1f 2b 3b at u11 as ermy with dissolve
    p "Then tell me, why do I see so many self-made people around?"
    show ermy1 pose2 1c 2a 3d at u11 as ermy with dissolve
    e "Meh, it's always a {i}lucky turn of events{/i}."
    show ermy1 pose2 1f 2a 3d at u11 as ermy with dissolve
    p "A lucky turn of events... after a whole streak of failures."
    p "Who knows, maybe that luck was well-deserved..."
    show ermy1 pose1 1c 2a 3a at u11 as ermy with dissolve
    e "So... what does it mean for me?"
    show ermy1 pose1 1a 2a 3a at u11 as ermy with dissolve
    p "Once again, you have to start doing {i}something{/i}."
    show ermy1 pose1 1c 2a 3d at u11 as ermy with dissolve
    e "But what exactly?"
    show ermy1 pose1 1a 2a 3d at u11 as ermy with dissolve
    p "Start from yourself! Like, eat healthy, work out, study..."
    show ermy1 pose2 1e 2a 3a at u11 as ermy with dissolve
    e "I've read something about the benefits of healthy living."
    show ermy1 pose2 1d 2c 3a at u11 as ermy with dissolve
    e "And if I work out, girls {i}will{/i} admire me! I'm going to make it!"
    show ermy1 pose2 1a 2c 3a at u11 as ermy with dissolve
    p "We're all going to make it."
    show ermy1 pose1 1c 2b 3d blush at u11 as ermy with dissolve
    e "I wonder where I should get my motivation from. It's a big issue for me."
    show ermy1 pose1 1a 2b 3d noblush at u11 as ermy with dissolve
    p "Hm... They say everything is easier when done with a friend."
    show ermy1 pose1 1a 2a 3a at u11 as ermy with dissolve
    p "Want to try making it together... together with me?"
    show ermy1 pose1 1a 2a 3a blush at u11 as ermy with dissolve
    e "..."
    show ermy1 pose1 1c 2a 3a at u11 as ermy with dissolve
    e "Are you saying that... that you want to be my... f-friend?"
    show ermy1 pose1 1a 2c 3c at u11 as ermy with dissolve
    p "Sure, why not?"
    show ermy1 pose2 1a 2a 3c at u11 as ermy with dissolve
    p "Don't think I'll support you for nothing though."
    show ermy1 pose2 1e 2a 3a at u11 as ermy with dissolve
    p "In return, I need your commitment. The day you start slacking again is the day we're done."
    p "No excuses. You ready for that? If you can't give back even that much, you better say it now."
    show ermy1 pose1 1a 2a 3a noblush at u11 as ermy with dissolve
    e "..."
    show ermy1 pose1 1e 2a 3a at u11 as ermy with dissolve
    e "I... I'm ready..."
    show ermy1 pose1 1a 2a 3a at u11 as ermy with dissolve
    p "Sorry, can't hear you!"
    show ermy1 pose2 1h 2c 3c blush at u11 as ermy with dissolve
    e "I... AM... READY!"
    show ermy1 pose1 1e 2b 3d blush at u11 as ermy with dissolve
    e "When talking to someone... Will you mention me as your friend?"
    show ermy1 pose1 1a 2a 3a noblush at u11 as ermy with dissolve
    p "Yep."
    show ermy1 pose2 1h 2d 3c at u11 as ermy with dissolve
    e "Very well! Then... I'm starting a new life tomorrow!"
    show ermy1 pose2 1a 2d 3c at u11 as ermy with dissolve
    p "Imagine you said it yesterday."
    show ermy1 pose1 1b 2a 3b at u11 as ermy with dissolve
    e "Haha!"
    scene black with fade
    "We finish our tea and cakes, split the bill and leave."
    scene mainmenu_sky
    play music "music/vaporwave.ogg" fadein 1.5 fadeout 2
    e "Hey, [player_name], I've never noticed it before, but the sky... the sky is so beautiful!"
    p "It is..."
    e "And the clouds, they're so fluffy!"
    e "Starting tomorrow... I mean, starting {i}now{/i}, I'll look at the sky every day."
    e "No, it's not enough! Every day {i}and night{/i}."
    e "I want to see the stars!"
    p "And I want you to reach for them."
    scene white with flash
    $ renpy.music.play("images/movies/click.mkv", channel="movie", loop=True)
    scene movie with flash
    e "The new era starts today, [player_name]."
    e "The new era!!!"
    stop music fadeout 2
    $ renpy.pause(2, hard=True)

    $achievement.grant("Weareallgonnamakeit")
    init:
        $achievement.register("Weareallgonnamakeit")
        $achievement.sync()
    $achievement.sync()

    return
label ermy_date_fail:
    show ermy1 pose2 1h 2d 3c blush at u11 as ermy with dissolve
    e "Yeah, I'm leaving."
    show ermy1 pose1 1e 2b 3a at u11 as ermy with dissolve
    e "When you invited me here, I really thought that..."
    show ermy1 pose1 1h 2d 3c at u11 as ermy with dissolve
    e "That you want to be my friend!"
    show ermy1 pose2 1f 2b 3a at u11 as ermy with dissolve
    e "..."
    show ermy1 pose1 1c 2b 3d at u11 as ermy with dissolve
    e "Sounds phony, right? But that's what I thought!"
    show ermy1 pose1 1h 2d 3c at u11 as ermy with dissolve
    e "Sorry to be a bother!"
    hide ermy with dissolve
    "He quickly leaves."
    jump failed_date
label failed_date:
    scene black with fade
    $ renpy.pause(2, hard=True)
    play music "music/vaporwave.ogg" fadein 1.5 fadeout 1.5
    scene mainmenu_sky with fade
    $ renpy.pause(2, hard=True)
    "I slowly walk down the street."
    "Where do I go? Well, it doesn't matter."
    "The sky... It's so beautiful today."
    "Why do I feel so bad?"
    "I mean... yeah, today wasn't the best day in my life, but still..."
    "I still have quite a lot of time on my hands."
    "Everything's going to be alright."
    "I keep staring at the sky, still feeling uneasy."
    "Well, whatever."
    "As for now... I'll just go home and relax."
    "But man, this sky! I need to take a picture."
    scene white with flash
    $ renpy.music.play("images/movies/click.mkv", channel="movie", loop=True)
    scene movie with flash
    "Click! Yep, goes right into my compilation."
    "Life is great. So nice to be young!"
    "I have so much time on my hands... A whole era!"
    "That's right, a whole era!"
    "Right?"
    stop music fadeout 2
    $ renpy.pause(2, hard=True)

    if game_restarted2 == 1:
        if persistent.game_done2 == True:
            if new_game2_sima_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                jump catgirl_extra10
            if new_game2_nana_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                jump catgirl_extra10
            if new_game2_marta_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                with flash
                jump catgirl_extra10

    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            if new_game1_sima_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                jump catgirl_extra10
            if new_game1_nana_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                jump catgirl_extra10
            if new_game1_marta_set == 1:
                scene mainmenu_sky
                stop movie
                scene mainmenu_sky with flash
                jump catgirl_extra10
    return
label date_end:
    scene black with fade
    stop music fadeout 2
    $ renpy.pause(2, hard=True)
    scene room_v1_night with fade
    play music "music/true_end_music.ogg"
    "My mind is all hazy..."
    if n_date_finished == 1:
        show cg_nana_5_1 as nana with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_nana_6_1 as nana with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_nana_9_1 as nana with dissolve
        $ renpy.pause(0.5, hard=True)
        hide nana with dissolve
        $ renpy.pause(1, hard=True)
    if s_date_finished == 1:
        show cg_sima_4_1 as sima with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_sima_6_1 as sima with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_sima_7_1_back
        show rain1 at arain1
        show rain2 at arain2
        show cg_sima_7_1
        show rain3 at arain3
        with dissolve
        $ renpy.pause(0.5, hard=True)
        hide sima
        hide cg_sima_7_1
        hide cg_sima_7_1_back
        hide rain1
        hide rain2
        hide rain3
        with dissolve
        $ renpy.pause(1, hard=True)
    if m_date_finished == 1:
        show cg_marta_4_1 as marta with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_marta_5_2 as marta with dissolve
        $ renpy.pause(0.5, hard=True)
        show cg_marta_6_b as marta with dissolve:
            zoom 1.4 ypos 1100
        $ renpy.pause(.5, hard=True)
        hide marta with dissolve
        $ renpy.pause(1, hard=True)
    "What just happened... Is this real life?"
    "I'm so excited..."
    "After we said good-bye to each other, I mindlessly roamed the streets..."
    "With a big, happy grin on my face."
    scene cg_photo with fade
    $ persistent.unlock_cg_photo = 1
    "{i}She{/i} gave me this picture before heading home."
    "The sky looks like as if she took it like an hour ago."
    "I'll cherish the memories from today."
    "Man, I'm so excited!"
    "I feel like a new chapter in my life is about to start."
    "A new beginning. A whole era!"
    "And this era... this era is going to be all mine!"
    $ renpy.pause(1, hard=True)
    stop music fadeout 2
    $ renpy.pause(3, hard=True)
    play sound "sound/chimes1.ogg"
    scene cg_room_v1_nighta with fade
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes2.ogg"
    scene cg_room_v1a with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes3.ogg"
    scene cg_room_v2 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes4.ogg"
    scene cg_room_v3 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes1.ogg"
    scene cg_room_v4 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes2.ogg"
    scene cg_room_v5 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes3.ogg"
    scene cg_room_v6 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes4.ogg"
    scene cg_room_v7 with dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(2.5, hard=True)
    play sound "sound/chimes1.ogg"
    scene black with fade
    $ renpy.pause(1.5, hard=True)
    stop sound fadeout 1
    $ renpy.pause(1.5, hard=True)

    $achievement.grant("Fullcircle")
    init:
        $achievement.register("Fullcircle")
        $achievement.sync()
    $achievement.sync()

    $ renpy.pause(2, hard=True)
    jump day5
return

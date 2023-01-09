label day5:
    play music "/music/ambient_black.ogg"
    scene arch_intro_p
    show teya2 1a 2a 3a fancyhand3 at d11 as teya
    with fade
    $ renpy.pause(1, hard=True)
    show teya2 1a 2a 3a fancyhand3 at u11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2 1c 2a 3a fancyhand3 at u11 as teya with dissolve
    t "Welcome back."
    show teya2 1b 2a 3b fancyhand2 at u11 as teya with dissolve
    t "You see, [player_name], they say that..."
    scene cg_teya_outtro_you_see with fade
    window hide
    $renpy.transition(dissolve)
    show screen scr_intro_you_see
    $ renpy.pause(4, hard=True)
    pause
    $renpy.transition(dissolve)
    hide screen scr_intro_you_see
    scene arch_intro_p
    show teya2 1b 2a 3a fancyhand1 at ui11 as teya
    with fade
    t "But you're not one of them, right?"
    show teya2 1e 2a 3d fancyhand4 at u11 as teya with dissolve
    t "It's about time you get an answer!"
    show teya2 1b 2a 3d fancyhand4 at u11 as teya with dissolve
    scene arch_empty
    show cg_the_end
    show teya2fullscale 1b 2a 3d fancyhand4 at ui11 as teya behind cg_the_end:
        xpos 1310
        yalign .2
    with fade
    $ renpy.pause(2, hard=True)
    show teya2fullscale 1e 2a 3d fancyhand4 at ui11 as teya behind cg_the_end with dissolve:
        xpos 1310
        yalign .2
    t "My, oh my..."
    show teya2fullscale 1c 2b 3a fancyhand4 at ui11 as teya behind cg_the_end with dissolve:
        xpos 1310
        yalign .2
    t "I'm afraid this doesn't look very promising."
    scene arch_intro_p
    show teya2 1d 2b 3b fancyhand3 at ui11 as teya
    with fade
    t "Well, what did I expect, a miracle?"
    show teya2 1e 2d 3a fancyhand4 at ui11 as teya with dissolve
    t "I've lost count of how many times it's ended like this."
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "Nothing but a meaningless, blank space."
    show teya3 1d 2b 3a fancy at u11 as teya with dissolve
    t "Maybe I should admit it... and let go."
    show teya1 1c 2d 3a fancy at u11 as teya with dissolve
    t "[player_name]! Say something at least."
    show teya1 1a 2a 3a fancy at u11 as teya with dissolve
    p "Where am I? What's going on?"
    show teya1 1c 2a 3d fancy at u11 as teya with dissolve
    t "Why, you've been here before, don't you remember?"
    show teya1 1a 2a 3a fancy at u11 as teya with dissolve
    show noise_outtro:
        alpha .3
    scene arch_outtro_t_m:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_b
    show marta3 1a 2c 3a regular1 blush at ui11 as marta
    with dissolve
    $ renpy.pause(1, hard=True)
    scene arch_outtro_m_s:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_o
    show sima2 1e 2a 3a regular1 at ui11 as sima
    with dissolve
    $ renpy.pause(1, hard=True)
    scene arch_outtro_s_n:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_g
    show nana3 1a 2a 3d at ui11 as nana
    with dissolve
    $ renpy.pause(1, hard=True)
    scene arch_outtro_n_t:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    hide noise_outtro
    scene arch_intro_p
    show teya1 1a 2a 3a fancy at ui11 as teya
    with dissolve
    $ renpy.pause(1, hard=True)
    show teya1 1c 2a 3a fancy at u11 as teya with dissolve
    t "So?"
    show teya1 1a 2a 3d fancy at u11 as teya with dissolve
    p "Oh yeah, I've visited this place in a dream..."
    p "And now I'm dreaming again, right?"
    show teya2 1b 2a 3a fancyhand4 at u11 as teya with dissolve
    t "I don't know. You tell me, [player_name]."
    show teya2 1e 2c 3a fancyhand2 at u11 as teya with dissolve
    t "If you say it's a dream, then wake up and message {i}her{/i}."
    show teya2 1b 2a 3d fancyhand1 at u11 as teya with dissolve
    t "You know who I'm talking about, don't you?"
    show teya2 1c 2a 3a fancyhand4 at u11 as teya with dissolve
    t "And if you say it's not a dream, you're welcome to stay here for a bit."
    show teya2 1a 2a 3a fancyhand4 at u11 as teya with dissolve
    menu:
        "I think it's a dream.":
            jump d5_itsadream
        "I think it's not a dream.":
            jump d5_itsnot
label d5_itsadream:
    show teya2 1e 2a 3b fancyhand2 at u11 as teya with dissolve
    t "So be it."
    show teya2 1e 2a 3a fancyhand3 at u11 as teya with dissolve
    t "See you on Monday, [player_name]!"
    show teya2 1b 2a 3a fancyhand3 at u11 as teya with dissolve
    t "Don't forget to do your homework!"
    scene black with fade
    stop movie
    play music "music/hero_room.ogg" fadein 1.5 fadeout 1.5
    $ renpy.pause(1, hard=True)
    scene cg_room_v1 with fade

    $achievement.grant("Wakeup")
    init:
        $achievement.register("Wakeup")
        $achievement.sync()
    $achievement.sync()

    "What a weird dream..."
    "Ah, Sunday morning! It feels so good."
    "I'm going to make myself a nice breakfast."
    "Should I message {i}her{/i} before that though?"
    "No. I need to be patient. It's better to give her some time."
    "I'm emotionally overwhelmed, I want to call her straight away!"
    "Don't rush it. Don't rush it!"
    "After all, I have plenty of time now. In fact, a whole new era."
    "A whole new era where I'm the one in charge!"
    return
label d5_itsnot:
    show teya2 1d 2c 3c fancyhand3 at u11 as teya with dissolve
    t "Oh my, I didn't expect that from you."
    show teya1 1e 2a 3b fancy at u11 as teya with dissolve
    t "Very well, [player_name], let's talk..."
    show teya1 1c 2a 3a fancy at u11 as teya with dissolve
    t "Is there anything you want to know?"
    show teya1 1a 2a 3a fancy at u11 as teya with dissolve
    p "Where am I? What's going on?"
    show teya2 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "You're in my home. Welcome! Be my guest, [player_name]."
    show teya2 1c 2a 3c fancyhand1 at u11 as teya with dissolve
    t "Now, you're probably thinking to yourself \"what's going on?\""
    show teya2 1b 2a 3b fancyhand2 at u11 as teya with dissolve
    t "It turns out the story of your life is actually empty."
    show teya2 1e 2a 3a fancyhand4 at u11 as teya with dissolve
    t "As promised, we made those four days very different."
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "We thought it would make your realize what you want to do with your life."
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "Math, arts, business... Well, you name it, you've seen it for yourself."
    show teya3 1d 2b 3a fancy at u11 as teya with dissolve
    t "Guess what? Nothing worked, as always."
    show teya1 1e 2a 3a fancy at u11 as teya with dissolve
    t "I made sure it's not a mistake, by the way."
    show teya1 1c 2a 3b fancy at u11 as teya with dissolve
    t "I've done a test run of your life, so to speak..."
    show teya2 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "I think you caught a glimpse of it in your room, several minutes ago."
    show cg_room_v1a as glimpse with fade
    $ renpy.pause(.001, hard=True)
    show cg_room_v2 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    show cg_room_v3 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    show cg_room_v4 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    show cg_room_v5 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    show cg_room_v6 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    show cg_room_v7 as glimpse with dissolve
    $ renpy.pause(.001, hard=True)
    hide glimpse
    show teya2 1c 2a 3a fancyhand4 at u11 as teya
    with fade
    t "It's interesting that the photo you had on your table..."
    show teya1 1c 2b 3b fancy at u11 as teya with dissolve
    t "It remained as the brightest memory you've ever had in your entire life."
    show teya1 1c 2b 3d fancy at u11 as teya with dissolve
    t "People often reminisce about the good old days, but..."
    show teya1 1e 2b 3a fancy at u11 as teya with dissolve
    t "Why is it always high school or university? Why not something else?"
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "I can only assume people usually plan and think big in life when they're young."
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "But life doesn't care much about living to their expectations."
    show teya2 1e 2a 3d fancyhand1 at u11 as teya with dissolve
    t "\"I tell you what, I wanted to be a jet pilot when I was a kid. But then...\""
    show teya2 1c 2a 3a fancyhand2 at u11 as teya with dissolve
    t "It's always about \"but then\", [player_name]. Oh well."
    show teya2 1e 2a 3a fancyhand3 at u11 as teya with dissolve
    t "By the way, I thought you'd be interested in knowing who I really am."
    show teya2 1a 2a 3a fancyhand3 at u11 as teya with dissolve
    p "I thought I knew it."
    show teya2 1e 2a 3d fancyhand1 at u11 as teya with dissolve
    t "Allow me to introduce myself properly, [player_name]..."
    show teya2 1b 2a 3a fancyhand3 at u11 as teya with dissolve
    $ t_name = "Adrasteia"
    t "My real name is Adrasteia, the distributor of rewards and punishments."
    show teya2 1e 2a 3b fancyhand1 at u11 as teya with dissolve
    t "I'm the one in charge here."
    show teya2 1b 2a 3a fancyhand4 at u11 as teya with dissolve
    p "Here? You said it's your home, right?"
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "I'm not the only one who lives here. It's the home of Moeera."
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "Oh, I misspelled it again. It's the home of Moerae."
    show teya2 1c 2a 3a fancyhand4 at u11 as teya with dissolve
    t "I'm looking after the Three Fates of Moerae."
    show teya2 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "The three sisters who decide the fate of every human."
    scene arch_outtro_t_clo:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_g
    show nana1 1b 2a 3a true at ui11 as nana
    $ renpy.pause(.5, hard=True)
    t "Meet Nana."
    if n_date_finished == 1:
        t "You got to know her quite well, I give you that."
    else:
        t "She wasn't the one you've spent the most of your time with..."
    show nana1 1a 2a 3d true at u11 as nana with dissolve
    t "Or should I call her Clotho the Spinner?"
    t "She said that name doesn't suit her at all."
    show nana1 1a 2a 3a true at u11 as nana with dissolve
    t "She also goes by the name of Nona. Nana is simply a cuter version of it."
    t "Clotho, or Nana, is responsible for spinning the thread of human life."
    t "By the way, sometimes we get bored with this and start writing on paper."
    t "That's what we've done with the story of your life."
    show nana1 1b 2a 3a true at u11 as nana with dissolve
    t "Like I've told you, all three sisters are responsible for your fate."
    t "However, Nana's the first one to assume who you're going to be in life."
    t "A farmer, a rock superstar, or both?"
    show nana1 1a 2b 3d true at u11 as nana with dissolve
    t "That's why Nana often looks bored. She can guess the ending from the start."
    t "Nana finds little joy in making forecasts."
    show nana1 1a 2d 3a true at u11 as nana with dissolve
    t "Moreover, her projections are often foggy or show nothing but emptiness."
    show nana1 1f 2b 3a true at u11 as nana with dissolve
    t "Nana suspects herself of doing a mediocre job."
    show nana1 1a 2a 3d true at u11 as nana with dissolve
    t "She says it's the reason why so many people live exactly that, a mediocre life."
    t "From another side, she's even more annoyed of people doing nothing to get better."
    t "That's why she calls them non-playable characters."
    show nana1 1b 2a 3a true at u11 as nana with dissolve
    t "She likes fun and cute things because it helps her to unwind."
    scene arch_outtro_clo_lac:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_o
    show sima2 1e 2a 3a true at ui11 as sima
    t "Enter Sima."
    if s_date_finished == 1:
        t "You got to know her quite well, I give you that."
    else:
        t "She wasn't the one you've spent the most of your time with..."
    t "Her real name is Lachesis the Alloter."
    t "She also goes by the name of Decima."
    t "Give it another go, and then you have Sima. Suits her better, don't you think?"
    show sima2 1a 2a 3d true at u11 as sima with dissolve
    t "She decides how much lifetime is to be allowed for each person."
    t "Having all the time in the world on her hands makes her the richest one..."
    t "Her observing nature is accompanied by calmness and patience."
    show sima2 1e 2a 3a true at u11 as sima with dissolve
    t "Sima enjoys small things as they tend to make a big difference."
    t "She's very delicate because she knows that one wrong step can ruin your life."
    t "When we're bored and use paper instead of threads, she's the one to write on it."
    t "As Sima watches over your whole life, she gets really attached over time."
    show sima2 1a 2b 3a true at u11 as sima with dissolve
    t "A human life is finite, so Sima always loses her friends in the end."
    t "Friends are temporary, loneliness is eternal for Sima."
    show sima2 1a 2b 3d true at u11 as sima with dissolve
    t "Maybe because of that she developed a somewhat cold, distant attitude."
    show sima2 1e 2a 3a true at u11 as sima with dissolve
    t "However, deep down she's a warm, caring soul."
    show arch_outtro_lac_ant:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_b
    show marta2 1g 2a 3a true at ui11 as marta
    t "Finally, here's Marta."
    if m_date_finished == 1:
        t "You got to know her quite well, I give you that."
    else:
        t "She wasn't the one you've spent the most of your time with..."
    t "I said \"finally\" on purpose."
    t "Her real name is Atropos the Inflexible."
    t "She's also known by the name of Morta."
    t "Morta... This name reminds you of death, right?"
    t "Marta thought the same, so one letter was changed."
    show marta2 1a 2a 3a true at u11 as marta with dissolve
    t "Now, death is actually her domain."
    t "She's the oldest one among the Three Fates."
    t "She cuts the thread of life... In your case, she'd just shred or tear that paper."
    show marta2 1g 2a 3d true at u11 as marta with dissolve
    t "She's very short-tempered and... that's right, inflexible."
    t "Marta's a really hard worker."
    t "She can't allow herself to relax as people die every day, every second."
    t "As Marta's mission is the grimmest, she can look rude from time to time."
    show marta2 1a 2b 3a true at u11 as marta with dissolve
    t "Few people love Marta because of her job, and those who do..."
    show marta2 1f 2b 3d true at u11 as marta with dissolve
    t "Well, those are people who want to die. Must be tough for Marta..."
    show marta2 1a 2a 3a true at u11 as marta with dissolve
    t "She has a fragile heart underneath her calloused exterior."
    t "Also, Marta often feels inferior, as she only excels in destruction."
    t "She feels like she lacks talent to do anything else."
    show arch_outtro_ant_t:
        linear .7 xpos -1920
    $ renpy.pause(.7, hard=True)
    scene arch_intro_p
    show teya2 1a 2a 3a fancyhand4 at ui11 as teya
    $ renpy.pause(.7, hard=True)
    show teya2 1e 2a 3a fancyhand2 at ui11 as teya with dissolve
    t "Well, that's pretty much it for the introductions, [player_name]."
    show teya2 1b 2a 3a fancyhand3 at u11 as teya with dissolve
    t "What do you think?"
    call day5_something_familiar from _call_day5_something_familiar
    $ c_name = "???"
    show catgirl as c:
        zoom  .95
        xalign .05
        ypos 300
    show teya2 1a 2c 3c fancyhand3 at u11 as teya
    with dissolve
    c "Hey!"
    show teya1 1a 2a 3d fancy at u11 as teya
    show catgirl2 as c:
        zoom  .95
        xalign -.15
        ypos 300
    with dissolve
    c "I too want to say hello."
    show teya1 1c 2a 3d fancy at u11 as teya with dissolve
    t "Oh, look who's here."
    $ c_name = "Tyche"
    show teya1 1e 2a 3a fancy at u11 as teya with dissolve
    t "How are you doing, Tyche?"
    show teya1 1a 2a 3a fancy at u11 as teya
    show catgirl3 as c:
        zoom  .95
        xalign -.15
        ypos 300
    with dissolve
    c "Great as always!"
    show teya1 1c 2a 3a fancy at u11 as teya with dissolve
    t "I believe you two have already met, [player_name]."
    show teya1 1d 2a 3a fancy at u11 as teya
    show catgirl2 as c:
        zoom  .95
        xalign -.15
        ypos 300
    with dissolve
    c "Yep! He was lucky enough to witness me."
    show teya3 1d 2a 3a fancy at u11 as teya with dissolve
    t "Luck is all you enjoy talking about, don't you?"
    show teya2 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "Tyche represents chance, fate and fortune."
    show teya2 1a 2a 3a fancyhand3 at u11 as teya
    show catgirl as c:
        zoom  .95
        xalign .05
        ypos 300
    with dissolve
    c "Chaos, to put it short!"
    hide c
    show teya2 1a 2a 3a fancyhand4 at u11 as teya
    with dissolve
    p "All what you said before about the story of my life..."
    p "So what? What's the big deal?"
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "Well, it's a long story..."
    show teya2 1b 2a 3a fancyhand2 at u11 as teya with dissolve
    t "On the one hand, I'm on good terms with time."
    show teya2 1e 2a 3a fancyhand4 at u11 as teya with dissolve
    t "[player_name], do you know which way this world, this planet goes?"
    show teya2 1b 2a 3a fancyhand4 at u11 as teya with dissolve
    p "Last I heard, it goes round."
    show teya2 1c 2a 3b fancyhand1 at u11 as teya with dissolve
    t "Close enough."
    play music "/music/ambient_white.ogg" fadein 1.5 fadeout 1.5
    scene b0
    $ persistent.unlock_cg_teya = 1
    show b1 at star_rotation0:
        alpha 1
        linear 2 alpha 0.4
        linear 1 alpha 1
        repeat
    show b2 at star_rotation1:
        alpha 1
        linear 4 alpha 0.4
        linear 2 alpha 1
        repeat
    show b3
    show b4:
        alpha 1
        linear 4 alpha 0.1
        linear 2 alpha 1
        repeat
    show b5 at clock_hands0:
        alpha 1
        linear 4 alpha 0.1
        linear 2 alpha 1
        repeat
    show b6 at clock_hands1:
        alpha 1
        linear 4 alpha 0.1
        linear 2 alpha 1
        repeat
    show b8_2:
        rotate 0.001
        yalign 0.5 xalign 0.5
        linear 6 yalign 0.6
        linear 6 yalign 0.5
        repeat
    show b8 at balls0:
        rotate 0.001
        yalign 0.5 xalign 0.5
        linear 6 yalign 0.6
        linear 6 yalign 0.5
        repeat
    show b9_2:
        rotate 0.001
        yalign 0.6 xalign 0.5
        linear 6 yalign 0.5
        linear 6 yalign 0.6
        repeat
    show b9 at balls1:
        rotate 0.001
        yalign 0.6 xalign 0.5
        linear 6 yalign 0.5
        linear 6 yalign 0.6
        repeat
    show teya_cg
    show br_n as br
    show m_c as m
    $ renpy.pause(2, hard=True)
    show m_o as m with dissolve
    t "It goes round and round... and down."
    t "We're going through a downward spiral, [player_name]."
    show br_f as br with dissolve
    t "It's neither good or bad, it's a natural cycle."
    t "What has a beginning, has an end. Rinse and repeat."
    t "Sadly, the end of the cycle always tends to be quite vicious."
    show br_n as br
    show m_c as m
    with dissolve
    t "Let me give you a few examples..."
    show br_e as br
    show m_o as m
    with dissolve
    t "Dark Ages, the Great Plague, the Renaissance."
    t "The Great Depression, World War II, the postwar economic boom."
    show br_n as br with dissolve
    t "These are the cycles or the Ages of Man I'm talking about."
    t "Almost every mythology or religion has something about it."
    show br_f as br with dissolve
    t "Say, a journey from the Golden to the Iron age in Greek mythology."
    t "Peace and harmony prevailed during the Golden Age."
    t "Good and noble, people were said to live among gods."
    show br_e as br with dissolve
    t "In the Iron Age, though, humans live an existence of toil and misery."
    show m_c as m with dissolve
    t "Children dishonor their parents..."
    show m_o as m with dissolve
    t "Brother fights with brother, might makes right..."
    show br_e as br with dissolve
    t "Does it ring any bells, [player_name]?"
    call day5_after_spiral from _call_day5_after_spiral
    show br_f as br with dissolve
    t "Maybe we're getting close to the end of yet another cycle right now."
    show br_n as br with dissolve
    t "That's what we're trying to understand."
    show m_c as m with dissolve
    t "You can call it a laughable theory, but truth to be told..."
    show m_o as m with dissolve
    t "Making something laughable stops people from believing in it."
    show br_f as br with dissolve
    t "Moreover, if you're a believer, it makes them laugh at {i}you{/i}."
    show br_e as br with dissolve
    t "No one likes to be a clown, so you're likely to change your mind."
    t "Do alternate sources of energy exist?"
    show br_n as br
    show m_c as m
    with dissolve
    t "What a joke, right?"
    show m_o as m with dissolve
    t "By the way, if it was true, the oil market would be no more. Funny coincidence."
    t "Just saying, you know."
    show br_f as br with dissolve
    t "Oh, and closer to the end of every cycle..."
    show br_e as br with dissolve
    t "It seems that more and more lives became meaningless and empty."
    show br_n as br with dissolve
    t "We decided to see if we can fix it, so we observed quite a lot of people."
    t "Sadly, we failed each time, and you're no exception."
    show m_c as m with dissolve
    menu:
        "Keep listening.":
            jump keep_listening
        "Argue that it was impossible to change anything in just four days.":
            jump ask_question
label keep_listening:
    show m_o as m with dissolve
    t "Now, people usually ask me..."
    show br_f as br with dissolve
    t "How do I define a meaningful life?"
    show br_e as br with dissolve
    t "In fact, everything you do has and hasn't any meaning at the same time."
    show br_f as br with dissolve
    t "Objectively speaking, a carpenter serves more purpose than a philosopher..."
    t "Because a carpenter creates tangible things."
    show br_n as br with dissolve
    t "But even that is debatable."
    t "I tend to think everything's fine as long as it abides by the most basic values."
    show m_c as m with dissolve
    p "Basic values?"
    show m_o as m with dissolve
    t "The fundamentals. Look, you probably know them yourself."
    t "Some people also call it \"common sense\"."
    show br_e as br
    show m_c as m
    with dissolve
    p "And you think life's getting worse with every generation?"
    show m_o as m with dissolve
    t "I'm afraid so."
    show m_c as m with dissolve
    p "C'mon... nowadays, people know like a hundred times more than they used to."
    show br_f as br
    show m_o as m
    with dissolve
    t "Don't mistake accumulated information with a high plane of intelligence."
    show m_c as m with dissolve
    p "What do you mean?"
    show m_o as m with dissolve
    t "Let's take spoken language as an example."
    t "Have you ever tried watching old news reports, live footages and so on?"
    show br_n as br with dissolve
    t "Give it a try! You'll be amazed by richness of vocabulary and clarity of speech."
    show m_c as m with dissolve
    p "What else do you expect from news anchors?"
    show m_o as m with dissolve
    t "Fair enough, let's take an average Joe from the crowd..."
    show br_e as br with dissolve
    t "He'd still handle the conversation at the level of a modern college graduate."
    t "Let's move on to logical fallacies..."
    show br_n as br with dissolve
    t "Before, your opinion on something more often than not had to be supported by solid proof."
    t "Otherwise, no one would even bother to listen."
    show br_f as br with dissolve
    t "Today, you can always go with \"just because\", and it's good enough."
    t "It's your right to express an opinion."
    show br_n as br
    show m_c as m
    with dissolve
    p "Maybe that's how the evolution works."
    show m_o as m with dissolve
    t "Just dropping the difficulty level? Pretty interesting concept, I should say."
    show m_c as m with dissolve
    p "The difficulty of life, you mean?"
    show m_o as m with dissolve
    t "Yes."
    show m_c as m with dissolve
    p "Anyway, even if not for the people..."
    show br_f as br with dissolve
    p "The world today is great because of the freedom."
    p "We have everything, we can do anything..."
    show br_n as br
    show m_o as m
    with dissolve
    t "I think that people handle the scarcity well, but abundance is the killer."
    show m_c as m with dissolve
    p "I don't get it."
    show m_o as m with dissolve
    t "Say, the Internet! The Holy Grail of our generation."
    show br_f as br with dissolve
    t "Freedom of information, communication, you name it..."
    show m_c as m with dissolve
    p "Let me guess, you want to say it's used as a source of mindless fun instead."
    show m_o as m with dissolve
    t "I won't, as there's nothing wrong with having a little fun."
    show br_e as br with dissolve
    t "No, the Internet did something much worse..."
    t "It set a wrong benchmark for life quality."
    show m_c as m with dissolve
    p "What?"
    show m_o as m with dissolve
    t "Imagine living in a small town... you don't have much yet you're happy."
    show br_n as br with dissolve
    t "Now, you go on the Internet and see other people living differently."
    t "It makes you feel uneasy. What are you, a loser? Are you wasting your life?"
    show m_c as m with dissolve
    p "But even a small-town girl wants to be a princess, a boy, well, a king..."
    show m_o as m with dissolve
    t "True, but the Internet made everyone think they're deserving applicants."
    show br_e as br with dissolve
    t "You see the disparity the same moment you turn on your phone."
    t "By the way, it will only get worse over time, now that I think about it."
    show m_c as m with dissolve
    p "Why?"
    show m_o as m with dissolve
    t "Because of the automation. A lot of jobs you see right now won't be needed."
    show br_n as br with dissolve
    t "Meaning even higher disparity in the near future."
    t "Oh, and don't forget the instant gratification."
    show br_f as br with dissolve
    t "No one wants to wait for the crops to grow nowadays."
    show m_c as m with dissolve
    p "Maybe you simply have a conservative, outdated view on the world, Teya."
    show m_o as m with dissolve
    t "Maybe so."
    t "Now, as for the freedom of speech..."
    show br_n as br
    show m_c as m
    with dissolve
    p "I can say pretty much anything as long as it's not offensive."
    show m_o as m with dissolve
    t "That's why you have nothing but \"hello\" and \"bye\"..."
    show br_f as br with dissolve
    t "Maybe we have less freedom compared to when no one cared about it."
    show m_c as m with dissolve
    p "It's hard to believe in what you say..."
    show m_o as m with dissolve
    t "I never said I want you to believe me."
    show br_n as br with dissolve
    t "Tell me just one thing..."
    t "Have you ever thought that something's really {i}off{/i} about this world?"
    p "..."
    jump ask_question
label ask_question:
    p "Well then, please tell me..."
    p "How on earth was I supposed to change anything in just four days?"
    p "That's right, only four days. It's nothing!"
    show m_o as m with dissolve
    t "If I gave you two weeks, what would be different?"
    show br_f as br with dissolve
    t "Based on my experience, a life can be condensed in a few days just fine."
    p "C'mon, I need at least a year."
    scene black with fade
    play music "/music/ambient_black.ogg" fadein 1.5 fadeout 1.5
    $ renpy.music.play("images/movies/tea.webm", channel="movie", loop=True)
    scene movie
    show teya1 1a 2a 3a fancy at u11 as teya
    with fade
    show teya1 1c 2c 3a fancy at u11 as teya with dissolve
    t "Wait a second... do you want to say that..."
    show teya2 1c 2a 3a fancyhand1 at u11 as teya with dissolve
    t "If I gave you a year, you would try to fill the story of your life?"
    show teya2 1e 2c 3a fancyhand1 at u11 as teya with dissolve
    t "You would work on improving your life every day for a {i}whole year{/i}?"
    show teya2 1e 2c 3c fancyhand1 blush at u11 as teya with dissolve
    t "Do you really mean it?"
    menu:
        "No, I don't.":
            jump just_an_example
        "Yes, I do.":
            jump not_an_example
label just_an_example:
    show teya1 1d 2b 3d fancy noblush at u11 as teya with dissolve
    t "..."
    show teya1 1e 2b 3b fancy at u11 as teya with dissolve
    t "Maybe you're right. Maybe what I say makes no sense, after all."
    show teya2 1e 2a 3a fancyhand3 at u11 as teya with dissolve
    t "You know what? Forget everything you heard here and wake up now."
    show teya2 1b 2a 3a fancyhand2 at u11 as teya with dissolve
    t "Have fun, [player_name]! Life is often simpler than we tend to think."
    jump d5_itsadream
label not_an_example:
    show teya3 1d 2c 3c fancy at u11 as teya with dissolve
    t "Wow..."
    show teya3 1b 2a 3b fancy noblush at u11 as teya with dissolve
    t "Believe it or not, you're actually the first one to say \"Yes\"!"
    show teya2 1e 2a 3a fancyhand1 at u11 as teya with dissolve
    t "A year, huh? Alright, deal."
    show teya2 1c 2a 3a fancyhand4 at u11 as teya with dissolve
    t "What're you going to do, by the way?"
    show teya2 1a 2a 3a fancyhand4 at u11 as teya with dissolve
    p "Well..."
    show teya2 1e 2c 3b fancyhand2 at u11 as teya with dissolve
    t "Look, I have an idea. Let the Moerae help you!"
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "Let's treat your next year as a small life, as a full cycle."
    show teya3 1d 2a 3b fancy at u11 as teya with dissolve
    t "Nana will give her advice on where to start."
    show teya2 1b 2a 3d fancyhand2 at u11 as teya with dissolve
    t "Sima knows better than everyone how to keep going..."
    show teya2 1e 2a 3a fancyhand1 at u11 as teya with dissolve
    t "And Marta's knowledgeable about the end."
    show teya2 1e 2a 3b fancyhand2 at u11 as teya with dissolve
    t "That kind of advice is personal, so you need to know the girls better."
    show teya2 1d 2a 3b fancyhand4 at u11 as teya with dissolve
    t "Good news is you've already learned quite a bit about one of them."
    show teya1 1c 2a 3a fancy at u11 as teya with dissolve
    t "Now, I can't really rewind your life, but..."
    show teya1 1c 2a 3b fancy at u11 as teya with dissolve
    t "I think Tyche has some tricks up her sleeve."
    show teya1 1b 2a 3a fancy at d22 as teya
    show catgirl as c:
        zoom  .95
        xalign .05
        ypos 300
    c "Leave it to me!"
    show catgirl2 as c with dissolve:
        zoom  .95
        xalign -.15
        ypos 300
    c "As soon as we finish things here, you'll be able to start all over again."
    show catgirl3 as c with dissolve:
        zoom  .95
        xalign -.15
        ypos 300
    c "Worry not, I won't make you go through the whole four days... It's going to be a breeze!"
    hide c with dissolve
    show teya2 1e 2c 3c blush fancyhand2 at u11 as teya
    t "Let's try it, [player_name]!"
    show teya2 1b 2c 3a blush fancyhand1 at u11 as teya with dissolve
    t "But first.. let me call {i}her{/i}!"   #fixed in None
    if m_date_finished == 1:
        scene black with fade
        stop movie
        jump wb1m
    if n_date_finished == 1:
        scene black with fade
        stop movie
        jump wb1n
    if s_date_finished == 1:
        scene black with fade
        stop movie
        jump wb1s
label wb1:
    play music "/music/ambient_white.ogg"  fadein 1.5 fadeout 1.5
    scene arch_intro_p
    show teya2 1a 2a 3a noblush fancyhand3 at u11 as teya
    with fade
    show teya2 1e 2a 3a noblush fancyhand3 at u11 as teya with dissolve
    t "Welcome back!"
    show teya2 1e 2a 3d fancyhand1 blush at u11 as teya with dissolve
    t "Now you got to know another one of the Moerae..."
    show teya2 1b 2a 3c fancyhand2 at u11 as teya with dissolve
    t "Let me call her right away!"
    if new_game1_nana_done == 1:
        jump wb1n
    if new_game1_marta_done == 1:
        jump wb1m
    if new_game1_sima_done == 1:
        jump wb1s
label wb2:
    play music "/music/ambient_white.ogg"  fadein 1.5 fadeout 1.5
    scene arch_intro_p
    show teya2 1a 2a 3a noblush fancyhand3 at u11 as teya
    with fade
    show teya2 1e 2a 3a noblush fancyhand3 at u11 as teya with dissolve
    t "Welcome back!"
    show teya2 1e 2c 3c blush fancyhand1 at u11 as teya with dissolve
    t "Congratulations, you made it!"
    show teya2 1b 2a 3c noblush fancyhand2 at u11 as teya with dissolve
    t "Let me call the last one of the Moerae..."

    if new_game2_nana_done == 1:
        jump wb1n
    if new_game2_marta_done == 1:
        jump wb1m
    if new_game2_sima_done == 1:
        jump wb1s
label wb1n:
    play music "music/personavibe.ogg" fadein 1.5 fadeout 1.5
    scene cafe_kawa
    show nana1close 1b 2a 3b true at u11 as nana
    with fade
    n "Heyyyy, [player_name]! I'm glad to see you!"
    show nana1close 1d 2a 3b blush true at u11 as nana with dissolve
    n "You've learned about my true identity, right?"
    show nana1close 1b 2a 3a true at u11 as nana with dissolve
    n "Well, what can I say... Being Nana is much more fun!"
    show nana1close 1c 2b 3a true at u11 as nana with dissolve
    n "Maybe Nana is the real me, after all!"
    show nana1close 1a 2a 3a true at u11 as nana with dissolve
    p "At least you're acting the same..."
    show nana1close 1b 2a 3b fancy1 at u11 as nana with dissolve
    n "Yep!"
    show nana1close 1e 2a 3a fancy2 at u11 as nana with dissolve
    n "Why did you decide to stay here, [player_name]?"
    show nana1close 1d 2a 3a fancy2 at u11 as nana with dissolve
    n "Anyway, I think you've made the right choice, [player_name]."
    show nana3close 1c 2a 3d fancy at u11 as nana with dissolve
    n "Oh, and..."
    show nana3close 1d 2a 3b blush fancy at u11 as nana with dissolve
    n "Thanks for yesterday. It was... very special for me."
    show nana3close 1b 2a 3a noblush fancy at u11 as nana with dissolve
    p "I would invite you again any time, Nona."
    show nana1close 1e 2c 3c fancy2 at u11 as nana with dissolve
    n "Call me by that name one more time and I won't help you at all!"
    show nana1close 1f 2d 3c fancy2 at u11 as nana with dissolve
    p "Alright, alright."
    show nana3close 1d 2a 3d noblush fancy at u11 as nana with dissolve
    n "So! You have a whole year ahead of you, but... where to start?"
    show nana3close 1b 2a 3b fancy at u11 as nana with dissolve
    n "What should you do?"
    show nana3close 1g 2a 3d fancy at u11 as nana with dissolve
    p "Tell me."
    show nana3close 1b 2a 3b fancy at u11 as nana with dissolve
    n "The thing is... it doesn't matter!"
    show nana3close 1g 2a 3d fancy at u11 as nana with dissolve
    p "Now, that's a useful one!"
    show nana1close 1d 2a 3a fancy2 at u11 as nana with dissolve
    n "Bonus points for sarcasm, but I mean it."
    show nana1close 1c 2a 3d fancy2 at u11 as nana with dissolve
    n "[player_name], do whatever you want, but..."
    show nana3close 1d 2d 3d fancy at u11 as nana with dissolve
    n "But only if it's impossible for you NOT to do it."
    show nana3close 1a 2a 3a fancy at u11 as nana with dissolve
    p "I'm confused..."
    show nana3close 1e 2c 3d fancy at u11 as nana with dissolve
    n "Well, would you like to be a writer?"
    show nana3close 1g 2c 3d fancy at u11 as nana with dissolve
    p "That doesn't sound too bad."
    show nana3close 1b 2a 3d fancy at u11 as nana with dissolve
    n "But if you were to pick just one thing to do every day, would it be writing?"
    show nana3close 1a 2a 3a fancy at u11 as nana with dissolve
    p "I don't think so."
    show nana1close 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "Then never write."
    show nana1close 1a 2a 3a fancy2 at u11 as nana with dissolve
    p "I can't live without eating."
    show nana1close 1b 2a 3b fancy2 at u11 as nana with dissolve
    p "Does it mean I should do nothing else starting tomorrow?"
    show nana3close 1e 2c 3a fancy at u11 as nana with dissolve
    n "Do you only think about eating the whole day?"
    show nana3close 1c 2a 3d fancy at u11 as nana with dissolve
    n "Is what you eat extremely important to you?"
    show nana3close 1g 2c 3a fancy at u11 as nana with dissolve
    p "Well, not really..."
    show nana1close 1e 2a 3a fancy2 at u11 as nana with dissolve
    n "Then eat to live, not live to eat."
    show nana1close 1d 2a 3d fancy2 at u11 as nana with dissolve
    n "Had you answered \"yes\", then I would've suggested you to become a cook."
    show nana1close 1e 2a 3b fancy2 at u11 as nana with dissolve
    n "Sorry, it's \"chef\" nowadays. I think you got my point."
    show nana1close 1a 2a 3a fancy2 at u11 as nana with dissolve
    p "Yeah."
    show nana3close 1b 2a 3a fancy at u11 as nana with dissolve
    n "Good. Then why don't you do the following..."
    show nana1close 1d 2a 3a fancy1 at u11 as nana with dissolve
    n "Get yourself a piece of paper and a pen... no smartphones, go old school!"
    show nana1close 1b 2c 3a fancy1 at u11 as nana with dissolve
    n "Write down a list of things you {i}really{/i} can't live without."
    show nana1close 1e 2a 3d fancy2 at u11 as nana with dissolve
    n "Then narrow it down as much as you can."
    show nana1close 1d 2a 3b fancy1 at u11 as nana with dissolve
    n "It doesnt matter what's left in the end, just do it."
    show nana1close 1d 2d 3c fancy2 at u11 as nana with dissolve
    n "Oh, and don't fall into the \"socially acceptable\" trap."
    show nana1close 1a 2d 3a fancy2 at u11 as nana with dissolve
    p "What?"
    show nana3close 1e 2d 3d fancy at u11 as nana with dissolve
    n "Marking something off your list just because it's considered \"not cool\"."
    show nana3close 1a 2a 3d fancy at u11 as nana with dissolve
    p "What if I realize I only like to do nothing?"
    show nana3close 1c 2a 3d fancy at u11 as nana with dissolve
    n "Those who say that usually delude themselves."
    show nana3close 1d 2a 3b fancy at u11 as nana with dissolve
    n "You think you enjoy something when you're deprived of it."
    show nana2close 1c 2a 3d fancy at u11 as nana with dissolve
    n "Do nothing for like half a year and you're guaranteed to go crazy."
    show nana3close 1d 2c 3a fancy at u11 as nana with dissolve
    n "Nowadays, you can make big money even by doing nothing on camera."
    show nana3close 1c 2c 3d fancy at u11 as nana with dissolve
    n "But guess what, it's still a lot of work behind the scenes."
    show nana1close 1e 2a 3b fancy1 at u11 as nana with dissolve
    n "Do your best! Trust me, it's going to be fun."
    show nana1close 1d 2a 3a fancy1 blush at u11 as nana with dissolve
    n "See you soon, [player_name]!"
    show nana1close 1g 2a 3a fancy2 blush at u11 as nana with dissolve
    $ renpy.pause(1, hard=True)
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene b0
    show nana1close 1g 2a 3a true blush at u11 as nana
    with fade
    $ renpy.pause(.3, hard=True)
    show nana1close 1d 2a 3a true blush at u11 as nana with dissolve
    n "I'll be there."
    show nana1close 1d 2a 3a true blush at ui11 as nana with dissolve:
        zoom 1.2
        ypos 1600
    n "I'll be there."
    show nana1date 1d 2a 3a true blush at ui11 as nana with dissolve
    n "I'll be there."
    show nana1date 1g 2a 3d true blush at ui11 as nana with dissolve
    $ renpy.pause(1, hard=True)

    if persistent.game_done3 == True:
        jump gb

    if persistent.game_done2 == True:
        if game_restarted2 == 1:
            jump gb
    if persistent.game_done1 == True:
        if game_restarted1 == 1:
            $ persistent.girl2_done = "N"
            $ persistent.game_done2 = True
            jump credits2
        else:
            $ persistent.girl1_done = "N"
            $ persistent.game_done1 = True
            jump credits1
    if persistent.game_done1 == None:
        $ persistent.girl1_done = "N"
        $ persistent.game_done1 = True
        jump credits1
label wb1s:
    play music "music/personavibe.ogg" fadein 1.5 fadeout 1.5
    scene cafe_kawa
    show sima2close 1e 2a 3a true at u11 as sima
    with fade
    s "How are you today, [player_name]?"
    show sima2close 1d 2a 3a true at u11 as sima with dissolve
    s "It must've been rough for you..."
    show sima2close 1e 2a 3d true at u11 as sima with dissolve
    s "By the way, thanks for yesterday. I enjoyed it!"
    show sima2close 1c 2b 3d true at u11 as sima with dissolve
    s "My, the clothes were so much more comfortable..."
    show sima2close 1a 2c 3a true at u11 as sima with dissolve
    p "And revealing."
    show sima2close 1c 2b 3d true at u11 as sima with dissolve
    s "Oh you... Did you like it?"
    show sima2close 1g 2a 3a true at u11 as sima with dissolve
    p "Yes!"
    show sima3bclose 1d 2a 3b fancy at u11 as sima with dissolve
    s "Here we go."
    show sima2close 1e 2a 3a fancy2 at u11 as sima with dissolve
    s "The beginning and the end..."
    show sima2close 1d 2a 3d fancy1 at u11 as sima with dissolve
    s "I'm going to tell you about something in between!"
    show sima2close 1c 2c 3d fancy1 at u11 as sima with dissolve
    s "Something extremely important for your success..."
    show sima2close 1a 2a 3d fancy1 at u11 as sima with dissolve
    p "What is it?"
    show sima2close 1d 2c 3c fancy1 at u11 as sima with dissolve
    s "The key to your success is productivity."
    show sima2close 1c 2a 3a fancy1 at u11 as sima with dissolve
    s "Every time you wake up, write down two things you need to do today."
    show sima2close 1d 2a 3b fancy2 at u11 as sima with dissolve
    s "Everything else is strictly optional."
    show sima2close 1e 2a 3a fancy2 at u11 as sima with dissolve
    s "Don't even start to do something else until you're done with both."
    show sima2close 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "I see."
    show sima1close 1d 2a 3a fancy at u11 as sima with dissolve
    s "Another big issue we have today is the lack of concentration."
    show sima1close 1c 2a 3b fancy at u11 as sima with dissolve
    s "Do you know that feeling when you want to do something..."
    show sima1close 1c 2a 3a fancy at u11 as sima with dissolve
    s "But then you keep getting distracted?"
    show sima1close 1d 2d 3a fancy at u11 as sima with dissolve
    s "Sit down, set a timer and focus only on your key task for 45 minutes."
    show sima2close 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "Take a short break and start all over again."
    show sima2close 1d 2a 3b fancy1 at u11 as sima with dissolve
    s "By the end of the day you'll notice the difference."
    show sima2close 1c 2a 3a fancy2 at u11 as sima with dissolve
    s "A lot of people nowadays boast about their long working hours..."
    show sima2close 1e 2b 3d fancy2 at u11 as sima with dissolve
    s "In reality, they simply waste too much time."
    show sima2close 1d 2c 3c fancy1 at u11 as sima with dissolve
    s "How can you do it with the most precious asset in the world?"
    show sima1close 1d 2b 3b fancy at u11 as sima with dissolve
    s "Long work meetings, endless coffee chats, social media..."
    show sima1close 1d 2a 3a fancy at u11 as sima with dissolve
    s "Keep in mind you also have to sleep, so... treasure every second!"
    show sima1close 1a 2a 3a fancy at u11 as sima with dissolve
    p "But there's so many things to do!"
    show sima3aclose 1d 2a 3a fancy at u11 as sima with dissolve
    s "Not as much as you think, let me assure you. Try to do what I say!"
    show sima3aclose 1c 2b 3d fancy at u11 as sima with dissolve
    s "In return, you'll get rid of another annoying feeling..."
    show sima3aclose 1d 2b 3a fancy at u11 as sima with dissolve
    s "You know, when you worked a lot, yet nothing's really done."
    show sima3aclose 1a 2b 3a fancy at u11 as sima with dissolve
    p "I know what you're talking about..."
    show sima2close 1d 2c 3c fancy1 at u11 as sima with dissolve
    s "Oh, and everything is possible."
    show sima2close 1a 2a 3a fancy1 at u11 as sima with dissolve
    p "What does that have to do with anything?"
    show sima2close 1e 2a 3a fancy2 at u11 as sima with dissolve
    s "At the start, your goal might not seem feasible at all."
    show sima3aclose 1e 2a 3b fancy at u11 as sima with dissolve
    s "Just don't stop, keep going, and it'll work out... somehow."
    show sima3bclose 1e 2a 3b fancy at u11 as sima with dissolve
    s "Who dares wins, [player_name]."
    show sima3aclose 1d 2a 3a fancy at u11 as sima with dissolve
    s "Also, don't do everything from scratch. Reach out to people."
    show sima3aclose 1a 2a 3a fancy at u11 as sima with dissolve
    p "What?"
    show sima2close 1e 2a 3b fancy2 at u11 as sima with dissolve
    s "It's a common mistake to reinvent the wheel."
    show sima2close 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "Do you mean that I should ask for help?"
    show sima2close 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "Correct. Let professionals do their job."
    show sima2close 1a 2a 3a fancy1 at u11 as sima with dissolve
    p "They're too busy for someone like me... they won't even notice me."
    show sima2close 1e 2c 3d fancy1 at u11 as sima with dissolve
    s "That's exactly what everyone thinks."
    show sima2close 1d 2a 3d fancy1 at u11 as sima with dissolve
    s "Just send them a message, and you'll be surprised."
    show sima2close 1a 2a 3a fancy2 at u11 as sima with dissolve
    p "What if they don't answer?"
    show sima2close 1e 2a 3a fancy2 at u11 as sima with dissolve
    s "Even if nine out of ten don't answer you..."
    show sima3aclose 1e 2a 3a fancy at u11 as sima with dissolve
    s "That's enough when you've sent a hundred messages."
    show sima3aclose 1d 2a 3d fancy at u11 as sima with dissolve
    s "And please do your research.  Information is free nowadays."
    show sima2close 1d 2c 3a fancy1 at u11 as sima with dissolve
    s "In the ancient times, people had to spend a fortune to own a small library."
    show sima2close 1e 2c 3c fancy1 at u11 as sima with dissolve
    s "Winning has never been easier, [player_name]."
    show sima2close 1g 2a 3a fancy1 at u11 as sima with dissolve
    p "Thanks... I'll remember it."
    show sima3bclose 1e 2a 3b blush fancy at u11 as sima with dissolve
    s "I expect only the best from you!"
    show sima3bclose 1e 2a 3a blush fancy at u11 as sima with dissolve
    s "See you soon!"
    show sima3bclose 1g 2a 3a blush fancy at u11 as sima with dissolve
    $ renpy.pause(1, hard=True)
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene b0
    show sima2close 1g 2a 3a true at u11 as sima
    with fade
    $ renpy.pause(.3, hard=True)
    show sima2close 1e 2a 3a true at u11 as sima with dissolve
    s "I'll be there."
    show sima2close 1e 2a 3a true at ui11 as sima with dissolve:
        zoom 1.2
        ypos 1700
    s "I'll be there."
    show sima2date 1e 2a 3a true at ui11 as sima with dissolve
    s "I'll be there."
    show sima2date 1g 2a 3a true at ui11 as sima with dissolve
    $ renpy.pause(1, hard=True)

    if persistent.game_done3 == True:
        jump gb

    if persistent.game_done2 == True:
        if game_restarted2 == 1:
            jump gb
    if persistent.game_done1 == True:
        if game_restarted1 == 1:
            $ persistent.girl2_done = "S"
            $ persistent.game_done2 = True
            jump credits2
        else:
            $ persistent.girl1_done = "S"
            $ persistent.game_done1 = True
            jump credits1
    if persistent.game_done1 == None:
        $ persistent.girl1_done = "S"
        $ persistent.game_done1 = True
        jump credits1
label wb1m:
    play music "music/lo-firomantic.ogg" fadeout 1.5 fadein 1.5
    scene cafe_kawa
    show marta2close 1g 2a 3a true at u11 as marta
    with fade
    show marta2close 1e 2a 3a true at u11 as marta with dissolve
    m "Hello, [player_name]. It's great to see you here..."
    show marta2close 1d 2b 3a true blush at u11 as marta with dissolve
    m "Now that you know my true identity... are you disappointed?"
    show marta2close 1a 2a 3a true at u11 as marta with dissolve
    p "I'm not."
    show marta2close 1e 2d 3c true at u11 as marta with dissolve
    m "Are you trying to say you don't miss the old me at all? How could you..."
    show marta2close 1f 2d 3c true at u11 as marta with dissolve
    p "Wait, I..."
    show marta2close 1e 2a 3b true noblush at u11 as marta with dissolve
    m "Just kidding!"
    show marta2close 1e 2a 3a true at u11 as marta with dissolve
    m "Hey, I enjoyed my time yesterday!"
    show marta2close 1g 2c 3a blush true at u11 as marta with dissolve
    m "M-mainly because of your company, you know."
    show marta2close 1g 2a 3b true at u11 as marta with dissolve
    p "You looked great in that dress..."
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "This one?"
    show marta2close 1g 2a 3a fancy1 at u11 as marta with dissolve
    p "Yes!"
    show marta3close 1g 2b 3a blush fancy1 at u11 as marta with dissolve
    m "You... you really think I looked cute?"
    show marta3close 1a 2b 3a fancy1 at u11 as marta with dissolve
    p "\"Looked\"?"
    show marta2close 1c 2b 3a fancy1 at u11 as marta with dissolve
    m "T-then I'll stay like this if you want."
    show marta2close 1b 2d 3a fancy2 noblush at u11 as marta with dissolve
    m "But don't you forget I'm the one who deals with death!"
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Anyway, please treasure this year ahead of you."
    show marta3close 1g 2a 3b fancy1 at u11 as marta with dissolve
    m "I'm sure you'll start doing a lot of new things. However..."
    show marta2close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Starting something is less complicated than finishing it."
    show marta2close 1a 2a 3a fancy1 at u11 as marta with dissolve
    p "How come?"
    show marta1close 1e 2a 3b fancy at u11 as marta with dissolve
    m "Even the most interesting activity gets boring when you do it every day."
    show marta2close 1e 2d 3a fancy2 at u11 as marta with dissolve
    m "Routine is the killer, [player_name], and it takes 90 percent of your time."
    show marta2close 1a 2d 3a fancy1 at u11 as marta with dissolve
    p "Yeah, I always wanted to do something creative..."
    show marta2close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Even the most creating process is no exception to this rule."
    show marta2close 1b 2c 3a fancy2 at u11 as marta with dissolve
    m "How long does it take you to imagine something? A few seconds, I guess..."
    show marta1close 1d 2a 3b fancy at u11 as marta with dissolve
    m "But then you need hours to put your image on paper."
    show marta1close 1e 2d 3a fancy at u11 as marta with dissolve
    m "And years of practice to become good at it."
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Sounds tough, right? So tough that people break down when they realize it."
    show marta2close 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "At the same time, that's why mediocre products often rise to the top."
    show marta2close 1g 2a 3a fancy1 at u11 as marta with dissolve
    p "Because they're at least finished."
    show marta2close 1b 2c 3a fancy2 at u11 as marta with dissolve
    m "Everyone can generate ideas; few are able to implement them."
    show marta3close 1ee 2c 3b fancy2 at u11 as marta with dissolve
    m "Being an unappreciated genius is an excuse for the lack of perseverance."
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Have you ever heard about the 10,000-Hour rule?"
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "They say success in any field is simply a matter of practicing."
    show marta2close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Practicing for ten thousand hours, to be more precise."
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "Therefore, during this year... please work on your goal every day!"
    show marta2close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "You won't see any progress overnight, think long term."
    show marta3close 1d 2b 3a fancy1 at u11 as marta with dissolve
    m "And... I hate to say it, but..."
    show marta1close 1d 2b 3b fancy at u11 as marta with dissolve
    m "Sometimes, you have to admit you're still no good. That's how life works."
    show marta1close 1e 2a 3a fancy at u11 as marta with dissolve
    m "If that's the case, start something new and keep going on."
    show marta2close 1b 2a 3a fancy1 at u11 as marta with dissolve
    m "Even Michael Jordan missed a lot of clutch shots..."
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "Yet we remember him for the ones he made."
    show marta2close 1g 2a 3a fancy1 at u11 as marta with dissolve
    p "Thanks, I'll try my best!"
    show marta2close 1e 2d 3c fancy2 at u11 as marta with dissolve
    m "Don't you dare go disappointing me, you hear?"
    show marta2close 1b 2a 3a fancy1 blush at u11 as marta with dissolve
    m "Start right now, [player_name]!"
    show marta2close 1g 2a 3a fancy1 blush at u11 as marta with dissolve
    $ renpy.pause(1, hard=True)
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene b0
    show marta2close 1g 2a 3a true blush at u11 as marta
    with fade
    $ renpy.pause(.3, hard=True)
    show marta2close 1b 2a 3a true blush at u11 as marta with dissolve
    m "I'll be there."
    show marta2close 1b 2a 3a true blush at ui11 as marta with dissolve:
        zoom 1.2
        ypos 1700
    m "I'll be there."
    show marta2date 1b 2a 3a true blush at ui11 as marta with dissolve
    m "I'll be there."
    show marta2date 1g 2a 3a true blush at u11 as marta with dissolve
    $ renpy.pause(1, hard=True)

    if persistent.game_done3 == True:
        jump gb

    if persistent.game_done2 == True:
        if game_restarted2 == 1:
            jump gb
    if persistent.game_done1 == True:
        if game_restarted1 == 1:
            $ persistent.girl2_done = "M"
            $ persistent.game_done2 = True
            jump credits2
        else:
            $ persistent.girl1_done = "M"
            $ persistent.game_done1 = True
            jump credits1
    if persistent.game_done1 == None:
        $ persistent.girl1_done = "M"
        $ persistent.game_done1 = True
        jump credits1
label gb:
    play music "music/vaporwave.ogg" fadein 1.5 fadeout 1.5
    scene black with fade
    scene mainmenu_sky
    show marta2 1a 2a 3a true at d44 as marta
    show sima2 1e 2a 3a true at d43 as sima
    show nana1 1a 2a 3a true at d41 as nana
    show teya2 1a 2a 3a fancyhand3 at d42 as teya
    with fade
    $ renpy.pause(1, hard=True)
    show teya2 1a 2a 3a fancyhand3 at u42 as teya
    $ renpy.pause(0.001, hard=True)
    show teya2 1b 2a 3a fancyhand3 at u42 as teya with dissolve
    t "I'm afraid it's time to say good-bye for now, [player_name]..."
    show teya2 1e 2a 3a fancyhand2 at u42 as teya with dissolve
    t "Don't worry, it won't be long! We'll see each other in a year."
    show teya2 1b 2b 3d fancyhand1 at u42 as teya with dissolve
    t "Are you going to miss us?"
    show teya2 1e 2a 3a fancyhand3 at u42 as teya with dissolve
    t "Please, make it the best year of your life, okay?"
    show teya1 1e 2a 3a fancy at u42 as teya with dissolve
    t "After all, the future depends on you."
    show teya2 1e 2a 3a fancyhand2 at u42 as teya with dissolve
    t "Yes, you and you only."
    show teya2 1b 2a 3a fancyhand3 at u42 as teya with dissolve
    t "Girls, do you have something to say to [player_name]?"
    scene mainmenu_sky
    show nana1close 1a 2a 3a true at ui11 as nana
    with dissolve
    $ renpy.pause(.25, hard=True)
    show nana3close 1b 2a 3d fancy at u11 as nana with dissolve
    n "It's always Nana who starts everything, huh..."
    show nana3close 1e 2a 3a fancy at u11 as nana with dissolve
    n "My last bit of advice would be to have fun."
    show nana1close 1d 2a 3a fancy2 at u11 as nana with dissolve
    n "Not too original, but very important."
    show nana1close 1b 2a 3b fancy2 at u11 as nana with dissolve
    n "Regardless of what you're doing, try to find joy in it."
    show nana1close 1d 2c 3c fancy1 at u11 as nana with dissolve
    n "Oh, and reward yourself!"
    show nana1close 1b 2c 3b fancy1 at u11 as nana with dissolve
    n "If you're busy with a boring task, go buy yourself a cake when you're done."
    show nana3close 1d 2a 3d fancy at u11 as nana with dissolve
    n "Last but not least, everything is easier when done together with someone."
    show nana3close 1b 2a 3b fancy at u11 as nana with dissolve
    n "I'm sure you'll find another main character in your life, [player_name]."
    show nana1close 1e 2a 3a fancy1 blush at u11 as nana with dissolve
    n "Have fun!"
    show nana1close 1g 2a 3a fancy2 blush at u11 as nana with dissolve
    $ renpy.pause(.5, hard=True)
    hide nana with dissolve
    $ renpy.pause(1, hard=True)
    show sima2close 1a 2a 3a fancy1 at u11 as sima
    $ renpy.pause(.001, hard=True)
    show sima2close 1d 2a 3a fancy1 at u11 as sima with dissolve
    s "Value things while they last, [player_name]."
    show sima2close 1e 2a 3b fancy1 at u11 as sima with dissolve
    s "There's no yesterday and there's no tomorrow."
    show sima2close 1d 2c 3c fancy1 at u11 as sima with dissolve
    s "Live today."
    show sima2close 1e 2a 3a fancy2 at u11 as sima with dissolve
    s "Oh, and please... care about your parents!"
    show sima3aclose 1d 2a 3a fancy at u11 as sima with dissolve
    s "When was the last time you called them? Why don't you do it today?"
    show sima3aclose 1c 2b 3d fancy at u11 as sima with dissolve
    s "It doesn't matter what kind of a past you had. It's long gone."
    show sima2close 1e 2c 3b fancy1 at u11 as sima with dissolve
    s "Have mercy, [player_name]. Be stronger."
    show sima2close 1c 2a 3d fancy2 at u11 as sima with dissolve
    s "Don't believe me? You will, but it's going to be too late by that moment."
    show sima1close 1d 2a 3a fancy at u11 as sima with dissolve
    s "The moment you visit their grave for the first time, [player_name]."
    show sima3bclose 1e 2a 3a fancy at u11 as sima with dissolve
    s "So... Call your parents today, okay?"
    show sima2close 1d 2a 3a blush fancy1 at u11 as sima with dissolve
    s "Take care, [player_name]!"
    show sima2close 1g 2a 3a blush fancy1 at u11 as sima with dissolve
    $ renpy.pause(.25, hard=True)
    hide sima with dissolve
    $ renpy.pause(1, hard=True)
    show marta2close 1a 2a 3a fancy1 at u11 as marta
    $ renpy.pause(.001, hard=True)
    show marta2close 1d 2a 3a fancy1 at u11 as marta with dissolve
    m "I'm the last one of the three, of course."
    show marta2close 1b 2a 3a fancy2 at u11 as marta with dissolve
    m "Right, I know a perfect conclusion."
    show marta3close 1e 2a 3a fancy1 at u11 as marta with dissolve
    m "Life has its ups and downs, [player_name], but remember..."
    show marta3close 1g 2a 3b fancy1 at u11 as marta with dissolve
    m "\"This too shall pass.\""
    show marta2close 1g 2a 3a fancy1 at u11 as marta with dissolve
    m "The happiest moments are finite, but the same goes for the darkest times."
    show marta2close 1b 2d 3a fancy2 at u11 as marta with dissolve
    m "Always, always move on."
    show marta3close 1g 2a 3a fancy1 at u11 as marta with dissolve
    m "Oh, and please don't pay any mind to the Negative Nancies."
    show marta3close 1e 2a 3b fancy1 at u11 as marta with dissolve
    m "\"The boos usually come from the cheap seats\", [player_name]."
    show marta2close 1b 2d 3b blush fancy2 at u11 as marta with dissolve
    m "Until we meet again!"
    show marta2close 1g 2a 3a blush fancy1 at u11 as marta with dissolve
    $ renpy.pause(.25, hard=True)
    hide marta with dissolve
    $ renpy.pause(1, hard=True)
    show teya3close 1a 2a 3a fancy at u11 as teya
    $ renpy.pause(.001, hard=True)
    show teya3close 1d 2a 3a fancy at u11 as teya with dissolve
    t "I'm back! Did ya miss me?"
    show teya3close 1c 2a 3b fancy at u11 as teya with dissolve
    t "I think the girls pretty much covered everything I wanted to say."
    show teya1close 1c 2a 3a fancy at u11 as teya with dissolve
    t "One last thing..."
    show teya2close 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "Please don't mistaken this with a final farewell."
    show teya2close 1c 2a 3a fancyhand4 at u11 as teya with dissolve
    t "Don't want to spoil too much... Just stay tuned!"
    show teya1close 1e 2a 3a fancy at u11 as teya with dissolve
    t "So... that's it. How do you feel?"
    show teya1close 1b 2a 3a fancy at u11 as teya with dissolve
    p "I..."
    show teya2close 1e 2c 3a fancyhand2 at u11 as teya with dissolve
    t "Take your time to think about it."
    show teya2close 1b 2a 3b blush fancyhand1 at u11 as teya with dissolve
    t "After all, you have a whole era ahead of you!"
    $achievement.grant("Realhumanbeing")
    init:
        $achievement.register("Realhumanbeing")
        $achievement.sync()
    $achievement.sync()

    $ persistent.game_done1 = None
    $ persistent.game_done2 = None
    jump end_credits
label new_game_plus1:
    scene jp_classroom_day
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima1 1g 2a 3a at d32 as sima
    show marta3 1b 2a 3a regular1 at d31 as marta
    with fade
    play music "music/lo-firomantic.ogg" fadeout 1.5 fadein 1.5
    call after_meditation from _call_after_meditation_1
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene teya_ivanovna
    show teya2close 1a 2a 3a regularhand4 at d11 as teya
    with fade
    $ renpy.pause(1, hard=True)
    show teya2close 1a 2a 3a regularhand4 at u11 as teya
    $ renpy.pause(.001, hard=True)
    show teya2close 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "[player_name], time to make a choice!"
    show teya2close 1a 2a 3a regularhand4 at u11 as teya with dissolve
    jump catgirl_extra1
label catgirl_extra0:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Hey, you already made the same choice before!"
    c "You need to make another first pick."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump after_meditation
label catgirl_extra1:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Great, so here we are... It's the first day again."
    c "Each book is directly connected with one of the girls."
    c "I hope you've figured out that much..."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_book_choice
label catgirl_extra2a:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Congratulations, you failed."
    c "Game over."
    c "..."
    c "Meh."
    c "Alright, I'll give you one more try."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    jump newgame1_book_choice
label newgame1_book_choice:
    if persistent.girl1_done == "M":
        if persistent.girl2_done == "N":
            $ sima_plusset = True
        if persistent.girl2_done == "S":
            $ nana_plusset = True

    if persistent.girl1_done == "S":
        if persistent.girl2_done == "N":
            $ marta_plusset = True
        if persistent.girl2_done == "M":
            $ nana_plusset = True

    if persistent.girl1_done == "M":
        if persistent.girl2_done == "S":
            $ nana_plusset = True
        if persistent.girl2_done == "N":
            $ sima_plusset = True
    menu:
        "\"The Catcher in the Rye\"":
            if persistent.girl1_done == "M":
                jump catgirl_extra3
            if persistent.girl2_done == "M":
                jump catgirl_extra3
            else:
                if marta_plusset == True:
                    call catgirl_extra4 from _call_catgirl_extra4
                    play music "music/date_extended.ogg" fadeout 2 fadein 2
                    jump catcher
                else:
                    jump catgirl_extra2a
        "\"Crime and Punishment\"":
            if persistent.girl1_done == "S":
                jump catgirl_extra3
            if persistent.girl2_done == "S":
                jump catgirl_extra3
            else:
                if sima_plusset == True:
                    call catgirl_extra4 from _call_catgirl_extra4_1
                    play music "music/date_extended.ogg" fadeout 2 fadein 2
                    jump crime
                else:
                    jump catgirl_extra2a
        "\"Winnie-the-Pooh\"":
            if persistent.girl1_done == "N":
                jump catgirl_extra3
            if persistent.girl2_done == "N":
                jump catgirl_extra3
            else:
                if nana_plusset == True:
                    call catgirl_extra4 from _call_catgirl_extra4_2
                    play music "music/date_extended.ogg" fadeout 2 fadein 2
                    jump Winnie
                else:
                    jump catgirl_extra2a
        "I don't like any of these books.":
            jump catgirl_extra2
label catgirl_extra2:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Seriously? Are you kidding me?"
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_book_choice
label catgirl_extra3:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Hey, you already made the same choice before!"
    c "You need to make another first pick."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_book_choice
label catgirl_extra4:
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Great! Leave everything else on me."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    return
label catgirl_extra5:
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene ru_classroom_day
    show shade_bottom
    show teya2 1a 2a 3a regularhand4 behind shade_bottom at d11 as teya
    with fade
    $ renpy.pause(1, hard=True)
    show menu_dark behind c with dissolve
    play music "music/jazzy_school.ogg" fadein 1.5 fadeout 1.5
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Okay, the second day. I made it easier for you, it's the last choice you need to make."
    c "Honestly, I'd like to continue with the piano puzzle, but..."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_math_choice
label newgame1_math_choice:
    if persistent.girl1_done == "M":
        if persistent.girl2_done == "N":
            $ sima_plusset = True
        if persistent.girl2_done == "S":
            $ nana_plusset = True

    if persistent.girl1_done == "S":
        if persistent.girl2_done == "N":
            $ marta_plusset = True
        if persistent.girl2_done == "M":
            $ nana_plusset = True

    if persistent.girl1_done == "M":
        if persistent.girl2_done == "S":
            $ nana_plusset = True
        if persistent.girl2_done == "N":
            $ sima_plusset = True
    menu:
        "Math and beauty.":
            if persistent.girl1_done == "N":
                jump catgirl_extra7b
            if persistent.girl2_done == "N":
                jump catgirl_extra7b
            else:
                if nana_plusset == True:
                    call catgirl_extra6 from _call_catgirl_extra6
                    play music "music/math1_day2.ogg" fadein 1.5 fadeout 1.5
                    jump beauty
                else:
                    jump catgirl_extra8
        "Math and the future.":
            if persistent.girl1_done == "S":
                jump catgirl_extra7b
            if persistent.girl2_done == "S":
                jump catgirl_extra7b
            else:
                if sima_plusset == True:
                    call catgirl_extra6 from _call_catgirl_extra6_1
                    play music "music/math1_day2.ogg" fadein 1.5 fadeout 1.5
                    jump future
                else:
                    jump catgirl_extra8
        "Math and success.":
            if persistent.girl1_done == "M":
                jump catgirl_extra7b
            if persistent.girl2_done == "M":
                jump catgirl_extra7b
            else:
                if marta_plusset == True:
                    call catgirl_extra6 from _call_catgirl_extra6_2
                    play music "music/math1_day2.ogg" fadein 1.5 fadeout 1.5
                    jump success
                else:
                    jump catgirl_extra8
        "I don't like any of these topics.":
            jump catgirl_extra7
label catgirl_extra7:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "..."
    c "Seriously? Are you kidding me?"
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_math_choice
label catgirl_extra6:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Great, you made it! Enjoy..."
    c "You'll have something to look at, I guarantee it."
    c "See you soon!"
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    return
label catgirl_extra7a:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Hey, you already made the same choice before!"
    c "You need to make another first pick."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    return
label catgirl_extra7b:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Hey, you already made the same choice before!"
    c "You need to make another first pick."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    jump newgame1_math_choice
label catgirl_extra8:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Congratulations, you failed."
    c "Game over."
    c "..."
    c "Meh."
    c "Alright, I'll give you one more try."
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    jump newgame1_math_choice
label catgirl_extra9:
    scene jp_classroom_day
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima1 1g 2a 3a at d32 as sima
    show marta3 1b 2a 3a regular1 at d31 as marta
    with fade
    play music "music/lo-firomantic.ogg" fadeout 1.5 fadein 1.5
    call after_meditation from _call_after_meditation_2
    scene teya_ivanovna
    show teya2 1a 2a 3a regularhand4 at d11 as teya
    with fade
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "I wish you luck, [player_name]. See you again... maybe!"
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    $ renpy.pause(1, hard=True)

    if persistent.girl1_done == "S":
        if persistent.girl2_done == "M":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump Winnie

    if persistent.girl1_done == "M":
        if persistent.girl2_done == "S":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump Winnie

    if persistent.girl1_done == "M":
        if persistent.girl2_done == "N":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump crime

    if persistent.girl1_done == "N":
        if persistent.girl2_done == "M":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump crime

    if persistent.girl1_done == "S":
        if persistent.girl2_done == "N":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump catcher
    if persistent.girl1_done == "N":
        if persistent.girl2_done == "S":
            play music "music/personavibe.ogg" fadeout 1.5 fadein 1.5
            $ renpy.pause(1, hard=True)
            jump catcher

label catgirl_extra10:
    show menu_dark behind c with dissolve
    $ renpy.pause(.5, hard=True)
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -500
        linear .5 xpos -100
    c "Oh my, [player_name]!"
    c "You're like that one runner who slipped right before the finish line."
    c "Tough luck!"
    c "Okay, I'll give you another chance. This time, choose wiser!"
    show catgirl at u21 as c:
        rotate 37
        ypos 1350
        xpos -100
        linear .5 xpos -500
    hide menu_dark with dissolve
    $ renpy.pause(1, hard=True)
    if new_game1_sima_set == 1:
        $ new_game2_sima_set = 1
        jump date_sima
    if new_game1_nana_set == 1:
        $ new_game2_nana_set = 1
        jump date_nana
    if new_game1_marta_set == 1:
        $ new_game2_marta_set = 1
        jump date_marta
label credits1:
    $ persistent.player_name = player_name
    scene black with fade
    stop music fadeout 2
    $ renpy.pause(2, hard=True)
    $ renpy.music.set_volume(.3, 0, channel = "music")
    play music "<from 28.5>sound/SOSPetlya.ogg" noloop fadein 1
    $ renpy.music.play("images/movies/end_credits1.mkv", channel="movie", loop=False)
    scene movie with fade
    credits1 "Moe Era \n by Comfy Company{w=10}{nw}"
    credits1 "Concept and Game Design\n {font=SourceHanSerifSC-Bold.otf}Ｄｏｍｉｔｏｒｉ{/font}{w=10}{nw}"
    credits1 "Coding and Programming\n {font=SourceHanSerifSC-Bold.otf}fe{/font}{w=10}{nw}"
    credits1 "Writing \n {font=SourceHanSerifSC-Bold.otf}Ｄｏｍｉｔｏｒｉ{/font}{w=10}{nw}"
    credits1 "Character Art\n {font=SourceHanSerifSC-Bold.otf}Orika Nekoi{/font}{w=10}{nw}"
    credits1 "Background Art\n {font=SourceHanSerifSC-Bold.otf}Shumoi{/font}{w=10}{nw}"
    credits1 "Music\n {font=SourceHanSerifSC-Bold.otf}Pazetic Ocean{/font}{w=10}{nw}"
    credits2 "Also Contributed to the Game:\n {font=SourceHanSerifSC-Bold.otf}Maxim_N, Nathan Park\n AreksNyan, Lumpychan\n VelinquenT, Kees Nelis\n Surafin{/font}{w=10}{nw}"
    credits2 "Special Thanks to:\n {font=SourceHanSerifSC-Bold.otf}Steve T., Nata M.\n Daria K., monononoke\n Ayano R., Alex S.{/font}{w=10}{nw}"
    credits2 "Featured Music:\n {font=SourceHanSerifSC-Bold.otf}\"Петля\" by \"Свидетельство О Смерти\"\n Erik Satie: \"Gymnopedie No. 1\" by Prodigal Procrastinator\n Frederic Chopin: \"Op. 9, No. 1 in B flat minor. Larghetto\" by Olga Gurevich\n Robert Schumann: \"Des Abends\" - \"Fantasiestücke\" op.12 by Olga Jegunova-Klavier{/font}{w=10}{nw}"
    credits1 "Thank You for playing\n Moe Era!{w=10}{nw}"
    $ renpy.pause(6, hard=False)
    stop music fadeout 4
    $ renpy.pause(3, hard=False)
    scene black with fade
    stop movie
    $ renpy.pause(2, hard=False)
    $ renpy.music.set_volume(1, 0, channel = "music")
    return
label credits2:
    $ persistent.player_name = player_name
    return
label end_credits:
    scene black with fade
    $ renpy.pause(1, hard=False)
    scene cg_nana_4_2 with fade
    $ renpy.pause(4, hard=False)
    if winnie_v == 0:
        scene cg_nana_8_2 with dissolve
        $ renpy.pause(4, hard=False)
    if winnie_v == 1:
        scene cg_nana_8_1 with dissolve
        $ renpy.pause(4, hard=False)
    scene cg_sima_3_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_7_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_all_2_2 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_nana_7_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_sima_1_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_3_2 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_2_4 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_all_3all with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_barashek with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_1_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_sima_2_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_nana_5_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_nana_6_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_nana_9_6 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_sima_4_1 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_sima_6_2 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_sima_7_1all with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_4_2 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_5_3 with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_marta_6_1all with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_teya with dissolve
    $ renpy.pause(4, hard=False)
    scene cg_photo with dissolve
    credits1 "Thank You for playing\n Moe Era!{w=5}{nw}"
    stop music fadeout 5
    $ renpy.pause(5, hard=False)
    $ persistent.game_done3 = True
return

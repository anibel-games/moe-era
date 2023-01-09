label inactivity_check_d1:
    if inactivity_done_d1 == 1:
        return
    if inactivity == 1:
        $ inactivity = 0
        call imouto_d1 from _call_imouto_d1
    if inactivity == 0:
        hide screen inactivity_timer_d1
        show screen inactivity_timer_d1
    return

label inactivity_check_d2:
    if inactivity_done_d2 == 1:
        return
    if inactivity == 1:
        $ inactivity = 0
        call imouto_d2 from _call_imouto_d2
    if inactivity == 0:
        hide screen inactivity_timer_d2
        show screen inactivity_timer_d2
    return
label imouto_d1:
    hide screen inactivity_timer_d1
    $ d1_imoto_var = renpy.random.choice(d1_random_imouto_var)
    python:
        d1_random_imouto_var.remove(d1_imoto_var)
        if len(d1_random_imouto_var) == 0:
            d1_random_imouto_var.append(99)
    if d1_imoto_var == 1:
        call d1_random_imouto1 from _call_d1_random_imouto1
    if d1_imoto_var == 2:
        call d1_random_imouto2 from _call_d1_random_imouto2
    if d1_imoto_var == 3:
        call d1_random_imouto3 from _call_d1_random_imouto3
    if d1_imoto_var == 4:
        call d1_random_imouto4 from _call_d1_random_imouto4
    if d1_imoto_var == 5:
        call d1_random_imouto5 from _call_d1_random_imouto5
    if d1_imoto_var == 6:
        call d1_random_imouto6 from _call_d1_random_imouto6
    if d1_imoto_var == 7:
        call d1_random_imouto7 from _call_d1_random_imouto7
    if d1_imoto_var == 8:
        call d1_random_imouto8 from _call_d1_random_imouto8
    if d1_imoto_var == 9:
        call d1_random_imouto9 from _call_d1_random_imouto9
    if d1_imoto_var == 10:
        call d1_random_imouto10 from _call_d1_random_imouto10
    if d1_imoto_var == 11:
        call d1_random_imouto11 from _call_d1_random_imouto11
    if d1_imoto_var == 12:
        call d1_random_imouto12 from _call_d1_random_imouto12
    if d1_imoto_var == 13:
        call d1_random_imouto13 from _call_d1_random_imouto13
    if d1_imoto_var == 14:
        call d1_random_imouto14 from _call_d1_random_imouto14
    if d1_imoto_var == 15:
        call d1_random_imouto15 from _call_d1_random_imouto15
    if d1_imoto_var == 16:
        call d1_random_imouto16 from _call_d1_random_imouto16
    if d1_imoto_var == 17:
        call d1_random_imouto17 from _call_d1_random_imouto17
    if d1_imoto_var == 18:
        call d1_random_imouto18 from _call_d1_random_imouto18
    if d1_imoto_var == 19:
        call d1_random_imouto19 from _call_d1_random_imouto19
    if d1_imoto_var == 20:
        call d1_random_imouto20 from _call_d1_random_imouto20
    if d1_imoto_var == 21:
        call d1_random_imouto21 from _call_d1_random_imouto21
    if d1_imoto_var == 22:
        call d1_random_imouto22 from _call_d1_random_imouto22
    if d1_imoto_var == 23:
        call d1_random_imouto23 from _call_d1_random_imouto23
    if d1_imoto_var == 24:
        call d1_random_imouto24 from _call_d1_random_imouto24
    if d1_imoto_var == 25:
        call d1_random_imouto25 from _call_d1_random_imouto25
    if d1_imoto_var == 99:
        call d1_random_imouto_last from _call_d1_random_imouto_last
    show screen inactivity_timer_d1
    return

label d1_random_imouto1:
    show imouto with fade
    imo "Go back to studying."
    hide imouto with fade

    return
label d1_random_imouto2:
    show imouto with fade
    imo "Stop slacking."
    hide imouto with fade

    return
label d1_random_imouto3:
    show imouto with fade
    imo "Did you learn something new today?"
    hide imouto with fade

    return
label d1_random_imouto4:
    show imouto with fade
    imo "You should write something."
    hide imouto with fade

    return
label d1_random_imouto5:
    show imouto with fade
    imo "Hey, don't procrastinate, it's bad for your health."
    hide imouto with fade

    return
label d1_random_imouto6:
    show imouto with fade
    imo "Did you eat?"
    hide imouto with fade

    return
label d1_random_imouto7:
    show imouto with fade
    imo "Hey, I want an ice cream!"
    hide imouto with fade

    return
label d1_random_imouto8:
    show imouto with fade
    imo "Take me to the movies!"
    hide imouto with fade

    return
label d1_random_imouto9:
    show imouto with fade
    imo "The video games you have here are all boring."
    hide imouto with fade

    return
label d1_random_imouto10:
    show imouto with fade
    imo "Was there anything fun today?"
    hide imouto with fade

    return
label d1_random_imouto11:
    show imouto with fade
    imo "What will you have tomorrow?"
    hide imouto with fade

    return
label d1_random_imouto12:
    show imouto with fade
    imo "What are your plans for the weekend?"
    hide imouto with fade

    return
label d1_random_imouto13:
    show imouto with fade
    imo "I'm hungry."
    hide imouto with fade

    return
label d1_random_imouto14:
    show imouto with fade
    imo "I'm bored."
    hide imouto with fade

    return
label d1_random_imouto15:
    show imouto with fade
    imo "Are you doing your homework?"
    hide imouto with fade

    return
label d1_random_imouto16:
    show imouto with fade
    imo "Pay attention to your homework."
    hide imouto with fade

    return
label d1_random_imouto17:
    show imouto with fade
    imo "What are you thinking about?"
    hide imouto with fade

    return
label d1_random_imouto18:
    show imouto with fade
    imo "Did you find a girl you like?"
    hide imouto with fade

    return
label d1_random_imouto19:
    show imouto with fade
    imo "You should study hard to get a good job and buy me a lot of things."
    hide imouto with fade

    return
label d1_random_imouto20:
    show imouto with fade
    imo "Buy me a new game! I'm tired of this one."
    hide imouto with fade

    return
label d1_random_imouto21:
    show imouto with fade
    imo "Mom called and told me to keep an eye on you."
    hide imouto with fade

    return
label d1_random_imouto22:
    show imouto with fade
    imo "Did you buy anything for me?"
    hide imouto with fade

    return
label d1_random_imouto23:
    show imouto with fade
    imo "I'm thirsty."
    hide imouto with fade

    return
label d1_random_imouto24:
    show imouto with fade
    imo "I'm tired."
    hide imouto with fade

    return
label d1_random_imouto25:
    show imouto with fade
    imo "I don't want to fly back home."
    hide imouto with fade

    return
label d1_random_imouto_last:
    $ inactivity_done_d1 = 1
    show imouto with fade
    hide screen inactivity_timer_d1
    imo "Still doing nothing? Fine! I'm not talking to you anymore!"
    hide imouto with fade

    return

label imouto_d2:
    hide screen inactivity_timer_d2
    $ d2_imoto_var = renpy.random.choice(d2_random_imouto_var)
    python:
        d2_random_imouto_var.remove(d2_imoto_var)
        if len(d2_random_imouto_var) == 0:
            d2_random_imouto_var.append(99)
    if d2_imoto_var == 1:
        call d2_random_imouto1 from _call_d2_random_imouto1
    if d2_imoto_var == 2:
        call d2_random_imouto2 from _call_d2_random_imouto2
    if d2_imoto_var == 3:
        call d2_random_imouto3 from _call_d2_random_imouto3
    if d2_imoto_var == 4:
        call d2_random_imouto4 from _call_d2_random_imouto4
    if d2_imoto_var == 5:
        call d2_random_imouto5 from _call_d2_random_imouto5
    if d2_imoto_var == 6:
        call d2_random_imouto6 from _call_d2_random_imouto6
    if d2_imoto_var == 7:
        call d2_random_imouto7 from _call_d2_random_imouto7
    if d2_imoto_var == 8:
        call d2_random_imouto8 from _call_d2_random_imouto8
    if d2_imoto_var == 9:
        call d2_random_imouto9 from _call_d2_random_imouto9
    if d2_imoto_var == 10:
        call d2_random_imouto10 from _call_d2_random_imouto10
    if d2_imoto_var == 11:
        call d2_random_imouto11 from _call_d2_random_imouto11
    if d2_imoto_var == 12:
        call d2_random_imouto12 from _call_d2_random_imouto12
    if d2_imoto_var == 13:
        call d2_random_imouto13 from _call_d2_random_imouto13
    if d2_imoto_var == 14:
        call d2_random_imouto14 from _call_d2_random_imouto14
    if d2_imoto_var == 15:
        call d2_random_imouto15 from _call_d2_random_imouto15
    if d2_imoto_var == 16:
        call d2_random_imouto16 from _call_d2_random_imouto16
    if d2_imoto_var == 17:
        call d2_random_imouto17 from _call_d2_random_imouto17
    if d2_imoto_var == 18:
        call d2_random_imouto18 from _call_d2_random_imouto18
    if d2_imoto_var == 19:
        call d2_random_imouto19 from _call_d2_random_imouto19
    if d2_imoto_var == 20:
        call d2_random_imouto20 from _call_d2_random_imouto20
    if d2_imoto_var == 21:
        call d2_random_imouto21 from _call_d2_random_imouto21
    if d2_imoto_var == 22:
        call d2_random_imouto22 from _call_d2_random_imouto22
    if d2_imoto_var == 23:
        call d2_random_imouto23 from _call_d2_random_imouto23
    if d2_imoto_var == 24:
        call d2_random_imouto24 from _call_d2_random_imouto24
    if d2_imoto_var == 25:
        call d2_random_imouto25 from _call_d2_random_imouto25
    if d2_imoto_var == 99:
        call d2_random_imouto_last from _call_d2_random_imouto_last
    show screen inactivity_timer_d2
    return

label d2_random_imouto1:
    show imouto with fade
    imo "Go back to studying."
    hide imouto with fade

    return
label d2_random_imouto2:
    show imouto with fade
    imo "Hey, I missed you!"
    hide imouto with fade

    return
label d2_random_imouto3:
    show imouto with fade
    imo "So, what did you have today?"
    hide imouto with fade

    return
label d2_random_imouto4:
    show imouto with fade
    imo "When will you finally become rich and famous?"
    hide imouto with fade

    return
label d2_random_imouto5:
    show imouto with fade
    imo "What are you doing in your room, alone?"
    hide imouto with fade

    return
label d2_random_imouto6:
    show imouto with fade
    imo "Fetch me a fancy dinner!"
    hide imouto with fade

    return
label d2_random_imouto7:
    show imouto with fade
    imo "I don't have anything to wear. I demand a new dress!"
    hide imouto with fade

    return
label d2_random_imouto8:
    show imouto with fade
    imo "Your room is so boring!"
    hide imouto with fade

    return
label d2_random_imouto9:
    show imouto with fade
    imo "I won't get fat from this junk food, right?"
    hide imouto with fade

    return
label d2_random_imouto10:
    show imouto with fade
    imo "Do other girls admire you?"
    hide imouto with fade

    return
label d2_random_imouto11:
    show imouto with fade
    imo "Do other boys admire you?"
    hide imouto with fade

    return
label d2_random_imouto12:
    show imouto with fade
    imo "You need to praise me more."
    hide imouto with fade

    return
label d2_random_imouto13:
    show imouto with fade
    imo "Give me some cash!"
    hide imouto with fade

    return
label d2_random_imouto14:
    show imouto with fade
    imo "Why haven't you come home earlier?"
    hide imouto with fade

    return
label d2_random_imouto15:
    show imouto with fade
    imo "Go do your best at studying!"
    hide imouto with fade

    return
label d2_random_imouto16:
    show imouto with fade
    imo "Why is your class so small?"
    hide imouto with fade

    return
label d2_random_imouto17:
    show imouto with fade
    imo "Don't you think everything was different yesterday?"
    hide imouto with fade

    return
label d2_random_imouto18:
    show imouto with fade
    imo "Get me some pictures, pictures of the girls you study with!"
    hide imouto with fade

    return
label d2_random_imouto19:
    show imouto with fade
    imo "Will you buy my a car when I grow up?"
    hide imouto with fade

    return
label d2_random_imouto20:
    show imouto with fade
    imo "I want to go to the sea!"
    hide imouto with fade

    return
label d2_random_imouto21:
    show imouto with fade
    imo "Parents called again, they're kinda worried."
    hide imouto with fade

    return
label d2_random_imouto22:
    show imouto with fade
    imo "What are we going to have for dinner?"
    hide imouto with fade

    return
label d2_random_imouto23:
    show imouto with fade
    imo "Do you want to play with me?"
    hide imouto with fade

    return
label d2_random_imouto24:
    show imouto with fade
    imo "You should clean your bathroom!"
    hide imouto with fade

    return
label d2_random_imouto25:
    show imouto with fade
    imo "I'm staying with you forever!"
    hide imouto with fade

    return
label d2_random_imouto_last:
    $ inactivity_done_d2 = 1
    show imouto with fade
    hide screen inactivity_timer_d2
    imo "Still doing nothing? Fine! I'm not talking to you anymore!"
    hide imouto with fade

    return

label sweet_home_d1:
    play music "music/hero_room.ogg" fadein 1.5 fadeout 1.5
    scene room_v1_night with fade
    "Home sweet home."
    "Edgy movies and games often have a lengthy monologue about the main hero's room."
    "Words \"confined\" and \"prison cell\" are a must in that case."
    "It's like an author feels that cliched scripts deserve jail time."
    "Anyway, my place is very comfy."
    "Having a two-bedroom apartment all for yourself is great."
    "Well, right now I do have a flatmate, though..."
    show imouto with fade
    imo "Hey, did you buy anythig tasty for me?" #corrected in None
    imo "By the way, a strange girl came and left something for you. It's on your table."
    imo "Was this your classmate? She left so quickly!"
    imo "Her ears were so weird!"
    imo "When're you going to buy a new console? This one is {i}old{/i}" #corrected in None
    hide imouto with fade
    "That's right, there's a strange scroll on my table."
    "I open it up."
    call game_progress_d1_r from _call_game_progress_d1_r
    show game_progress_d1 with dissolve
    "Uh... What?"
    "Looks like a remnant from the 8-bit era."
    "Is this intended to make me think about something?"
    "I wonder who made it and why..."
    hide game_progress_d1 with dissolve
    show screen inactivity_timer_d1
    "Alright, it's time to do my homework."
    hide screen inactivity_timer_d1
    show black with fade
    $ renpy.pause(1, hard=True)
    hide black with fade
    show screen inactivity_timer_d1
    "Great, all done! Man, my back is stiff..."
    "I decide to rise and stretch my cramped muscles."
    hide screen inactivity_timer_d1
    show black with fade
    $ renpy.pause(1, hard=True)
    hide black with fade
    show screen inactivity_timer_d1
    "Why don't I check out Ermy's game? I'm quite sure it's something..."

    menu:
        "Play Ermy's game":
            jump ermy_game_d1
        "Skip it":
            hide screen inactivity_timer_d1
            jump lbl_lpg_2

label ermy_game_d1:
    play music "music/ambient_bright.ogg" fadein 1.5 fadeout 1.5
    scene black with fade
    $ renpy.pause(3, hard=True)
    hide screen inactivity_timer_d1
    scene ermy_jp_classroom_day
    show menu_dark
    with fade
    nvl clear
    show screen close_ermy_game
    $ config.nvl_list_length = None
    $ renpy.music.set_volume(.3, 0, channel = "sound")
    ermy_game '\"I don’t think I’m supposed to be here.\"'
    ermy_game 'This thought is nothing new to me. In fact, it’s what I wake up to every single morning... I must admit it’s a rather disappointing thought, almost as much as waking up hungry.'
    ermy_game 'Yes, hungry, as it tries to devour me day by day, to no avail. I never retaliate, yet it always stops after the first bite – I probably taste awful, like a sour grape.'
    ermy_game 'I’ve been here, I’ve been there, I’ve been in between. I don’t believe in aliens, yet I always feel like one. Where am I supposed to be then? If only I knew... If only they knew. No one does, seriously, it’s just some people are ridiculously good at hiding the obvious.'
    ermy_game 'After some time, I decided to change my strategy and get rid of every single thought appearing in my feverish mind. Completely, entirely, eternally. After some time, I found the best solution to do so – something which I called \'mindless living\', as opposed to this mindfulness nonsense, oh so popular among the masses.'
    ermy_game 'Mindless living is easy – you simply need to be dead tired all the time. I mean, when you’re exhausted, you don’t want to think, you want to sleep. In a way, I decided to go through an inverted Maslow pyramid.'
    nvl clear
    ermy_game 'Strangely enough, soon my body got used to being deprived of sleep. I drastically cut down my calorie intake as a next step – this also allowed me to become quite slim, it concentrated me, one hundred percent, on food and food only, regardless of how tired I was. Meat. Fish. Pasta. Pizza. I could smell each of these words…'
    ermy_game 'I’m not a monk or anything, so limiting myself that much became problematic – my stupid body craved sleep and food. \"Feed me! Get me some rest!\"'
    ermy_game 'Every time I succumbed to that voice of reason, I ate until I was about to blow up, and then I could sleep for a day or so, only to wake up and think…'
    ermy_game 'I’m not supposed to be here.'
    ermy_game 'I realized I struggle that much because I probably lack training – after all, I thought, my mindless living should be treated not only as a clever invention, but also as a skill to develop. I decided to pursue a career in it, and shortly after I found my dream job. It was the number one in my shortlist – in fact, it got me enlisted.'
    ermy_game 'Yes, I joined the army.'
    nvl clear
    ermy_game 'However, they fed me so well at the training camp that my silly mind decided to think again. So annoying, I’m telling you! And there was no stopping it… A phone started to ring in my head from time to time, driving me crazy. I know that as soon as I pick it up, I’d hear the same phrase…'
    ermy_game '\"Hey! I don’t think you’re supposed to be here.\"'
    ermy_game 'That’s why, as soon as I could, I asked to be moved away from a grass-fed heaven of a military base to a wild, stinky battlefield.'
    ermy_game 'Codename Hermes, that was my new name. Have you ever heard of a soldier named Ermy? Well, me neither.'
    ermy_game 'I’ve been the happiest man on planet Earth since my first deployment, but then it ended with a buzz – at least that’s what I last heard, the buzz of a bullet, before it got so dark and lonely around me.'
    ermy_game 'Darkness gave way to a white tube of light that sucked me in like a vacuum. What a strange place that was – going all the way up to somewhere above the clouds, I could’ve sworn I saw familiar faces, faces of people long gone from this world.'
    nvl clear
    ermy_game 'They looked like they wanted to tell me something, but all I could hear was that annoying buzz. Or maybe it sounded more like a distorted phone call… doesn’t matter though.'
    ermy_game 'I don’t think I’m supposed to be here.'
    ermy_game 'I spent enough time in this otherwise unremarkable room, spare for a very weird note on a whiteboard.'
    ermy_game 'To leave this room, you must tell me the answer.'
    ermy_game 'What does it mean? Who \'me\'? What’s the question to begin with?'
    ermy_game 'The only semblance of a hint came from a few more words below. Four in total: \"Love\", \"Hate\", \"Life\", \"Death\".'
    ermy_game 'Well… so what of it?'
    nvl clear
    show screen ermy_gui
    $ config.nvl_list_length = 3
    hide menu_dark with dissolve
    $ renpy.pause(.2, hard=True)
    $ renpy.pause(.2, hard=True)
    play music "music/ambient_beat.ogg" fadein 1.5 fadeout 1.5
    e1 'All this makes no sense'
    show nrs sp at u11 as nrs
    s1 'I know, dear. What is the question, I wonder? That’s what my friend and I are trying to realize.'
    show nrs s at u11 as nrs with dissolve
    ee 'A young woman appears seemingly out of nowhere. Dressed in an overly tight nurse uniform, she carries a syringe filled with a strange, bright liquid.'
    e1 'Who are you?'
    show nrs sp at u11 as nrs with dissolve
    s1 'My name is Sophie. Nice to meet you! As for my friend, he doesn’t talk much, so I’m afraid I can’t introduce him to you properly.'
    show nrs s at u11 as nrs with dissolve
    e1 'Your friend?'
    show nrs h at u11 as nrs with dissolve
    s1 'Yes, here, right in my hand. My precious friend who always knows the truth. Always but today it seems.'
    show nrs s at u11 as nrs with dissolve
    ee 'I thought back to my military training… The best way to deal with mentally unstable people is to take them seriously.'
    e1 'I guess it’s nice to have such a wise friend.'
    show nrs h at u11 as nrs with dissolve
    s1 'More like \"persistent\", I should say. It takes my friend quite some time to kick in but then there’s no stopping him, and you’re guaranteed to tell me everything I want.'
    show nrs h at ui11 as nrs:
        ypos 1130
        linear 1 zoom 1.2 ypos 1400
    ee 'She moves closer, and I can’t help but notice that the button on Sophie’s blouse is about to be ripped off by her… well…'
    show nrs h at ui11 as nrs:
        zoom 1.2
        ypos 1400
        linear 1 zoom 1.3 ypos 1500
    s1 'Hey darling, care to have a taste? Who knows, maybe you’re just pretending, not willing to tell me the answer… Hey, I really want to get out of this place. I don’t think I’m supposed be here.'
    show nrs h at ui11 as nrs:
        zoom 1.3
        ypos 1500
        linear .5 zoom 1 ypos 1130
    $ renpy.pause(0.5, hard=True)
    show nrs s at d22 as nrs
    show tsndr p at u21 as tsndr
    m1 'Stay away, she’s clearly out of her mind.'
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d21 as tsndr with dissolve
    ee 'This room gets more crowded, now that a second girl, wrapped up in a latex costume serving presumably no other purpose rather than an aesthetic one, shows up in front of me.'
    show nrs s at u22 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs sp at u22 as nrs with dissolve
    s1 'I’m much saner than you… Megan, right? At least I’m not making up a ridiculous explanation of what bound us all together here like you do.'
    show nrs sp at d22 as nrs
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs s at d22 as nrs
    show tsndr f at u21 as tsndr
    with dissolve
    m1 'It’s not ridiculous, it’s true. I come from an era far more advanced than yours, I know things you can’t even imagine.'
    show nrs s at u22 as nrs
    show tsndr f at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs h at u22 as nrs
    show tsndr fp at d21 as tsndr
    with dissolve
    s1 'See? That’s what I’m talking about. Megan think she’s from the future.'
    show nrs h at d22 as nrs
    show tsndr fp at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs s at d22 as nrs
    show tsndr p at u21 as tsndr
    with dissolve
    m1 'Still don’t believe me? Fine. What’s your last memory before you got here? I’m asking you as well, by the way. What’s your name?'
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d21 as tsndr with dissolve
    e1 'Hermes.'
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr p at u21 as tsndr with dissolve
    m1 'So, Hermes, do you remember anything?'
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d21 as tsndr with dissolve
    play sound "sound/ring.ogg"
    e1 'I heard the phone ringing somewhere very close to where I was.'
    play sound "sound/ring.ogg"
    ee 'The second I say that the phone starts ringing again. Ring-ring… ring-ring… like those machines in old detective phones.'
    play sound "sound/ring.ogg"
    ee 'The sound becomes more and more loud. My head hurts! Someone should stop it. Pick up the phone, please…'
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr p at u21 as tsndr with dissolve
    m1 'What did you say?'
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d21 as tsndr with dissolve
    e1 'Can you hear it?'
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr p at u21 as tsndr with dissolve
    m1 'Hear what?'
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d21 as tsndr with dissolve
    e1 'That phone ringing over and over again… Jeez, it really gets on my nerves.'
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at u21 as tsndr with dissolve
    m1 'My, this room must be a hangout spot for weirdos. And I thought it couldn’t be worse than when our spaceship was invaded by those creatures…'
    show tsndr fp at d21 as tsndr
    show nrs s at u22 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr fp at d21 as tsndr
    show nrs sp at u22 as nrs with dissolve
    s1 'Please don’t mention this word again, Megan.'
    show tsndr fp at u21 as tsndr
    show nrs sp at d22 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs s at d22 as nrs
    show tsndr p at u21 as tsndr
    with dissolve
    m1 'What are you talking about?'
    show nrs s at u22 as nrs
    show tsndr p at d21 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs sp at u22 as nrs
    show tsndr d at d21 as tsndr
    with dissolve
    s1 'Hang, you said… what a painful word. I was doing my daily routine, helping people to open up and talk… the guy we had back then, he just couldn’t relax, he was so nervous!'
    s1 '\"You won’t get a single word out of me!\" he shouted, rolling eyes like a madman. So silly of him! Then I heard the footsteps…'
    s1 'Bam! They ran out the door and barged in. \"Hey girl, nothing personal, but we don’t like to see our friend suffer. That’s a nice rope you tied him with, by the way. Why don’t we really put it to use?\"'
    show nrs sp at d22 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs s at d22 as nrs with dissolve
    ee 'Sophie shivers and stops talking.'
    show tsndr d at u21 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at u21 as tsndr with dissolve
    m1 'Hm… I think I just realized that, although we came from different eras, we share one thing in common.'
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    show md d at u32 as md
    n1 'Yes, yes! We’re all dead nyaw! Naomi knows what she’s talking about!'
    show md d at d32 as md
    ee 'A cute girl, dressed in a maid outfit, joins the conversation. Where was she hiding? Weird… By the way, she holds a plushie in one hand.'
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show md h at u32 as md with dissolve
    n1 'What, can’t you see it? You can, can’t you? You just don’t want to admit it… Ease up – death is the best answer-nya!'
    show md h at d32 as md
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'This little brat… She keeps spouting nonsense.'
    show md d at u32 as md
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show md h at u32 as md
    show tsndr d at d31 as tsndr
    with dissolve
    n1 'Why, I’m just trying to play this game! Unlike you, I realized these are all answers and death is the best one of them all!'
    show md h at d32 as md
    $ renpy.pause(.001, hard=True)
    show md h at d32 as md
    with dissolve
    play sound "sound/ring.ogg"
    ee 'Ring-ring…'
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at u31 as tsndr
    with dissolve
    m1 'Death is certainly not an answer to anything, but, you know, if it helps us to get out of this place, I’m fine with it. I really need to head back home.'
    show tsndr fp at d31 as tsndr
    show md h at u32 as md
    n1 'No one likes the dead coming back, I’m afraid~'
    show md h at d32 as md
    show tsndr f at u31 as tsndr
    m1 'I’m not dead!'
    show nrs s at u33 as nrs
    show tsndr f at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'I agree with Naomi… maybe death is the ultimate answer to everything. At the very least, it has the ultimate degree of certainty.'
    show tsndr fp at u31 as tsndr
    show nrs sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs h at d33 as nrs
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'What?'
    show nrs h at u33 as nrs
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Well, how do you know whether or not you actually live? What qualifies you as a living person?'
    show tsndr d at u31 as tsndr
    show nrs sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr fp at u31 as tsndr
    show nrs s at d33 as nrs
    with dissolve
    m1 'Ridiculous. Don’t be silly. My heartbeat, for instance.'
    show tsndr fp at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Then you compare yourself to an animal.'
    show tsndr d at u31 as tsndr
    show nrs sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr p at u31 as tsndr
    show nrs s at d33 as nrs
    with dissolve
    m1 'You’re getting on my nerves.'
    show tsndr p at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs h at u33 as nrs
    with dissolve
    s1 'Hey, I’m just trying to say that, compared to the lives of some people, you’re just occupying space. On the other hand, when you die, you’re one hundred percent dead. Everyone is equal 6 feet underground. No one can challenge this fact.'
    show tsndr d at u31 as tsndr
    show nrs h at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr p at u31 as tsndr
    show nrs s at d33 as nrs
    with dissolve
    m1 'Spoken like a true genius.'
    show tsndr p at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs h at u33 as nrs
    with dissolve
    s1 'I know, right? I’m an underappreciated asset.'
    show tsndr d at u31 as tsndr
    show nrs h at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr p at u31 as tsndr
    show nrs h at d33 as nrs
    with dissolve
    m1 'Where are you from, again?'
    show tsndr p at d31 as tsndr
    show nrs h at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'The present time.'
    show nrs sp at d33 as nrs
    show md h at u32 as md
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show md he at u32 as md
    with dissolve
    n1 'Death is the answer simply because eternal life is much worse.'
    show md he at d32 as md
    e1 'Say what?'
    show md he at u32 as md
    $ renpy.pause(.001, hard=True)
    show md h at u32 as md
    with dissolve
    n1 'I think I still have my magic powers to show you. Kitty cat, kitty cat! Make me happy, make them sad!'
    show md h at d32 as md
    ee 'I’m quite sure she’s referring to that plushie.'
    show md d at d32 as md
    with dissolve
    e1 'Um, so what’s going to happen now?'
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show md h at u32 as md
    with dissolve
    n1 'Eternity!'
    show md h at d32 as md
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    with dissolve
    e1 'What do you mean?'
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show md he at u32 as md
    with dissolve
    n1 'Time will go, but we won’t follow!'
    show md he at d32 as md
    ee 'And she was right.'
    stop music fadeout 2
    $ renpy.pause(2, hard=True)
    play music "music/melancholic_ambient.ogg" fadein 2
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show ermy_jp_classroom_night behind md, nrs, tsndr
    show mdredtint he at d32 as md
    show nrsredtint s at d33 as nrs
    show tsndrredtint d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    hide ermy_jp_classroom_night
    show md he at d32 as md
    show nrs s at d33 as nrs
    show tsndr d at d31 as tsndr
    with dissolve
    $ renpy.pause(.1, hard=True)
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs sp at u33 as nrs
    with dissolve
    s1 'What day is it today?'
    show nrs sp at d33 as nrs
    show md he at u32 as md
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show md h at u32 as md
    with dissolve
    n1 'Friday-nya!'
    show md h at d32 as md
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'Jeez, how would you know? Thanks for your trick, time lost its meaning.'
    show md d at u32 as md
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at d31 as tsndr
    show md h at u32 as md
    with dissolve
    n1 'Therefore, it might as well always be Friday?'
    show tsndr fp at u31 as tsndr
    show md h at d32 as md
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'It’s been what… days, months, years?'
    show tsndr p at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Hey Naomi, can you revert your spell?'
    show nrs sp at d33 as nrs
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show md h at u32 as md
    with dissolve
    n1 'Tee-hee… if you all admit death is the answer, maybe I could!'
    show nrs s at u33 as nrs
    show md h at d32 as md
    $ renpy.pause(.001, hard=True)
    show md h at d32 as md
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Okay, I admit it.'
    show nrs sp at d33 as nrs
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'No way I’m going to fall for this trick. You want to stay here forever? Fine, let’s talk. Little by little, the future will come, and that’s exactly where I’m from.'
    show tsndr p at d31 as tsndr
    show md h at u32 as md
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show md d at u32 as md
    with dissolve
    n1 'Okay! Let’s talk about cats.'
    ee 'So we did.'
    show ermy_jp_classroom_night behind md,nrs,tsndr
    show mdredtint h at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    with dissolve
    n1 'Let’s talk about food.'
    hide ermy_jp_classroom_night
    show md d at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    with dissolve
    n1 'Let’s talk about fun.'
    show mdredtint he at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    show ermy_jp_classroom_night behind md,nrs,tsndr
    with dissolve
    n1 'Let’s talk about films.'
    show md d at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    hide ermy_jp_classroom_night
    with dissolve
    n1 'Let’s talk about fiction.'
    show mdredtint he at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    show ermy_jp_classroom_night behind md,nrs,tsndr
    with dissolve
    n1 'Let’s talk about friends.'
    show md h at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    hide ermy_jp_classroom_night
    with dissolve
    n1 'Let’s talk about freedom.'
    show mdredtint he at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    show ermy_jp_classroom_night behind md,nrs,tsndr
    with dissolve
    n1 'Let’s talk about feelings.'
    show md d at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    hide ermy_jp_classroom_night
    with dissolve
    n1 'Let’s talk about foals.'
    show mdredtint h at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    show ermy_jp_classroom_night behind md,nrs,tsndr
    with dissolve
    n1 'Let’s talk about foxes.'
    show md d at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    hide ermy_jp_classroom_night
    with dissolve
    n1 'Let’s talk about forests.'
    show mdredtint he at u32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    show ermy_jp_classroom_night behind md,nrs,tsndr
    with dissolve
    n1 'Let’s talk about fonts.'
    show md he at u32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    hide ermy_jp_classroom_night
    with dissolve
    show md he at d32 as md
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr f at u31 as tsndr
    with dissolve
    m1 'Stop it! I can’t take it anymore!'
    show tsndr fp at u31 as tsndr with dissolve
    m1 'Fine, maybe death is the answer. Whatever…'
    show tsndr fp at d31 as tsndr
    ee 'I too agreed with that. However, nothing happened.'
    e1 'Uh, what’s next? What should we do?'
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrs sp at u33 as nrs
    with dissolve
    s1 'I think we should be more proactive, now that we all agree on our answer. See this purple liquid? It’s the last resort liquid, so to speak. Let me help you, friends…'
    stop music fadeout 5
    show nrs sp at ui33 as nrs:
        ypos 1130
        linear .25 zoom 1.2 ypos 1400
        linear .25 zoom 1 ypos 1130
    ee 'She moves so swiftly. It doesn’t even hurt… My vision starts to become blurry.'
    hide screen ermy_gui
    scene black
    with fade
    play sound "sound/ring.ogg"
    ee 'Ring-ring. The phone rings again, but this time I manage to answer it, somehow.'
    ee 'The guy on the other end of the line tells me that if I die, I’ll stay in this room forever. Uhm… why haven’t I thought about it before?'
    ee 'I’m afraid it’s too late now.'
    play music "music/intro.ogg"
    scene ermy_jp_classroom_day
    show screen ermy_gui
    with fade
    ee '\"Love\"'
    e1 'Love? What is love?'
    show md h at u11 as md
    n1 'Baby don’t hurt me… oh, pardon me! Hi! What would your order be?'
    e1 'Naomi? You’re… alive?'
    show md d at u11 as md with dissolve
    n1 'Yes, why? However, I woke up in this room today. You know, that milk tea I had yesterday… it tasted so weird. Anyway, although it’s not my tavern anymore , I certainly have a customer.'
    e1 'What can I order?'
    show md he at u11 as md with dissolve
    n1 'Nothing, I’m afraid. We’re short on everything. But I can make you company! I’m a good maid, after all.'
    e1 'Did you see this strange whiteboard?'
    show md d at u11 as md with dissolve
    n1 'Sure I did! What do you think the answer is-nya?'
    e1 'Love.'
    show md p at u11 as md with dissolve
    n1 'How romantic of you! Sadly, I know nothing of it. I’m not allowed to get into an affair with a customer, even with one as handsome as you. However… let my magic do the work and say whether or not you’re right-nya! Kitty cat, kitty cat, make me happy, make them sad!'
    ee 'Two other girls appear right in front of my eyes.'
    show md d at u32 as md
    show tsndr d at di31 as tsndr
    show nrs s at di33 as nrs
    with dissolve
    n1 'Tell me, what is love?'
    show md d at d32 as md
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'Love is reducible to the absurd act of chemicals. Therefore, there is no intrinsic value in this material universe.'
    show tsndr p at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr fp at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Hypocrite that you are, for you trust the chemicals in your brain to tell you they are chemicals. All knowledge is ultimately based on that which we cannot prove. Will you fight? Or will you perish like a dog?'
    show nrs sp at d33 as nrs
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show md he at u32 as md
    with dissolve
    n1 'Sorry, they’re a bit broken. Let me fix it-nya!'
    show black
    hide screen ermy_gui
    with fade
    $ renpy.pause(1.0, hard=True)
    show tsndr d at d31 as tsndr behind black
    show nrs s at d33 as nrs behind black
    show md d at d32 as md behind black
    hide black with fade
    show screen ermy_gui
    show md d at u32 as md
    n1 'Tell me, what is love?'
    ee 'Silence was her answer.'
    show md he at u32 as md with dissolve
    n1 'Oh my, oh my, still no good. Well, let me try this little trick! In a second, they’re going to fall for you, Hermes!'
    show md h at u32 as md with dissolve
    ee 'She spanks me with her plushie.'
    show md h at d32 as md
    $ renpy.pause(.001, hard=True)
    show md d at d32 as md
    with dissolve
    ee 'I notice Sophie and Megan staring at me.'
    show tsndr d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr f at u31 as tsndr with dissolve
    m1 'Um, Hermes?'
    show tsndr f at d31 as tsndr
    e1 'Yes?'
    show tsndr f at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr fp at u31 as tsndr with dissolve
    m1 'I… I love you.'
    show tsndr fp at d31 as tsndr
    e1 'Why?'
    show tsndr fp at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr p at u31 as tsndr with dissolve
    m1 'Should I have a reason?'
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    e1 'No, but I’m curious.'
    show tsndr p at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr h at u31 as tsndr with dissolve
    m1 'Just because you’re here.'
    show tsndr h at d31 as tsndr
    e1 'I’ve been here before.'
    show tsndr h at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr f at u31 as tsndr with dissolve
    m1 'Really? Well, people change, don’t they?'
    show tsndr f at d31 as tsndr
    show nrs s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show tsndr fp at d31 as tsndr
    show nrs h at u33 as nrs
    with dissolve
    s1 'He’s mine! He will be my darling. Only you and I forever more, Hermes.'
    show nrs h at d33 as nrs
    e1 'Hey, we’re kind of stuck here together.'
    show md d at u32 as md
    $ renpy.pause(.001, hard=True)
    show md h at u32 as md
    with dissolve
    n1 'But if you could leave… which one of them would you choose to go with you-nya?'
    menu:
        "Nana":
            show md d at u32 as md with dissolve
            n1 'You’re being weird. I don’t recognize any of these names.'
        "Marta":
            show md d at u32 as md with dissolve
            n1 'You’re being weird. I don’t recognize any of these names.'
        "Sima":
            show md d at u32 as md with dissolve
            n1 'You’re being weird. I don’t recognize any of these names.'
    show md d at d32 as md
    show tsndr p at u31 as tsndr
    m1 'It hurts me that you’d think of other girls during a moment like this.'
    show nrs h at u33 as nrs
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Yeah, how could you? It’s so selfish… from another side, love is the most selfish feeling anyway.'
    show nrs s at d33 as nrs
    e1 'What?'
    show nrs sp at u33 as nrs
    s1 'Selfish, of course, if it’s not eternal… and what is eternal love? Eternal love means you should stay together until the very end. Till death do us part!'
    show nrs h at u33 as nrs
    with dissolve
    s1 'Now, I’m sure that after some time you’re definitely going to choose me over anyone else. The question is, how can I be sure that your feeling lasts forever?'
    show nrs h at d33 as nrs
    show tsndr p at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrs s at d33 as nrs
    show tsndr p at u31 as tsndr
    with dissolve
    m1 'What are you talking about? Stop babbling nonsense.'
    show nrs s at u33 as nrs
    show tsndr p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndr d at d31 as tsndr
    show nrs sp at u33 as nrs
    with dissolve
    s1 'Trust me, my words make perfect sense. Here, let my friend explain this to you.'
    hide tsndr
    hide md
    with dissolve
    show nrs h at u11 as nrs
    ee 'She does a few quick swings, and shortly after that we’re the only ones standing in the room.'
    e1 'W-what have you done? How could you?'
    show nrs sp at u11 as nrs with dissolve
    s1 'Same as you, I’m just being selfish. All fair and square! Fair… you know what? Love is not the answer. Love is not fair.'
    show nrs s at u11 as nrs with dissolve
    ee 'I feel cold sweat dripping down my back. Sophie’s clearly bonkers, and I need to calm her down somehow.'
    e1 'Not fair? But why? I always thought love is one of the best feelings in the world.'
    show nrs sp at u11 as nrs with dissolve
    s1 'I never said it’s bad, I said it’s not fair. Love should be mutual, but it never works that way.'
    show nrs h at u11 as nrs with dissolve
    s1 'Remember, Hermes, between two people involved, one loves while the other allows himself or herself to be loved. How is this fair?'
    show nrs s at u11 as nrs with dissolve
    e1 'I don’t believe you.'
    show nrs sp at u11 as nrs with dissolve
    s1 'Oh, and love is also very selfish, remember? Even more selfish than you and me.'
    show nrs s at u11 as nrs with dissolve
    e1 'What about love you have for your parents?'
    show nrs sp at u11 as nrs with dissolve
    s1 'It all goes down the same street. Every time you buy them something, you feel like a good kid. In a way, you buy it for yourself, Hermes... Now, what I’m going to do is to have you all for myself.'
    ee 'Swing! The needle bites me like a snake. My legs start to tremble.'
    show nrs h at u11 as nrs with dissolve
    s1 'It feels so… satisfying!'
    hide screen ermy_gui
    scene black
    with fade
    'Sophie’s face is the last thing to flash in my mind before darkness covers everything around me.'
    play music "music/wayback_russia.ogg" fadeout 1.5 fadein 1.5
    show screen ermy_gui
    scene ermy_jp_classroom_night
    show mdredtint d at d32 as md
    show tsndrredtint d at d31 as tsndr
    show nrsredtint s at d33 as nrs
    with fade
    ee 'I’m back from the dead, it seems. Even more, the usual crowd’s here, as if nothing happened at all. The phone starts ringing again.'
    play sound "sound/ring.ogg"
    ee 'I don’t think I can get rid of that pain in my head, so I badly need to concentrate on something else… maybe small talk can help.'
    e1 'Hey, do you guys remember what just happened?'
    show tsndrredtint d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndrredtint p at u31 as tsndr
    with dissolve
    m1 'Um, nothing yet? We have to find the answer, and…'
    show tsndrredtint p at d31 as tsndr
    show mdredtint d at u32 as md
    $ renpy.pause(.001, hard=True)
    show tsndrredtint p at d31 as tsndr
    show mdredtint h at u32 as md
    with dissolve
    n1 'And I’m sure the answer is one of these words-nya!'
    show mdredtint h at d32 as md
    $ renpy.pause(.001, hard=True)
    show mdredtint d at d32 as md
    with dissolve
    ee 'You’re kidding me. Have they entirely forgotten about what happened before?'
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'Hm… which word would it be?'
    show nrsredtint sp at d33 as nrs
    show mdredtint d at u32 as md
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    show mdredtint d at u32 as md
    with dissolve
    n1 'Easy… Hate! Hate is the answer!'
    show nrsredtint s at u33 as nrs
    show mdredtint d at d32 as md
    $ renpy.pause(.001, hard=True)
    show mdredtint d at d32 as md
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'Why do you think so?'
    show mdredtint d at u32 as md
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    show mdredtint he at u32 as md
    with dissolve
    n1 'Well, I hate you all, so this word is definitely a suitable answer for me. '
    show mdredtint he at d32 as md
    show tsndrredtint p at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show mdredtint he at d32 as md
    show tsndrredtint fp at u31 as tsndr
    with dissolve
    m1 'For you, yes, for me, no.'
    show mdredtint he at u32 as md
    show tsndrredtint fp at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show mdredtint h at u32 as md
    show tsndrredtint fp at d31 as tsndr
    with dissolve
    n1 'But why would I care about you-nya?'
    show mdredtint h at d32 as md
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show mdredtint d at d32 as md
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'I wonder what’s your reason for hating us that much.'
    show mdredtint d at u32 as md
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show mdredtint he at u32 as md
    show nrsredtint s at d33 as nrs
    with dissolve
    n1 'It’s simple, you know-nya… I hate you because you leave me no hope.'
    show mdredtint he at d32 as md
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show mdredtint p at d32 as md
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'Why, I wonder?'
    show mdredtint p at u32 as md
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show mdredtint he at u32 as md
    show nrsredtint s at d33 as nrs
    with dissolve
    n1 'If you’re right and I came from the past, then I see my future in the two of you. What can I say? This future looks pathetic…'
    show mdredtint he at d32 as md
    show tsndrredtint fp at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show mdredtint p at d32 as md
    show tsndrredtint p at u31 as tsndr
    with dissolve
    m1 'But you don’t know us at all.'
    show mdredtint p at u32 as md
    show tsndrredtint p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show mdredtint he at u32 as md
    show tsndrredtint d at d31 as tsndr
    with dissolve
    n1 'Even five minutes is enough. I despise you.'
    show mdredtint he at d32 as md
    $ renpy.pause(.001, hard=True)
    show mdredtint p at d32 as md
    with dissolve
    ee 'Her annoyance doesn’t seem to be justified at the very slightest, but I’m not surprised, as it fits perfectly with the weird ambiance of that place.'
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'I don’t think hate is the answer because it’s too easy to hate something.'
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    with dissolve
    e1 'And who said the answer should be complicated?'
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'What do you hate, Hermes?'
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    with dissolve
    e1 'Other people.'
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'Including me?'
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    with dissolve
    e1 'We just met, but I’m sure I’m capable of developing a whole nanoangstrom of hate directed towards you.'
    show nrsredtint s at u33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'Why?'
    show nrsredtint sp at d33 as nrs
    show tsndrredtint d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    show tsndrredtint p at u31 as tsndr
    with dissolve
    m1 'Yeah, why?'
    show tsndrredtint p at d31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndrredtint d at d31 as tsndr
    with dissolve
    e1 'Because you make me feel like I’m not supposed to be here.'
    show tsndrredtint d at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndrredtint fp at u31 as tsndr
    with dissolve
    m1 'What would’ve changed had we not existed at all?'
    show tsndrredtint fp at d31 as tsndr
    show mdredtint p at u32 as md
    $ renpy.pause(.001, hard=True)
    show tsndrredtint fp at d31 as tsndr
    show mdredtint d at u32 as md
    with dissolve
    n1 'Then he couldn’t compare. If he had no other place to be, his thought would become invalid. I agree with you, Hermes. If I hadn’t seen the future right before my eyes, I’d have been fine with everything.'
    show nrsredtint s at u33 as nrs
    show mdredtint d at d32 as md
    $ renpy.pause(.001, hard=True)
    show mdredtint p at d32 as md
    show nrsredtint sp at u33 as nrs
    with dissolve
    s1 'You guys don’t even know about the right reason to hate everyone around you. I mean… they exist. They smell, they take space, they’re loud and annoying.'
    s1 'That’s why I always stay in my lab, so I could have some personal space. But even there, when I visit the bathroom, I look in the mirror and realize I’m no different.'
    show nrsredtint sp at d33 as nrs
    $ renpy.pause(.001, hard=True)
    show nrsredtint s at d33 as nrs
    with dissolve
    e1 'What about you, Megan?'
    show tsndrredtint fp at u31 as tsndr
    $ renpy.pause(.001, hard=True)
    show tsndrredtint p at u31 as tsndr
    with dissolve
    m1 'I don’t know. In the future, our personalities are removed as they serve little to no purpose. We don’t live, we function. I still have some emotions but hate is too strong, it’s off limits.'
    stop music fadeout 2
    show text ("{size=100}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t1:
        xalign .4
        yalign .6
    $ renpy.pause(.1, hard=True)
    show text ("{size=180}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t2:
        xalign .2
        yalign .3
    $ renpy.pause(.1, hard=True)
    show text ("{size=120}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t3:
        xalign .7
        yalign .1
    $ renpy.pause(.1, hard=True)
    show text ("{size=170}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t4:
        xalign .87
        yalign .63
    $ renpy.pause(.1, hard=True)
    show text ("{size=210}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t5:
        xalign .2
        yalign .8
    $ renpy.pause(.1, hard=True)
    show text ("{size=150}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t6:
        xalign .83
        yalign .27
    $ renpy.pause(.1, hard=True)
    show text ("{size=300}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t7:
        xalign .5
        yalign .3
    $ renpy.pause(.1, hard=True)
    show text ("{size=250}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t8:
        xalign .01
        yalign .01
    $ renpy.pause(.1, hard=True)
    show text ("{size=190}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t9:
        xalign .6
        yalign .8
    $ renpy.pause(.1, hard=True)
    show text ("{size=230}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t10:
        xalign .06
        yalign .6
    $ renpy.pause(.1, hard=True)
    show text ("{size=280}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t11:
        xalign .4
        yalign -.1
    $ renpy.pause(.1, hard=True)
    show text ("{size=200}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t12:
        xalign .95
        yalign .4
    $ renpy.pause(.1, hard=True)
    show text ("{size=90}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t13:
        xalign .9
        yalign .77
    $ renpy.pause(.1, hard=True)
    show text ("{size=260}{color=#f00}{font=earwig_factory.ttf}Hate{/color}{/font}{/size}") as t14:
        xalign .95
        yalign -.1
    $ renpy.pause(.1, hard=True)
    hide screen ermy_gui
    scene black
    with fade
    $ renpy.pause(3.0, hard=True)
    show screen ermy_gui
    scene ermy_jp_classroom_day
    show md h at u11 as md
    with fade
    play music "music/final_scene_soft.ogg"
    n1 'Hermes! Hi-nya! Finally, it’s only me and you here!'
    show md d at u11 as md with dissolve
    e1 'Where has everyone else gone?'
    show md he at u11 as md with dissolve
    n1 'What makes you think they’ve ever been here to begin with?'
    show md h at u11 as md with dissolve
    n1 'Anyway… I’m here to support you-nya! Trust me, hate is not the answer! Life, yes, life is!'
    show md d at u11 as md with dissolve
    n1 'I want you to know that you’re supposed to be here with me. Stay with me forever, Hermes.'
    e1 'Why are you so sure about it?'
    show md he at u11 as md with dissolve
    n1 'Because I don’t think this place was supposed to exist in the first place. It feels made up. Therefore, you fit in perfectly. Think of it as a new life for both of us.'
    e1 'Life… you think life is the answer?'
    show md h at u11 as md with dissolve
    n1 'Yes, because I want to spend my life with you.'
    e1 'What… what are we going to do?'
    show md d at u11 as md with dissolve
    n1 'Everything but one thing… we’ll never walk alone. And… you know, I’m a maid. I can always serve you a cup of tea when you need it. Trust me, having a friend like this is what matters the most.'
    e1 'Thanks, Naomi… I-I don’t even know what to say.'
    show nrs h at u11 as md with dissolve
    s1 'It’s because you actually want to spend your whole life with me instead, you know.'
    e1 'Hey, where did Naomi go?'
    show nrs sp at u11 as md with dissolve
    s1 'It doesn’t matter. It’s just you and I here now, Hermes. You and I.'
    e1 'What are we going to do?'
    show nrs h at u11 as md with dissolve
    s1 'We’re going to have some fun, you know. Admit it, that’s what you really want. Everything else is just a façade to mask your desire.'
    e1 'T-that’s not true…'
    show nrs sp at u11 as md with dissolve
    s1 'Well, do you want my friend to ask you this question again? He’ll get an honest answer out of you.'
    e1 'T-there’s no need for that…'
    show nrs h at u11 as md with dissolve
    s1 'See? Now you’re being frank. Don’t worry, it’s okay. Think of yourself as a part of a hunter-gatherer world, it will make your life a whole lot easier. It’s just you, the things you own and the things you want to own.'
    e1 'But I don’t want to think of you as a thing.'
    show nrs sp at u11 as md with dissolve
    s1 'Well then, someone else would, my dear, and you’d be surprised about the choice I make.'
    e1 'Life is not as primitive as you portray it.'
    show nrs h at u11 as md with dissolve
    s1 'Life works the way you make it work, simple as that. I want my life to be primitive, so here I am. You know why you feel like you’re not supposed to be here? Because you don’t even know what kind of life you want to live.'
    e1 'I… well…'
    show nrs sp at u11 as md with dissolve
    s1 'Don’t worry, Hermes. Let me take care of it. Let me comfort you, my dear, so you could forget about everything else.'
    show tsndr p at u11 as md with dissolve
    m1 'No way!'
    e1 'Hey, what just happened? Where did Sophie go?'
    show tsndr fp at u11 as md with dissolve
    m1 'I got rid of that succubus.'
    show tsndr f at u11 as md with dissolve
    m1 'Hey, stay with me, Hermes. I’ve seen the future, and it’s not the best one, I admit… now we’ll have a second chance to make it great.'
    e1 'What are we going to do?'
    show tsndr h at u11 as md with dissolve
    m1 'We’re going to believe in tomorrow. If you think you’re not supposed to be here, make tomorrow the place to be. Please… do it for me'
    show tsndr fp at u11 as md with dissolve
    e1 'Will you love me?'
    show tsndr h at u11 as md with dissolve
    m1 'I’ll love the you of tomorrow, I promise.'
    $ renpy.pause(1, hard=True)
    $ renpy.music.set_volume(1, 0, channel = "sound")
    stop music fadeout 1.5
    hide md
    hide screen ermy_gui
    hide screen close_ermy_game
    with dissolve
    show noise:
        alpha 0.1
        linear .3 alpha 0
        linear .3 alpha 0.1
        repeat
    menu:
        "True Root":
            hide screen close_ermy_game
            scene room_v1_night with fade
            $ renpy.pause(.5, hard=True)
            jump close_game_done
label close_game:
    hide screen ermy_gui
    hide screen close_ermy_game
    stop music fadeout 1.5
    scene room_v1_night with fade
    $ renpy.pause(.5, hard=True)
    "Okay, I had enough... I should think of a proper way to give feedback on this masterpiece."
    jump lbl_lpg_2
label close_game_done:
    $ ermy_game_finished_d1 = 1
    'I try to push the button, but nothing happens. Maybe I should try tomorrow.'
    jump game_done
label game_done:
    hide screen inactivity_timer_d1
    jump lbl_lpg_2
label sweet_home_d2:
    play music "music/hero_room.ogg" fadein 1.5 fadeout 1.5
    scene room_v1_night with fade
    "Man, I'm beat."
    "My mind still goes over what I heard on the way home."
    "Never judge the book by its cover, right?"
    if ermy_game_finished_d1 == 1:
        "Should I give Ermy's game another go?"
    "But first, let me check on my sister."
    show imouto with fade
    imo "I can't believe you came empty-handed again."
    imo1 "That girl from yesterday came again, saying she needs to check on your progress."
    imo "I replied that you can handle everything yourself."
    imo "By the way, what was in that document she gave you?"
    hide imouto with fade
    "Honestly, I forgot about that strange, pixelated thing."
    call game_progress_d1_r from _call_game_progress_d1_r_1
    show game_progress_d1 with dissolve
    "Hm... Is it a bit different today? Just my imagination, probably."
    hide game_progress_d1 with dissolve
    show screen inactivity_timer_d2
    "Same as yesterday... Who on earth writes this nonsense?"

    if ermy_game_finished_d1 == 1:
        "Alright, time for Ermy's masterpiece."
        menu:
            "Play Ermy's game":
                jump ermy_game_d2
            "Skip it":
                hide screen inactivity_timer_d2
                jump lbl_lpg_3
    else:
        hide screen inactivity_timer_d2
        jump lbl_lpg_3

label ermy_game_d2:
    scene black with fade
    play music "music/ambient_bright.ogg" fadein 1.5 fadeout 1.5
    hide screen inactivity_timer_d2
    hide screen scr_ermy_game_d2
    $ renpy.pause(2, hard=True)
    scene ermy_jp_classroom_night
    show md d at d32 as md
    show tsndr d at d31 as tsndr
    show nrs s at d33 as nrs
    show menu_dark
    with fade
    nvl clear
    $ config.nvl_list_length = None
    ermy_game 'I’m in this room again, the girls staring at me, awaiting eagerly what’s going to happen next.'
    ermy_game 'Well, truth is… Nothing’s going to happen.'
    ermy_game 'No one’s going to play this joke of a game, so I could as well just write a develop diary here.'
    ermy_game 'It’s time to be fair with myself. I lack imagination to write anything at all.'
    ermy_game 'It’s… I mean, I wrote quite a lot, but it took me so much time… and, the truth is, it’s all worthless.'
    ermy_game 'The characters don’t live. They’re made up. I’m made up myself. I don’t know what to write next, I really don’t know. My mind is totally empty, like a… jeez, I can’t even come up with a suitable description.'
    ermy_game 'The plot, you say? It’s non-existing. It’s a cliché of a cliché of a cliché… Just like me. And you know what? That’s what people want. They don’t want my originality, but I fail even at copying things in a proper way.'
    nvl clear
    ermy_game 'What did I want to say with all this? Who’s going to read it? Man… I wanted this game to be exciting, but it’s so boring. The characters, I’ve seen them all countless times… a random bunch of characters thrown together in one room. My game is empty. I am empty.'
    ermy_game 'The real answer is that there’s none. It’s all pointless.'
    ermy_game 'I wanted to turn this game into a dating simulator or whatnot, but how can I write anything about a date if my current goal is to hold hands with a girl?'
    ermy_game 'How can I come up with a decent plot if nothing happens in my life? I know nothing about the past and the future, and my present time is… well, nothingness.'
    ermy_game 'Jeez, I wish someone would just put an end to my misery. Maybe it’d be a decent answer, after all.'
    ermy_game 'Hello? Hello? Just don’t leave me alone. Please… don’t leave me alone. I can be a good friend, I swear. How come there are so many people in the world yet I’m alone? Does it mean I’m the worst? No… no way. My game will show’em all. I just need to come up with a decent answer… Yes. Please. Don’t leave me alone…'
    nvl clear
    $ config.nvl_list_length = 3
    show screen inactivity_timer_d2
    play music "music/hero_room.ogg" fadein 1.5 fadeout 1.5
    $ ermy_game_finished_d2 = 1
    scene room_v1_night with fade
    "Alright, I {i}really{/i} need to discuss it with Ermy..."
    "Let's hope it's just a joke."
    "Okay, time to do my homework."
    hide screen inactivity_timer_d2
    jump lbl_lpg_3

label sweet_home_d3:
    scene black with fade
    play music "music/hero_room.ogg" fadein 1.5 fadeout 1.5
    $ renpy.pause(1, hard=True)
    scene room_v1_night with fade
    "I don't feel too well. Better get to sleep early..."
    "I wonder what my sister's doing."
    show imouto with fade
    imo "Your face is all red!"
    imo "Are you okay?"
    imo "Tomorrow is Friday, will you spent time with me?"
    imo "By the way, that girl came yet again!"
    hide imouto with fade
    "My head hurts."
    "That girl... Oh, right, the scroll..."
    call game_progress_d1_r from _call_game_progress_d1_r_2
    show game_progress_d1 with dissolve
    "It's different again, but I'm too tired to be surprised about it."
    hide game_progress_d1 with dissolve
    "Enough with it. I better go to bed... now..."
    jump day4
return

label game_progress_d1_r:
    $ game_progress_d1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    $ book_pos = renpy.random.choice(game_progress_d1_list)
    python:
        book_x = game_progress_x[book_pos]
        book_y = game_progress_y[book_pos]
    python:
        game_progress_d1_list.remove(book_pos)

    $ numbers_pos = renpy.random.choice(game_progress_d1_list)
    python:
        numbers_x = game_progress_x[numbers_pos]
        numbers_y = game_progress_y[numbers_pos]
    python:
        game_progress_d1_list.remove(numbers_pos)

    $ cup_pos = renpy.random.choice(game_progress_d1_list)
    python:
        cup_x = game_progress_x[cup_pos]
        cup_y = game_progress_y[cup_pos]
    python:
        game_progress_d1_list.remove(cup_pos)

    $ e_pos = renpy.random.choice(game_progress_d1_list)
    python:
        e_x = game_progress_x[e_pos]
        e_y = game_progress_y[e_pos]
    python:
        game_progress_d1_list.remove(e_pos)

    $ heart_pos = renpy.random.choice(game_progress_d1_list)
    python:
        heart_x = game_progress_x[heart_pos]
        heart_y = game_progress_y[heart_pos]
    python:
        game_progress_d1_list.remove(heart_pos)

    $ note_pos = renpy.random.choice(game_progress_d1_list)
    python:
        note_x = game_progress_x[note_pos]
        note_y = game_progress_y[note_pos]
    python:
        game_progress_d1_list.remove(note_pos)
    return

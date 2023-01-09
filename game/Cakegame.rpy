label cake_game:
    scene black with fade
    $ renpy.pause(0.5, hard=True)
    $ renpy.pause(0.5, hard=True)
    play music "music/cake_minigame.ogg" fadein 1
    scene book1 with fade
    show plate:
        xalign 0.1
        yalign 0.35
    p "Okay, here we go!"
    p "I wonder where I should start..."
    show base as nana with dissolve:
        xpos 500
    n "Let's begin from the base!"
    hide nana with dissolve
    p "Hm, what do I have here..."
    $config.skipping = None
    show screen cake_base_select
    $ renpy.pause(60.0, hard=True)
    s "What's taking you so long? Just pick a mille-feuille!"
    $ base_type = 3
    hide screen cake_base_select
    jump base_type_selected
label base_type_selected:

    if base_type == 1:
        show tard none:
            xalign 0.19
            yalign 0.34
        with dissolve

    elif base_type == 2:
        show cake none:
            xalign 0.15
            yalign 0.22
        with dissolve

    elif base_type == 3:
        show ml none:
            xalign 0.15
            yalign 0.22
        with dissolve

    p "Done!"
    p "What comes next?"
    show filling as marta with dissolve:
        xpos 500
    m "Well, you need to choose a tasty filling."
    hide marta with dissolve
    p "Hm, what do I have here..."
    $config.skipping = None
    show screen cake_filling_select
    $ renpy.pause(60.0, hard=True)
    m "What's taking you so long? Just pick chocolate!"
    $ filling_type = 6
    hide screen cake_filling_select
    jump filling_type_selected
label filling_type_selected:
    if base_type == 1:

        if filling_type == 1:
            show tard tard ketchup:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif filling_type == 3:
            show tard tard tooth:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif filling_type == 4:
            show tard tard cream:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif filling_type == 5:
            show tard tard custard:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif filling_type == 6:
            show tard tard choco:
                xalign 0.19
                yalign 0.34
            with dissolve

    elif base_type == 2:

        if filling_type == 1:
            show cake cake ketchup:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 3:
            show cake cake tooth:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 4:
            show cake cake cream:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 5:
            show cake cake custard:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 6:
            show cake cake choco:
                xalign 0.15
                yalign 0.22
            with dissolve

    elif base_type == 3:

        if filling_type == 1:
            show ml ml ketchup:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 3:
            show ml ml tooth:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 4:
            show ml ml cream:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 5:
            show ml ml custard:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif filling_type == 6:
            show ml ml choco:
                xalign 0.15
                yalign 0.22
            with dissolve

    p "Yep, all ready."
    show topping as sima with dissolve:
        xpos 500
    s "Las but not least... the topping!"#
    hide sima with dissolve
    p "Hm, what do I have here..."
    $config.skipping = None
    show screen cake_topping_select
    $ renpy.pause(60.0, hard=True)
    n "What's taking you so long? Just pick strawberries!"
    hide screen cake_topping_select
    $ topping_type = 3
    jump topping_type_selected
label topping_type_selected:

    if base_type == 1:

        if topping_type == 1:
            show tard peach:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif topping_type == 2:
            show tard cherry:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif topping_type == 3:
            show tard strawberry:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif topping_type == 4:
            show tard pepe:
                xalign 0.19
                yalign 0.34
            with dissolve

        elif topping_type == 5:
            show tard yoba:
                xalign 0.19
                yalign 0.34
            with dissolve

    elif base_type == 2:

        if topping_type == 1:
            show cake peach:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 2:
            show cake cherry:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 3:
            show cake strawberry:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 4:
            show cake pepe:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 5:
            show cake yoba:
                xalign 0.15
                yalign 0.22
            with dissolve

    elif base_type == 3:

        if topping_type == 1:
            show ml peach:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 2:
            show ml cherry:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 3:
            show ml strawberry:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 4:
            show ml pepe:
                xalign 0.15
                yalign 0.22
            with dissolve

        elif topping_type == 5:
            show ml yoba:
                xalign 0.15
                yalign 0.22
            with dissolve

    p "Done!"
    menu:
        "The imaginary cake is ready!":
            jump dekimashita
        "I'll give it another go.":
            $ base_type = 0
            $ filling_type = 0
            $ topping_type = 0
            hide tard
            hide ml
            hide cake
            jump cake_game
label dekimashita:
    if base_type == 1:
        $ n_points = 1
    elif base_type == 2:
        $ m_points = 1
    elif base_type == 3:
        $ s_points = 1

    if filling_type == 4:
        $ n_points += 1
    elif filling_type == 6:
        $ m_points += 1
    elif filling_type == 5:
        $ s_points += 1

    if topping_type == 3:
        $ n_points += 1
    elif topping_type == 1:
        $ m_points += 1
    elif topping_type == 2:
        $ s_points += 1

    if s_points < 3:
        if n_points < 3:
            if m_points < 3:
                play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
                scene club3 with fade
                show nana2 1a 2b 3a at u31 as nana
                $ renpy.pause(.001, hard=True)
                show nana2 1d 2b 3a at u31 as nana with dissolve
                n "This looks a bit strange..."
                show nana2 1d 2b 3a at d31 as nana
                $ renpy.pause(.001, hard=True)
                show nana2 1a 2b 3a at d31 as nana
                show marta1 1a 2a 3a at u32 as marta
                with dissolve
                show marta1 1e 2a 3a at u32 as marta with dissolve
                m "I should've been the one making it."
                show marta1 1e 2a 3a at d32 as marta
                $ renpy.pause(.001, hard=True)
                show marta1 1a 2a 3a at d32 as marta
                show sima3a 1a 2b 3a at u33 as sima
                with dissolve
                show sima3a 1c 2b 3a at u33 as sima with dissolve
                s "I appreciate your effort, but it doesn't look very good."
                show sima3a 1c 2b 3a at d33 as sima
                $ renpy.pause(.001, hard=True)
                show sima3a 1a 2b 3a at d33 as sima with dissolve
                "Well, there was an attempt."
                show sima3a 1a 2b 3a at u33 as sima
                $ renpy.pause(.001, hard=True)
                show sima3a 1e 2a 3a at u33 as sima
                show marta1 1a 2b 3b at d32 as marta
                show nana2 1a 2b 3a at d31 as nana
                with dissolve
                s "[player_name], don't worry, it's still better than nothing."
                show sima3a 1d 2b 3a at u33 as sima
                show nana2 1a 2b 3a at d31 as nana
                with dissolve
                s "Wait, it's actually nothing, right?"
                show sima3a 1d 2b 3a at d33 as sima
                $ renpy.pause(.001, hard=True)
                show sima3a 1a 2b 3a at d33 as sima with dissolve
                "No one wants my imaginary cake... How could they!"
                jump tea_after

    if s_points == 3:
        jump sima_cake_win
    if n_points == 3:
        jump nana_cake_win
    if m_points ==3:
        jump marta_cake_win
label nana_cake_win:
    play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
    scene club3 with fade
    show nana1 1e 2c 3c blush at u11 as nana
    $achievement.grant("pastrypuffer")
    init:
        $achievement.register("pastrypuffer")
        $achievement.sync()
    $achievement.sync()
    n "Looks delicious! I'll go buy something like this today."
    jump tea_after
label sima_cake_win:
    play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
    scene club3 with fade
    show sima2 1c 2c 3c regular2 blush at u11 as sima
    $achievement.grant("pastrypuffer")
    init:
        $achievement.register("pastrypuffer")
        $achievement.sync()
    $achievement.sync()
    s "Oh! Looks so tasty, I can't wait to make something like this home."
    jump tea_after
label marta_cake_win:
    play music "music/club_afterhours.ogg" fadein 1.5 fadeout 1.5
    scene club3 with fade
    show marta3 1e 2a 3b blush at u11 as marta
    $achievement.grant("pastrypuffer")
    init:
        $achievement.register("pastrypuffer")
        $achievement.sync()
    $achievement.sync()
    m "Looks cool! Now, I crave some cakes, everyone!"
    jump tea_after
return

label pianogame:
    show piano 1top 7top 6top 2top 5top 3top 4top as piano
    stop music fadeout 3
    $ renpy.pause(1.0, hard=True)
    e "Look, here's the first octave."
    show piano 1top_hover 7top_hover 6top_hover 2top_hover 5top_hover 3top_hover 4top_hover as piano with dissolve
    $ renpy.pause(.5, hard=True)
    e "Yeah, these keys."
    show piano 1top 7top 6top 2top 5top 3top 4top as piano with dissolve
    e "Just use the white ones, alright? Keep it simple."
    jump pianogame1
label pianogame1:
    $config.skipping = None
    show screen pianogame_scr_note1
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_1:
    $ note1 = 1
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a1.ogg"
    show piano 1bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_2:
    $ note1 = 2
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a2.ogg"
    show piano 2bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_3:
    $ note1 = 3
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a3.ogg"
    show piano 3bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_4:
    $ note1 = 4
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a4.ogg"
    show piano 4bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_5:
    $ note1 = 5
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a5.ogg"
    show piano 5bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_6:
    $ note1 = 6
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a6.ogg"
    show piano 6bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note1_7:
    $ note1 = 7
    hide screen pianogame_scr_note1
    play sound "/pianogame/piano-f-a7.ogg"
    show piano 7bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note2
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_1:
    $ note2 = 1
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a1.ogg"
    show piano 1bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_2:
    $ note2 = 2
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a2.ogg"
    show piano 2bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_3:
    $ note2 = 3
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a3.ogg"
    show piano 3bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_4:
    $ note2 = 4
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a4.ogg"
    show piano 4bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_5:
    $ note2 = 5
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a5.ogg"
    show piano 5bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_6:
    $ note2 = 6
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a6.ogg"
    show piano 6bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note2_7:
    $ note2 = 7
    hide screen pianogame_scr_note2
    play sound "/pianogame/piano-f-a7.ogg"
    show piano 7bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note3
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_1:
    $ note3 = 1
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a1.ogg"
    show piano 1bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_2:
    $ note3 = 2
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a2.ogg"
    show piano 2bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_3:
    $ note3 = 3
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a3.ogg"
    show piano 3bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_4:
    $ note3 = 4
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a4.ogg"
    show piano 4bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_5:
    $ note3 = 5
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a5.ogg"
    show piano 5bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_6:
    $ note3 = 6
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a6.ogg"
    show piano 6bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note3_7:
    $ note3 = 7
    hide screen pianogame_scr_note3
    play sound "/pianogame/piano-f-a7.ogg"
    show piano 7bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note4
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_1:
    $ note4 = 1
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a1.ogg"
    show piano 1bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_2:
    $ note4 = 2
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a2.ogg"
    show piano 2bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_3:
    $ note4 = 3
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a3.ogg"
    show piano 3bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_4:
    $ note4 = 4
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a4.ogg"
    show piano 4bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_5:
    $ note4 = 5
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a5.ogg"
    show piano 5bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_6:
    $ note4 = 6
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a6.ogg"
    show piano 6bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note4_7:
    $ note4 = 7
    hide screen pianogame_scr_note4
    play sound "/pianogame/piano-f-a7.ogg"
    show piano 7bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    $config.skipping = None
    show screen pianogame_scr_note5
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_1:
    $ note5 = 1
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a1.ogg"
    show piano 1bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_2:
    $ note5 = 2
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a2.ogg"
    show piano 2bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_3:
    $ note5 = 3
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a3.ogg"
    show piano 3bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_4:
    $ note5 = 4
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a4.ogg"
    show piano 4bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_5:
    $ note5 = 5
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a5.ogg"
    show piano 5bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_6:
    $ note5 = 6
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a6.ogg"
    show piano 6bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label pianogame_note5_7:
    $ note5 = 7
    hide screen pianogame_scr_note5
    play sound "/pianogame/piano-f-a7.ogg"
    show piano 7bottom with dissolve
    $ renpy.pause(.05, hard=True)
    show piano 1top 7top 6top 2top 5top 3top 4top with dissolve
    $ renpy.pause(.05, hard=True)
    jump notes_ready
    $ renpy.pause(1000.0, hard=True)
label notes_ready:
    hide screen wth
    with dissolve
    p "It aint't much, but it's honest work."
    python:
        notes_picked = [note1, note2, note3, note4, note5];
        notes_sima = [1,3,2,2,3];
        notes_marta = [2,2,1,1,5];
        notes_nana = [7,1,5,3,4];
        correct_sima = [];
        correct_marta = [];
        correct_nana = [];
        for i in range(len(notes_picked)):
            if notes_picked[i] == notes_sima[i]:
                correct_sima.append(notes_picked[i])
        for i in range(len(notes_picked)):
            if notes_picked[i] == notes_marta[i]:
                correct_marta.append(notes_picked[i])
        for i in range(len(notes_picked)):
            if notes_picked[i] == notes_nana[i]:
                correct_nana.append(notes_picked[i])
        sima_notes_correct = len(correct_sima);
        marta_notes_correct = len(correct_marta);
        nana_notes_correct = len(correct_nana);
    if sima_notes_correct == 5:
        jump piano_win_sima
    if marta_notes_correct == 5:
        jump piano_win_marta
    if nana_notes_correct == 5:
        jump piano_win_nana
    jump piano_fail

$ renpy.pause(1000.0, hard=True)
return

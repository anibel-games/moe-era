transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
transform arain1:
    yalign 1.0 xalign 0.0
    linear .4 yalign 0.0 xalign 1.0
    repeat
transform arain2:
    yalign 1.0 xalign 0.0
    linear .6 yalign 0.0 xalign 1.0
    repeat
transform arain3:
    yalign 1.0 xalign 0.0
    linear .2 yalign 0.0 xalign 1.0
    repeat
transform rain:
    yalign 1.0 xalign 0.0
    linear 0.4 yalign 0.0
    repeat
transform barashek_roll_1:
    xalign 0.7
    yalign 0.6
    linear 10 rotate 360
    rotate 0
    repeat
transform barashek_roll_2:
    xalign 0.7
    yalign 0.6
    linear 15 rotate 360
    rotate 0
    repeat
default game_restarted1 = 0
default game_restarted2 = 0
default frame = 1
default quick_menu = True
define gui.history_allow_tags = set()
define config.nvl_list_length = gui.nvl_list_length
define config.narrator_menu = True
define gui.about = ""
default g_p_1 = 0
default g_p_2 = 0
default g_p_3 = 0
default g_p_4 = 0
default g_p_y_1 = 0
default g_p_y_2 = 0
default g_p_y_3 = 0
default g_p_y_4 = 0
default books_skip = 0
default math_skip = 0
default books_chosen = 0
default math_chosen = 0
default dont_like_reading = 0
default g_p_y = 0
default n_date_finished = 0
default s_date_finished = 0
default m_date_finished = 0
default sch_complete = 0
default sat_complete = 0
default chp_complete = 0
default disguise_real = 0
default wrong_answer_sima_sg = 0
default wrong_answer_marta_sg = 0
default wrong_answer_nana_sg = 0
default story_told = 0
default ido = 0
default first_date = 0
default inactivity = 0
default inactivity_done_d1 = 0
default inactivity_done_d2 = 0
default inactivity_done_d3 = 0
default maidens_chosen = 0
default naomi_chosen = 0
default megan_chosen = 0
default sophie_chosen = 0
default note1 = 0
default note2 = 0
default note3 = 0
default note4 = 0
default note5 = 0
default sima_notes_correct = 0
default marta_notes_correct = 0
default nana_notes_correct = 0
default base_type = 0
default filling_type = 0
default topping_type = 0
default s_points = 0
default n_points = 0
default m_points = 0
default restart = 0
default as_p = 0
default an_p = 0
default am_p = 0
default as_tp = 0
default an_tp = 0
default am_tp = 0
default bs_tp = 0
default bn_tp = 0
default bm_tp = 0
default acs_p = 0
default acn_p = 0
default acm_p = 0
default bs_p = 0
default bn_p = 0
default bm_p = 0
default bhs_p = 0
default bhn_p = 0
default bhm_p = 0
default bhe_p = 0
default cs_p = 0
default cn_p = 0
default cm_p = 0
default csp_p = 0
default cnp_p = 0
default cmp_p = 0
default cs_tp = 0
default cn_tp = 0
default cm_tp = 0
default new_game1 = 0
default new_game1_nana_set = 0
default new_game1_sima_set = 0
default new_game1_marta_set = 0
default new_game2_nana_set = 0
default new_game2_sima_set = 0
default new_game2_marta_set = 0
default new_game1_nana_done = 0
default new_game1_sima_done = 0
default new_game1_marta_done = 0
default new_game2_nana_done = 0
default new_game2_sima_done = 0
default new_game2_marta_done = 0
default ermy_game_finished_d1 = 0
default ermy_game_finished_d2 = 0
default marta_plusset = 0
default sima_plusset = 0
default nana_plusset = 0
default persistent.language_chosen = 0
define game_progress_d1_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
define game_progress_y = [.208, .208, .208, .208, .208, .3145, .3145, .3145, .3145, .3145, .4185, .4185, .4185, .4185, .4185, .5175, .5175, .5175, .5175, .5175, .6219, .6219, .6219, .6219, .6219, .208]
define game_progress_x = [.388, .433, .5, .555, .61, .388, .433, .5, .555, .61, .388, .433, .5, .555, .61, .388, .433, .5, .555, .61, .388, .433, .5, .555, .61, .388]
define book_x = 0
define book_y = 0
define numbers_x = 0
define numbers_y = 0
define note_x = 0
define note_y = 0
define cup_x = 0
define cup_y = 0
define heart_x = 0
define heart_y = 0
define e_x = 0
define e_y = 0
define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }
define config.mouse_hide_time = 5
define d1_random_imouto_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
define d2_random_imouto_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
define un = Character('???', color = 'FFD4AD')
define c = DynamicCharacter('c_name', color = '68984C')
define catgirl_text = Character('???', color = '68984C', who_ypos=92, who_xpos=15, what_ypos=60, who_size = 50, what_textalign=1.0, window_yalign=1.0, what_xalign = 0.5, what_xmaximum = 1720, what_size = 50)
define s = DynamicCharacter('s_name', color = '5E98E0')
define m = DynamicCharacter('m_name', color = 'CE3350')
define n = DynamicCharacter('n_name', color = 'ff66cc')
define t = DynamicCharacter('t_name', color = '98ff98')
define e = DynamicCharacter('e_name', color = '00FFFF')
define chad = DynamicCharacter('chad_name', color = 'C7753D')
define p = Character('[player_name]', color = '808080')
define credits1 = Character(' ', what_style="what_credits1", what_textalign=0.5, window_yalign=.5)
define credits2 = Character(' ', what_style="what_credits2", what_textalign=0.5, window_yalign=.5)
define imo = Character(' ', what_style="what_imo", what_textalign=0.0, window_yalign=1.0)
define imo1 = Character(' ', what_style="what_imo1", what_textalign=0.0, window_yalign=1.0)
define s1 = Character('Sophie',xfill = True,who_outlines = [(2, "000000", 0, 0)], what_style="what_sophie", what_textalign=0.0, window_yalign=1.0, window_xalign=0.0, color="C7753D", who_style="who_sophie")
define n1 = Character('Naomi',xfill = True,who_outlines = [(2, "000000", 0, 0)], what_style="what_sophie", what_textalign=0.0, window_yalign=1.0, window_xalign=0.0, color="909233",who_style="who_sophie")
define m1 = Character('Megan',xfill = True,who_outlines = [(2, "000000", 0, 0)], what_style="what_sophie", what_textalign=0.0, window_yalign=1.0, window_xalign=0.0, color="6A958B", who_style="who_sophie")
define e1 = Character('Hermes',xfill = True,who_outlines = [(2, "000000", 0, 0)], what_style="what_sophie", what_textalign=0.0, window_yalign=1.0, window_xalign=0.0, color="808080", who_style="who_sophie")
define ee = Character(' ',xfill = True,who_outlines = [(2, "000000", 0, 0)], what_style="what_sophie", what_textalign=0.0, window_yalign=1.0, window_xalign=0.0, color="808080",who_style="who_sophie")
define narrator1 = Character('Narrator', color = '000000')
define ermy_game = Character(None, kind=nvl)
define peteacher = Character('P.E. teacher', color = 'A0A0A0')
define npc = DynamicCharacter('npc_name')
define how = Image("cg/how.png")
define language_english = Image("buttons/english.png")
define language_english_hover = Image("buttons/english_hover.png")
define language_russian = Image("buttons/russian.png")
define language_russian_hover = Image("buttons/russian_hover.png")
define language_belarusian = Image("buttons/belarusian.png")
define language_belarusian_hover = Image("buttons/belarusian_hover.png")
define language_japanese = Image("buttons/japanese.png")
define language_japanese_hover = Image("buttons/japanese_hover.png")
define language_ch = Image("buttons/ch.png")
define language_ch_hover = Image("buttons/ch_hover.png")
define language_chtr = Image("buttons/chtr.png")
define language_chtr_hover = Image("buttons/chtr_hover.png")
define piano_base_empty = Image("pianogame/piano_base_empty.jpg")
define piano_1_1top = Image("pianogame/piano_1_1top.png")
define piano_1_1top_hover = Image("pianogame/piano_1_1top_hover.png")
define piano_1_1bottom = Image("pianogame/piano_1_1bottom.png")
define piano_2_2top = Image("pianogame/piano_2_2top.png")
define piano_2_2top_hover = Image("pianogame/piano_2_2top_hover.png")
define piano_2_2bottom = Image("pianogame/piano_2_2bottom.png")
define piano_3_3top = Image("pianogame/piano_3_3top.png")
define piano_3_3top_hover = Image("pianogame/piano_3_3top_hover.png")
define piano_3_3bottom = Image("pianogame/piano_3_3bottom.png")
define piano_4_4top = Image("pianogame/piano_4_4top.png")
define piano_4_4top_hover = Image("pianogame/piano_4_4top_hover.png")
define piano_4_4bottom = Image("pianogame/piano_4_4bottom.png")
define piano_4_4top_hover = Image("pianogame/piano_4_4top_hover.png")
define piano_5_5top = Image("pianogame/piano_5_5top.png")
define piano_5_5top_hover = Image("pianogame/piano_5_5top_hover.png")
define piano_5_5bottom = Image("pianogame/piano_5_5bottom.png")
define piano_6_6top = Image("pianogame/piano_6_6top.png")
define piano_6_6top_hover = Image("pianogame/piano_6_6top_hover.png")
define piano_6_6bottom = Image("pianogame/piano_6_6bottom.png")
define piano_7_7top = Image("pianogame/piano_7_7top.png")
define piano_7_7top_hover = Image("pianogame/piano_7_7top_hover.png")
define piano_7_7bottom = Image("pianogame/piano_7_7bottom.png")

label splashscreen:
    if not persistent.chose_language:
        $ persistent.chose_language = True
        menu:
            "{font=ProximaNova-Bold.otf}English{/font}":
                show screen language_english
            "{font=ProximaNova-Bold.otf}Русский{/font}":
                show screen language_russian
            "{font=ProximaNova-Bold.otf}Белауруская{/font}":
                show screen language_belarusian
            "{font=SourceHanSerifSC-Bold.otf}日本語{/font}":
                show screen language_japanese
            "{font=SourceHanSerifSC-Bold.otf}简体中文{/font}":
                show screen language_chinese
            "{font=SourceHanSerifSC-Bold.otf}繁體中文{/font}":
                show screen language_chinese_trad
    $ renpy.music.play("images/movies/click.mkv", channel="movie", loop=True)
    scene movie
    call screen allrights
    return
label before_main_menu:
    play music "music/the_dream_2.ogg"
    queue music "music/the_dream.ogg"
    $ renpy.music.play("images/movies/click.mkv", channel="movie", loop=True)
    scene movie
    show screen logo_scr
    $ renpy.pause(4.5, hard=True)
    scene selfie
    stop movie
    hide screen logo_scr
    $ renpy.movie_cutscene("images/movies/selfie.mkv",stop_music=False)
    scene white with flash
    $ renpy.pause(.01, hard=True)
    jump main_menu
    return
default isplaying = 1
label main_menu:
    $ renpy.music.play("images/movies/main_menu_movie_girls.mkv", channel="movie", loop=False)
    $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
    show movie with flash
    jump main_menu_screen
label start:
    $ _game_menu_screen = "navigation"
    if persistent.game_done1 == True:
        if restart == 1:
            $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
            $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
            show movie
            show gui_shade
            with dissolve
            menu:
                "Start a new game (this action will delete your save data)":
                    $ persistent.girl1_done = None
                    $ persistent.girl2_done = None
                    $ persistent.game_done1 = None
                    $ persistent.game_done2 = None
                    $ persistent.game_done3 = None
                    $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
                    $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
                    show movie
                    show gui_shade
                    with dissolve
                    python:
                        player_name = ""
                        while not player_name:
                            player_name = renpy.input("What is your name?", length=9)
                            player_name = player_name.strip()
                    $ delete_slot(0, True)
                    stop movie
                    jump intro
                "Return":
                    return
    if persistent.game_done2 == True:
        if restart == 1:
            $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
            $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
            show movie
            show gui_shade
            with dissolve
            menu:
                "Start a new game (this action will delete your save data)":
                    $ persistent.girl1_done = None
                    $ persistent.girl2_done = None
                    $ persistent.game_done1 = None
                    $ persistent.game_done2 = None
                    $ persistent.game_done3 = None
                    $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
                    $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
                    show movie
                    show gui_shade
                    with dissolve
                    python:
                        player_name = ""
                        while not player_name:
                            player_name = renpy.input("What is your name?", length=9)
                            player_name = player_name.strip()
                    $ delete_slot(0, True)
                    stop movie
                    jump intro
                "Return":
                    return
    if persistent.game_done3 == True:
        if restart == 1:
            $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
            $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
            show movie
            show gui_shade
            with dissolve
            menu:
                "Start a new game (this action will delete your save data)":
                    $ persistent.girl1_done = None
                    $ persistent.girl2_done = None
                    $ persistent.game_done1 = None
                    $ persistent.game_done2 = None
                    $ persistent.game_done3 = None
                    $ delete_slot(0, True)
                    $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
                    $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
                    show movie
                    show gui_shade
                    with dissolve
                    python:
                        player_name = ""
                        while not player_name:
                            player_name = renpy.input("What is your name?", length=9)
                            player_name = player_name.strip()
                    stop movie
                    jump intro
                "Return":
                    return

    if persistent.player_name:
        $ player_name = persistent.player_name
        stop movie
        jump intro
    $ renpy.music.queue("images/movies/main_menu_movie.mkv", channel="movie", loop=True)
    $ renpy.music.queue("music/the_dream.ogg", channel="music", loop=True)
    show movie
    show gui_shade
    with dissolve
    python:
        player_name = ""
        while not player_name:
            player_name = renpy.input("What is your name?", length=9)
            player_name = player_name.strip()
    stop movie
    jump intro
    return

image main_menu_movie = Movie(play="images/movies/main_menu_movie.webm")
image selfie_movie = Movie(play="images/movies/selfie.webm")
image cg_marta_6_1all:
    contains:
        "cg_marta_6_3"
        ypos 0
    contains:
        "cg_marta_6_1"
        ypos 0
image cg_marta_6_1allg:
    contains:
        "cg_marta_6_3"
        ypos 0
    contains:
        "cg_marta_6_1"
        ypos 0
    contains:
        "cg_marta_6_2"
        ypos 0
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 2.5
        linear .5 alpha 0
        repeat
image cg_sima_7_1all:
    contains:
        "cg_sima_7_1_back"
    contains:
        "rain1"
        yalign 1.0 xalign 0.0
        linear .4 yalign 0.0 xalign 1.0
        repeat
    contains:
        "rain2"
        yalign 1.0 xalign 0.0
        linear .6 yalign 0.0 xalign 1.0
        repeat
    contains:
        "cg_sima_7_3"
image cg_sima_7_1allg:
    contains:
        "cg_sima_7_1_back"
    contains:
        "rain1"
        yalign 1.0 xalign 0.0
        linear .4 yalign 0.0 xalign 1.0
        repeat
    contains:
        "rain2"
        yalign 1.0 xalign 0.0
        linear .6 yalign 0.0 xalign 1.0
        repeat
    contains:
        "cg_sima_7_3"
    contains:
        "cg_sima_7_1"
        pause 2.5
        linear .5 alpha 1
        pause 2.5
        linear .5 alpha 0
        repeat
image cg_teya:
    contains:
        "b0"
    contains:
        "b1"
        parallel:
            alpha 1
            linear 2 alpha 0.4
            linear 1 alpha 1
            repeat
        parallel:
            yalign 0.5 xalign 0.5
            rotate 0
            linear 3 rotate 1.5
            linear 3 rotate 0
            rotate 0
            repeat
    contains:
        "b2"
        parallel:
            alpha 1
            linear 4 alpha 0.4
            linear 2 alpha 1
            repeat
        parallel:
            yalign 0.5 xalign 0.5
            rotate 0
            linear 3 rotate 3
            linear 3 rotate 0
            rotate 0
            repeat
    contains:
        "b3"
    contains:
        "b4"
        alpha 1
        linear 4 alpha 0.1
        linear 2 alpha 1
        repeat
    contains:
        "b5"
        parallel:
            alpha 1
            linear 4 alpha 0.1
            linear 2 alpha 1
            repeat
        parallel:
            yalign 0.5 xalign 0.5
            linear 12 rotate 360
            rotate 0
            repeat
    contains:
        "b6"
        parallel:
            alpha 1
            linear 4 alpha 0.1
            linear 2 alpha 1
            repeat
        parallel:
            yalign 0.5 xalign 0.5
            linear 144 rotate 360
            rotate 0
            repeat
    contains:
        "b8_2"
        rotate 0.001
        yalign 0.5 xalign 0.5
        linear 6 yalign 0.6
        linear 6 yalign 0.5
        repeat
    contains:
        "b8"
        parallel:
            rotate 0.001
            yalign 0.5 xalign 0.5
            linear 6 yalign 0.6
            linear 6 yalign 0.5
            repeat
        parallel:
            alpha 0
            linear 6 alpha 1
            linear 6 alpha 0
            repeat
    contains:
        "b9_2"
        rotate 0.001
        yalign 0.6 xalign 0.5
        linear 6 yalign 0.5
        linear 6 yalign 0.6
        repeat
    contains:
        "b9"
        parallel:
            rotate 0.001
            yalign 0.6 xalign 0.5
            linear 6 yalign 0.5
            linear 6 yalign 0.6
            repeat
        parallel:
            alpha 1
            linear 6 alpha 0
            linear 6 alpha 1
            repeat
    contains:
        "teya_cg"
    contains:
        "br_n"
    contains:
        "m_c"
image meditation_back = im.Scale("cg/cg_barashek_3.jpg", 2880, 1620)
image shadesmall:
    Solid("0000005F")
    size (480,270)
image cg_all_2_2small = im.Scale("cg/cg_all_2_2.jpg", 480, 270)
image cg_nana_8_1small = im.Scale("cg/cg_nana_8_1.jpg", 480, 270)
image cg_nana_8_2small = im.Scale("cg/cg_nana_8_2.jpg", 480, 270)
image cg_nana_4_2small = im.Scale("cg/cg_nana_4_2.jpg", 480, 270)
image cg_sima_3_1small = im.Scale("cg/cg_sima_3_1.jpg", 480, 270)
image cg_marta_7_1small = im.Scale("cg/cg_marta_7_1.jpg", 480, 270)
image cg_nana_7_1small = im.Scale("cg/cg_nana_7_1.jpg", 480, 270)
image cg_sima_1_1small = im.Scale("cg/cg_sima_1_1.jpg", 480, 270)
image cg_marta_3_2small = im.Scale("cg/cg_marta_3_2.jpg", 480, 270)
image cg_marta_1_1small = im.Scale("cg/cg_marta_1_1.jpg", 480, 270)
image cg_marta_2_5small = im.Scale("cg/cg_marta_2_5.jpg", 480, 270)
image cg_all_3_ssmall = im.Scale("cg/cg_all_3_s.png", 480, 270)
image cg_all_3_nsmall = im.Scale("cg/cg_all_3_n.png", 480, 270)
image cg_all_3_msmall = im.Scale("cg/cg_all_3_m.png", 480, 270)
image b0small = im.Scale("cg/cg_teya_clock/b0.jpg", 480, 270)
image b1small = im.Scale("cg/cg_teya_clock/b1.png", 480, 270)
image b2small = im.Scale("cg/cg_teya_clock/b2.png", 480, 270)
image b3small = im.Scale("cg/cg_teya_clock/b3.png", 480, 270)
image b4small = im.Scale("cg/cg_teya_clock/b4.png", 480, 270)
image b5small = im.Scale("cg/cg_teya_clock/b5.png", 480, 270)
image b6small = im.Scale("cg/cg_teya_clock/b6.png", 480, 270)
image b8small = im.Scale("cg/cg_teya_clock/b8.png", 480, 270)
image b9_2small = im.Scale("cg/cg_teya_clock/b9_2.png", 480, 270)
image g_l_osmall = im.Scale("cg/cg_teya_clock/g_l_o.png", 480, 270)
image br_nsmall = im.Scale("cg/cg_teya_clock/br_n.png", 480, 270)
image m_csmall = im.Scale("cg/cg_teya_clock/m_c.png", 480, 270)
image cg_teya_small = Image("cg/cg_teya_clock/cg_teya_small.jpg")
image cg_all_3all:
    contains:
        "cg_all_3_s"
    contains:
        "cg_all_3_n"
    contains:
        "cg_all_3_m"
image cg_all_3small:
    size (480,270)
    contains:
        "cg_all_3_ssmall"
    contains:
        "cg_all_3_nsmall"
    contains:
        "cg_all_3_msmall"
image cg_sima_2_1small = im.Scale("cg/cg_sima_2_1.jpg", 480, 270)
image cg_sima_4_1small = im.Scale("cg/cg_sima_4_1.jpg", 480, 270)
image cg_sima_6_2small = im.Scale("cg/cg_sima_6_2.jpg", 480, 270)
image cg_sima_7_1allsmall = Image("cg/cg_sima_7_3small.jpg")
image cg_marta_4_1small = im.Scale("cg/cg_marta_4_1.jpg", 480, 270)
image cg_marta_5_3small = im.Scale("cg/cg_marta_5_3.jpg", 480, 270)
image cg_marta_6_1small = im.Scale("cg/cg_marta_6_1.png", 480, 480)
image cg_marta_6_1smallcropped = Crop((0, 0, 480, 270), "cg_marta_6_1small")
image cg_marta_6_3small = im.Scale("cg/cg_marta_6_3.jpg", 480, 480)
image cg_marta_6_3smallcropped = Crop((0, 0, 480, 270), "cg_marta_6_3small")
image cg_marta_6_1allsmall:
    size (480,270)
    contains:
        "cg_marta_6_3smallcropped"
    contains:
        "cg_marta_6_1smallcropped"
image cg_nana_3_1small = im.Scale("cg/cg_nana_3_1.jpg", 480, 270)
image cg_nana_5_1small = im.Scale("cg/cg_nana_5_1.jpg", 480, 270)
image cg_nana_6_1small = im.Scale("cg/cg_nana_6_1.jpg", 480, 270)
image cg_nana_9_6small = im.Scale("cg/cg_nana_9_6.jpg", 480, 270)
image cg_photosmall = im.Scale("cg_photo", 480, 270)
image mainmenu_skysmall = im.Scale("bg/mainmenu_sky.jpg", 480, 270)
image cg_all_2_1small = im.Scale("cg/cg_all_2_1.png", 480, 270)
image cg_photosmall:
    size (480,270)
    contains:
        "mainmenu_skysmall"
    contains:
        "cg_all_2_1small"
image barashek_1_small = im.Scale("cg/cg_barashek_1.png", 629, 622)
image barashek_1_smallcropped = Crop((170, 270, 480, 270), "barashek_1_small")
image barashek_2_small = im.Scale("cg/cg_barashek_2.png", 629, 622)
image barashek_2_smallcropped = Crop((170, 270, 480, 270), "barashek_2_small")
image barashek_3_small = im.Scale("cg/cg_barashek_3.jpg", 480, 270)
image barashek_4_small = im.Scale("cg/cg_barashek_4.png", 480, 270)
image cg_barasheksmall:
    size (480,270)
    contains:
        "barashek_3_small"
    contains:
        "barashek_2_smallcropped"
    contains:
        "barashek_1_smallcropped"
    contains:
        "barashek_4_small"
image black:
  Solid("#000")
image white:
  Solid("#FFF")
image ermy_gui = Image("room/textbox3.png")
image mainmenu_scroll = Image("bg/mainmenu_scroll.png")
image right_here = Image("cg/right_here.png")
image plate = Image("cakegame/plate.png")
image do_this = Image("/cg/do_this.jpg")
image do_this_1 = Image("/cg/do_this_1.png")
image do_this_2 = Image("/cg/do_this_2.png")
image do_this_3 = Image("/cg/do_this_3.png")
image do_this_4 = Image("/cg/do_this_4.png")
image do_this_5 = Image("/cg/do_this_5.png")
image do_this_unfocused = Image("/cg/do_this_unfocused.jpg")
image cat1t = Image("/images/catgirl_intro/cat1t.png")
image cat1 = Image("/images/catgirl_intro/cat1.png")
image cat1rt = redtint("/images/catgirl_intro/cat1.png")
image cat2t = Image("/images/catgirl_intro/cat2t.png")
image cat2 = Image("/images/catgirl_intro/cat2.png")
image cat3t = Image("/images/catgirl_intro/cat3t.png")
image cat3 = Image("/images/catgirl_intro/cat3.png")
image cat4 = Image("/images/catgirl_intro/cat4.png")
image null_image = Null()
image catgirl = Image("/images/chr/catgirl.png")
image catgirl2 = Image("/images/chr/catgirl2.png")
image catgirl3 = Image("/images/chr/catgirl3.png")
image right_menu = Image("/images/gui_button/right_menu.png")
image shade_bottom = Image("/images/gui_button/shade_bottom.png")
image gui_shade:
    Solid("0000005F")
image menu_dark:
    Solid("00000080")
image history_dark:
    Solid("000000C8")
image hide_mask:
    Solid("00000000")
    size (1420, 1080)
image idle_mask:
    Solid("00000000")
    size (20, 1080)
image frame:
    Solid("00000000")
    size (1920, 85)
image catcher1 = Image("/images/manga/catcher1.png")
image catcher2 = Image("/images/manga/catcher2.png")
image catcher3 = Image("/images/manga/catcher3.png")
image winnie1 = Image("/images/manga/winnie1.png")
image winnie2 = Image("/images/manga/winnie2.png")
image winnie3 = Image("/images/manga/winnie3.png")
image crime1 = Image("/images/manga/crime1.png")
image crime2 = Image("/images/manga/crime2.png")
image crime3 = Image("/images/manga/crime3.png")
image crime4 = Image("/images/manga/crime4.png")
image MR_rain = Image("/images/bg/MR_rain.png")
image MR_sky = Image("/images/bg/MR_sky.png")
image MR_room = Image("/images/bg/MR_room.png")
image JPCR_room = Image("/images/bg/JPCR_room.png")
image JPCR_back = Image("/images/bg/JPCR_back.png")
image JPCR_matrix = Image("/images/bg/JPCR_matrix.png")
image JPCR_room_nf = Image("/images/bg/JPCR_room_nf.png")
image JPCR_back_nf = Image("/images/bg/JPCR_back_nf.png")
image JPCR_matrix_nf = Image("/images/bg/JPCR_matrix_nf.png")
image meditation1 = Image("cg/meditation1.png")
image meditation2b = Image("cg/meditation2b.png")
image cg_isthatso = Image("cg/isthatso.png")
image cg_isthatso_sima = Image("cg/isthatso_sima.png")
image cg_isthatso_marta = Image("cg/isthatso_marta.png")
image teya_intro_whoops1 = Image("cg/Teya_intro_whoops1.png")
image teya_intro_whoops2 = Image("cg/Teya_intro_whoops2.png")
image cat_day1a = Image("cg/cats/cat_day1a.jpg")
image cat_day2b = Image("cg/cats/cat_day2b.jpg")
image cat_day3b = Image("cg/cats/cat_day3b.jpg")
image cg_invite = Image("cg/cg_invite.jpg")
image cg_all_1_2 = Image("cg/cg_all_1_2.jpg")
image cg_all_1_3 = Image("cg/cg_all_1_3.jpg")
image cg_all_2_1 = Image("cg/cg_all_2_1.png")
image cg_all_3_s = Image("cg/cg_all_3_s.png")
image cg_all_3_n = Image("cg/cg_all_3_n.png")
image cg_all_3_m = Image("cg/cg_all_3_m.png")
image cg_marta_1_1 = Image("cg/cg_marta_1_1.jpg")
image cg_marta_2_3 = Image("cg/cg_marta_2_3.jpg")
image cg_marta_2_4 = Image("cg/cg_marta_2_4.jpg")
image cg_marta_2_5 = Image("cg/cg_marta_2_5.jpg")
image cg_marta_2:
    contains:
        "cg_marta_2_5"
    contains:
        "cg_marta_2_4"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 3
        repeat
    contains:
        "cg_marta_2_3"
        alpha 0
        pause 5.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_marta_3_1 = Image("cg/cg_marta_3_1.jpg")
image cg_marta_3_2 = Image("cg/cg_marta_3_2.jpg")
image cg_marta_3_3 = Image("cg/cg_marta_3_3.jpg")
image cg_marta_3_4 = Image("cg/cg_marta_3_4.jpg")
image cg_marta_3_5 = Image("cg/cg_marta_3_5.jpg")
image cg_marta_3_6 = Image("cg/cg_marta_3_6.jpg")
image cg_marta_3:
    contains:
        "cg_marta_3_1"
    contains:
        "cg_marta_3_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 12
        repeat
    contains:
        "cg_marta_3_3"
        alpha 0
        pause 5.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 9
        repeat
    contains:
        "cg_marta_3_4"
        alpha 0
        pause 8.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 6
        repeat
    contains:
        "cg_marta_3_5"
        alpha 0
        pause 11.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 3
        repeat
    contains:
        "cg_marta_3_6"
        alpha 0
        pause 14.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_marta_4_1 = Image("cg/cg_marta_4_1.jpg")
image cg_marta_4_2 = Image("cg/cg_marta_4_2.jpg")
image cg_marta_4:
    contains:
        "cg_marta_4_1"
    contains:
        "cg_marta_4_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_marta_5_2 = Image("cg/cg_marta_5_2.jpg")
image cg_marta_5_3 = Image("cg/cg_marta_5_3.jpg")
image cg_marta_5:
    contains:
        "cg_marta_5_2"
    contains:
        "cg_marta_5_3"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_marta_6_1 = Image("cg/cg_marta_6_1.png")
image cg_marta_6_2 = Image("cg/cg_marta_6_2.png")
image cg_marta_6_3 = Image("cg/cg_marta_6_3.jpg")
image cg_marta_7_1 = Image("cg/cg_marta_7_1.jpg")
image rain1 = Image("cg/rain1.png")
image rain2 = Image("cg/rain2.png")
image rain3 = Image("cg/rain3.png")
image cafe_table = Image("cg/cafe_table.jpg")
image cg_nana_3_1 = Image("cg/cg_nana_3_1.jpg")
image cg_nana_3_2 = Image("cg/cg_nana_3_2.jpg")
image cg_nana_3_3 = Image("cg/cg_nana_3_3.jpg")
image cg_nana_3_4 = Image("cg/cg_nana_3_4.jpg")
image cg_nana_3_5 = Image("cg/cg_nana_3_5.jpg")
image cg_nana_3_6 = Image("cg/cg_nana_3_6.jpg")
image cg_nana_4_1 = Image("cg/cg_nana_4_1.jpg")
image cg_nana_4_2 = Image("cg/cg_nana_4_2.jpg")
image cg_nana_4:
    contains:
        "cg_nana_4_2"
    contains:
        "cg_nana_4_1"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_nana_5_1 = Image("cg/cg_nana_5_1.jpg")
image cg_nana_6_1 = Image("cg/cg_nana_6_1.jpg")
image cg_nana_7_1 = Image("cg/cg_nana_7_1.jpg")
image cg_nana_7_2 = Image("cg/cg_nana_7_2.jpg")
image cg_nana_7:
    contains:
        "cg_nana_7_1"
    contains:
        "cg_nana_7_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_nana_8_1 = Image("cg/cg_nana_8_1.jpg")
image cg_nana_8_2 = Image("cg/cg_nana_8_2.jpg")
image cg_nana_9_1 = Image("cg/cg_nana_9_1.jpg")
image cg_nana_9_2 = Image("cg/cg_nana_9_2.jpg")
image cg_nana_9_4 = Image("cg/cg_nana_9_4.jpg")
image cg_nana_9_6 = Image("cg/cg_nana_9_6.jpg")
image cg_nana_9:
    contains:
        "cg_nana_9_6"
    contains:
        "cg_nana_9_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 3
        repeat
    contains:
        "cg_nana_9_1"
        alpha 0
        pause 5.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_sima_1_1 = Image("cg/cg_sima_1_1.jpg")
image cg_sima_1_2 = Image("cg/cg_sima_1_2.jpg")
image cg_sima_1_3 = Image("cg/cg_sima_1_3.jpg")
image cg_sima_1:
    contains:
        "cg_sima_1_1"
    contains:
        "cg_sima_1_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        pause 3
        repeat
    contains:
        "cg_sima_1_3"
        alpha 0
        pause 5.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_sima_2_1 = Image("cg/cg_sima_2_1.jpg")
image cg_sima_2_2 = Image("cg/cg_sima_2_2.jpg")
image cg_sima_2_3 = Image("cg/cg_sima_2_3.jpg")
image cg_sima_2_4 = Image("cg/cg_sima_2_4.jpg")
image cg_sima_2:
    contains:
        "cg_sima_2_1"
    contains:
        "cg_sima_2_3"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_sima_3_1 = Image("cg/cg_sima_3_1.jpg")
image cg_sima_4_1 = Image("cg/cg_sima_4_1.jpg")
image cg_sima_4_2 = Image("cg/cg_sima_4_2.jpg")
image cg_sima_4:
    contains:
        "cg_sima_4_1"
    contains:
        "cg_sima_4_2"
        alpha 0
        pause 2.5
        linear .5 alpha 1
        pause 3
        linear .5 alpha 0
        repeat
image cg_sima_6_1 = Image("cg/cg_sima_6_1.jpg")
image cg_sima_6_2 = Image("cg/cg_sima_6_2.jpg")
image cg_sima_7_1 = Image("cg/cg_sima_7_1.png")
image cg_sima_7_3 = Image("cg/cg_sima_7_3.png")
image cg_sima_7_1_back = Image("cg/cg_sima_7_1_back.jpg")
image cg_room_v1 = Image("images/room/room_v1.jpg")
image cg_room_v1a = Image("images/room/room_v1a.jpg")
image room_v1_night = Image("images/room/room_v1_night.jpg")
image cg_room_v1_nighta = Image("images/room/room_v1_nighta.jpg")
image cg_room_v2 = Image("images/room/room_v2.jpg")
image cg_room_v3 = Image("images/room/room_v3.jpg")
image cg_room_v4 = Image("images/room/room_v4.jpg")
image cg_room_v5 = Image("images/room/room_v5.jpg")
image cg_room_v6 = Image("images/room/room_v6.jpg")
image cg_room_v7 = Image("images/room/room_v7.jpg")
image cg_barashek_1 = Image("cg/cg_barashek_1.png")
image cg_barashek_2 = Image("cg/cg_barashek_2.png")
image cg_barashek_3 = Image("cg/cg_barashek_3.jpg")
image cg_barashek_4 = Image("cg/cg_barashek_4.png")
image note = Image("room/note.png")
image heart = Image("room/heart.png")
image cup = Image("room/cup.png")
image book2 = Image("room/book1.png")
image numbers = Image("room/numbers.png")
image mainmenu = Image("gui/main_menu.jpg")
image mainmenu_girls = Image("cg/main_menu_girls.png")
image mainmenugirls:
    contains:
        "mainmenu"
    contains:
        "mainmenu_girls"
image game_menu = Image("gui/main_menu.jpg")
image mainmenu_sky = Image("/images/bg/mainmenu_sky.jpg")
image arch_nf = Image("bg/arch_intro/arch_nf.jpg")
image arch_nf2 = Image("bg/arch_intro/arch_nf2.jpg")
image the = Image("cg/the.png")
image the_the = Image("cg/the_the.png")
image the_the_end = Image("cg/the_the_end.png")
image teya_intro_you_not = Image("cg/teya_intro_you_not.png")
image teya_intro_you_see = Image("cg/teya_intro_you_see.png")
image teya_outtro_you_see = Image("cg/teya_outtro_you_see.png")
image marta_phony:
    contains:
        "/CHR/marta1/date/marta1date_clothes_regular1.png"
    contains:
        "/CHR/marta1/date/marta1date_1_1g.png"
    contains:
        "/CHR/marta1/date/marta1date_2_2a.png"
    contains:
        "/CHR/marta1/date/marta1date_3_3d.png"
    xalign .5
image main_menuimage = Image("gui/main_menu.jpg")
image mb_sv = Image("/images/cg/musicbox/sv.png")
image mb_bg = Image("/images/cg/musicbox/bg.jpg")
image mb_1 = Image("/images/cg/musicbox/1.png")
image mb_2 = Image("/images/cg/musicbox/2.png")
image mb_3 = Image("/images/cg/musicbox/3.png")
image mb_4 = Image("/images/cg/musicbox/4.png")
image mb_5 = Image("/images/cg/musicbox/5.png")
image mb_6 = Image("/images/cg/musicbox/6.png")
image mb_7 = Image("/images/cg/musicbox/7.png")
image mb_8 = Image("/images/cg/musicbox/8.png")
image mb = Animation("mb_1",0.1,"mb_2",0.1,"mb_3",0.1,"mb_4",0.1,"mb_5",0.1,"mb_6",0.1,"mb_7",0.1,"mb_8",0.1)
image club_0 = Image("/images/bg/club/club_0.png")
image club_1 = Image("/images/bg/club/club_1.png")
image club_2 = Image("/images/bg/club/club_2.png")
image club_3 = Image("/images/bg/club/club_3.png")
image lpg_0 = Image("/images/bg/lpg/lpg_0.png")
image lpg_1 = Image("/images/bg/lpg/lpg_1.png")
image lpg_2a = Image("/images/bg/lpg/lpg_2a.png")
image lpg_2b = Image("/images/bg/lpg/lpg_2b.png")
image lpg_i_0 = Image("/images/bg/lpg/lpg_i_0.png")
image lpg_i_1 = Image("/images/bg/lpg/lpg_i_1.png")
image lpg_i_2 = Image("/images/bg/lpg/lpg_i_2.png")
image lpg_i_3 = Image("/images/bg/lpg/lpg_i_3.png")
image lpg_i_4 = Image("/images/bg/lpg/lpg_i_4.png")
image lpg_i_7 = Image("/images/bg/lpg/lpg_i_7.png")
image lpg_i_8 = Image("/images/bg/lpg/lpg_i_8.png")
image lpg_i_ni = Image("/images/bg/lpg/lpg_i_ni.png")
image lpg_i_qr = Image("/images/bg/lpg/lpg_i_qr.png")
image lpg_i_rr = Image("/images/bg/lpg/lpg_i_rr.png")
image lpg_i_tr = Image("/images/bg/lpg/lpg_i_tr.png")
image lpg_i_yr = Image("/images/bg/lpg/lpg_i_yr.png")
image lpg_i_pr = Image("/images/bg/lpg/lpg_i_pr.png")
image lpg_i_sr = Image("/images/bg/lpg/lpg_i_sr.png")
image lpg_i_ur = Image("/images/bg/lpg/lpg_i_ur.png")
image lpg_i_cr = Image("/images/bg/lpg/lpg_i_cr.png")
image lpg_i_am = Image("/images/bg/lpg/lpg_i_am.png")
image lpg_i_ad = Image("/images/bg/lpg/lpg_i_ad.png")
image lpg_i_ae = Image("/images/bg/lpg/lpg_i_ae.png")
image lpg_i_ar = Image("/images/bg/lpg/lpg_i_ar.png")
image lpg_i_af = Image("/images/bg/lpg/lpg_i_af.png")
image lpg_i_aa = Image("/images/bg/lpg/lpg_i_aa.png")
image lpg_i_as = Image("/images/bg/lpg/lpg_i_as.png")
image lpg_i_ao = Image("/images/bg/lpg/lpg_i_ao.png")
image lpg_i_au = Image("/images/bg/lpg/lpg_i_au.png")
image cats_1 = Image("/images/cg/cats/cats_1.jpg")
image cats_2 = Image("/images/cg/cats/cats_2.jpg")
image backroom = Image("/images/bg/backroom.jpg")
image imouto = Image("/images/cg/imouto.jpg")
image ru_classroom2 = Image("/images/bg/ru_classroom2.jpg")
image b0 = Image("/images/cg/cg_teya_clock/b0.jpg")
image b1 = Image("/images/cg/cg_teya_clock/b1.png")
image b2 = Image("/images/cg/cg_teya_clock/b2.png")
image b3 = Image("/images/cg/cg_teya_clock/b3.png")
image b4 = Image("/images/cg/cg_teya_clock/b4.png")
image b5 = Image("/images/cg/cg_teya_clock/b5.png")
image b6 = Image("/images/cg/cg_teya_clock/b6.png")
image b8 = Image("/images/cg/cg_teya_clock/b8.png")
image b8_2 = Image("/images/cg/cg_teya_clock/b8_2.png")
image b9 = Image("/images/cg/cg_teya_clock/b9.png")
image b9_2 = Image("/images/cg/cg_teya_clock/b9_2.png")
image g_r_o = Image("/images/cg/cg_teya_clock/g_r_o.png")
image g_l_o = Image("/images/cg/cg_teya_clock/g_l_o.png")
image g_r_c = Image("/images/cg/cg_teya_clock/g_r_c.png")
image g_l_c = Image("/images/cg/cg_teya_clock/g_l_c.png")
image br_e = Image("/images/cg/cg_teya_clock/br_e.png")
image br_f = Image("/images/cg/cg_teya_clock/br_f.png")
image br_n = Image("/images/cg/cg_teya_clock/br_n.png")
image m_c = Image("/images/cg/cg_teya_clock/m_c.png")
image m_o = Image("/images/cg/cg_teya_clock/m_o.png")
image BG3_0 = Image("/images/bg/jp_street/BG3_0.png")
image BG3_1 = Image("/images/bg/jp_street/BG3_1.png")
image BG3_2 = Image("/images/bg/jp_street/BG3_2.png")
image BG3_3 = Image("/images/bg/jp_street/BG3_3.png")
image BG3_4 = Image("/images/bg/jp_street/BG3_4.png")
image book1 = Image("/images/cg/book.jpg")
image base = Image("/images/cg/base.png")
image selfie = Image("/images/selfie.jpg")
image filling = Image("/images/cg/filling.png")
image topping = Image("/images/cg/topping.png")
image BG4_0 = Image("/images/bg/ru_street/BG4_0.jpg")
image BG4_1 = Image("/images/bg/ru_street/BG4_1.png")
image BG4_2 = Image("/images/bg/ru_street/BG4_2.png")
image BG4_3 = Image("/images/bg/ru_street/BG4_3.png")
image n0 = Image("/images/cg/musicroom/n0.jpg")
image n1 = Image("/images/cg/musicroom/n1.png")
image n2 = Image("/images/cg/musicroom/n2.png")
image n3 = Image("/images/cg/musicroom/n3.png")
image n4 = Image("/images/cg/musicroom/n4.png")
image n6 = Image("/images/cg/musicroom/n6.png")
image n7 = Image("/images/cg/musicroom/n7.png")
image n8 = Image("/images/cg/musicroom/n8.png")
image n9 = Image("/images/cg/musicroom/n9.png")
image n10 = Image("/images/cg/musicroom/n10.png")
image n11 = Image("/images/cg/musicroom/n11.png")
image n12 = Image("/images/cg/musicroom/n12.png")
image n13 = Image("/images/cg/musicroom/n13.png")
image melody:
    contains:
        "n0"
    contains:
        "n1"
        yalign 0.0 xalign 0.0
        linear 60.0 xalign 1.0
        repeat
    contains:
        "n2"
        yalign 1.0 xalign 0.0
        linear 0.3 yalign 0.0 xalign 1.0
        repeat
    contains:
        "n3"
        yalign 1.0 xalign 0.0
        linear 0.15 yalign 0.0 xalign 1.0
        repeat
    contains:
        "n4"
image melody1:
    contains:
        "n6"
        alpha 0
        block:
            linear .5 alpha 1
            linear 1.5 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.5 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.4
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.4
            linear .6 alpha 1
            linear 1.3 alpha 0.2
            pause .5
            pause 1.1
            linear .6 alpha 1
            linear 2.2 alpha 0.2
            pause 0.8
            linear .6 alpha 1
            linear 2.328 alpha 0.2
            pause .6
            repeat
    contains:
        "n7"
        alpha 0
        block:
            linear .5 alpha 1
            linear 1.5 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.5 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.4
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.5
            linear .5 alpha 1
            linear 1.6 alpha 0.2
            pause 1.4
            linear .6 alpha 1
            linear 1.3 alpha 0.2
            pause .5
            pause 1.1
            linear .6 alpha 1
            linear 2.2 alpha 0.2
            pause 0.8
            linear .6 alpha 1
            linear 2.328 alpha 0.2
            pause .6
            repeat
    contains:
        "n8"
        alpha 0
        block:
            pause .6
            linear .2 alpha 1
            linear 1.2 alpha 0.2
            pause 1.5
            pause .6
            linear .2 alpha 1
            linear 1.2 alpha 0.2
            pause 1.5
            pause .6
            linear .2 alpha 1
            linear 2.2 alpha 0.2
            pause 0.6
            pause .6
            linear .2 alpha 1
            linear 2.3 alpha 0.2
            pause 0.4
            pause .6
            linear .2 alpha 1
            linear 0.9 alpha 0.6
            linear 0.2 alpha 1
            linear 0.9 alpha 0.2
            pause .7
            pause .6
            linear .2 alpha 1
            linear 1.1 alpha 0.2
            pause .5
            pause 1.1
            pause .6
            linear .2 alpha 1
            linear 2 alpha 0.2
            pause 1.4
            linear .2 alpha 1
            linear 2.128 alpha 0.2
            pause .6
            repeat
    contains:
        "n9"
        alpha 0
        block:
            pause .7
            linear .2 alpha 1
            linear 1.1 alpha 0.2
            pause 1.5
            pause .7
            linear .2 alpha 1
            linear 1.1 alpha 0.2
            pause 1.5
            pause .7
            linear .2 alpha 1
            linear 2.1 alpha 0.2
            pause 0.6
            pause .7
            linear .2 alpha 1
            linear 2.2 alpha 0.2
            pause 0.4
            pause .7
            linear .2 alpha 1
            linear 0.8 alpha 0.6
            linear 0.2 alpha 1
            linear 0.9 alpha 0.2
            pause .7
            pause .6
            linear .2 alpha 1
            linear 1.1 alpha 0.2
            pause .5
            pause 1.1
            pause .6
            linear .2 alpha 1
            linear 2 alpha 0.2
            pause 1.4
            linear .2 alpha 1
            linear 2.128 alpha 0.2
            pause .6
            repeat
    contains:
        "n10"
        alpha 0
        block:
            pause .8
            linear .2 alpha 1
            linear 1 alpha 0.2
            pause 1.5
            pause .8
            linear .2 alpha 1
            linear 1 alpha 0.2
            pause 1.5
            pause .8
            linear .2 alpha 1
            linear 2 alpha 0.2
            pause 0.6
            pause .8
            linear .2 alpha 1
            linear 2.1 alpha 0.2
            pause 0.4
            pause .8
            linear .2 alpha 1
            linear 0.7 alpha 0.6
            linear 0.2 alpha 1
            linear 0.9 alpha 0.2
            pause .7
            pause 1.2
            linear .2 alpha 1
            linear .8 alpha 0.2
            linear .5 alpha 1
            linear .8 alpha 0.2
            pause .6
            linear .2 alpha 1
            linear 2 alpha 0.2
            pause 1.4
            linear .2 alpha 1
            linear 2.128 alpha 0.2
            pause .6
            repeat
    contains:
        "n11"
        alpha 0
        pause .6
        block:
            linear 2 alpha 0.5
            linear 2 alpha 1
            linear 2 alpha 0.25
            repeat
    contains:
        "n12"
        alpha 0
        pause 2.6
        block:
            linear 2 alpha 0.5
            linear 2 alpha 1
            linear 2 alpha 0.25
            repeat
    contains:
        "n13"
        alpha 0
        pause 4.6
        block:
            linear 2 alpha 0.5
            linear 2 alpha 1
            linear 2 alpha 0.25
            repeat
image melody2:
    contains:
        "n6"
        alpha 0
        block:
            pause .4
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 1.5
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 1.6
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 2.7
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 3.8
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 1.5
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 1.9
            linear .3 alpha 1
            linear 1.5 alpha .2
            pause 2.7
            linear .3 alpha 1
            linear 1.5 alpha .1
            pause 4.752
            repeat
    contains:
        "n7"
        alpha 0
        block:
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 4.352
            repeat
    contains:
        "n8"
        alpha 0
        pause .25
        block:
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 4.352
            repeat
    contains:
        "n9"
        alpha 0
        pause .5
        block:
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 4.352
            repeat
    contains:
        "n10"
        alpha 0
        pause .75
        block:
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause .6
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            pause 2.4
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .8 alpha .2
            linear .2 alpha 1
            linear .5 alpha .2
            linear .2 alpha 1
            linear .2 alpha .4
            linear .2 alpha 1
            linear .2 alpha .4
            linear .2 alpha 1
            linear .2 alpha 1.2
            pause .6
            linear .2 alpha 1
            linear .8 alpha .2
            pause .4
            linear .2 alpha 1
            linear .6 alpha .2
            linear .2 alpha 1
            linear .6 alpha .2
            linear .2 alpha 1
            linear .6 alpha .2
            linear .2 alpha 1
            linear .6 alpha .2
            pause 5.052
            repeat
    contains:
        "n11"
        alpha 0
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
    contains:
        "n12"
        alpha 0
        pause 1.5
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
    contains:
        "n13"
        alpha 0
        pause 3
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
image melody3:
    contains:
        "n6"
        alpha 0
        pause .8
        block:
            linear 1.5 alpha 1
            linear 1.5 alpha .2
            repeat
    contains:
        "n7"
        alpha 0
        pause 1.1
        block:
            linear 1.5 alpha 1
            linear 1.5 alpha .2
            repeat
    contains:
        "n8"
        alpha 0
        pause 1.4
        block:
            linear 1.5 alpha 1
            linear 1.5 alpha .2
            repeat
    contains:
        "n9"
        alpha 0
        pause 1.7
        block:
            linear 1.5 alpha 1
            linear 1.5 alpha .2
            repeat
    contains:
        "n10"
        alpha 0
        pause 2
        block:
            linear 1.5 alpha 1
            linear 1.5 alpha .2
            repeat
    contains:
        "n11"
        alpha 0
        pause 2
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
    contains:
        "n12"
        alpha 0
        pause 3.5
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
    contains:
        "n13"
        alpha 0
        pause 5
        block:
            linear 1.5 alpha 0.5
            linear 1.5 alpha 1
            linear 1.5 alpha 0.25
            repeat
image street_ru:
    contains:
        "BG4_0"
    contains:
        "BG4_1"
        xalign 0.0 yalign 1.0
        pause 5.0
        linear 10.0 yalign 1.15
        pause 60.0
        linear 10.0 yalign 1.0
        pause 125.0
        repeat
    contains:
        "BG4_2"
    contains:
        "BG4_3"
image street:
    contains:
        "BG3_0"
    contains:
        "BG3_1"
        xalign 0.5
        ypos 0
        parallel:
            alpha 1
            linear 0.2 alpha 0.95
            linear 0.1 alpha 1
            linear 0.2 alpha 0.9
            linear 0.1 alpha 1
            repeat
        parallel:
            linear 5 ypos 230
            ypos -230
            linear 5 ypos 0
            pause 3
            repeat
    contains:
        "BG3_2"
    contains:
        "BG3_3"
        alpha 1
        pause 7.0
        linear 0.1 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
        linear 0.1 alpha 1
        repeat
    contains:
        "BG3_4"
        alpha 1
        linear 0.1 alpha 0.7
        linear 0.1 alpha 1
        linear 0.15 alpha 0.8
        linear 0.1 alpha 1
        repeat
image teya_cg:
    contains:
        "g_r_o"
    contains:
        "g_l_o"
        alpha 0
        block:
            linear 6 alpha 1
            linear 6 alpha 0
            repeat
    contains:
        "g_r_c"
        alpha 0
        block:
            pause 23
            linear 1 alpha 1
            pause 23
            linear 1 alpha 0
            repeat
    contains:
        "g_l_c"
        alpha 0
        block:
            pause 24
            linear 6 alpha 1
            linear 6 alpha 0
            linear 6 alpha 1
            linear 6 alpha 0
            repeat
image club1:
    contains:
        "club_0"
    contains:
        "club_2"
        pause 10.0
        yalign 0.0 xalign 0.9
        linear 55.0 xalign 1.9
    contains:
        "club_3"
image club2:
    contains:
        "club_0"
    contains:
        "club_1"
        yalign 0.0 xalign -0.2
        pause 3.0
        linear 55.0 xalign -1.2
    contains:
        "club_3"
image club3:
    contains:
        "club_0"
    contains:
        "club_3"

layeredimage piano:
    always:
        "piano_base_empty"
    group 1 auto
    group 7 auto
    group 6 auto
    group 2 auto
    group 5 auto
    group 3 auto
    group 4 auto
layeredimage cake:
    group base auto
    group filling auto:
        attribute none default
    group topping auto
layeredimage ml:
    group base auto
    group filling auto:
        attribute none default
    group topping auto
layeredimage tard:
    group base auto
    group filling auto:
        attribute none default
    group topping auto
layeredimage topping:
    group base auto
layeredimage filling:
    group base auto
image cg_barashek:
    contains:
        "cg_barashek_3"
    contains:
        "cg_barashek_2"
        xalign 0.65
        yalign 0.65
        rotate 180
        linear 25 rotate 540
        rotate 180
        repeat
    contains:
        "cg_barashek_1"
        xalign 0.65
        yalign 0.65
        rotate 180
        linear 20 rotate 540
        rotate 180
        repeat
    contains:
        "cg_barashek_4"
image doing_it:
    contains:
        "do_this"
        alpha 1
        pause 4
        alpha 0
    contains:
        "do_this_unfocused"
        alpha 0
        pause 2
        linear 2 alpha 1
image cg_photo:
    contains:
        "mainmenu_sky"
    contains:
        "cg_all_2_1"
image game_progress_d1:
    contains:
        "the"
        size (900, 950)
        xalign .5
    contains:
        "e"
        align (e_x,e_y)
    contains:
        "book2"
        align (book_x,book_y)
    contains:
        "numbers"
        align (numbers_x,numbers_y)
    contains:
        "note"
        align (note_x,note_y)
    contains:
        "cup"
        align (cup_x,cup_y)
    contains:
        "heart"
        align (heart_x,heart_y)
image arch_intro_p:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_g_baw:
    contains:
        baw("/bg/arch_intro/back.jpg")
    contains:
        baw("/bg/arch_intro/rays.png")
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        baw("/bg/arch_intro/rays.png")
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        baw("/bg/arch_intro/arch_g.png")
    contains:
        baw("/bg/arch_intro/light_g.png")
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_p_baw:
    contains:
        baw("/bg/arch_intro/back.jpg")
    contains:
        baw("/bg/arch_intro/rays.png")
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        baw("/bg/arch_intro/rays.png")
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        baw("/bg/arch_intro/arch_p.png")
    contains:
        baw("/bg/arch_intro/light_p.png")
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat

image arch_intro_o:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_b:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        "/bg/arch_intro/arch_b.png"
    contains:
        "/bg/arch_intro/light_b.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_g:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        "/bg/arch_intro/arch_g.png"
    contains:
        "/bg/arch_intro/light_g.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_g1:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        alpha .5 zoom 1
    contains:
        "/bg/arch_intro/arch_g.png"
    contains:
        "/bg/arch_intro/light_g.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_p1:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        alpha .5 zoom 1
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_b1:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        alpha .5 zoom 1
    contains:
        "/bg/arch_intro/arch_b.png"
    contains:
        "/bg/arch_intro/light_b.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_o1:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        alpha .5 zoom 1
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat

image arch_intro_t_m:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
    contains:
        "/CHR/teya2/teya2_clothes_regularhand1.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_1_1b.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_2_2a.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_3_3a.png"
        ypos 140
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_b.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_b.png"
        xpos 1920
    contains:
        "/CHR/marta3/marta3_clothes_regular1.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_1_1a.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_2_2c.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_3_3a.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_blush_blush.png"
        ypos 180
        xalign .5
        xpos 2880
image arch_outtro_t_m:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
    contains:
        "/CHR/teya1/teya1_clothes_fancy.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya1/teya1_1_1a.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya1/teya1_2_2a.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya1/teya1_3_3a.png"
        ypos 140
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_b.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_b.png"
        xpos 1920
    contains:
        "/CHR/marta3/marta3_clothes_regular1.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_1_1a.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_2_2c.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_3_3a.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta3/marta3_blush_blush.png"
        ypos 180
        xalign .5
        xpos 2880
image arch_intro_m_s:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_b.png"
    contains:
        "/bg/arch_intro/light_b.png"
    contains:
        "/CHR/marta1/marta1_clothes_regular1.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta1/marta1_1_1g.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta1/marta1_2_2a.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta1/marta1_3_3b.png"
        ypos 180
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_o.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_o.png"
        xpos 1920
    contains:
        "/CHR/sima2/sima2_clothes_regular1.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_1_1e.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_2_2a.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_3_3a.png"
        ypos 55
        xalign .5
        xpos 2880
image arch_outtro_m_s:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_b.png"
    contains:
        "/bg/arch_intro/light_b.png"
    contains:
        "/CHR/marta3/marta3_clothes_regular1.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta3/marta3_1_1a.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta3/marta3_2_2c.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta3/marta3_3_3a.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta3/marta3_blush_blush.png"
        ypos 180
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_o.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_o.png"
        xpos 1920
    contains:
        "/CHR/sima2/sima2_clothes_regular1.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_1_1e.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_2_2a.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_3_3a.png"
        ypos 55
        xalign .5
        xpos 2880
image arch_intro_s_n:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
    contains:
        "/CHR/sima3b/sima3b_clothes_regular.png"
        ypos 65
        xalign .5
    contains:
        "/CHR/sima3b/sima3b_1_1e.png"
        ypos 65
        xalign .5
    contains:
        "/CHR/sima3b/sima3b_2_2c.png"
        ypos 65
        xalign .5
    contains:
        "/CHR/sima3b/sima3b_3_3d.png"
        ypos 65
        xalign .5
    contains:
        "/CHR/sima3b/sima3b_blush_blush.png"
        ypos 65
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_g.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_g.png"
        xpos 1920
    contains:
        "/CHR/nana3/nana3_clothes_regular.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_1_1a.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_2_2a.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_3_3d.png"
        ypos 322
        xalign .5
        xpos 2880
image arch_outtro_s_n:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
    contains:
        "/CHR/sima2/sima2_clothes_regular1.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_1_1e.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_2_2a.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_3_3a.png"
        ypos 55
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_g.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_g.png"
        xpos 1920
    contains:
        "/CHR/nana3/nana3_clothes_regular.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_1_1a.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_2_2a.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana3/nana3_3_3d.png"
        ypos 322
        xalign .5
        xpos 2880
image arch_intro_n_t:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_g.png"
    contains:
        "/bg/arch_intro/light_g.png"
    contains:
        "/CHR/nana1/nana1_clothes_regular1.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_1_1a.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_2_2b.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_3_3a.png"
        ypos 322
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_p.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_p.png"
        xpos 1920
    contains:
        "/CHR/teya2/teya2_clothes_regularhand3.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_2_2a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_1_1a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_3_3a.png"
        ypos 140
        xalign .5
        xpos 2880
image arch_outtro_n_t:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_g.png"
    contains:
        "/bg/arch_intro/light_g.png"
    contains:
        "/CHR/nana3/nana3_clothes_regular.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana3/nana3_1_1a.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana3/nana3_2_2a.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana3/nana3_3_3d.png"
        ypos 322
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_p.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_p.png"
        xpos 1920
    contains:
        "/CHR/teya1/teya1_clothes_fancy.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya1/teya1_2_2a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya1/teya1_1_1a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya1/teya1_3_3a.png"
        ypos 140
        xalign .5
        xpos 2880
image arch_outtro_t_clo:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
    contains:
        "/CHR/teya2/teya2_clothes_fancyhand2.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_1_1e.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_2_2a.png"
        ypos 140
        xalign .5
    contains:
        "/CHR/teya2/teya2_3_3a.png"
        ypos 140
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_g.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_g.png"
        xpos 1920
    contains:
        "/CHR/nana1/nana1_clothes_true.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana1/nana1_1_1b.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana1/nana1_2_2a.png"
        ypos 322
        xalign .5
        xpos 2880
    contains:
        "/CHR/nana1/nana1_3_3a.png"
        ypos 322
        xalign .5
        xpos 2880
image arch_outtro_clo_lac:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_g.png"
    contains:
        "/bg/arch_intro/light_g.png"
    contains:
        "/CHR/nana1/nana1_clothes_true.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_1_1b.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_2_2a.png"
        ypos 322
        xalign .5
    contains:
        "/CHR/nana1/nana1_3_3a.png"
        ypos 322
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_o.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_o.png"
        xpos 1920
    contains:
        "/CHR/sima2/sima2_clothes_true.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_1_1e.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_2_2a.png"
        ypos 55
        xalign .5
        xpos 2880
    contains:
        "/CHR/sima2/sima2_3_3a.png"
        ypos 55
        xalign .5
        xpos 2880
image arch_outtro_lac_ant:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
    contains:
        "/CHR/sima2/sima2_clothes_true.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_1_1e.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_2_2a.png"
        ypos 55
        xalign .5
    contains:
        "/CHR/sima2/sima2_3_3a.png"
        ypos 55
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_b.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_b.png"
        xpos 1920
    contains:
        "/CHR/marta2/marta2_clothes_true.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta2/marta2_1_1g.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta2/marta2_2_2a.png"
        ypos 180
        xalign .5
        xpos 2880
    contains:
        "/CHR/marta2/marta2_3_3a.png"
        ypos 180
        xalign .5
        xpos 2880
image arch_outtro_ant_t:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/arch_b.png"
    contains:
        "/bg/arch_intro/light_b.png"
    contains:
        "/CHR/marta2/marta2_clothes_true.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta2/marta2_1_1a.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta2/marta2_2_2a.png"
        ypos 180
        xalign .5
    contains:
        "/CHR/marta2/marta2_3_3a.png"
        ypos 180
        xalign .5
    contains:
        "/bg/arch_intro/back.jpg"
        xpos 1920
    contains:
        "/bg/arch_intro/arch_p.png"
        xpos 1920
    contains:
        "/bg/arch_intro/light_p.png"
        xpos 1920
    contains:
        "/CHR/teya2/teya2_clothes_fancyhand4.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_1_1a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_2_2a.png"
        ypos 140
        xalign .5
        xpos 2880
    contains:
        "/CHR/teya2/teya2_3_3a.png"
        ypos 140
        xalign .5
        xpos 2880
image cg_meditation:
    contains:
        "meditation_back"
        subpixel True
        yalign 1.0
        xpos 0
        linear 8 xpos -950
    contains:
        "meditation1"
        subpixel True
        yalign 1.0
        xpos -100
        linear 8 xpos -2380
    contains:
        "meditation2b"
        subpixel True
        yalign 1.0
        xpos -100
        linear 8 xpos -2380
image cg_teya_intro_whoops2:
    contains:
        "arch_intro_p"
        xpos 0
    contains:
        "teya_intro_whoops2"
image cg_teya_intro_whoops:
    contains:
        Solid("000000")
        xpos 0
    contains:
        "arch_intro_p"
        xpos 0
        alpha 0
        pause .3
        linear .3 alpha 1
image cg_marta_phony:
    contains:
        "/bg/arch_intro/arch_b.png"
        zoom 4
        xalign .5
        yalign .5
    contains:
        "/bg/arch_intro/light_b.png"
        zoom 4
        xalign .5
        yalign .5
        block:
            alpha 0
            linear .5 alpha .6
            linear .5 alpha .8
            linear 1 alpha .5
            linear .5 alpha .6
            linear .5 alpha .9
            linear 1 alpha .5
            linear 1 alpha 0
            repeat
    contains:
        "marta_phony"
        xpos 1190
image cg_teya_intro_you_see_back:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
    contains:
        "/bg/arch_intro/arch_p.png"
        xpos -1650
        ypos -450
        zoom 1.85
    contains:
        "/bg/arch_intro/light_p.png"
        xpos -1650
        ypos -450
        zoom 1.85
        block:
            alpha 0
            linear .5 alpha .6
            linear .5 alpha .8
            linear 1 alpha .5
            linear .5 alpha .6
            linear .5 alpha .9
            linear 1 alpha .5
            linear 1 alpha 0
            repeat
image cg_teya_intro_you_see:
    contains:
        "cg_teya_intro_you_see_back"
    contains:
        "teya_intro_you_see"
        xpos -630
image cg_teya_outtro_you_see:
    contains:
        "cg_teya_intro_you_see_back"
    contains:
        "teya_outtro_you_see"
        xpos -630
image cg_teya_intro_you_not:
    contains:
        "cg_teya_intro_you_see_back"
    contains:
        "teya_intro_you_not"
        xpos -630
image sima_right:
    contains:
        "/CHR/sima3b/date/sima3bdate_clothes_regular.png"
    contains:
        "/CHR/sima3b/date/sima3bdate_1_1e.png"
    contains:
        "/CHR/sima3b/date/sima3bdate_2_2a.png"
    contains:
        "/CHR/sima3b/date/sima3bdate_3_3d.png"
    xalign .5
image cg_sima_right:
    contains:
        "/bg/arch_intro/arch_o.png"
        zoom 4
        xalign .5
        yalign .5
    contains:
        "/bg/arch_intro/light_o.png"
        zoom 4
        xalign .5
        yalign .5
        block:
            alpha 0
            linear .5 alpha .6
            linear .5 alpha .8
            linear 1 alpha .5
            linear .5 alpha .6
            linear .5 alpha .9
            linear 1 alpha .5
            linear 1 alpha 0
            repeat
    contains:
        "sima_right"
        xpos 1380
        ypos -100
image arch_empty:
    contains:
        "/bg/arch_intro/back.jpg"
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        linear .5 alpha .5 zoom 1.1
        linear .5 alpha 1 zoom 1.2
        linear 2 alpha .5 zoom 1.6
        linear 2 alpha 0 zoom 2
        repeat
    contains:
        "/bg/arch_intro/rays.png"
        size (1920, 1080)
        xalign .5
        yalign .5
        alpha 0 zoom 1
        pause 2.5
        block:
            alpha 0 zoom 1
            linear .5 alpha .5 zoom 1.1
            linear .5 alpha 1 zoom 1.2
            linear 2 alpha .5 zoom 1.6
            linear 2 alpha 0 zoom 2
            repeat
image cg_the:
    contains:
        "the"
        xalign .1
    contains:
        "the_the"
        ypos -50
        xalign .085
image cg_the_end:
    contains:
        "the"
        xalign .1
    contains:
        "the_the"
        ypos -50
        xalign .085
    contains:
        "the_the_end"
        ypos -50
        xalign .085
        alpha 0
        pause 2
        linear .5 alpha 1

image arch_nonf:
    contains:
        "arch_nf2"
        alpha 1
    contains:
        "arch_nf"
        alpha 0
        linear .5 alpha 1
        pause 0.6
        linear .5 alpha 0
image room_switch:
    contains:
        "jp_classroom_day"
        size (1920, 1080)
        linear .5 alpha 0
    contains:
        "jp_classroom_day2"
        size (1920, 1080)
        alpha 0
        linear .75 alpha 1
image noise_outtro:
    contains:
        "noise1"
        size (1920, 1080)
        block:
            alpha .05
            linear .5 alpha 0
            linear .5 alpha .1
            repeat
        block:
            xpos 0
            pause .05
            linear 1.25 xpos 48
            linear 1.25 xpos 0
            repeat
    contains:
        "noise2"
        size (1920, 1080)
        block:
            alpha .025
            linear .5 alpha 0
            linear .5 alpha 0.05
            repeat
        block:
            pause .1
            linear 1.25 xpos 48
            linear 1.25 xpos 0
            repeat
    contains:
        "noise1"
        size (1920, 1080)
        block:
            alpha .05
            linear .5 alpha 0
            linear .5 alpha .1
            repeat
        block:
            xpos 0
            pause .15
            linear 1.25 ypos 27
            linear 1.25 ypos 0
            repeat
    contains:
        "noise2"
        size (1920, 1080)
        block:
            alpha .025
            linear .5 alpha 0
            linear .5 alpha .05
            repeat
        block:
            pause .2
            linear 1.25 ypos 27
            linear 1.25 ypos 0
            repeat
image noise:
    contains:
        "noise1"
        size (1920, 1080)
        alpha .6
        xpos 0
        pause .05
        linear 1.25 xpos 192
    contains:
        "noise2"
        size (1920, 1080)
        alpha .3
        pause .1
        linear 1.25 xpos 192
    contains:
        "noise1"
        size (1920, 1080)
        alpha .3
        xpos 0
        pause .15
        linear 1.25 ypos 108
    contains:
        "noise2"
        size (1920, 1080)
        alpha .15
        pause .2
        linear 1.25 ypos 108
image noise_sleep:
    contains:
        "noise1"
        size (2880, 1620)
        alpha .6
        xpos -288
        pause .05
        linear 2 xpos -384
    contains:
        "noise2"
        size (2880, 1620)
        alpha .3
        xpos -288
        pause .1
        linear 2 xpos -384
    contains:
        "noise1"
        size (2880, 1620)
        alpha .3
        ypos -162
        pause .15
        linear 2 ypos -324
    contains:
        "noise2"
        size (2880, 1620)
        alpha .15
        ypos -162
        pause .2
        linear 2 ypos -324
image music_room_rain_animation:
    subpixel True
    contains:
        "MR_sky"
    contains:
        "MR_rain"
        yalign 1.0 xalign 0.0
        linear 0.4 yalign 0.0
        repeat
    contains:
        "MR_room"
image jp_classroom_matrix_animation:
    subpixel True
    contains:
        "JPCR_back"
    contains:
        "JPCR_matrix"
        yalign 1.0 xalign 0.0
        linear 45 yalign 0.0
        repeat
    contains:
        "JPCR_room"
image jp_classroom_matrix_animation_nf:
    subpixel True
    contains:
        "JPCR_back_nf"
    contains:
        "JPCR_matrix"
        yalign 1.0 xalign 0.0
        linear 45 yalign 0.0
        repeat
    contains:
        "JPCR_room_nf"
image the_future:
    contains:
        "/images/bg/ru_classroom_day.jpg"
    contains:
        "/images/bg/ru_classroom_night.jpg"
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/sima2/sima2_clothes_regular1.png"
        ypos 55
        xalign .167
    contains:
        runight("/images/chr/sima2/sima2_clothes_regular1.png")
        ypos 55
        xalign .167
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/sima2/sima2_1_1d.png"
        ypos 55
        xalign .167
    contains:
        runight("/images/chr/sima2/sima2_1_1d.png")
        ypos 55
        xalign .167
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/sima2/sima2_2_2c.png"
        ypos 55
        xalign .167
    contains:
        runight("/images/chr/sima2/sima2_2_2c.png")
        ypos 55
        xalign .167
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/sima2/sima2_3_3c.png"
        ypos 55
        xalign .167
    contains:
        runight("/images/chr/sima2/sima2_3_3c.png")
        ypos 55
        xalign .167
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/marta3/marta3_clothes_regular1.png"
        ypos 222
        xalign .5
        zoom 0.98
    contains:
        runight("/images/chr/marta3/marta3_clothes_regular1.png")
        ypos 222
        xalign .5
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/marta3/marta3_1_1f.png"
        ypos 222
        xalign .5
        zoom 0.98
    contains:
        runight("/images/chr/marta3/marta3_1_1f.png")
        ypos 222
        xalign .5
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/marta3/marta3_2_2c.png"
        ypos 222
        xalign .5
        zoom 0.98
    contains:
        runight("/images/chr/marta3/marta3_2_2c.png")
        ypos 222
        xalign .5
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/marta3/marta3_3_3c.png"
        ypos 222
        xalign .5
        zoom 0.98
    contains:
        runight("/images/chr/marta3/marta3_3_3c.png")
        ypos 222
        xalign .5
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/nana1/nana1_clothes_regular2.png"
        ypos 360
        xalign .815
        zoom 0.98
    contains:
        runight("/images/chr/nana1/nana1_clothes_regular2.png")
        ypos 360
        xalign .815
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/nana1/nana1_1_1a.png"
        ypos 360
        xalign .815
        zoom 0.98
    contains:
        runight("/images/chr/nana1/nana1_1_1a.png")
        ypos 360
        xalign .815
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/nana1/nana1_2_2c.png"
        ypos 360
        xalign .815
        zoom 0.98
    contains:
        runight("/images/chr/nana1/nana1_2_2c.png")
        ypos 360
        xalign .815
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat
    contains:
        "/images/chr/nana1/nana1_3_3c.png"
        ypos 360
        xalign .815
        zoom 0.98
    contains:
        runight("/images/chr/nana1/nana1_3_3c.png")
        ypos 360
        xalign .815
        zoom 0.98
        block:
            alpha 0
            pause .35
            linear .4 alpha 1
            pause .35
            linear .4 alpha 0
            repeat

image cg_marta_6_a:
    contains:
        "cg_marta_6_3"
        ypos -840
        linear 6 ypos 0
    contains:
        "cg_marta_6_1"
        ypos -840
        linear 6 ypos 0
image cg_marta_6_b:
    contains:
        "cg_marta_6_3"
        ypos 0
    contains:
        "cg_marta_6_2"
        ypos 0
image arch_intro_p2:
    contains:
        "/bg/arch_intro/arch_p.png"
    contains:
        "/bg/arch_intro/light_p.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
image arch_intro_o2:
    contains:
        "/bg/arch_intro/arch_o.png"
    contains:
        "/bg/arch_intro/light_o.png"
        alpha 0
        linear .5 alpha .6
        linear .5 alpha .8
        linear 1 alpha .5
        linear .5 alpha .6
        linear .5 alpha .9
        linear 1 alpha .5
        linear 1 alpha 0
        repeat
define pos11 = 0.5
define pos21 = 0.33
define pos22 = 0.67
define pos31 = 0.25
define pos32 = 0.5
define pos33 = 0.75
define pos41 = 0.15
define pos42 = 0.383
define pos43 = 0.617
define pos44 = 0.85
define wpos11 = 0.5
define wpos21 = 0.33
define wpos22 = 0.67
define wpos31 = 0.2
define wpos32 = 0.5
define wpos33 = 0.8
define wpos41 = 0.15
define wpos42 = 0.383
define wpos43 = 0.617
define wpos44 = 0.85
init:
    $ p11 = Position(xpos=pos11)
init:
    $ p21 = Position(xpos=pos21)
init:
    $ p22 = Position(xpos=pos22)
init:
    $ p31 = Position(xpos=pos31)
init:
    $ p32 = Position(xpos=pos32)
init:
    $ p33 = Position(xpos=pos33)
init:
    $ p41 = Position(xpos=pos41)
init:
    $ p42 = Position(xpos=pos42)
init:
    $ p43 = Position(xpos=pos43)
init:
    $ p44 = Position(xpos=pos44)
transform up_general(xp=0.5, z=1):
    yanchor 1.0 subpixel True
    on show:
        zoom z*0.95 alpha 0.00
        xcenter xp yoffset 10
        easein .25 yoffset -10 zoom z alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom z xcenter xp
        parallel:
            easein .15 yoffset -10
transform down_general(xp=0.5, z=1):
    yanchor 1.0 subpixel True
    on show:
        zoom z alpha 0.00
        xcenter xp yoffset -10
        easein .25 yoffset 10 zoom z*0.98 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom z*0.98 xcenter xp
        parallel:
            easein .15 yoffset 10
transform down_instant(xp=0.5, z=1):
    yanchor 1.0 subpixel True
    on show:
        zoom 0.98
        xcenter xp yoffset 10
    on replace:
        alpha 1.00
        zoom z*0.98 xcenter xp yoffset 10
transform up_instant(xp=0.5, z=1):
    yanchor 1.0 subpixel True
    on show:
        zoom z alpha 1.00
        xcenter xp yoffset -10
    on replace:
        alpha 1.00
        zoom z xcenter xp yoffset -10
transform u11:
    up_general(pos11)
transform u21:
    up_general(pos21)
transform u22:
    up_general(pos22)
transform u31:
    up_general(pos31)
transform u32:
    up_general(pos32)
transform u33:
    up_general(pos33)
transform u41:
    up_general(pos41)
transform u42:
    up_general(pos42)
transform u43:
    up_general(pos43)
transform u44:
    up_general(pos44)
transform d11:
    down_general(pos11)
transform d21:
    down_general(pos21)
transform d22:
    down_general(pos22)
transform d31:
    down_general(pos31)
transform d32:
    down_general(pos32)
transform d33:
    down_general(pos33)
transform d41:
    down_general(pos41)
transform d42:
    down_general(pos42)
transform d43:
    down_general(pos43)
transform d44:
    down_general(pos44)
transform di11:
    down_instant(pos11)
transform di21:
    down_instant(pos21)
transform di22:
    down_instant(pos22)
transform di31:
    down_instant(pos31)
transform di32:
    down_instant(pos32)
transform di33:
    down_instant(pos33)
transform di41:
    down_instant(pos41)
transform di42:
    down_instant(pos42)
transform di43:
    down_instant(pos43)
transform di44:
    down_instant(pos44)
transform ui11:
    up_instant(pos11)
transform ui21:
    up_instant(pos21)
transform ui22:
    up_instant(pos22)
transform ui31:
    up_instant(pos31)
transform ui32:
    up_instant(pos32)
transform ui33:
    up_instant(pos33)
transform ui41:
    up_instant(pos41)
transform ui42:
    up_instant(pos42)
transform ui43:
    up_instant(pos43)
transform ui44:
    up_instant(pos44)

init python:
    def baw(name_expr):
        return im.MatrixColor(name_expr,im.matrix.saturation(0.0))

init python:
    def Darken(name_expr):
        return im.MatrixColor(name_expr,im.matrix.tint(.9,.9,.95)*im.matrix.brightness(-0.01))
init python:
    def rain(name_expr):
       return im.MatrixColor(name_expr,im.matrix.brightness(-0.02))
init python:
    def redtint(name_expr):
        return im.MatrixColor(name_expr,im.matrix.tint(.9,.8,.8)*im.matrix.brightness(0.01))
init python:
    def runight(name_expr):
        return im.MatrixColor(name_expr,im.matrix.tint(.99,.95,.95)*im.matrix.brightness(-0.02))
init python:
    def grey(name_expr):
       return im.MatrixColor(name_expr,im.matrix.contrast(.85)*im.matrix.brightness(-0.02))
init python:
    def boring(name_expr):
       return im.MatrixColor(name_expr,im.matrix.contrast(.75)*im.matrix.brightness(-0.04))

layeredimage ermy1_boring:
        group clothes:
            attribute pose1 default:
                boring("/CHR/ermy/ermy1_pose_pose1.png")

            attribute pose2:
                boring("/CHR/ermy/ermy1_pose_pose2.png")

        group blush:
            attribute noblush default:
                "null_image"

            attribute blush:
                boring("/CHR/ermy/ermy1_blush_blush.png")

        group 1 auto:
            attribute 1a default:
                boring("/CHR/ermy/ermy1_1_1a.png")

            attribute 1b:
                boring("/CHR/ermy/ermy1_1_1b.png")

            attribute 1c:
                boring("/CHR/ermy/ermy1_1_1c.png")

            attribute 1d:
                boring("/CHR/ermy/ermy1_1_1d.png")

            attribute 1e:
                boring("/CHR/ermy/ermy1_1_1e.png")

            attribute 1f:
                boring("/CHR/ermy/ermy1_1_1f.png")

            attribute 1g:
                boring("/CHR/ermy/ermy1_1_1g.png")

            attribute 1h:
                boring("/CHR/ermy/ermy1_1_1h.png")

        group 2 auto:
            attribute 2a default:
                boring("/CHR/ermy/ermy1_2_2a.png")

            attribute 2b:
                boring("/CHR/ermy/ermy1_2_2b.png")

            attribute 2c:
                boring("/CHR/ermy/ermy1_2_2c.png")

            attribute 2d:
                boring("/CHR/ermy/ermy1_2_2d.png")

        group 3 auto:
            attribute 3a default:
                boring("/CHR/ermy/ermy1_3_3a.png")

            attribute 3b:
                boring("/CHR/ermy/ermy1_3_3b.png")

            attribute 3c:
                boring("/CHR/ermy/ermy1_3_3c.png")

            attribute 3d:
                boring("/CHR/ermy/ermy1_3_3d.png")

        ypos 1270
layeredimage nrs:
    always:
        "/CHR/nrs/body.png"
    group emo:
        attribute s default:
            "/CHR/nrs/sad.png"
        attribute h:
            "/CHR/nrs/happy.png"
        attribute sp:
            "/CHR/nrs/speaking.png"
    ypos 1130
layeredimage nrsredtint:
    always:
        redtint("/CHR/nrs/body.png")
    group emo:
        attribute s default:
            redtint("/CHR/nrs/sad.png")
        attribute h:
            redtint("/CHR/nrs/happy.png")
        attribute sp:
            redtint("/CHR/nrs/speaking.png")
    ypos 1130
layeredimage md:
    always:
        "/CHR/md/base.png"
    group emo:
        attribute d default:
            "/CHR/md/default.png"
        attribute h:
            "/CHR/md/happy.png"
        attribute he:
            "/CHR/md/hesitant.png"
        attribute p:
            "/CHR/md/pensive.png"
    ypos 1190
layeredimage mdredtint:
    always:
        redtint("/CHR/md/base.png")
    group emo:
        attribute d default:
            redtint("/CHR/md/default.png")
        attribute h:
            redtint("/CHR/md/happy.png")
        attribute he:
            redtint("/CHR/md/hesitant.png")
        attribute p:
            redtint("/CHR/md/pensive.png")
    ypos 1190
layeredimage tsndr:
    always:
        "/CHR/tsndr/body.png"
    group emo:
        attribute d default:
            "/CHR/tsndr/default.png"
        attribute h:
            "/CHR/tsndr/happy.png"
        attribute f:
            "/CHR/tsndr/flustered.png"
        attribute p:
            "/CHR/tsndr/pout.png"
        attribute fp:
            "/CHR/tsndr/fpout.png"
    ypos 1200
layeredimage tsndrredtint:
    always:
        redtint("/CHR/tsndr/body.png")
    group emo:
        attribute d default:
            redtint("/CHR/tsndr/default.png")
        attribute h:
            redtint("/CHR/tsndr/happy.png")
        attribute f:
            redtint("/CHR/tsndr/flustered.png")
        attribute p:
            redtint("/CHR/tsndr/pout.png")
        attribute fp:
            redtint("/CHR/tsndr/fpout.png")
    ypos 1200
layeredimage nana1:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1250
layeredimage nana1date:
    group clothes auto:
        attribute fancy1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2550
layeredimage nana1close:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage nana2:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1250
layeredimage nana2close:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage nana2date:
    group clothes auto:
        attribute fancy default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2550

layeredimage nana3:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1250
layeredimage nana3close:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage nana3date:
    group clothes auto:
        attribute fancy default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2550
layeredimage marta1:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1270
layeredimage marta1close:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1470
layeredimage marta1date:
    group clothes auto:
        attribute fancy1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2450
layeredimage marta2:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1270
layeredimage marta2close:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1470
layeredimage marta2date:
    group clothes auto:
        attribute fancy1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2450

layeredimage marta3:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1270
layeredimage marta3close:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1460
layeredimage marta3date:
    group clothes auto:
        attribute fancy1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2450
layeredimage sima1:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1240
layeredimage sima1close:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1475
layeredimage sima1date:
    group clothes auto:
        attribute fancy default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2400
layeredimage sima2date:
    group clothes auto:
        attribute fancy1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2400
layeredimage sima2fullscale:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
layeredimage sima2:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default

    group 3 auto:
        attribute 3a default

    ypos 1220
layeredimage sima2close:
    group clothes auto:
        attribute regular1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1445
layeredimage sima3a:
    group clothes auto:
        attribute regular default

    group blush auto:
        attribute noblush:
            "null_image"

    group 1 auto:
        attribute 1a default

    group 2 auto:
        attribute 2a default

    group 3 auto:
        attribute 3a default

    ypos 1230
layeredimage sima3adate:
    group clothes auto:
        attribute regular default

    group blush auto:
        attribute noblush:
            "null_image"

    group 1 auto:
        attribute 1a default

    group 2 auto:
        attribute 2a default

    group 3 auto:
        attribute 3a default

    ypos 2400
layeredimage sima3aclose:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1485
layeredimage sima3b:
    group clothes auto:
        attribute regular default

    group blush auto:
        attribute noblush:
            "null_image"

    group 1 auto:
        attribute 1a default

    group 2 auto:
        attribute 2a default

    group 3 auto:
        attribute 3a default

    ypos 1230
layeredimage sima3bclose:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1485
layeredimage sima3bdate:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 2400
layeredimage teya1:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1230
layeredimage teya1close:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage teya2:
    group clothes auto:
        attribute regularhand1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1230
layeredimage teya2fullscale:
    group clothes auto:
        attribute regularhand1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
layeredimage teya2close:
    group clothes auto:
        attribute regularhand1 default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage teya3:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1230
layeredimage teya3close:
    group clothes auto:
        attribute regular default
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1400
layeredimage ermy1:
    group pose auto
    group blush auto:
        attribute noblush:
            "null_image"
    group 1 auto:
        attribute 1a default
    group 2 auto:
        attribute 2a default
    group 3 auto:
        attribute 3a default
    ypos 1270
layeredimage nana3_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/nana3/close/nana3close_clothes_regular.png")
        attribute fancy:
            Darken("/CHR/nana3/close/nana3close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/nana3/close/nana3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/nana3/close/nana3close_1_1a.png")
        attribute 1b:
            Darken("/CHR/nana3/close/nana3close_1_1b.png")
        attribute 1c:
            Darken("/CHR/nana3/close/nana3close_1_1c.png")
        attribute 1d:
            Darken("/CHR/nana3/close/nana3close_1_1d.png")
        attribute 1e:
            Darken("/CHR/nana3/close/nana3close_1_1e.png")
        attribute 1f:
            Darken("/CHR/nana3/close/nana3close_1_1f.png")
        attribute 1g:
            Darken("/CHR/nana3/close/nana3close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/nana3/close/nana3close_2_2a.png")
        attribute 2b:
            Darken("/CHR/nana3/close/nana3close_2_2b.png")
        attribute 2c:
            Darken("/CHR/nana3/close/nana3close_2_2c.png")
        attribute 2d:
            Darken("/CHR/nana3/close/nana3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/nana3/close/nana3close_3_3a.png")
        attribute 3b:
            Darken("/CHR/nana3/close/nana3close_3_3b.png")
        attribute 3c:
            Darken("/CHR/nana3/close/nana3close_3_3c.png")
        attribute 3d:
            Darken("/CHR/nana3/close/nana3close_3_3d.png")
    ypos 1400
layeredimage nana2_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/nana2/close/nana2close_clothes_regular.png")
        attribute fancy:
            Darken("/CHR/nana2/close/nana2close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/nana2/close/nana2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/nana2/close/nana2close_1_1a.png")
        attribute 1b:
            Darken("/CHR/nana2/close/nana2close_1_1b.png")
        attribute 1c:
            Darken("/CHR/nana2/close/nana2close_1_1c.png")
        attribute 1d:
            Darken("/CHR/nana2/close/nana2close_1_1d.png")
        attribute 1e:
            Darken("/CHR/nana2/close/nana2close_1_1e.png")
        attribute 1f:
            Darken("/CHR/nana2/close/nana2close_1_1f.png")
        attribute 1g:
            Darken("/CHR/nana2/close/nana2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/nana2/close/nana2close_2_2a.png")
        attribute 2b:
            Darken("/CHR/nana2/close/nana2close_2_2b.png")
        attribute 2c:
            Darken("/CHR/nana2/close/nana2close_2_2c.png")
        attribute 2d:
            Darken("/CHR/nana2/close/nana2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/nana2/close/nana2close_3_3a.png")
        attribute 3b:
            Darken("/CHR/nana2/close/nana2close_3_3b.png")
        attribute 3c:
            Darken("/CHR/nana2/close/nana2close_3_3c.png")
        attribute 3d:
            Darken("/CHR/nana2/close/nana2close_3_3d.png")
    ypos 1400
layeredimage nana2date_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/nana2/date/nana2date_clothes_regular.png")
        attribute fancy:
            Darken("/CHR/nana2/date/nana2date_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/nana2/date/nana2date_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/nana2/date/nana2date_1_1a.png")
        attribute 1b:
            Darken("/CHR/nana2/date/nana2date_1_1b.png")
        attribute 1c:
            Darken("/CHR/nana2/date/nana2date_1_1c.png")
        attribute 1d:
            Darken("/CHR/nana2/date/nana2date_1_1d.png")
        attribute 1e:
            Darken("/CHR/nana2/date/nana2date_1_1e.png")
        attribute 1f:
            Darken("/CHR/nana2/date/nana2date_1_1f.png")
        attribute 1g:
            Darken("/CHR/nana2/date/nana2date_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/nana2/date/nana2date_2_2a.png")
        attribute 2b:
            Darken("/CHR/nana2/date/nana2date_2_2b.png")
        attribute 2c:
            Darken("/CHR/nana2/date/nana2date_2_2c.png")
        attribute 2d:
            Darken("/CHR/nana2/date/nana2date_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/nana2/date/nana2date_3_3a.png")
        attribute 3b:
            Darken("/CHR/nana2/date/nana2date_3_3b.png")
        attribute 3c:
            Darken("/CHR/nana2/date/nana2date_3_3c.png")
        attribute 3d:
            Darken("/CHR/nana2/date/nana2date_3_3d.png")
    ypos 2550
layeredimage nana1date_dark:
    group clothes:
        attribute regular2 default:
            Darken("/CHR/nana1/date/nana1date_clothes_regular2.png")
        attribute fancy2:
            Darken("/CHR/nana1/date/nana1date_clothes_fancy2.png")
        attribute regular1:
            Darken("/CHR/nana1/date/nana1date_clothes_regular1.png")
        attribute fancy1:
            Darken("/CHR/nana1/date/nana1date_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/nana1/date/nana1date_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/nana1/date/nana1date_1_1a.png")
        attribute 1b:
            Darken("/CHR/nana1/date/nana1date_1_1b.png")
        attribute 1c:
            Darken("/CHR/nana1/date/nana1date_1_1c.png")
        attribute 1d:
            Darken("/CHR/nana1/date/nana1date_1_1d.png")
        attribute 1e:
            Darken("/CHR/nana1/date/nana1date_1_1e.png")
        attribute 1f:
            Darken("/CHR/nana1/date/nana1date_1_1f.png")
        attribute 1g:
            Darken("/CHR/nana1/date/nana1date_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/nana1/date/nana1date_2_2a.png")
        attribute 2b:
            Darken("/CHR/nana1/date/nana1date_2_2b.png")
        attribute 2c:
            Darken("/CHR/nana1/date/nana1date_2_2c.png")
        attribute 2d:
            Darken("/CHR/nana1/date/nana1date_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/nana1/date/nana1date_3_3a.png")
        attribute 3b:
            Darken("/CHR/nana1/date/nana1date_3_3b.png")
        attribute 3c:
            Darken("/CHR/nana1/date/nana1date_3_3c.png")
        attribute 3d:
            Darken("/CHR/nana1/date/nana1_3_3d.png")
    ypos 2550
layeredimage nana1_dark:
    group clothes:
        attribute regular2 default:
            Darken("/CHR/nana1/close/nana1close_clothes_regular2.png")
        attribute fancy2:
            Darken("/CHR/nana1/close/nana1close_clothes_fancy2.png")
        attribute regular1:
            Darken("/CHR/nana1/close/nana1close_clothes_regular1.png")
        attribute fancy1:
            Darken("/CHR/nana1/close/nana1close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/nana1/close/nana1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/nana1/close/nana1close_1_1a.png")
        attribute 1b:
            Darken("/CHR/nana1/close/nana1close_1_1b.png")
        attribute 1c:
            Darken("/CHR/nana1/close/nana1close_1_1c.png")
        attribute 1d:
            Darken("/CHR/nana1/close/nana1close_1_1d.png")
        attribute 1e:
            Darken("/CHR/nana1/close/nana1close_1_1e.png")
        attribute 1f:
            Darken("/CHR/nana1/close/nana1close_1_1f.png")
        attribute 1g:
            Darken("/CHR/nana1/close/nana1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/nana1/close/nana1close_2_2a.png")
        attribute 2b:
            Darken("/CHR/nana1/close/nana1close_2_2b.png")
        attribute 2c:
            Darken("/CHR/nana1/close/nana1close_2_2c.png")
        attribute 2d:
            Darken("/CHR/nana1/close/nana1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/nana1/close/nana1close_3_3a.png")
        attribute 3b:
            Darken("/CHR/nana1/close/nana1close_3_3b.png")
        attribute 3c:
            Darken("/CHR/nana1/close/nana1close_3_3c.png")
        attribute 3d:
            Darken("/CHR/nana1/close/nana1close_3_3d.png")
    ypos 1400
layeredimage marta3_dark:
    group clothes:
        attribute regular2:
            Darken("/CHR/marta3/close/marta3close_clothes_regular2.png")
        attribute fancy2:
            Darken("/CHR/marta3/close/marta3close_clothes_fancy2.png")
        attribute regular1 default:
            Darken("/CHR/marta3/close/marta3close_clothes_regular1.png")
        attribute fancy1:
            Darken("/CHR/marta3/close/marta3close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/marta3/close/marta3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/marta3/close/marta3close_1_1a.png")
        attribute 1b:
            Darken("/CHR/marta3/close/marta3close_1_1b.png")
        attribute 1c:
            Darken("/CHR/marta3/close/marta3close_1_1c.png")
        attribute 1d:
            Darken("/CHR/marta3/close/marta3close_1_1d.png")
        attribute 1e:
            Darken("/CHR/marta3/close/marta3close_1_1e.png")
        attribute 1f:
            Darken("/CHR/marta3/close/marta3close_1_1f.png")
        attribute 1g:
            Darken("/CHR/marta3/close/marta3close_1_1g.png")
        attribute 1aa:
            Darken("/CHR/marta3/close/marta3close_1_1aa.png")
        attribute 1bb:
            Darken("/CHR/marta3/close/marta3close_1_1bb.png")
        attribute 1cc:
            Darken("/CHR/marta3/close/marta3close_1_1cc.png")
        attribute 1dd:
            Darken("/CHR/marta3/close/marta3close_1_1dd.png")
        attribute 1ee:
            Darken("/CHR/marta3/close/marta3close_1_1ee.png")
        attribute 1ff:
            Darken("/CHR/marta3/close/marta3close_1_1ff.png")
        attribute 1gg:
            Darken("/CHR/marta3/close/marta3close_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/marta3/close/marta3close_2_2a.png")
        attribute 2b:
            Darken("/CHR/marta3/close/marta3close_2_2b.png")
        attribute 2c:
            Darken("/CHR/marta3/close/marta3close_2_2c.png")
        attribute 2d:
            Darken("/CHR/marta3/close/marta3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/marta3/close/marta3close_3_3a.png")
        attribute 3b:
            Darken("/CHR/marta3/close/marta3close_3_3b.png")
        attribute 3c:
            Darken("/CHR/marta3/close/marta3close_3_3c.png")
        attribute 3d:
            Darken("/CHR/marta3/close/marta3close_3_3d.png")
    ypos 1460
layeredimage marta2_dark:
    group clothes:
        attribute regular1 default:
            Darken("/CHR/marta2/close/marta2close_clothes_regular1.png")
        attribute fancy1:
            Darken("/CHR/marta2/close/marta2close_clothes_fancy1.png")
        attribute regular2:
            Darken("/CHR/marta2/close/marta2close_clothes_regular2.png")
        attribute fancy2:
            Darken("/CHR/marta2/close/marta2close_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/marta2/close/marta2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/marta2/close/marta2close_1_1a.png")
        attribute 1b:
            Darken("/CHR/marta2/close/marta2close_1_1b.png")
        attribute 1c:
            Darken("/CHR/marta2/close/marta2close_1_1c.png")
        attribute 1d:
            Darken("/CHR/marta2/close/marta2close_1_1d.png")
        attribute 1e:
            Darken("/CHR/marta2/close/marta2close_1_1e.png")
        attribute 1f:
            Darken("/CHR/marta2/close/marta2close_1_1f.png")
        attribute 1g:
            Darken("/CHR/marta2/close/marta2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/marta2/close/marta2close_2_2a.png")
        attribute 2b:
            Darken("/CHR/marta2/close/marta2close_2_2b.png")
        attribute 2c:
            Darken("/CHR/marta2/close/marta2close_2_2c.png")
        attribute 2d:
            Darken("/CHR/marta2/close/marta2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/marta2/close/marta2close_3_3a.png")
        attribute 3b:
            Darken("/CHR/marta2/close/marta2close_3_3b.png")
        attribute 3c:
            Darken("/CHR/marta2/close/marta2close_3_3c.png")
        attribute 3d:
            Darken("/CHR/marta2/close/marta2close_3_3d.png")
    ypos 1470
layeredimage marta1_dark:
    group clothes:
        attribute regular2 default:
            Darken("/CHR/marta1/close/marta1close_clothes_regular1.png")
        attribute fancy2:
            Darken("/CHR/marta1/close/marta1close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/marta1/close/marta1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/marta1/close/marta1close_1_1a.png")
        attribute 1b:
            Darken("/CHR/marta1/close/marta1close_1_1b.png")
        attribute 1c:
            Darken("/CHR/marta1/close/marta1close_1_1c.png")
        attribute 1d:
            Darken("/CHR/marta1/close/marta1close_1_1d.png")
        attribute 1e:
            Darken("/CHR/marta1/close/marta1close_1_1e.png")
        attribute 1f:
            Darken("/CHR/marta1/close/marta1close_1_1f.png")
        attribute 1g:
            Darken("/CHR/marta1/close/marta1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/marta1/close/marta1close_2_2a.png")
        attribute 2b:
            Darken("/CHR/marta1/close/marta1close_2_2b.png")
        attribute 2c:
            Darken("/CHR/marta1/close/marta1close_2_2c.png")
        attribute 2d:
            Darken("/CHR/marta1/close/marta1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/marta1/close/marta1close_3_3a.png")
        attribute 3b:
            Darken("/CHR/marta1/close/marta1close_3_3b.png")
        attribute 3c:
            Darken("/CHR/marta1/close/marta1close_3_3c.png")
        attribute 3d:
            Darken("/CHR/marta1/close/marta1close_3_3d.png")
    ypos 1470
layeredimage sima1_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/sima1/close/sima1close_clothes_regular.png")

        attribute fancy:
            Darken("/CHR/sima1/close/sima1close_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            Darken("/CHR/sima1/close/sima1close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            Darken("/CHR/sima1/close/sima1close_1_1a.png")

        attribute 1c:
            Darken("/CHR/sima1/close/sima1close_1_1c.png")

        attribute 1d:
            Darken("/CHR/sima1/close/sima1close_1_1d.png")

        attribute 1e:
            Darken("/CHR/sima1/close/sima1close_1_1e.png")

        attribute 1g:
            Darken("/CHR/sima1/close/sima1close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            Darken("/CHR/sima1/close/sima1close_2_2a.png")

        attribute 2b:
            Darken("/CHR/sima1/close/sima1close_2_2b.png")

        attribute 2c:
            Darken("/CHR/sima1/close/sima1close_2_2c.png")

        attribute 2d:
            Darken("/CHR/sima1/close/sima1close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            Darken("/CHR/sima1/close/sima1close_3_3a.png")

        attribute 3b:
            Darken("/CHR/sima1/close/sima1close_3_3b.png")

        attribute 3c:
            Darken("/CHR/sima1/close/sima1close_3_3c.png")

        attribute 3d:
            Darken("/CHR/sima1/close/sima1close_3_3d.png")

    ypos 1475
layeredimage sima2_dark:
    group clothes:
        attribute regular1 default:
            Darken("/CHR/sima2/close/sima2close_clothes_regular1.png")

        attribute fancy1:
            Darken("/CHR/sima2/close/sima2close_clothes_fancy1.png")

        attribute regular2:
            Darken("/CHR/sima2/close/sima2close_clothes_regular2.png")

        attribute fancy2:
            Darken("/CHR/sima2/close/sima2close_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            Darken("/CHR/sima2/close/sima2close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            Darken("/CHR/sima2/close/sima2close_1_1a.png")

        attribute 1c:
            Darken("/CHR/sima2/close/sima2close_1_1c.png")

        attribute 1d:
            Darken("/CHR/sima2/close/sima2close_1_1d.png")

        attribute 1e:
            Darken("/CHR/sima2/close/sima2close_1_1e.png")

        attribute 1g:
            Darken("/CHR/sima2/close/sima2close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            Darken("/CHR/sima2/close/sima2close_2_2a.png")

        attribute 2b:
            Darken("/CHR/sima2/close/sima2close_2_2b.png")

        attribute 2c:
            Darken("/CHR/sima2/close/sima2close_2_2c.png")

        attribute 2d:
            Darken("/CHR/sima2/close/sima2close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            Darken("/CHR/sima2/close/sima2close_3_3a.png")

        attribute 3b:
            Darken("/CHR/sima2/close/sima2close_3_3b.png")

        attribute 3c:
            Darken("/CHR/sima2/close/sima2close_3_3c.png")

        attribute 3d:
            Darken("/CHR/sima2/close/sima2close_3_3d.png")

    ypos 1445
layeredimage sima3a_dark:
    group clothes:
        attribute regular2 default:
            Darken("/CHR/sima3a/close/sima3aclose_clothes_regular.png")

        attribute fancy2:
            Darken("/CHR/sima3a/close/sima3aclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            Darken("/CHR/sima3a/close/sima3aclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            Darken("/CHR/sima3a/close/sima3aclose_1_1a.png")

        attribute 1c:
            Darken("/CHR/sima3a/close/sima3aclose_1_1c.png")

        attribute 1d:
            Darken("/CHR/sima3a/close/sima3aclose_1_1d.png")

        attribute 1e:
            Darken("/CHR/sima3a/close/sima3aclose_1_1e.png")

        attribute 1g:
            Darken("/CHR/sima3a/close/sima3aclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            Darken("/CHR/sima3a/close/sima3aclose_2_2a.png")

        attribute 2b:
            Darken("/CHR/sima3a/close/sima3aclose_2_2b.png")

        attribute 2c:
            Darken("/CHR/sima3a/close/sima3aclose_2_2c.png")

        attribute 2d:
            Darken("/CHR/sima3a/close/sima3aclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            Darken("/CHR/sima3a/close/sima3aclose_3_3a.png")

        attribute 3b:
            Darken("/CHR/sima3a/close/sima3aclose_3_3b.png")

        attribute 3c:
            Darken("/CHR/sima3a/close/sima3aclose_3_3c.png")

        attribute 3d:
            Darken("/CHR/sima3a/close/sima3aclose_3_3d.png")

    ypos 1485
layeredimage sima3b_dark:
    group clothes:
        attribute regular2 default:
            Darken("/CHR/sima3b/close/sima3bclose_clothes_regular.png")

        attribute fancy2:
            Darken("/CHR/sima3b/close/sima3bclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            Darken("/CHR/sima3b/close/sima3bclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            Darken("/CHR/sima3b/close/sima3bclose_1_1a.png")

        attribute 1c:
            Darken("/CHR/sima3b/close/sima3bclose_1_1c.png")

        attribute 1d:
            Darken("/CHR/sima3b/close/sima3bclose_1_1d.png")

        attribute 1e:
            Darken("/CHR/sima3b/close/sima3bclose_1_1e.png")

        attribute 1g:
            Darken("/CHR/sima3b/close/sima3bclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            Darken("/CHR/sima3b/close/sima3bclose_2_2a.png")

        attribute 2b:
            Darken("/CHR/sima3b/close/sima3bclose_2_2b.png")

        attribute 2c:
            Darken("/CHR/sima3b/close/sima3bclose_2_2c.png")

        attribute 2d:
            Darken("/CHR/sima3b/close/sima3bclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            Darken("/CHR/sima3b/close/sima3bclose_3_3a.png")

        attribute 3b:
            Darken("/CHR/sima3b/close/sima3bclose_3_3b.png")

        attribute 3c:
            Darken("/CHR/sima3b/close/sima3bclose_3_3c.png")

        attribute 3d:
            Darken("/CHR/sima3b/close/sima3bclose_3_3d.png")

    ypos 1485
layeredimage ermy1_dark:
        group clothes:
            attribute pose1 default:
                Darken("/CHR/ermy/ermy1_pose_pose1.png")

            attribute pose2:
                Darken("/CHR/ermy/ermy1_pose_pose2.png")

        group blush:
            attribute noblush default:
                "null_image"

            attribute blush:
                Darken("/CHR/ermy/ermy1_blush_blush.png")

        group 1 auto:
            attribute 1a default:
                Darken("/CHR/ermy/ermy1_1_1a.png")

            attribute 1b:
                Darken("/CHR/ermy/ermy1_1_1b.png")

            attribute 1c:
                Darken("/CHR/ermy/ermy1_1_1c.png")

            attribute 1d:
                Darken("/CHR/ermy/ermy1_1_1d.png")

            attribute 1e:
                Darken("/CHR/ermy/ermy1_1_1e.png")

            attribute 1f:
                Darken("/CHR/ermy/ermy1_1_1f.png")

            attribute 1g:
                Darken("/CHR/ermy/ermy1_1_1g.png")

            attribute 1h:
                Darken("/CHR/ermy/ermy1_1_1h.png")

        group 2 auto:
            attribute 2a default:
                Darken("/CHR/ermy/ermy1_2_2a.png")

            attribute 2b:
                Darken("/CHR/ermy/ermy1_2_2b.png")

            attribute 2c:
                Darken("/CHR/ermy/ermy1_2_2c.png")

            attribute 2d:
                Darken("/CHR/ermy/ermy1_2_2d.png")

        group 3 auto:
            attribute 3a default:
                Darken("/CHR/ermy/ermy1_3_3a.png")

            attribute 3b:
                Darken("/CHR/ermy/ermy1_3_3b.png")

            attribute 3c:
                Darken("/CHR/ermy/ermy1_3_3c.png")

            attribute 3d:
                Darken("/CHR/ermy/ermy1_3_3d.png")

        ypos 1270
layeredimage teya1_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/teya1/teya1_clothes_regular.png")
        attribute fancy:
            Darken("/CHR/teya1/teya1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/sima1/sima1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/teya1/teya1_1_1a.png")
        attribute 1b:
            Darken("/CHR/teya1/teya1_1_1b.png")
        attribute 1c:
            Darken("/CHR/teya1/teya1_1_1c.png")
        attribute 1d:
            Darken("/CHR/teya1/teya1_1_1d.png")
        attribute 1e:
            Darken("/CHR/teya1/teya1_1_1e.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/teya1/teya1_2_2a.png")
        attribute 2b:
            Darken("/CHR/teya1/teya1_2_2b.png")
        attribute 2c:
            Darken("/CHR/teya1/teya1_2_2c.png")
        attribute 2d:
            Darken("/CHR/teya1/teya1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/teya1/teya1_3_3a.png")
        attribute 3b:
            Darken("/CHR/teya1/teya1_3_3b.png")
        attribute 3c:
            Darken("/CHR/teya1/teya1_3_3c.png")
        attribute 3d:
            Darken("/CHR/teya1/teya1_3_3d.png")
    ypos 1230
layeredimage teya2_dark:
    group clothes:
        attribute regularhand1 default:
            Darken("/CHR/teya2/teya2_clothes_regularhand1.png")
        attribute fancyhand1:
            Darken("/CHR/teya2/teya2_clothes_fancyhand1.png")
        attribute regularhand2:
            Darken("/CHR/teya2/teya2_clothes_regularhand2.png")
        attribute fancyhand2:
            Darken("/CHR/teya2/teya2_clothes_fancyhand2.png")
        attribute regularhand3:
            Darken("/CHR/teya2/teya2_clothes_regularhand3.png")
        attribute fancyhand3:
            Darken("/CHR/teya2/teya2_clothes_fancyhand3.png")
        attribute regularhand4:
            Darken("/CHR/teya2/teya2_clothes_regularhand4.png")
        attribute fancyhand4:
            Darken("/CHR/teya2/teya2_clothes_fancyhand4.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/teya2/teya2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/teya2/teya2_1_1a.png")
        attribute 1b:
            Darken("/CHR/teya2/teya2_1_1b.png")
        attribute 1c:
            Darken("/CHR/teya2/teya2_1_1c.png")
        attribute 1d:
            Darken("/CHR/teya2/teya2_1_1d.png")
        attribute 1e:
            Darken("/CHR/teya2/teya2_1_1e.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/teya2/teya2_2_2a.png")
        attribute 2b:
            Darken("/CHR/teya2/teya2_2_2b.png")
        attribute 2c:
            Darken("/CHR/teya2/teya2_2_2c.png")
        attribute 2d:
            Darken("/CHR/teya2/teya2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/teya2/teya2_3_3a.png")
        attribute 3b:
            Darken("/CHR/teya2/teya2_3_3b.png")
        attribute 3c:
            Darken("/CHR/teya2/teya2_3_3c.png")
        attribute 3d:
            Darken("/CHR/teya2/teya2_3_3d.png")
    ypos 1230
layeredimage teya3_dark:
    group clothes:
        attribute regular default:
            Darken("/CHR/teya3/teya3_clothes_regular.png")
        attribute fancy:
            Darken("/CHR/teya3/teya3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            Darken("/CHR/teya3/teya3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            Darken("/CHR/teya3/teya3_1_1a.png")
        attribute 1b:
            Darken("/CHR/teya3/teya3_1_1b.png")
        attribute 1c:
            Darken("/CHR/teya3/teya3_1_1c.png")
        attribute 1d:
            Darken("/CHR/teya3/teya3_1_1d.png")
        attribute 1e:
            Darken("/CHR/teya3/teya3_1_1e.png")
    group 2 auto:
        attribute 2a default:
            Darken("/CHR/teya3/teya3_2_2a.png")
        attribute 2b:
            Darken("/CHR/teya3/teya3_2_2b.png")
        attribute 2c:
            Darken("/CHR/teya3/teya3_2_2c.png")
        attribute 2d:
            Darken("/CHR/teya3/teya3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            Darken("/CHR/teya3/teya3_3_3a.png")
        attribute 3b:
            Darken("/CHR/teya3/teya3_3_3b.png")
        attribute 3c:
            Darken("/CHR/teya3/teya3_3_3c.png")
        attribute 3d:
            Darken("/CHR/teya3/teya3_3_3d.png")
    ypos 1230
layeredimage nana3_redtint:
    group clothes:
        attribute regular default:
            redtint("/CHR/nana3/close/nana3close_clothes_regular.png")
        attribute fancy:
            redtint("/CHR/nana3/close/nana3close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/nana3/nana3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/nana3/close/nana3close_1_1a.png")
        attribute 1b:
            redtint("/CHR/nana3/close/nana3close_1_1b.png")
        attribute 1c:
            redtint("/CHR/nana3/close/nana3close_1_1c.png")
        attribute 1d:
            redtint("/CHR/nana3/close/nana3close_1_1d.png")
        attribute 1e:
            redtint("/CHR/nana3/close/nana3close_1_1e.png")
        attribute 1f:
            redtint("/CHR/nana3/close/nana3close_1_1f.png")
        attribute 1g:
            redtint("/CHR/nana3/close/nana3close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/nana3/close/nana3close_2_2a.png")
        attribute 2b:
            redtint("/CHR/nana3/close/nana3close_2_2b.png")
        attribute 2c:
            redtint("/CHR/nana3/close/nana3close_2_2c.png")
        attribute 2d:
            redtint("/CHR/nana3/close/nana3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/nana3/close/nana3close_3_3a.png")
        attribute 3b:
            redtint("/CHR/nana3/close/nana3close_3_3b.png")
        attribute 3c:
            redtint("/CHR/nana3/close/nana3close_3_3c.png")
        attribute 3d:
            redtint("/CHR/nana3/close/nana3close_3_3d.png")
    ypos 1400
layeredimage nana3_ruclose:
    group clothes:
        attribute regular default:
            runight("/CHR/nana3/close/nana3close_clothes_regular.png")
        attribute fancy:
            runight("/CHR/nana3/close/nana3close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana3/nana3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana3/close/nana3close_1_1a.png")
        attribute 1b:
            runight("/CHR/nana3/close/nana3close_1_1b.png")
        attribute 1c:
            runight("/CHR/nana3/close/nana3close_1_1c.png")
        attribute 1d:
            runight("/CHR/nana3/close/nana3close_1_1d.png")
        attribute 1e:
            runight("/CHR/nana3/close/nana3close_1_1e.png")
        attribute 1f:
            runight("/CHR/nana3/close/nana3close_1_1f.png")
        attribute 1g:
            runight("/CHR/nana3/close/nana3close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana3/close/nana3close_2_2a.png")
        attribute 2b:
            runight("/CHR/nana3/close/nana3close_2_2b.png")
        attribute 2c:
            runight("/CHR/nana3/close/nana3close_2_2c.png")
        attribute 2d:
            runight("/CHR/nana3/close/nana3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana3/close/nana3close_3_3a.png")
        attribute 3b:
            runight("/CHR/nana3/close/nana3close_3_3b.png")
        attribute 3c:
            runight("/CHR/nana3/close/nana3close_3_3c.png")
        attribute 3d:
            runight("/CHR/nana3/close/nana3close_3_3d.png")
    ypos 1400
layeredimage nana2_ruclose:
    group clothes:
        attribute regular default:
            runight("/CHR/nana2/close/nana2close_clothes_regular.png")
        attribute fancy:
            runight("/CHR/nana2/close/nana2close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana2/close/nana2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana2/close/nana2close_1_1a.png")
        attribute 1b:
            runight("/CHR/nana2/close/nana2close_1_1b.png")
        attribute 1c:
            runight("/CHR/nana2/close/nana2close_1_1c.png")
        attribute 1d:
            runight("/CHR/nana2/close/nana2close_1_1d.png")
        attribute 1e:
            runight("/CHR/nana2/close/nana2close_1_1e.png")
        attribute 1f:
            runight("/CHR/nana2/close/nana2close_1_1f.png")
        attribute 1g:
            runight("/CHR/nana2/close/nana2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana2/close/nana2close_2_2a.png")
        attribute 2b:
            runight("/CHR/nana2/close/nana2close_2_2b.png")
        attribute 2c:
            runight("/CHR/nana2/close/nana2close_2_2c.png")
        attribute 2d:
            runight("/CHR/nana2/close/nana2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana2/close/nana2close_3_3a.png")
        attribute 3b:
            runight("/CHR/nana2/close/nana2close_3_3b.png")
        attribute 3c:
            runight("/CHR/nana2/close/nana2close_3_3c.png")
        attribute 3d:
            runight("/CHR/nana2/close/nana2close_3_3d.png")
    ypos 1400
layeredimage nana2_redtint:
    group clothes:
        attribute regular default:
            redtint("/CHR/nana2/close/nana2close_clothes_regular.png")
        attribute fancy:
            redtint("/CHR/nana2/close/nana2close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/nana2/close/nana2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/nana2/close/nana2close_1_1a.png")
        attribute 1b:
            redtint("/CHR/nana2/close/nana2close_1_1b.png")
        attribute 1c:
            redtint("/CHR/nana2/close/nana2close_1_1c.png")
        attribute 1d:
            redtint("/CHR/nana2/close/nana2close_1_1d.png")
        attribute 1e:
            redtint("/CHR/nana2/close/nana2close_1_1e.png")
        attribute 1f:
            redtint("/CHR/nana2/close/nana2close_1_1f.png")
        attribute 1g:
            redtint("/CHR/nana2/close/nana2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/nana2/close/nana2close_2_2a.png")
        attribute 2b:
            redtint("/CHR/nana2/close/nana2close_2_2b.png")
        attribute 2c:
            redtint("/CHR/nana2/close/nana2close_2_2c.png")
        attribute 2d:
            redtint("/CHR/nana2/close/nana2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/nana2/close/nana2close_3_3a.png")
        attribute 3b:
            redtint("/CHR/nana2/close/nana2close_3_3b.png")
        attribute 3c:
            redtint("/CHR/nana2/close/nana2close_3_3c.png")
        attribute 3d:
            redtint("/CHR/nana2/close/nana2close_3_3d.png")
    ypos 1400
layeredimage nana1_redtint:
    group clothes:
        attribute regular2 default:
            redtint("/CHR/nana1/close/nana1close_clothes_regular2.png")
        attribute fancy2:
            redtint("/CHR/nana1/close/nana1close_clothes_fancy2.png")
        attribute regular1:
            redtint("/CHR/nana1/close/nana1close_clothes_regular1.png")
        attribute fancy1:
            redtint("/CHR/nana1/close/nana1close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/nana1/close/nana1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/nana1/close/nana1close_1_1a.png")
        attribute 1b:
            redtint("/CHR/nana1/close/nana1close_1_1b.png")
        attribute 1c:
            redtint("/CHR/nana1/close/nana1close_1_1c.png")
        attribute 1d:
            redtint("/CHR/nana1/close/nana1close_1_1d.png")
        attribute 1e:
            redtint("/CHR/nana1/close/nana1close_1_1e.png")
        attribute 1f:
            redtint("/CHR/nana1/close/nana1close_1_1f.png")
        attribute 1g:
            redtint("/CHR/nana1/close/nana1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/nana1/close/nana1close_2_2a.png")
        attribute 2b:
            redtint("/CHR/nana1/close/nana1close_2_2b.png")
        attribute 2c:
            redtint("/CHR/nana1/close/nana1close_2_2c.png")
        attribute 2d:
            redtint("/CHR/nana1/close/nana1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/nana1/close/nana1close_3_3a.png")
        attribute 3b:
            redtint("/CHR/nana1/close/nana1close_3_3b.png")
        attribute 3c:
            redtint("/CHR/nana1/close/nana1close_3_3c.png")
        attribute 3d:
            redtint("/CHR/nana1/close/nana1close_3_3d.png")
    ypos 1400
layeredimage nana1_ruclose:
    group clothes:
        attribute regular2 default:
            runight("/CHR/nana1/close/nana1close_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/nana1/close/nana1close_clothes_fancy2.png")
        attribute regular1:
            runight("/CHR/nana1/close/nana1close_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/nana1/close/nana1close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana1/close/nana1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana1/close/nana1close_1_1a.png")
        attribute 1b:
            runight("/CHR/nana1/close/nana1close_1_1b.png")
        attribute 1c:
            runight("/CHR/nana1/close/nana1close_1_1c.png")
        attribute 1d:
            runight("/CHR/nana1/close/nana1close_1_1d.png")
        attribute 1e:
            runight("/CHR/nana1/close/nana1close_1_1e.png")
        attribute 1f:
            runight("/CHR/nana1/close/nana1close_1_1f.png")
        attribute 1g:
            runight("/CHR/nana1/close/nana1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana1/close/nana1close_2_2a.png")
        attribute 2b:
            runight("/CHR/nana1/close/nana1close_2_2b.png")
        attribute 2c:
            runight("/CHR/nana1/close/nana1close_2_2c.png")
        attribute 2d:
            runight("/CHR/nana1/close/nana1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana1/close/nana1close_3_3a.png")
        attribute 3b:
            runight("/CHR/nana1/close/nana1close_3_3b.png")
        attribute 3c:
            runight("/CHR/nana1/close/nana1close_3_3c.png")
        attribute 3d:
            runight("/CHR/nana1/close/nana1close_3_3d.png")
    ypos 1400
layeredimage marta3_redtint:
    group clothes:
        attribute regular2:
            redtint("/CHR/marta3/close/marta3close_clothes_regular2.png")
        attribute fancy2:
            redtint("/CHR/marta3/close/marta3close_clothes_fancy2.png")
        attribute regular1 default:
            redtint("/CHR/marta3/close/marta3close_clothes_regular1.png")
        attribute fancy1:
            redtint("/CHR/marta3/close/marta3close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/marta3/close/marta3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/marta3/close/marta3close_1_1a.png")
        attribute 1b:
            redtint("/CHR/marta3/close/marta3close_1_1b.png")
        attribute 1c:
            redtint("/CHR/marta3/close/marta3close_1_1c.png")
        attribute 1d:
            redtint("/CHR/marta3/close/marta3close_1_1d.png")
        attribute 1e:
            redtint("/CHR/marta3/close/marta3close_1_1e.png")
        attribute 1f:
            redtint("/CHR/marta3/close/marta3close_1_1f.png")
        attribute 1g:
            redtint("/CHR/marta3/close/marta3close_1_1g.png")
        attribute 1aa:
            redtint("/CHR/marta3/close/marta3close_1_1aa.png")
        attribute 1bb:
            redtint("/CHR/marta3/close/marta3close_1_1bb.png")
        attribute 1cc:
            redtint("/CHR/marta3/close/marta3close_1_1cc.png")
        attribute 1dd:
            redtint("/CHR/marta3/close/marta3close_1_1dd.png")
        attribute 1ee:
            redtint("/CHR/marta3/close/marta3close_1_1ee.png")
        attribute 1ff:
            redtint("/CHR/marta3/close/marta3close_1_1ff.png")
        attribute 1gg:
            redtint("/CHR/marta3/close/marta3close_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/marta3/close/marta3close_2_2a.png")
        attribute 2b:
            redtint("/CHR/marta3/close/marta3close_2_2b.png")
        attribute 2c:
            redtint("/CHR/marta3/close/marta3close_2_2c.png")
        attribute 2d:
            redtint("/CHR/marta3/close/marta3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/marta3/close/marta3close_3_3a.png")
        attribute 3b:
            redtint("/CHR/marta3/close/marta3close_3_3b.png")
        attribute 3c:
            redtint("/CHR/marta3/close/marta3close_3_3c.png")
        attribute 3d:
            redtint("/CHR/marta3/close/marta3close_3_3d.png")
    ypos 1460
layeredimage marta3_ruclose:
    group clothes:
        attribute regular2:
            runight("/CHR/marta3/close/marta3close_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/marta3/close/marta3close_clothes_fancy2.png")
        attribute regular1 default:
            runight("/CHR/marta3/close/marta3close_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/marta3/close/marta3close_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta3/close/marta3close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta3/close/marta3close_1_1a.png")
        attribute 1b:
            runight("/CHR/marta3/close/marta3close_1_1b.png")
        attribute 1c:
            runight("/CHR/marta3/close/marta3close_1_1c.png")
        attribute 1d:
            runight("/CHR/marta3/close/marta3close_1_1d.png")
        attribute 1e:
            runight("/CHR/marta3/close/marta3close_1_1e.png")
        attribute 1f:
            runight("/CHR/marta3/close/marta3close_1_1f.png")
        attribute 1g:
            runight("/CHR/marta3/close/marta3close_1_1g.png")
        attribute 1aa:
            runight("/CHR/marta3/close/marta3close_1_1aa.png")
        attribute 1bb:
            runight("/CHR/marta3/close/marta3close_1_1bb.png")
        attribute 1cc:
            runight("/CHR/marta3/close/marta3close_1_1cc.png")
        attribute 1dd:
            runight("/CHR/marta3/close/marta3close_1_1dd.png")
        attribute 1ee:
            runight("/CHR/marta3/close/marta3close_1_1ee.png")
        attribute 1ff:
            runight("/CHR/marta3/close/marta3close_1_1ff.png")
        attribute 1gg:
            runight("/CHR/marta3/close/marta3close_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta3/close/marta3close_2_2a.png")
        attribute 2b:
            runight("/CHR/marta3/close/marta3close_2_2b.png")
        attribute 2c:
            runight("/CHR/marta3/close/marta3close_2_2c.png")
        attribute 2d:
            runight("/CHR/marta3/close/marta3close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta3/close/marta3close_3_3a.png")
        attribute 3b:
            runight("/CHR/marta3/close/marta3close_3_3b.png")
        attribute 3c:
            runight("/CHR/marta3/close/marta3close_3_3c.png")
        attribute 3d:
            runight("/CHR/marta3/close/marta3close_3_3d.png")
    ypos 1460
layeredimage marta2_redtint:
    group clothes:
        attribute regular1 default:
            redtint("/CHR/marta2/close/marta2close_clothes_regular1.png")
        attribute fancy1:
            redtint("/CHR/marta2/close/marta2close_clothes_fancy1.png")
        attribute regular2:
            redtint("/CHR/marta2/close/marta2close_clothes_regular2.png")
        attribute fancy2:
            redtint("/CHR/marta2/close/marta2close_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/marta2/close/marta2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/marta2/close/marta2close_1_1a.png")
        attribute 1b:
            redtint("/CHR/marta2/close/marta2close_1_1b.png")
        attribute 1c:
            redtint("/CHR/marta2/close/marta2close_1_1c.png")
        attribute 1d:
            redtint("/CHR/marta2/close/marta2close_1_1d.png")
        attribute 1e:
            redtint("/CHR/marta2/close/marta2close_1_1e.png")
        attribute 1f:
            redtint("/CHR/marta2/close/marta2close_1_1f.png")
        attribute 1g:
            redtint("/CHR/marta2/close/marta2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/marta2/close/marta2close_2_2a.png")
        attribute 2b:
            redtint("/CHR/marta2/close/marta2close_2_2b.png")
        attribute 2c:
            redtint("/CHR/marta2/close/marta2close_2_2c.png")
        attribute 2d:
            redtint("/CHR/marta2/close/marta2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/marta2/close/marta2close_3_3a.png")
        attribute 3b:
            redtint("/CHR/marta2/close/marta2close_3_3b.png")
        attribute 3c:
            redtint("/CHR/marta2/close/marta2close_3_3c.png")
        attribute 3d:
            redtint("/CHR/marta2/close/marta2close_3_3d.png")
    ypos 1470
layeredimage marta2_ruclose:
    group clothes:
        attribute regular1 default:
            runight("/CHR/marta2/close/marta2close_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/marta2/close/marta2close_clothes_fancy1.png")
        attribute regular2:
            runight("/CHR/marta2/close/marta2close_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/marta2/close/marta2close_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta2/close/marta2close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta2/close/marta2close_1_1a.png")
        attribute 1b:
            runight("/CHR/marta2/close/marta2close_1_1b.png")
        attribute 1c:
            runight("/CHR/marta2/close/marta2close_1_1c.png")
        attribute 1d:
            runight("/CHR/marta2/close/marta2close_1_1d.png")
        attribute 1e:
            runight("/CHR/marta2/close/marta2close_1_1e.png")
        attribute 1f:
            runight("/CHR/marta2/close/marta2close_1_1f.png")
        attribute 1g:
            runight("/CHR/marta2/close/marta2close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta2/close/marta2close_2_2a.png")
        attribute 2b:
            runight("/CHR/marta2/close/marta2close_2_2b.png")
        attribute 2c:
            runight("/CHR/marta2/close/marta2close_2_2c.png")
        attribute 2d:
            runight("/CHR/marta2/close/marta2close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta2/close/marta2close_3_3a.png")
        attribute 3b:
            runight("/CHR/marta2/close/marta2close_3_3b.png")
        attribute 3c:
            runight("/CHR/marta2/close/marta2close_3_3c.png")
        attribute 3d:
            runight("/CHR/marta2/close/marta2close_3_3d.png")
    ypos 1470
layeredimage marta1_redtint:
    group clothes:
        attribute regular2 default:
            redtint("/CHR/marta1/close/marta1close_clothes_regular1.png")
        attribute fancy2:
            redtint("/CHR/marta1/close/marta1close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/marta1/close/marta1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/marta1/close/marta1close_1_1a.png")
        attribute 1b:
            redtint("/CHR/marta1/close/marta1close_1_1b.png")
        attribute 1c:
            redtint("/CHR/marta1/close/marta1close_1_1c.png")
        attribute 1d:
            redtint("/CHR/marta1/close/marta1close_1_1d.png")
        attribute 1e:
            redtint("/CHR/marta1/close/marta1close_1_1e.png")
        attribute 1f:
            redtint("/CHR/marta1/close/marta1close_1_1f.png")
        attribute 1g:
            redtint("/CHR/marta1/close/marta1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/marta1/close/marta1close_2_2a.png")
        attribute 2b:
            redtint("/CHR/marta1/close/marta1close_2_2b.png")
        attribute 2c:
            redtint("/CHR/marta1/close/marta1close_2_2c.png")
        attribute 2d:
            redtint("/CHR/marta1/close/marta1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/marta1/close/marta1close_3_3a.png")
        attribute 3b:
            redtint("/CHR/marta1/close/marta1close_3_3b.png")
        attribute 3c:
            redtint("/CHR/marta1/close/marta1close_3_3c.png")
        attribute 3d:
            redtint("/CHR/marta1/close/marta1close_3_3d.png")
    ypos 1470
layeredimage marta1_ruclose:
    group clothes:
        attribute regular2 default:
            runight("/CHR/marta1/close/marta1close_clothes_regular1.png")
        attribute fancy2:
            runight("/CHR/marta1/close/marta1close_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta1/close/marta1close_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta1/close/marta1close_1_1a.png")
        attribute 1b:
            runight("/CHR/marta1/close/marta1close_1_1b.png")
        attribute 1c:
            runight("/CHR/marta1/close/marta1close_1_1c.png")
        attribute 1d:
            runight("/CHR/marta1/close/marta1close_1_1d.png")
        attribute 1e:
            runight("/CHR/marta1/close/marta1close_1_1e.png")
        attribute 1f:
            runight("/CHR/marta1/close/marta1close_1_1f.png")
        attribute 1g:
            runight("/CHR/marta1/close/marta1close_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta1/close/marta1close_2_2a.png")
        attribute 2b:
            runight("/CHR/marta1/close/marta1close_2_2b.png")
        attribute 2c:
            runight("/CHR/marta1/close/marta1close_2_2c.png")
        attribute 2d:
            runight("/CHR/marta1/close/marta1close_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta1/close/marta1close_3_3a.png")
        attribute 3b:
            runight("/CHR/marta1/close/marta1close_3_3b.png")
        attribute 3c:
            runight("/CHR/marta1/close/marta1close_3_3c.png")
        attribute 3d:
            runight("/CHR/marta1/close/marta1close_3_3d.png")
    ypos 1470
layeredimage sima1_redtint:
    group clothes:
        attribute regular default:
            redtint("/CHR/sima1/close/sima1close_clothes_regular.png")

        attribute fancy:
            redtint("/CHR/sima1/close/sima1close_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            redtint("/CHR/sima1/close/sima1close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            redtint("/CHR/sima1/close/sima1close_1_1a.png")

        attribute 1c:
            redtint("/CHR/sima1/close/sima1close_1_1c.png")

        attribute 1d:
            redtint("/CHR/sima1/close/sima1close_1_1d.png")

        attribute 1e:
            redtint("/CHR/sima1/close/sima1close_1_1e.png")

        attribute 1g:
            redtint("/CHR/sima1/close/sima1close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            redtint("/CHR/sima1/close/sima1close_2_2a.png")

        attribute 2b:
            redtint("/CHR/sima1/close/sima1close_2_2b.png")

        attribute 2c:
            redtint("/CHR/sima1/close/sima1close_2_2c.png")

        attribute 2d:
            redtint("/CHR/sima1/close/sima1close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            redtint("/CHR/sima1/close/sima1close_3_3a.png")

        attribute 3b:
            redtint("/CHR/sima1/close/sima1close_3_3b.png")

        attribute 3c:
            redtint("/CHR/sima1/close/sima1close_3_3c.png")

        attribute 3d:
            redtint("/CHR/sima1/close/sima1close_3_3d.png")

    ypos 1475
layeredimage sima1_ruclose:
    group clothes:
        attribute regular default:
            runight("/CHR/sima1/close/sima1close_clothes_regular.png")

        attribute fancy:
            runight("/CHR/sima1/close/sima1close_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima1/close/sima1close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima1/close/sima1close_1_1a.png")

        attribute 1c:
            runight("/CHR/sima1/close/sima1close_1_1c.png")

        attribute 1d:
            runight("/CHR/sima1/close/sima1close_1_1d.png")

        attribute 1e:
            runight("/CHR/sima1/close/sima1close_1_1e.png")

        attribute 1g:
            runight("/CHR/sima1/close/sima1close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima1/close/sima1close_2_2a.png")

        attribute 2b:
            runight("/CHR/sima1/close/sima1close_2_2b.png")

        attribute 2c:
            runight("/CHR/sima1/close/sima1close_2_2c.png")

        attribute 2d:
            runight("/CHR/sima1/close/sima1close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima1/close/sima1close_3_3a.png")

        attribute 3b:
            runight("/CHR/sima1/close/sima1close_3_3b.png")

        attribute 3c:
            runight("/CHR/sima1/close/sima1close_3_3c.png")

        attribute 3d:
            runight("/CHR/sima1/close/sima1close_3_3d.png")

    ypos 1475
layeredimage sima2_redtint:
    group clothes:
        attribute regular1 default:
            redtint("/CHR/sima2/close/sima2close_clothes_regular1.png")

        attribute fancy1:
            redtint("/CHR/sima2/close/sima2close_clothes_fancy1.png")

        attribute regular2:
            redtint("/CHR/sima2/close/sima2close_clothes_regular2.png")

        attribute fancy2:
            redtint("/CHR/sima2/close/sima2close_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            redtint("/CHR/sima2/close/sima2close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            redtint("/CHR/sima2/close/sima2close_1_1a.png")

        attribute 1c:
            redtint("/CHR/sima2/close/sima2close_1_1c.png")

        attribute 1d:
            redtint("/CHR/sima2/close/sima2close_1_1d.png")

        attribute 1e:
            redtint("/CHR/sima2/close/sima2close_1_1e.png")

        attribute 1g:
            redtint("/CHR/sima2/close/sima2close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            redtint("/CHR/sima2/close/sima2close_2_2a.png")

        attribute 2b:
            redtint("/CHR/sima2/close/sima2close_2_2b.png")

        attribute 2c:
            redtint("/CHR/sima2/close/sima2close_2_2c.png")

        attribute 2d:
            redtint("/CHR/sima2/close/sima2close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            redtint("/CHR/sima2/close/sima2close_3_3a.png")

        attribute 3b:
            redtint("/CHR/sima2/close/sima2close_3_3b.png")

        attribute 3c:
            redtint("/CHR/sima2/close/sima2close_3_3c.png")

        attribute 3d:
            redtint("/CHR/sima2/close/sima2close_3_3d.png")

    ypos 1445
layeredimage sima2_ruclose:
    group clothes:
        attribute regular1 default:
            runight("/CHR/sima2/close/sima2close_clothes_regular1.png")

        attribute fancy1:
            runight("/CHR/sima2/close/sima2close_clothes_fancy1.png")

        attribute regular2:
            runight("/CHR/sima2/close/sima2close_clothes_regular2.png")

        attribute fancy2:
            runight("/CHR/sima2/close/sima2close_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima2/close/sima2close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima2/close/sima2close_1_1a.png")

        attribute 1c:
            runight("/CHR/sima2/close/sima2close_1_1c.png")

        attribute 1d:
            runight("/CHR/sima2/close/sima2close_1_1d.png")

        attribute 1e:
            runight("/CHR/sima2/close/sima2close_1_1e.png")

        attribute 1g:
            runight("/CHR/sima2/close/sima2close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima2/close/sima2close_2_2a.png")

        attribute 2b:
            runight("/CHR/sima2/close/sima2close_2_2b.png")

        attribute 2c:
            runight("/CHR/sima2/close/sima2close_2_2c.png")

        attribute 2d:
            runight("/CHR/sima2/close/sima2close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima2/close/sima2close_3_3a.png")

        attribute 3b:
            runight("/CHR/sima2/close/sima2close_3_3b.png")

        attribute 3c:
            runight("/CHR/sima2/close/sima2close_3_3c.png")

        attribute 3d:
            runight("/CHR/sima2/close/sima2close_3_3d.png")

    ypos 1445
layeredimage sima3a_redtint:
    group clothes:
        attribute regular2 default:
            redtint("/CHR/sima3a/close/sima3aclose_clothes_regular.png")

        attribute fancy2:
            redtint("/CHR/sima3a/close/sima3aclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            redtint("/CHR/sima3a/close/sima3aclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            redtint("/CHR/sima3a/close/sima3aclose_1_1a.png")

        attribute 1c:
            redtint("/CHR/sima3a/close/sima3aclose_1_1c.png")

        attribute 1d:
            redtint("/CHR/sima3a/close/sima3aclose_1_1d.png")

        attribute 1e:
            redtint("/CHR/sima3a/close/sima3aclose_1_1e.png")

        attribute 1g:
            redtint("/CHR/sima3a/close/sima3aclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            redtint("/CHR/sima3a/close/sima3aclose_2_2a.png")

        attribute 2b:
            redtint("/CHR/sima3a/close/sima3aclose_2_2b.png")

        attribute 2c:
            redtint("/CHR/sima3a/close/sima3aclose_2_2c.png")

        attribute 2d:
            redtint("/CHR/sima3a/close/sima3aclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            redtint("/CHR/sima3a/close/sima3aclose_3_3a.png")

        attribute 3b:
            redtint("/CHR/sima3a/close/sima3aclose_3_3b.png")

        attribute 3c:
            redtint("/CHR/sima3a/close/sima3aclose_3_3c.png")

        attribute 3d:
            redtint("/CHR/sima3a/close/sima3aclose_3_3d.png")

    ypos 1485
layeredimage sima3a_ruclose:
    group clothes:
        attribute regular2 default:
            runight("/CHR/sima3a/close/sima3aclose_clothes_regular.png")

        attribute fancy2:
            runight("/CHR/sima3a/close/sima3aclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima3a/close/sima3aclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima3a/close/sima3aclose_1_1a.png")

        attribute 1c:
            runight("/CHR/sima3a/close/sima3aclose_1_1c.png")

        attribute 1d:
            runight("/CHR/sima3a/close/sima3aclose_1_1d.png")

        attribute 1e:
            runight("/CHR/sima3a/close/sima3aclose_1_1e.png")

        attribute 1g:
            runight("/CHR/sima3a/close/sima3aclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima3a/close/sima3aclose_2_2a.png")

        attribute 2b:
            runight("/CHR/sima3a/close/sima3aclose_2_2b.png")

        attribute 2c:
            runight("/CHR/sima3a/close/sima3aclose_2_2c.png")

        attribute 2d:
            runight("/CHR/sima3a/close/sima3aclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima3a/close/sima3aclose_3_3a.png")

        attribute 3b:
            runight("/CHR/sima3a/close/sima3aclose_3_3b.png")

        attribute 3c:
            runight("/CHR/sima3a/close/sima3aclose_3_3c.png")

        attribute 3d:
            runight("/CHR/sima3a/close/sima3aclose_3_3d.png")

    ypos 1485
layeredimage sima3b_redtint:
    group clothes:
        attribute regular2 default:
            redtint("/CHR/sima3b/close/sima3bclose_clothes_regular.png")

        attribute fancy2:
            redtint("/CHR/sima3b/close/sima3bclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            redtint("/CHR/sima3b/close/sima3bclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            redtint("/CHR/sima3b/close/sima3bclose_1_1a.png")

        attribute 1c:
            redtint("/CHR/sima3b/close/sima3bclose_1_1c.png")

        attribute 1d:
            redtint("/CHR/sima3b/close/sima3bclose_1_1d.png")

        attribute 1e:
            redtint("/CHR/sima3b/close/sima3bclose_1_1e.png")

        attribute 1g:
            redtint("/CHR/sima3b/close/sima3bclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            redtint("/CHR/sima3b/close/sima3bclose_2_2a.png")

        attribute 2b:
            redtint("/CHR/sima3b/close/sima3bclose_2_2b.png")

        attribute 2c:
            redtint("/CHR/sima3b/close/sima3bclose_2_2c.png")

        attribute 2d:
            redtint("/CHR/sima3b/close/sima3bclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            redtint("/CHR/sima3b/close/sima3bclose_3_3a.png")

        attribute 3b:
            redtint("/CHR/sima3b/close/sima3bclose_3_3b.png")

        attribute 3c:
            redtint("/CHR/sima3b/close/sima3bclose_3_3c.png")

        attribute 3d:
            redtint("/CHR/sima3b/close/sima3bclose_3_3d.png")

    ypos 1485
layeredimage sima3b_ruclose:
    group clothes:
        attribute regular2 default:
            runight("/CHR/sima3b/close/sima3bclose_clothes_regular.png")

        attribute fancy2:
            runight("/CHR/sima3b/close/sima3bclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima3b/close/sima3bclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima3b/close/sima3bclose_1_1a.png")

        attribute 1c:
            runight("/CHR/sima3b/close/sima3bclose_1_1c.png")

        attribute 1d:
            runight("/CHR/sima3b/close/sima3bclose_1_1d.png")

        attribute 1e:
            runight("/CHR/sima3b/close/sima3bclose_1_1e.png")

        attribute 1g:
            runight("/CHR/sima3b/close/sima3bclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima3b/close/sima3bclose_2_2a.png")

        attribute 2b:
            runight("/CHR/sima3b/close/sima3bclose_2_2b.png")

        attribute 2c:
            runight("/CHR/sima3b/close/sima3bclose_2_2c.png")

        attribute 2d:
            runight("/CHR/sima3b/close/sima3bclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima3b/close/sima3bclose_3_3a.png")

        attribute 3b:
            runight("/CHR/sima3b/close/sima3bclose_3_3b.png")

        attribute 3c:
            runight("/CHR/sima3b/close/sima3bclose_3_3c.png")

        attribute 3d:
            runight("/CHR/sima3b/close/sima3bclose_3_3d.png")

    ypos 1485
layeredimage ermy1_redtint:
        group clothes:
            attribute pose1 default:
                redtint("/CHR/ermy/ermy1_pose_pose1.png")
            attribute pose2:
                redtint("/CHR/ermy/ermy1_pose_pose2.png")
        group blush:
            attribute noblush default:
                "null_image"
            attribute blush:
                redtint("/CHR/ermy/ermy1_blush_blush.png")
        group 1 auto:
            attribute 1a default:
                redtint("/CHR/ermy/ermy1_1_1a.png")
            attribute 1b:
                redtint("/CHR/ermy/ermy1_1_1b.png")
            attribute 1c:
                redtint("/CHR/ermy/ermy1_1_1c.png")
            attribute 1d:
                redtint("/CHR/ermy/ermy1_1_1d.png")
            attribute 1e:
                redtint("/CHR/ermy/ermy1_1_1e.png")
            attribute 1f:
                redtint("/CHR/ermy/ermy1_1_1f.png")
            attribute 1g:
                redtint("/CHR/ermy/ermy1_1_1g.png")
            attribute 1h:
                redtint("/CHR/ermy/ermy1_1_1h.png")
        group 2 auto:
            attribute 2a default:
                redtint("/CHR/ermy/ermy1_2_2a.png")
            attribute 2b:
                redtint("/CHR/ermy/ermy1_2_2b.png")
            attribute 2c:
                redtint("/CHR/ermy/ermy1_2_2c.png")
            attribute 2d:
                redtint("/CHR/ermy/ermy1_2_2d.png")
        group 3 auto:
            attribute 3a default:
                redtint("/CHR/ermy/ermy1_3_3a.png")
            attribute 3b:
                redtint("/CHR/ermy/ermy1_3_3b.png")
            attribute 3c:
                redtint("/CHR/ermy/ermy1_3_3c.png")
            attribute 3d:
                redtint("/CHR/ermy/ermy1_3_3d.png")
        ypos 1270
layeredimage teya1_redtint:
    group clothes:
        attribute regular default:
            redtint("/CHR/teya1/teya1_clothes_regular.png")
        attribute fancy:
            redtint("/CHR/teya1/teya1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/sima1/sima1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/teya1/teya1_1_1a.png")
        attribute 1b:
            redtint("/CHR/teya1/teya1_1_1b.png")
        attribute 1c:
            redtint("/CHR/teya1/teya1_1_1c.png")
        attribute 1d:
            redtint("/CHR/teya1/teya1_1_1d.png")
        attribute 1e:
            redtint("/CHR/teya1/teya1_1_1e.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/teya1/teya1_2_2a.png")
        attribute 2b:
            redtint("/CHR/teya1/teya1_2_2b.png")
        attribute 2c:
            redtint("/CHR/teya1/teya1_2_2c.png")
        attribute 2d:
            redtint("/CHR/teya1/teya1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/teya1/teya1_3_3a.png")
        attribute 3b:
            redtint("/CHR/teya1/teya1_3_3b.png")
        attribute 3c:
            redtint("/CHR/teya1/teya1_3_3c.png")
        attribute 3d:
            redtint("/CHR/teya1/teya1_3_3d.png")
    ypos 1230
layeredimage teya2_redtint:
    group clothes:
        attribute regularhand1 default:
            redtint("/CHR/teya2/teya2_clothes_regularhand1.png")
        attribute fancyhand1:
            redtint("/CHR/teya2/teya2_clothes_fancyhand1.png")
        attribute regularhand2:
            redtint("/CHR/teya2/teya2_clothes_regularhand2.png")
        attribute fancyhand2:
            redtint("/CHR/teya2/teya2_clothes_fancyhand2.png")
        attribute regularhand3:
            redtint("/CHR/teya2/teya2_clothes_regularhand3.png")
        attribute fancyhand3:
            redtint("/CHR/teya2/teya2_clothes_fancyhand3.png")
        attribute regularhand4:
            redtint("/CHR/teya2/teya2_clothes_regularhand4.png")
        attribute fancyhand4:
            redtint("/CHR/teya2/teya2_clothes_fancyhand4.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/teya2/teya2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/teya2/teya2_1_1a.png")
        attribute 1b:
            redtint("/CHR/teya2/teya2_1_1b.png")
        attribute 1c:
            redtint("/CHR/teya2/teya2_1_1c.png")
        attribute 1d:
            redtint("/CHR/teya2/teya2_1_1d.png")
        attribute 1e:
            redtint("/CHR/teya2/teya2_1_1e.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/teya2/teya2_2_2a.png")
        attribute 2b:
            redtint("/CHR/teya2/teya2_2_2b.png")
        attribute 2c:
            redtint("/CHR/teya2/teya2_2_2c.png")
        attribute 2d:
            redtint("/CHR/teya2/teya2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/teya2/teya2_3_3a.png")
        attribute 3b:
            redtint("/CHR/teya2/teya2_3_3b.png")
        attribute 3c:
            redtint("/CHR/teya2/teya2_3_3c.png")
        attribute 3d:
            redtint("/CHR/teya2/teya2_3_3d.png")
    ypos 1230
layeredimage teya3_redtint:
    group clothes:
        attribute regular default:
            redtint("/CHR/teya3/teya3_clothes_regular.png")
        attribute fancy:
            redtint("/CHR/teya3/teya3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            redtint("/CHR/teya3/teya3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            redtint("/CHR/teya3/teya3_1_1a.png")
        attribute 1b:
            redtint("/CHR/teya3/teya3_1_1b.png")
        attribute 1c:
            redtint("/CHR/teya3/teya3_1_1c.png")
        attribute 1d:
            redtint("/CHR/teya3/teya3_1_1d.png")
        attribute 1e:
            redtint("/CHR/teya3/teya3_1_1e.png")
    group 2 auto:
        attribute 2a default:
            redtint("/CHR/teya3/teya3_2_2a.png")
        attribute 2b:
            redtint("/CHR/teya3/teya3_2_2b.png")
        attribute 2c:
            redtint("/CHR/teya3/teya3_2_2c.png")
        attribute 2d:
            redtint("/CHR/teya3/teya3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            redtint("/CHR/teya3/teya3_3_3a.png")
        attribute 3b:
            redtint("/CHR/teya3/teya3_3_3b.png")
        attribute 3c:
            redtint("/CHR/teya3/teya3_3_3c.png")
        attribute 3d:
            redtint("/CHR/teya3/teya3_3_3d.png")
    ypos 1230
layeredimage nana3_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/nana3/nana3_clothes_regular.png")
        attribute fancy:
            rain("/CHR/nana3/nana3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/nana3/nana3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/nana3/nana3_1_1a.png")
        attribute 1b:
            rain("/CHR/nana3/nana3_1_1b.png")
        attribute 1c:
            rain("/CHR/nana3/nana3_1_1c.png")
        attribute 1d:
            rain("/CHR/nana3/nana3_1_1d.png")
        attribute 1e:
            rain("/CHR/nana3/nana3_1_1e.png")
        attribute 1f:
            rain("/CHR/nana3/nana3_1_1f.png")
        attribute 1g:
            rain("/CHR/nana3/nana3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/nana3/nana3_2_2a.png")
        attribute 2b:
            rain("/CHR/nana3/nana3_2_2b.png")
        attribute 2c:
            rain("/CHR/nana3/nana3_2_2c.png")
        attribute 2d:
            rain("/CHR/nana3/nana3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/nana3/nana3_3_3a.png")
        attribute 3b:
            rain("/CHR/nana3/nana3_3_3b.png")
        attribute 3c:
            rain("/CHR/nana3/nana3_3_3c.png")
        attribute 3d:
            rain("/CHR/nana3/nana3_3_3d.png")
    ypos 1250
layeredimage nana3d3_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/nana3/d3/nana3d3_clothes_regular.png")
        attribute fancy:
            rain("/CHR/nana3/d3/nana3d3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/nana3/d3/nana3d3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/nana3/d3/nana3d3_1_1a.png")
        attribute 1b:
            rain("/CHR/nana3/d3/nana3d3_1_1b.png")
        attribute 1c:
            rain("/CHR/nana3/d3/nana3d3_1_1c.png")
        attribute 1d:
            rain("/CHR/nana3/d3/nana3d3_1_1d.png")
        attribute 1e:
            rain("/CHR/nana3/d3/nana3d3_1_1e.png")
        attribute 1f:
            rain("/CHR/nana3/d3/nana3d3_1_1f.png")
        attribute 1g:
            rain("/CHR/nana3/d3/nana3d3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/nana3/d3/nana3d3_2_2a.png")
        attribute 2b:
            rain("/CHR/nana3/d3/nana3d3_2_2b.png")
        attribute 2c:
            rain("/CHR/nana3/d3/nana3d3_2_2c.png")
        attribute 2d:
            rain("/CHR/nana3/d3/nana3d3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/nana3/d3/nana3d3_3_3a.png")
        attribute 3b:
            rain("/CHR/nana3/d3/nana3d3_3_3b.png")
        attribute 3c:
            rain("/CHR/nana3/d3/nana3d3_3_3c.png")
        attribute 3d:
            rain("/CHR/nana3/d3/nana3d3_3_3d.png")
layeredimage nana2_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/nana2/nana2_clothes_regular.png")
        attribute fancy:
            rain("/CHR/nana2/nana2_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/nana2/nana2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/nana2/nana2_1_1a.png")
        attribute 1b:
            rain("/CHR/nana2/nana2_1_1b.png")
        attribute 1c:
            rain("/CHR/nana2/nana2_1_1c.png")
        attribute 1d:
            rain("/CHR/nana2/nana2_1_1d.png")
        attribute 1e:
            rain("/CHR/nana2/nana2_1_1e.png")
        attribute 1f:
            rain("/CHR/nana2/nana2_1_1f.png")
        attribute 1g:
            rain("/CHR/nana2/nana2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/nana2/nana2_2_2a.png")
        attribute 2b:
            rain("/CHR/nana2/nana2_2_2b.png")
        attribute 2c:
            rain("/CHR/nana2/nana2_2_2c.png")
        attribute 2d:
            rain("/CHR/nana2/nana2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/nana2/nana2_3_3a.png")
        attribute 3b:
            rain("/CHR/nana2/nana2_3_3b.png")
        attribute 3c:
            rain("/CHR/nana2/nana2_3_3c.png")
        attribute 3d:
            rain("/CHR/nana2/nana2_3_3d.png")
    ypos 1250
layeredimage nana1_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/nana1/nana1_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/nana1/nana1_clothes_fancy2.png")
        attribute regular1:
            rain("/CHR/nana1/nana1_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/nana1/nana1_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/nana1/nana1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/nana1/nana1_1_1a.png")
        attribute 1b:
            rain("/CHR/nana1/nana1_1_1b.png")
        attribute 1c:
            rain("/CHR/nana1/nana1_1_1c.png")
        attribute 1d:
            rain("/CHR/nana1/nana1_1_1d.png")
        attribute 1e:
            rain("/CHR/nana1/nana1_1_1e.png")
        attribute 1f:
            rain("/CHR/nana1/nana1_1_1f.png")
        attribute 1g:
            rain("/CHR/nana1/nana1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/nana1/nana1_2_2a.png")
        attribute 2b:
            rain("/CHR/nana1/nana1_2_2b.png")
        attribute 2c:
            rain("/CHR/nana1/nana1_2_2c.png")
        attribute 2d:
            rain("/CHR/nana1/nana1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/nana1/nana1_3_3a.png")
        attribute 3b:
            rain("/CHR/nana1/nana1_3_3b.png")
        attribute 3c:
            rain("/CHR/nana1/nana1_3_3c.png")
        attribute 3d:
            rain("/CHR/nana1/nana1_3_3d.png")
    ypos 1250
layeredimage nana1d3_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/nana1/d3/nana1d3_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/nana1/d3/nana1d3_clothes_fancy2.png")
        attribute regular1:
            rain("/CHR/nana1/d3/nana1d3_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/nana1/d3/nana1d3_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/nana1/d3/nana1d3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/nana1/d3/nana1d3_1_1a.png")
        attribute 1b:
            rain("/CHR/nana1/d3/nana1d3_1_1b.png")
        attribute 1c:
            rain("/CHR/nana1/d3/nana1d3_1_1c.png")
        attribute 1d:
            rain("/CHR/nana1/d3/nana1d3_1_1d.png")
        attribute 1e:
            rain("/CHR/nana1/d3/nana1d3_1_1e.png")
        attribute 1f:
            rain("/CHR/nana1/d3/nana1d3_1_1f.png")
        attribute 1g:
            rain("/CHR/nana1/d3/nana1d3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/nana1/d3/nana1d3_2_2a.png")
        attribute 2b:
            rain("/CHR/nana1/d3/nana1d3_2_2b.png")
        attribute 2c:
            rain("/CHR/nana1/d3/nana1d3_2_2c.png")
        attribute 2d:
            rain("/CHR/nana1/d3/nana1d3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/nana1/d3/nana1d3_3_3a.png")
        attribute 3b:
            rain("/CHR/nana1/d3/nana1d3_3_3b.png")
        attribute 3c:
            rain("/CHR/nana1/d3/nana1d3_3_3c.png")
        attribute 3d:
            rain("/CHR/nana1/d3/nana1d3_3_3d.png")
layeredimage marta3_rain:
    group clothes:
        attribute regular2:
            rain("/CHR/marta3/marta3_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/marta3/marta3_clothes_fancy2.png")
        attribute regular1 default:
            rain("/CHR/marta3/marta3_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/marta3/marta3_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/marta3/marta3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/marta3/marta3_1_1a.png")
        attribute 1b:
            rain("/CHR/marta3/marta3_1_1b.png")
        attribute 1c:
            rain("/CHR/marta3/marta3_1_1c.png")
        attribute 1d:
            rain("/CHR/marta3/marta3_1_1d.png")
        attribute 1e:
            rain("/CHR/marta3/marta3_1_1e.png")
        attribute 1f:
            rain("/CHR/marta3/marta3_1_1f.png")
        attribute 1g:
            rain("/CHR/marta3/marta3_1_1g.png")
        attribute 1aa:
            rain("/CHR/marta3/marta3_1_1aa.png")
        attribute 1bb:
            rain("/CHR/marta3/marta3_1_1bb.png")
        attribute 1cc:
            rain("/CHR/marta3/marta3_1_1cc.png")
        attribute 1dd:
            rain("/CHR/marta3/marta3_1_1dd.png")
        attribute 1ee:
            rain("/CHR/marta3/marta3_1_1ee.png")
        attribute 1ff:
            rain("/CHR/marta3/marta3_1_1ff.png")
        attribute 1gg:
            rain("/CHR/marta3/marta3_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/marta3/marta3_2_2a.png")
        attribute 2b:
            rain("/CHR/marta3/marta3_2_2b.png")
        attribute 2c:
            rain("/CHR/marta3/marta3_2_2c.png")
        attribute 2d:
            rain("/CHR/marta3/marta3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/marta3/marta3_3_3a.png")
        attribute 3b:
            rain("/CHR/marta3/marta3_3_3b.png")
        attribute 3c:
            rain("/CHR/marta3/marta3_3_3c.png")
        attribute 3d:
            rain("/CHR/marta3/marta3_3_3d.png")
    ypos 1270
layeredimage marta3d3_rain:
    group clothes:
        attribute regular2:
            rain("/CHR/marta3/d3/marta3d3_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/marta3/d3/marta3d3_clothes_fancy2.png")
        attribute regular1 default:
            rain("/CHR/marta3/d3/marta3d3_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/marta3/d3/marta3d3_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/marta3/d3/marta3d3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/marta3/d3/marta3d3_1_1a.png")
        attribute 1b:
            rain("/CHR/marta3/d3/marta3d3_1_1b.png")
        attribute 1c:
            rain("/CHR/marta3/d3/marta3d3_1_1c.png")
        attribute 1d:
            rain("/CHR/marta3/d3/marta3d3_1_1d.png")
        attribute 1e:
            rain("/CHR/marta3/d3/marta3d3_1_1e.png")
        attribute 1f:
            rain("/CHR/marta3/d3/marta3d3_1_1f.png")
        attribute 1g:
            rain("/CHR/marta3/d3/marta3d3_1_1g.png")
        attribute 1aa:
            rain("/CHR/marta3/d3/marta3d3_1_1aa.png")
        attribute 1bb:
            rain("/CHR/marta3/d3/marta3d3_1_1bb.png")
        attribute 1cc:
            rain("/CHR/marta3/d3/marta3d3_1_1cc.png")
        attribute 1dd:
            rain("/CHR/marta3/d3/marta3d3_1_1dd.png")
        attribute 1ee:
            rain("/CHR/marta3/d3/marta3d3_1_1ee.png")
        attribute 1ff:
            rain("/CHR/marta3/d3/marta3d3_1_1ff.png")
        attribute 1gg:
            rain("/CHR/marta3/d3/marta3d3_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/marta3/d3/marta3d3_2_2a.png")
        attribute 2b:
            rain("/CHR/marta3/d3/marta3d3_2_2b.png")
        attribute 2c:
            rain("/CHR/marta3/d3/marta3d3_2_2c.png")
        attribute 2d:
            rain("/CHR/marta3/d3/marta3d3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/marta3/d3/marta3d3_3_3a.png")
        attribute 3b:
            rain("/CHR/marta3/d3/marta3d3_3_3b.png")
        attribute 3c:
            rain("/CHR/marta3/d3/marta3d3_3_3c.png")
        attribute 3d:
            rain("/CHR/marta3/d3/marta3d3_3_3d.png")
layeredimage marta2_rain:
    group clothes:
        attribute regular1 default:
            rain("/CHR/marta2/marta2_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/marta2/marta2_clothes_fancy1.png")
        attribute regular2:
            rain("/CHR/marta2/marta2_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/marta2/marta2_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/marta2/marta2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/marta2/marta2_1_1a.png")
        attribute 1b:
            rain("/CHR/marta2/marta2_1_1b.png")
        attribute 1c:
            rain("/CHR/marta2/marta2_1_1c.png")
        attribute 1d:
            rain("/CHR/marta2/marta2_1_1d.png")
        attribute 1e:
            rain("/CHR/marta2/marta2_1_1e.png")
        attribute 1f:
            rain("/CHR/marta2/marta2_1_1f.png")
        attribute 1g:
            rain("/CHR/marta2/marta2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/marta2/marta2_2_2a.png")
        attribute 2b:
            rain("/CHR/marta2/marta2_2_2b.png")
        attribute 2c:
            rain("/CHR/marta2/marta2_2_2c.png")
        attribute 2d:
            rain("/CHR/marta2/marta2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/marta2/marta2_3_3a.png")
        attribute 3b:
            rain("/CHR/marta2/marta2_3_3b.png")
        attribute 3c:
            rain("/CHR/marta2/marta2_3_3c.png")
        attribute 3d:
            rain("/CHR/marta2/marta2_3_3d.png")
    ypos 1270
layeredimage marta2d3_rain:
    group clothes:
        attribute regular1 default:
            rain("/CHR/marta2/d3/marta2d3_clothes_regular1.png")
        attribute fancy1:
            rain("/CHR/marta2/d3/marta2d3_clothes_fancy1.png")
        attribute regular2:
            rain("/CHR/marta2/d3/marta2d3_clothes_regular2.png")
        attribute fancy2:
            rain("/CHR/marta2/d3/marta2d3_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/marta2/d3/marta2d3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/marta2/d3/marta2d3_1_1a.png")
        attribute 1b:
            rain("/CHR/marta2/d3/marta2d3_1_1b.png")
        attribute 1c:
            rain("/CHR/marta2/d3/marta2d3_1_1c.png")
        attribute 1d:
            rain("/CHR/marta2/d3/marta2d3_1_1d.png")
        attribute 1e:
            rain("/CHR/marta2/d3/marta2d3_1_1e.png")
        attribute 1f:
            rain("/CHR/marta2/d3/marta2d3_1_1f.png")
        attribute 1g:
            rain("/CHR/marta2/d3/marta2d3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/marta2/d3/marta2d3_2_2a.png")
        attribute 2b:
            rain("/CHR/marta2/d3/marta2d3_2_2b.png")
        attribute 2c:
            rain("/CHR/marta2/d3/marta2d3_2_2c.png")
        attribute 2d:
            rain("/CHR/marta2/d3/marta2d3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/marta2/d3/marta2d3_3_3a.png")
        attribute 3b:
            rain("/CHR/marta2/d3/marta2d3_3_3b.png")
        attribute 3c:
            rain("/CHR/marta2/d3/marta2d3_3_3c.png")
        attribute 3d:
            rain("/CHR/marta2/d3/marta2d3_3_3d.png")
layeredimage marta1_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/marta1/marta1_clothes_regular1.png")
        attribute fancy2:
            rain("/CHR/marta1/marta1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/marta1/marta1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/marta1/marta1_1_1a.png")
        attribute 1b:
            rain("/CHR/marta1/marta1_1_1b.png")
        attribute 1c:
            rain("/CHR/marta1/marta1_1_1c.png")
        attribute 1d:
            rain("/CHR/marta1/marta1_1_1d.png")
        attribute 1e:
            rain("/CHR/marta1/marta1_1_1e.png")
        attribute 1f:
            rain("/CHR/marta1/marta1_1_1f.png")
        attribute 1g:
            rain("/CHR/marta1/marta1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/marta1/marta1_2_2a.png")
        attribute 2b:
            rain("/CHR/marta1/marta1_2_2b.png")
        attribute 2c:
            rain("/CHR/marta1/marta1_2_2c.png")
        attribute 2d:
            rain("/CHR/marta1/marta1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/marta1/marta1_3_3a.png")
        attribute 3b:
            rain("/CHR/marta1/marta1_3_3b.png")
        attribute 3c:
            rain("/CHR/marta1/marta1_3_3c.png")
        attribute 3d:
            rain("/CHR/marta1/marta1_3_3d.png")
    ypos 1270
layeredimage sima1_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/sima1/sima1_clothes_regular.png")

        attribute fancy:
            rain("/CHR/sima1/sima1_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima1/sima1_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima1/sima1_1_1a.png")

        attribute 1c:
            rain("/CHR/sima1/sima1_1_1c.png")

        attribute 1d:
            rain("/CHR/sima1/sima1_1_1d.png")

        attribute 1e:
            rain("/CHR/sima1/sima1_1_1e.png")

        attribute 1g:
            rain("/CHR/sima1/sima1_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima1/sima1_2_2a.png")

        attribute 2b:
            rain("/CHR/sima1/sima1_2_2b.png")

        attribute 2c:
            rain("/CHR/sima1/sima1_2_2c.png")

        attribute 2d:
            rain("/CHR/sima1/sima1_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima1/sima1_3_3a.png")

        attribute 3b:
            rain("/CHR/sima1/sima1_3_3b.png")

        attribute 3c:
            rain("/CHR/sima1/sima1_3_3c.png")

        attribute 3d:
            rain("/CHR/sima1/sima1_3_3d.png")

    ypos 1240
layeredimage sima1close_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/sima1/close/sima1close_clothes_regular.png")

        attribute fancy:
            rain("/CHR/sima1/close/sima1close_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima1/close/sima1close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima1/close/sima1close_1_1a.png")

        attribute 1c:
            rain("/CHR/sima1/close/sima1close_1_1c.png")

        attribute 1d:
            rain("/CHR/sima1/close/sima1close_1_1d.png")

        attribute 1e:
            rain("/CHR/sima1/close/sima1close_1_1e.png")

        attribute 1g:
            rain("/CHR/sima1/close/sima1close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima1/close/sima1close_2_2a.png")

        attribute 2b:
            rain("/CHR/sima1/close/sima1close_2_2b.png")

        attribute 2c:
            rain("/CHR/sima1/close/sima1close_2_2c.png")

        attribute 2d:
            rain("/CHR/sima1/close/sima1close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima1/close/sima1close_3_3a.png")

        attribute 3b:
            rain("/CHR/sima1/close/sima1close_3_3b.png")

        attribute 3c:
            rain("/CHR/sima1/close/sima1close_3_3c.png")

        attribute 3d:
            rain("/CHR/sima1/close/sima1close_3_3d.png")

    ypos 1475
layeredimage sima2_rain:
    group clothes:
        attribute regular1 default:
            rain("/CHR/sima2/sima2_clothes_regular1.png")

        attribute fancy1:
            rain("/CHR/sima2/sima2_clothes_fancy1.png")

        attribute regular2:
            rain("/CHR/sima2/sima2_clothes_regular2.png")

        attribute fancy2:
            rain("/CHR/sima2/sima2_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima2/sima2_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima2/sima2_1_1a.png")

        attribute 1c:
            rain("/CHR/sima2/sima2_1_1c.png")

        attribute 1d:
            rain("/CHR/sima2/sima2_1_1d.png")

        attribute 1e:
            rain("/CHR/sima2/sima2_1_1e.png")

        attribute 1g:
            rain("/CHR/sima2/sima2_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima2/sima2_2_2a.png")

        attribute 2b:
            rain("/CHR/sima2/sima2_2_2b.png")

        attribute 2c:
            rain("/CHR/sima2/sima2_2_2c.png")

        attribute 2d:
            rain("/CHR/sima2/sima2_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima2/sima2_3_3a.png")

        attribute 3b:
            rain("/CHR/sima2/sima2_3_3b.png")

        attribute 3c:
            rain("/CHR/sima2/sima2_3_3c.png")

        attribute 3d:
            rain("/CHR/sima2/sima2_3_3d.png")

    ypos 1220
layeredimage sima2d3_rain:
    group clothes:
        attribute regular1 default:
            rain("/CHR/sima2/d3/sima2d3_clothes_regular1.png")

        attribute fancy1:
            rain("/CHR/sima2/d3/sima2d3_clothes_fancy1.png")

        attribute regular2:
            rain("/CHR/sima2/d3/sima2d3_clothes_regular2.png")

        attribute fancy2:
            rain("/CHR/sima2/d3/sima2d3_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima2/d3/sima2d3_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima2/d3/sima2d3_1_1a.png")

        attribute 1c:
            rain("/CHR/sima2/d3/sima2d3_1_1c.png")

        attribute 1d:
            rain("/CHR/sima2/d3/sima2d3_1_1d.png")

        attribute 1e:
            rain("/CHR/sima2/d3/sima2d3_1_1e.png")

        attribute 1g:
            rain("/CHR/sima2/d3/sima2d3_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima2/d3/sima2d3_2_2a.png")

        attribute 2b:
            rain("/CHR/sima2/d3/sima2d3_2_2b.png")

        attribute 2c:
            rain("/CHR/sima2/d3/sima2d3_2_2c.png")

        attribute 2d:
            rain("/CHR/sima2/d3/sima2d3_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima2/d3/sima2d3_3_3a.png")

        attribute 3b:
            rain("/CHR/sima2/d3/sima2d3_3_3b.png")

        attribute 3c:
            rain("/CHR/sima2/d3/sima2d3_3_3c.png")

        attribute 3d:
            rain("/CHR/sima2/d3/sima2d3_3_3d.png")
layeredimage sima2close_rain:
    group clothes:
        attribute regular1 default:
            rain("/CHR/sima2/close/sima2close_clothes_regular1.png")

        attribute fancy1:
            rain("/CHR/sima2/close/sima2close_clothes_fancy1.png")

        attribute regular2:
            rain("/CHR/sima2/close/sima2close_clothes_regular2.png")

        attribute fancy2:
            rain("/CHR/sima2/close/sima2close_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima2/close/sima2close_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima2/close/sima2close_1_1a.png")

        attribute 1c:
            rain("/CHR/sima2/close/sima2close_1_1c.png")

        attribute 1d:
            rain("/CHR/sima2/close/sima2close_1_1d.png")

        attribute 1e:
            rain("/CHR/sima2/close/sima2close_1_1e.png")

        attribute 1g:
            rain("/CHR/sima2/close/sima2close_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima2/close/sima2close_2_2a.png")

        attribute 2b:
            rain("/CHR/sima2/close/sima2close_2_2b.png")

        attribute 2c:
            rain("/CHR/sima2/close/sima2close_2_2c.png")

        attribute 2d:
            rain("/CHR/sima2/close/sima2close_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima2/close/sima2close_3_3a.png")

        attribute 3b:
            rain("/CHR/sima2/close/sima2close_3_3b.png")

        attribute 3c:
            rain("/CHR/sima2/close/sima2close_3_3c.png")

        attribute 3d:
            rain("/CHR/sima2/close/sima2close_3_3d.png")

    ypos 1445
layeredimage sima3a_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3a/sima3a_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3a/sima3a_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3a/sima3a_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3a/sima3a_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3a/sima3a_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3a/sima3a_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3a/sima3a_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3a/sima3a_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3a/sima3a_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3a/sima3a_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3a/sima3a_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3a/sima3a_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3a/sima3a_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3a/sima3a_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3a/sima3a_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3a/sima3a_3_3d.png")

    ypos 1230
layeredimage sima3ad3_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3a/d3/sima3ad3_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3a/d3/sima3ad3_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3a/d3/sima3ad3_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3a/d3/sima3ad3_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3a/d3/sima3ad3_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3a/d3/sima3ad3_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3a/d3/sima3ad3_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3a/d3/sima3ad3_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3a/d3/sima3ad3_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3a/d3/sima3ad3_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3a/d3/sima3ad3_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3a/d3/sima3ad3_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3a/d3/sima3ad3_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3a/d3/sima3ad3_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3a/d3/sima3ad3_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3a/d3/sima3ad3_3_3d.png")
layeredimage sima3aclose_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3a/close/sima3aclose_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3a/close/sima3aclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3a/close/sima3aclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3a/close/sima3aclose_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3a/close/sima3aclose_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3a/close/sima3aclose_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3a/close/sima3aclose_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3a/close/sima3aclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3a/close/sima3aclose_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3a/close/sima3aclose_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3a/close/sima3aclose_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3a/close/sima3aclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3a/close/sima3aclose_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3a/close/sima3aclose_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3a/close/sima3aclose_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3a/close/sima3aclose_3_3d.png")

    ypos 1485
layeredimage sima3b_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3b/sima3b_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3b/sima3b_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3b/sima3b_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3b/sima3b_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3b/sima3b_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3b/sima3b_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3b/sima3b_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3b/sima3b_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3b/sima3b_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3b/sima3b_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3b/sima3b_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3b/sima3b_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3b/sima3b_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3b/sima3b_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3b/sima3b_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3b/sima3b_3_3d.png")

    ypos 1230
layeredimage sima3bd3_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3b/d3/sima3bd3_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3b/d3/sima3bd3_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3b/d3/sima3bd3_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3b/d3/sima3bd3_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3b/d3/sima3bd3_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3b/d3/sima3bd3_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3b/d3/sima3bd3_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3b/d3/sima3bd3_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3b/d3/sima3bd3_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3b/d3/sima3bd3_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3b/d3/sima3bd3_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3b/d3/sima3bd3_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3b/d3/sima3bd3_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3b/d3/sima3bd3_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3b/d3/sima3bd3_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3b/d3/sima3bd3_3_3d.png")
layeredimage sima3bclose_rain:
    group clothes:
        attribute regular2 default:
            rain("/CHR/sima3b/close/sima3bclose_clothes_regular.png")

        attribute fancy2:
            rain("/CHR/sima3b/close/sima3bclose_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            rain("/CHR/sima3b/close/sima3bclose_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            rain("/CHR/sima3b/close/sima3bclose_1_1a.png")

        attribute 1c:
            rain("/CHR/sima3b/close/sima3bclose_1_1c.png")

        attribute 1d:
            rain("/CHR/sima3b/close/sima3bclose_1_1d.png")

        attribute 1e:
            rain("/CHR/sima3b/close/sima3bclose_1_1e.png")

        attribute 1g:
            rain("/CHR/sima3b/close/sima3bclose_1_1g.png")

    group 2 auto:
        attribute 2a default:
            rain("/CHR/sima3b/close/sima3bclose_2_2a.png")

        attribute 2b:
            rain("/CHR/sima3b/close/sima3bclose_2_2b.png")

        attribute 2c:
            rain("/CHR/sima3b/close/sima3bclose_2_2c.png")

        attribute 2d:
            rain("/CHR/sima3b/close/sima3bclose_2_2d.png")

    group 3 auto:
        attribute 3a default:
            rain("/CHR/sima3b/close/sima3bclose_3_3a.png")

        attribute 3b:
            rain("/CHR/sima3b/close/sima3bclose_3_3b.png")

        attribute 3c:
            rain("/CHR/sima3b/close/sima3bclose_3_3c.png")

        attribute 3d:
            rain("/CHR/sima3b/close/sima3bclose_3_3d.png")

    ypos 1485
layeredimage ermy1_rain:
        group clothes:
            attribute pose1 default:
                rain("/CHR/ermy/ermy1_pose_pose1.png")
            attribute pose2:
                rain("/CHR/ermy/ermy1_pose_pose2.png")
        group blush:
            attribute noblush default:
                "null_image"
            attribute blush:
                rain("/CHR/ermy/ermy1_blush_blush.png")
        group 1 auto:
            attribute 1a default:
                rain("/CHR/ermy/ermy1_1_1a.png")
            attribute 1b:
                rain("/CHR/ermy/ermy1_1_1b.png")
            attribute 1c:
                rain("/CHR/ermy/ermy1_1_1c.png")
            attribute 1d:
                rain("/CHR/ermy/ermy1_1_1d.png")
            attribute 1e:
                rain("/CHR/ermy/ermy1_1_1e.png")
            attribute 1f:
                rain("/CHR/ermy/ermy1_1_1f.png")
            attribute 1g:
                rain("/CHR/ermy/ermy1_1_1g.png")
            attribute 1h:
                rain("/CHR/ermy/ermy1_1_1h.png")
        group 2 auto:
            attribute 2a default:
                rain("/CHR/ermy/ermy1_2_2a.png")
            attribute 2b:
                rain("/CHR/ermy/ermy1_2_2b.png")
            attribute 2c:
                rain("/CHR/ermy/ermy1_2_2c.png")
            attribute 2d:
                rain("/CHR/ermy/ermy1_2_2d.png")
        group 3 auto:
            attribute 3a default:
                rain("/CHR/ermy/ermy1_3_3a.png")
            attribute 3b:
                rain("/CHR/ermy/ermy1_3_3b.png")
            attribute 3c:
                rain("/CHR/ermy/ermy1_3_3c.png")
            attribute 3d:
                rain("/CHR/ermy/ermy1_3_3d.png")
        ypos 1270
layeredimage teya1_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/teya1/teya1_clothes_regular.png")
        attribute fancy:
            rain("/CHR/teya1/teya1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/sima1/sima1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/teya1/teya1_1_1a.png")
        attribute 1b:
            rain("/CHR/teya1/teya1_1_1b.png")
        attribute 1c:
            rain("/CHR/teya1/teya1_1_1c.png")
        attribute 1d:
            rain("/CHR/teya1/teya1_1_1d.png")
        attribute 1e:
            rain("/CHR/teya1/teya1_1_1e.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/teya1/teya1_2_2a.png")
        attribute 2b:
            rain("/CHR/teya1/teya1_2_2b.png")
        attribute 2c:
            rain("/CHR/teya1/teya1_2_2c.png")
        attribute 2d:
            rain("/CHR/teya1/teya1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/teya1/teya1_3_3a.png")
        attribute 3b:
            rain("/CHR/teya1/teya1_3_3b.png")
        attribute 3c:
            rain("/CHR/teya1/teya1_3_3c.png")
        attribute 3d:
            rain("/CHR/teya1/teya1_3_3d.png")
    ypos 1230
layeredimage teya2_baw:
    group clothes:
        attribute regularhand1 default:
            baw("/CHR/teya2/teya2_clothes_regularhand1.png")
        attribute fancyhand1:
            baw("/CHR/teya2/teya2_clothes_fancyhand1.png")
        attribute regularhand2:
            baw("/CHR/teya2/teya2_clothes_regularhand2.png")
        attribute fancyhand2:
            baw("/CHR/teya2/teya2_clothes_fancyhand2.png")
        attribute regularhand3:
            baw("/CHR/teya2/teya2_clothes_regularhand3.png")
        attribute fancyhand3:
            baw("/CHR/teya2/teya2_clothes_fancyhand3.png")
        attribute regularhand4:
            baw("/CHR/teya2/teya2_clothes_regularhand4.png")
        attribute fancyhand4:
            baw("/CHR/teya2/teya2_clothes_fancyhand4.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            baw("/CHR/teya2/teya2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            baw("/CHR/teya2/teya2_1_1a.png")
        attribute 1b:
            baw("/CHR/teya2/teya2_1_1b.png")
        attribute 1c:
            baw("/CHR/teya2/teya2_1_1c.png")
        attribute 1d:
            baw("/CHR/teya2/teya2_1_1d.png")
        attribute 1e:
            baw("/CHR/teya2/teya2_1_1e.png")
    group 2 auto:
        attribute 2a default:
            baw("/CHR/teya2/teya2_2_2a.png")
        attribute 2b:
            baw("/CHR/teya2/teya2_2_2b.png")
        attribute 2c:
            baw("/CHR/teya2/teya2_2_2c.png")
        attribute 2d:
            baw("/CHR/teya2/teya2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            baw("/CHR/teya2/teya2_3_3a.png")
        attribute 3b:
            baw("/CHR/teya2/teya2_3_3b.png")
        attribute 3c:
            baw("/CHR/teya2/teya2_3_3c.png")
        attribute 3d:
            baw("/CHR/teya2/teya2_3_3d.png")
    ypos 1230
layeredimage teya2_rain:
    group clothes:
        attribute regularhand1 default:
            rain("/CHR/teya2/teya2_clothes_regularhand1.png")
        attribute fancyhand1:
            rain("/CHR/teya2/teya2_clothes_fancyhand1.png")
        attribute regularhand2:
            rain("/CHR/teya2/teya2_clothes_regularhand2.png")
        attribute fancyhand2:
            rain("/CHR/teya2/teya2_clothes_fancyhand2.png")
        attribute regularhand3:
            rain("/CHR/teya2/teya2_clothes_regularhand3.png")
        attribute fancyhand3:
            rain("/CHR/teya2/teya2_clothes_fancyhand3.png")
        attribute regularhand4:
            rain("/CHR/teya2/teya2_clothes_regularhand4.png")
        attribute fancyhand4:
            rain("/CHR/teya2/teya2_clothes_fancyhand4.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/teya2/teya2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/teya2/teya2_1_1a.png")
        attribute 1b:
            rain("/CHR/teya2/teya2_1_1b.png")
        attribute 1c:
            rain("/CHR/teya2/teya2_1_1c.png")
        attribute 1d:
            rain("/CHR/teya2/teya2_1_1d.png")
        attribute 1e:
            rain("/CHR/teya2/teya2_1_1e.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/teya2/teya2_2_2a.png")
        attribute 2b:
            rain("/CHR/teya2/teya2_2_2b.png")
        attribute 2c:
            rain("/CHR/teya2/teya2_2_2c.png")
        attribute 2d:
            rain("/CHR/teya2/teya2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/teya2/teya2_3_3a.png")
        attribute 3b:
            rain("/CHR/teya2/teya2_3_3b.png")
        attribute 3c:
            rain("/CHR/teya2/teya2_3_3c.png")
        attribute 3d:
            rain("/CHR/teya2/teya2_3_3d.png")
    ypos 1230
layeredimage teya3_rain:
    group clothes:
        attribute regular default:
            rain("/CHR/teya3/teya3_clothes_regular.png")
        attribute fancy:
            rain("/CHR/teya3/teya3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            rain("/CHR/teya3/teya3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            rain("/CHR/teya3/teya3_1_1a.png")
        attribute 1b:
            rain("/CHR/teya3/teya3_1_1b.png")
        attribute 1c:
            rain("/CHR/teya3/teya3_1_1c.png")
        attribute 1d:
            rain("/CHR/teya3/teya3_1_1d.png")
        attribute 1e:
            rain("/CHR/teya3/teya3_1_1e.png")
    group 2 auto:
        attribute 2a default:
            rain("/CHR/teya3/teya3_2_2a.png")
        attribute 2b:
            rain("/CHR/teya3/teya3_2_2b.png")
        attribute 2c:
            rain("/CHR/teya3/teya3_2_2c.png")
        attribute 2d:
            rain("/CHR/teya3/teya3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            rain("/CHR/teya3/teya3_3_3a.png")
        attribute 3b:
            rain("/CHR/teya3/teya3_3_3b.png")
        attribute 3c:
            rain("/CHR/teya3/teya3_3_3c.png")
        attribute 3d:
            rain("/CHR/teya3/teya3_3_3d.png")
    ypos 1230
layeredimage nana3_runight:
    group clothes:
        attribute regular default:
            runight("/CHR/nana3/nana3_clothes_regular.png")
        attribute fancy:
            runight("/CHR/nana3/nana3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana3/nana3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana3/nana3_1_1a.png")
        attribute 1b:
            runight("/CHR/nana3/nana3_1_1b.png")
        attribute 1c:
            runight("/CHR/nana3/nana3_1_1c.png")
        attribute 1d:
            runight("/CHR/nana3/nana3_1_1d.png")
        attribute 1e:
            runight("/CHR/nana3/nana3_1_1e.png")
        attribute 1f:
            runight("/CHR/nana3/nana3_1_1f.png")
        attribute 1g:
            runight("/CHR/nana3/nana3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana3/nana3_2_2a.png")
        attribute 2b:
            runight("/CHR/nana3/nana3_2_2b.png")
        attribute 2c:
            runight("/CHR/nana3/nana3_2_2c.png")
        attribute 2d:
            runight("/CHR/nana3/nana3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana3/nana3_3_3a.png")
        attribute 3b:
            runight("/CHR/nana3/nana3_3_3b.png")
        attribute 3c:
            runight("/CHR/nana3/nana3_3_3c.png")
        attribute 3d:
            runight("/CHR/nana3/nana3_3_3d.png")
    ypos 1250
layeredimage nana2_runight:
    group clothes:
        attribute regular default:
            runight("/CHR/nana2/nana2_clothes_regular.png")
        attribute fancy:
            runight("/CHR/nana2/nana2_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana2/nana2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana2/nana2_1_1a.png")
        attribute 1b:
            runight("/CHR/nana2/nana2_1_1b.png")
        attribute 1c:
            runight("/CHR/nana2/nana2_1_1c.png")
        attribute 1d:
            runight("/CHR/nana2/nana2_1_1d.png")
        attribute 1e:
            runight("/CHR/nana2/nana2_1_1e.png")
        attribute 1f:
            runight("/CHR/nana2/nana2_1_1f.png")
        attribute 1g:
            runight("/CHR/nana2/nana2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana2/nana2_2_2a.png")
        attribute 2b:
            runight("/CHR/nana2/nana2_2_2b.png")
        attribute 2c:
            runight("/CHR/nana2/nana2_2_2c.png")
        attribute 2d:
            runight("/CHR/nana2/nana2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana2/nana2_3_3a.png")
        attribute 3b:
            runight("/CHR/nana2/nana2_3_3b.png")
        attribute 3c:
            runight("/CHR/nana2/nana2_3_3c.png")
        attribute 3d:
            runight("/CHR/nana2/nana2_3_3d.png")
    ypos 1250
layeredimage nana1_runight:
    group clothes:
        attribute regular2 default:
            runight("/CHR/nana1/nana1_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/nana1/nana1_clothes_fancy2.png")
        attribute regular1:
            runight("/CHR/nana1/nana1_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/nana1/nana1_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/nana1/nana1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/nana1/nana1_1_1a.png")
        attribute 1b:
            runight("/CHR/nana1/nana1_1_1b.png")
        attribute 1c:
            runight("/CHR/nana1/nana1_1_1c.png")
        attribute 1d:
            runight("/CHR/nana1/nana1_1_1d.png")
        attribute 1e:
            runight("/CHR/nana1/nana1_1_1e.png")
        attribute 1f:
            runight("/CHR/nana1/nana1_1_1f.png")
        attribute 1g:
            runight("/CHR/nana1/nana1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/nana1/nana1_2_2a.png")
        attribute 2b:
            runight("/CHR/nana1/nana1_2_2b.png")
        attribute 2c:
            runight("/CHR/nana1/nana1_2_2c.png")
        attribute 2d:
            runight("/CHR/nana1/nana1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/nana1/nana1_3_3a.png")
        attribute 3b:
            runight("/CHR/nana1/nana1_3_3b.png")
        attribute 3c:
            runight("/CHR/nana1/nana1_3_3c.png")
        attribute 3d:
            runight("/CHR/nana1/nana1_3_3d.png")
    ypos 1250
layeredimage marta3_runight:
    group clothes:
        attribute regular2:
            runight("/CHR/marta3/marta3_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/marta3/marta3_clothes_fancy2.png")
        attribute regular1 default:
            runight("/CHR/marta3/marta3_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/marta3/marta3_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta3/marta3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta3/marta3_1_1a.png")
        attribute 1b:
            runight("/CHR/marta3/marta3_1_1b.png")
        attribute 1c:
            runight("/CHR/marta3/marta3_1_1c.png")
        attribute 1d:
            runight("/CHR/marta3/marta3_1_1d.png")
        attribute 1e:
            runight("/CHR/marta3/marta3_1_1e.png")
        attribute 1f:
            runight("/CHR/marta3/marta3_1_1f.png")
        attribute 1g:
            runight("/CHR/marta3/marta3_1_1g.png")
        attribute 1aa:
            runight("/CHR/marta3/marta3_1_1aa.png")
        attribute 1bb:
            runight("/CHR/marta3/marta3_1_1bb.png")
        attribute 1cc:
            runight("/CHR/marta3/marta3_1_1cc.png")
        attribute 1dd:
            runight("/CHR/marta3/marta3_1_1dd.png")
        attribute 1ee:
            runight("/CHR/marta3/marta3_1_1ee.png")
        attribute 1ff:
            runight("/CHR/marta3/marta3_1_1ff.png")
        attribute 1gg:
            runight("/CHR/marta3/marta3_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta3/marta3_2_2a.png")
        attribute 2b:
            runight("/CHR/marta3/marta3_2_2b.png")
        attribute 2c:
            runight("/CHR/marta3/marta3_2_2c.png")
        attribute 2d:
            runight("/CHR/marta3/marta3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta3/marta3_3_3a.png")
        attribute 3b:
            runight("/CHR/marta3/marta3_3_3b.png")
        attribute 3c:
            runight("/CHR/marta3/marta3_3_3c.png")
        attribute 3d:
            runight("/CHR/marta3/marta3_3_3d.png")
    ypos 1270
layeredimage marta2_runight:
    group clothes:
        attribute regular1 default:
            runight("/CHR/marta2/marta2_clothes_regular1.png")
        attribute fancy1:
            runight("/CHR/marta2/marta2_clothes_fancy1.png")
        attribute regular2:
            runight("/CHR/marta2/marta2_clothes_regular2.png")
        attribute fancy2:
            runight("/CHR/marta2/marta2_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta2/marta2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta2/marta2_1_1a.png")
        attribute 1b:
            runight("/CHR/marta2/marta2_1_1b.png")
        attribute 1c:
            runight("/CHR/marta2/marta2_1_1c.png")
        attribute 1d:
            runight("/CHR/marta2/marta2_1_1d.png")
        attribute 1e:
            runight("/CHR/marta2/marta2_1_1e.png")
        attribute 1f:
            runight("/CHR/marta2/marta2_1_1f.png")
        attribute 1g:
            runight("/CHR/marta2/marta2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta2/marta2_2_2a.png")
        attribute 2b:
            runight("/CHR/marta2/marta2_2_2b.png")
        attribute 2c:
            runight("/CHR/marta2/marta2_2_2c.png")
        attribute 2d:
            runight("/CHR/marta2/marta2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta2/marta2_3_3a.png")
        attribute 3b:
            runight("/CHR/marta2/marta2_3_3b.png")
        attribute 3c:
            runight("/CHR/marta2/marta2_3_3c.png")
        attribute 3d:
            runight("/CHR/marta2/marta2_3_3d.png")
    ypos 1270
layeredimage marta1_runight:
    group clothes:
        attribute regular2 default:
            runight("/CHR/marta1/marta1_clothes_regular1.png")
        attribute fancy2:
            runight("/CHR/marta1/marta1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            runight("/CHR/marta1/marta1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            runight("/CHR/marta1/marta1_1_1a.png")
        attribute 1b:
            runight("/CHR/marta1/marta1_1_1b.png")
        attribute 1c:
            runight("/CHR/marta1/marta1_1_1c.png")
        attribute 1d:
            runight("/CHR/marta1/marta1_1_1d.png")
        attribute 1e:
            runight("/CHR/marta1/marta1_1_1e.png")
        attribute 1f:
            runight("/CHR/marta1/marta1_1_1f.png")
        attribute 1g:
            runight("/CHR/marta1/marta1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            runight("/CHR/marta1/marta1_2_2a.png")
        attribute 2b:
            runight("/CHR/marta1/marta1_2_2b.png")
        attribute 2c:
            runight("/CHR/marta1/marta1_2_2c.png")
        attribute 2d:
            runight("/CHR/marta1/marta1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            runight("/CHR/marta1/marta1_3_3a.png")
        attribute 3b:
            runight("/CHR/marta1/marta1_3_3b.png")
        attribute 3c:
            runight("/CHR/marta1/marta1_3_3c.png")
        attribute 3d:
            runight("/CHR/marta1/marta1_3_3d.png")
    ypos 1270
layeredimage sima1_runight:
    group clothes:
        attribute regular default:
            runight("/CHR/sima1/sima1_clothes_regular.png")

        attribute fancy:
            runight("/CHR/sima1/sima1_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima1/sima1_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima1/sima1_1_1a.png")

        attribute 1c:
            runight("/CHR/sima1/sima1_1_1c.png")

        attribute 1d:
            runight("/CHR/sima1/sima1_1_1d.png")

        attribute 1e:
            runight("/CHR/sima1/sima1_1_1e.png")

        attribute 1g:
            runight("/CHR/sima1/sima1_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima1/sima1_2_2a.png")

        attribute 2b:
            runight("/CHR/sima1/sima1_2_2b.png")

        attribute 2c:
            runight("/CHR/sima1/sima1_2_2c.png")

        attribute 2d:
            runight("/CHR/sima1/sima1_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima1/sima1_3_3a.png")

        attribute 3b:
            runight("/CHR/sima1/sima1_3_3b.png")

        attribute 3c:
            runight("/CHR/sima1/sima1_3_3c.png")

        attribute 3d:
            runight("/CHR/sima1/sima1_3_3d.png")

    ypos 1240
layeredimage sima2_runight:
    group clothes:
        attribute regular1 default:
            runight("/CHR/sima2/sima2_clothes_regular1.png")

        attribute fancy1:
            runight("/CHR/sima2/sima2_clothes_fancy1.png")

        attribute regular2:
            runight("/CHR/sima2/sima2_clothes_regular2.png")

        attribute fancy2:
            runight("/CHR/sima2/sima2_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima2/sima2_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima2/sima2_1_1a.png")

        attribute 1c:
            runight("/CHR/sima2/sima2_1_1c.png")

        attribute 1d:
            runight("/CHR/sima2/sima2_1_1d.png")

        attribute 1e:
            runight("/CHR/sima2/sima2_1_1e.png")

        attribute 1g:
            runight("/CHR/sima2/sima2_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima2/sima2_2_2a.png")

        attribute 2b:
            runight("/CHR/sima2/sima2_2_2b.png")

        attribute 2c:
            runight("/CHR/sima2/sima2_2_2c.png")

        attribute 2d:
            runight("/CHR/sima2/sima2_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima2/sima2_3_3a.png")

        attribute 3b:
            runight("/CHR/sima2/sima2_3_3b.png")

        attribute 3c:
            runight("/CHR/sima2/sima2_3_3c.png")

        attribute 3d:
            runight("/CHR/sima2/sima2_3_3d.png")

    ypos 1220
layeredimage sima3a_runight:
    group clothes:
        attribute regular2 default:
            runight("/CHR/sima3a/sima3a_clothes_regular.png")

        attribute fancy2:
            runight("/CHR/sima3a/sima3a_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima3a/sima3a_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima3a/sima3a_1_1a.png")

        attribute 1c:
            runight("/CHR/sima3a/sima3a_1_1c.png")

        attribute 1d:
            runight("/CHR/sima3a/sima3a_1_1d.png")

        attribute 1e:
            runight("/CHR/sima3a/sima3a_1_1e.png")

        attribute 1g:
            runight("/CHR/sima3a/sima3a_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima3a/sima3a_2_2a.png")

        attribute 2b:
            runight("/CHR/sima3a/sima3a_2_2b.png")

        attribute 2c:
            runight("/CHR/sima3a/sima3a_2_2c.png")

        attribute 2d:
            runight("/CHR/sima3a/sima3a_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima3a/sima3a_3_3a.png")

        attribute 3b:
            runight("/CHR/sima3a/sima3a_3_3b.png")

        attribute 3c:
            runight("/CHR/sima3a/sima3a_3_3c.png")

        attribute 3d:
            runight("/CHR/sima3a/sima3a_3_3d.png")

    ypos 1230
layeredimage sima3b_runight:
    group clothes:
        attribute regular2 default:
            runight("/CHR/sima3b/sima3b_clothes_regular.png")

        attribute fancy2:
            runight("/CHR/sima3b/sima3b_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            runight("/CHR/sima3b/sima3b_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            runight("/CHR/sima3b/sima3b_1_1a.png")

        attribute 1c:
            runight("/CHR/sima3b/sima3b_1_1c.png")

        attribute 1d:
            runight("/CHR/sima3b/sima3b_1_1d.png")

        attribute 1e:
            runight("/CHR/sima3b/sima3b_1_1e.png")

        attribute 1g:
            runight("/CHR/sima3b/sima3b_1_1g.png")

    group 2 auto:
        attribute 2a default:
            runight("/CHR/sima3b/sima3b_2_2a.png")

        attribute 2b:
            runight("/CHR/sima3b/sima3b_2_2b.png")

        attribute 2c:
            runight("/CHR/sima3b/sima3b_2_2c.png")

        attribute 2d:
            runight("/CHR/sima3b/sima3b_2_2d.png")

    group 3 auto:
        attribute 3a default:
            runight("/CHR/sima3b/sima3b_3_3a.png")

        attribute 3b:
            runight("/CHR/sima3b/sima3b_3_3b.png")

        attribute 3c:
            runight("/CHR/sima3b/sima3b_3_3c.png")

        attribute 3d:
            runight("/CHR/sima3b/sima3b_3_3d.png")

    ypos 1230
layeredimage nana3_grey:
    group clothes:
        attribute regular default:
            grey("/CHR/nana3/nana3_clothes_regular.png")
        attribute fancy:
            grey("/CHR/nana3/nana3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/nana3/nana3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/nana3/nana3_1_1a.png")
        attribute 1b:
            grey("/CHR/nana3/nana3_1_1b.png")
        attribute 1c:
            grey("/CHR/nana3/nana3_1_1c.png")
        attribute 1d:
            grey("/CHR/nana3/nana3_1_1d.png")
        attribute 1e:
            grey("/CHR/nana3/nana3_1_1e.png")
        attribute 1f:
            grey("/CHR/nana3/nana3_1_1f.png")
        attribute 1g:
            grey("/CHR/nana3/nana3_1_1g.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/nana3/nana3_2_2a.png")
        attribute 2b:
            grey("/CHR/nana3/nana3_2_2b.png")
        attribute 2c:
            grey("/CHR/nana3/nana3_2_2c.png")
        attribute 2d:
            grey("/CHR/nana3/nana3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/nana3/nana3_3_3a.png")
        attribute 3b:
            grey("/CHR/nana3/nana3_3_3b.png")
        attribute 3c:
            grey("/CHR/nana3/nana3_3_3c.png")
        attribute 3d:
            grey("/CHR/nana3/nana3_3_3d.png")
    ypos 1250
layeredimage nana2_grey:
    group clothes:
        attribute regular default:
            grey("/CHR/nana2/nana2_clothes_regular.png")
        attribute fancy:
            grey("/CHR/nana2/nana2_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/nana2/nana2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/nana2/nana2_1_1a.png")
        attribute 1b:
            grey("/CHR/nana2/nana2_1_1b.png")
        attribute 1c:
            grey("/CHR/nana2/nana2_1_1c.png")
        attribute 1d:
            grey("/CHR/nana2/nana2_1_1d.png")
        attribute 1e:
            grey("/CHR/nana2/nana2_1_1e.png")
        attribute 1f:
            grey("/CHR/nana2/nana2_1_1f.png")
        attribute 1g:
            grey("/CHR/nana2/nana2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/nana2/nana2_2_2a.png")
        attribute 2b:
            grey("/CHR/nana2/nana2_2_2b.png")
        attribute 2c:
            grey("/CHR/nana2/nana2_2_2c.png")
        attribute 2d:
            grey("/CHR/nana2/nana2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/nana2/nana2_3_3a.png")
        attribute 3b:
            grey("/CHR/nana2/nana2_3_3b.png")
        attribute 3c:
            grey("/CHR/nana2/nana2_3_3c.png")
        attribute 3d:
            grey("/CHR/nana2/nana2_3_3d.png")
    ypos 1250
layeredimage nana1_grey:
    group clothes:
        attribute regular2 default:
            grey("/CHR/nana1/nana1_clothes_regular2.png")
        attribute fancy2:
            grey("/CHR/nana1/nana1_clothes_fancy2.png")
        attribute regular1:
            grey("/CHR/nana1/nana1_clothes_regular1.png")
        attribute fancy1:
            grey("/CHR/nana1/nana1_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/nana1/nana1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/nana1/nana1_1_1a.png")
        attribute 1b:
            grey("/CHR/nana1/nana1_1_1b.png")
        attribute 1c:
            grey("/CHR/nana1/nana1_1_1c.png")
        attribute 1d:
            grey("/CHR/nana1/nana1_1_1d.png")
        attribute 1e:
            grey("/CHR/nana1/nana1_1_1e.png")
        attribute 1f:
            grey("/CHR/nana1/nana1_1_1f.png")
        attribute 1g:
            grey("/CHR/nana1/nana1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/nana1/nana1_2_2a.png")
        attribute 2b:
            grey("/CHR/nana1/nana1_2_2b.png")
        attribute 2c:
            grey("/CHR/nana1/nana1_2_2c.png")
        attribute 2d:
            grey("/CHR/nana1/nana1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/nana1/nana1_3_3a.png")
        attribute 3b:
            grey("/CHR/nana1/nana1_3_3b.png")
        attribute 3c:
            grey("/CHR/nana1/nana1_3_3c.png")
        attribute 3d:
            grey("/CHR/nana1/nana1_3_3d.png")
    ypos 1250
layeredimage marta3_grey:
    group clothes:
        attribute regular2:
            grey("/CHR/marta3/marta3_clothes_regular2.png")
        attribute fancy2:
            grey("/CHR/marta3/marta3_clothes_fancy2.png")
        attribute regular1 default:
            grey("/CHR/marta3/marta3_clothes_regular1.png")
        attribute fancy1:
            grey("/CHR/marta3/marta3_clothes_fancy1.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/marta3/marta3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/marta3/marta3_1_1a.png")
        attribute 1b:
            grey("/CHR/marta3/marta3_1_1b.png")
        attribute 1c:
            grey("/CHR/marta3/marta3_1_1c.png")
        attribute 1d:
            grey("/CHR/marta3/marta3_1_1d.png")
        attribute 1e:
            grey("/CHR/marta3/marta3_1_1e.png")
        attribute 1f:
            grey("/CHR/marta3/marta3_1_1f.png")
        attribute 1g:
            grey("/CHR/marta3/marta3_1_1g.png")
        attribute 1aa:
            grey("/CHR/marta3/marta3_1_1aa.png")
        attribute 1bb:
            grey("/CHR/marta3/marta3_1_1bb.png")
        attribute 1cc:
            grey("/CHR/marta3/marta3_1_1cc.png")
        attribute 1dd:
            grey("/CHR/marta3/marta3_1_1dd.png")
        attribute 1ee:
            grey("/CHR/marta3/marta3_1_1ee.png")
        attribute 1ff:
            grey("/CHR/marta3/marta3_1_1ff.png")
        attribute 1gg:
            grey("/CHR/marta3/marta3_1_1gg.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/marta3/marta3_2_2a.png")
        attribute 2b:
            grey("/CHR/marta3/marta3_2_2b.png")
        attribute 2c:
            grey("/CHR/marta3/marta3_2_2c.png")
        attribute 2d:
            grey("/CHR/marta3/marta3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/marta3/marta3_3_3a.png")
        attribute 3b:
            grey("/CHR/marta3/marta3_3_3b.png")
        attribute 3c:
            grey("/CHR/marta3/marta3_3_3c.png")
        attribute 3d:
            grey("/CHR/marta3/marta3_3_3d.png")
    ypos 1270
layeredimage marta2_grey:
    group clothes:
        attribute regular1 default:
            grey("/CHR/marta2/marta2_clothes_regular1.png")
        attribute fancy1:
            grey("/CHR/marta2/marta2_clothes_fancy1.png")
        attribute regular2:
            grey("/CHR/marta2/marta2_clothes_regular2.png")
        attribute fancy2:
            grey("/CHR/marta2/marta2_clothes_fancy2.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/marta2/marta2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/marta2/marta2_1_1a.png")
        attribute 1b:
            grey("/CHR/marta2/marta2_1_1b.png")
        attribute 1c:
            grey("/CHR/marta2/marta2_1_1c.png")
        attribute 1d:
            grey("/CHR/marta2/marta2_1_1d.png")
        attribute 1e:
            grey("/CHR/marta2/marta2_1_1e.png")
        attribute 1f:
            grey("/CHR/marta2/marta2_1_1f.png")
        attribute 1g:
            grey("/CHR/marta2/marta2_1_1g.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/marta2/marta2_2_2a.png")
        attribute 2b:
            grey("/CHR/marta2/marta2_2_2b.png")
        attribute 2c:
            grey("/CHR/marta2/marta2_2_2c.png")
        attribute 2d:
            grey("/CHR/marta2/marta2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/marta2/marta2_3_3a.png")
        attribute 3b:
            grey("/CHR/marta2/marta2_3_3b.png")
        attribute 3c:
            grey("/CHR/marta2/marta2_3_3c.png")
        attribute 3d:
            grey("/CHR/marta2/marta2_3_3d.png")
    ypos 1270
layeredimage marta1_grey:
    group clothes:
        attribute regular2 default:
            grey("/CHR/marta1/marta1_clothes_regular1.png")
        attribute fancy2:
            grey("/CHR/marta1/marta1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/marta1/marta1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/marta1/marta1_1_1a.png")
        attribute 1b:
            grey("/CHR/marta1/marta1_1_1b.png")
        attribute 1c:
            grey("/CHR/marta1/marta1_1_1c.png")
        attribute 1d:
            grey("/CHR/marta1/marta1_1_1d.png")
        attribute 1e:
            grey("/CHR/marta1/marta1_1_1e.png")
        attribute 1f:
            grey("/CHR/marta1/marta1_1_1f.png")
        attribute 1g:
            grey("/CHR/marta1/marta1_1_1g.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/marta1/marta1_2_2a.png")
        attribute 2b:
            grey("/CHR/marta1/marta1_2_2b.png")
        attribute 2c:
            grey("/CHR/marta1/marta1_2_2c.png")
        attribute 2d:
            grey("/CHR/marta1/marta1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/marta1/marta1_3_3a.png")
        attribute 3b:
            grey("/CHR/marta1/marta1_3_3b.png")
        attribute 3c:
            grey("/CHR/marta1/marta1_3_3c.png")
        attribute 3d:
            grey("/CHR/marta1/marta1_3_3d.png")
    ypos 1270
layeredimage sima1_grey:
    group clothes:
        attribute regular default:
            grey("/CHR/sima1/sima1_clothes_regular.png")

        attribute fancy:
            grey("/CHR/sima1/sima1_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            grey("/CHR/sima1/sima1_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            grey("/CHR/sima1/sima1_1_1a.png")

        attribute 1c:
            grey("/CHR/sima1/sima1_1_1c.png")

        attribute 1d:
            grey("/CHR/sima1/sima1_1_1d.png")

        attribute 1e:
            grey("/CHR/sima1/sima1_1_1e.png")

        attribute 1g:
            grey("/CHR/sima1/sima1_1_1g.png")

    group 2 auto:
        attribute 2a default:
            grey("/CHR/sima1/sima1_2_2a.png")

        attribute 2b:
            grey("/CHR/sima1/sima1_2_2b.png")

        attribute 2c:
            grey("/CHR/sima1/sima1_2_2c.png")

        attribute 2d:
            grey("/CHR/sima1/sima1_2_2d.png")

    group 3 auto:
        attribute 3a default:
            grey("/CHR/sima1/sima1_3_3a.png")

        attribute 3b:
            grey("/CHR/sima1/sima1_3_3b.png")

        attribute 3c:
            grey("/CHR/sima1/sima1_3_3c.png")

        attribute 3d:
            grey("/CHR/sima1/sima1_3_3d.png")

    ypos 1240
layeredimage sima2_grey:
    group clothes:
        attribute regular1 default:
            grey("/CHR/sima2/sima2_clothes_regular1.png")

        attribute fancy1:
            grey("/CHR/sima2/sima2_clothes_fancy1.png")

        attribute regular2:
            grey("/CHR/sima2/sima2_clothes_regular2.png")

        attribute fancy2:
            grey("/CHR/sima2/sima2_clothes_fancy2.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            grey("/CHR/sima2/sima2_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            grey("/CHR/sima2/sima2_1_1a.png")

        attribute 1c:
            grey("/CHR/sima2/sima2_1_1c.png")

        attribute 1d:
            grey("/CHR/sima2/sima2_1_1d.png")

        attribute 1e:
            grey("/CHR/sima2/sima2_1_1e.png")

        attribute 1g:
            grey("/CHR/sima2/sima2_1_1g.png")

    group 2 auto:
        attribute 2a default:
            grey("/CHR/sima2/sima2_2_2a.png")

        attribute 2b:
            grey("/CHR/sima2/sima2_2_2b.png")

        attribute 2c:
            grey("/CHR/sima2/sima2_2_2c.png")

        attribute 2d:
            grey("/CHR/sima2/sima2_2_2d.png")

    group 3 auto:
        attribute 3a default:
            grey("/CHR/sima2/sima2_3_3a.png")

        attribute 3b:
            grey("/CHR/sima2/sima2_3_3b.png")

        attribute 3c:
            grey("/CHR/sima2/sima2_3_3c.png")

        attribute 3d:
            grey("/CHR/sima2/sima2_3_3d.png")

    ypos 1220
layeredimage sima3a_grey:
    group clothes:
        attribute regular2 default:
            grey("/CHR/sima3a/sima3a_clothes_regular.png")

        attribute fancy2:
            grey("/CHR/sima3a/sima3a_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            grey("/CHR/sima3a/sima3a_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            grey("/CHR/sima3a/sima3a_1_1a.png")

        attribute 1c:
            grey("/CHR/sima3a/sima3a_1_1c.png")

        attribute 1d:
            grey("/CHR/sima3a/sima3a_1_1d.png")

        attribute 1e:
            grey("/CHR/sima3a/sima3a_1_1e.png")

        attribute 1g:
            grey("/CHR/sima3a/sima3a_1_1g.png")

    group 2 auto:
        attribute 2a default:
            grey("/CHR/sima3a/sima3a_2_2a.png")

        attribute 2b:
            grey("/CHR/sima3a/sima3a_2_2b.png")

        attribute 2c:
            grey("/CHR/sima3a/sima3a_2_2c.png")

        attribute 2d:
            grey("/CHR/sima3a/sima3a_2_2d.png")

    group 3 auto:
        attribute 3a default:
            grey("/CHR/sima3a/sima3a_3_3a.png")

        attribute 3b:
            grey("/CHR/sima3a/sima3a_3_3b.png")

        attribute 3c:
            grey("/CHR/sima3a/sima3a_3_3c.png")

        attribute 3d:
            grey("/CHR/sima3a/sima3a_3_3d.png")

    ypos 1230
layeredimage sima3b_grey:
    group clothes:
        attribute regular2 default:
            grey("/CHR/sima3b/sima3b_clothes_regular.png")

        attribute fancy2:
            grey("/CHR/sima3b/sima3b_clothes_fancy.png")

    group blush:
        attribute noblush default:
            "null_image"

        attribute blush:
            grey("/CHR/sima3b/sima3b_blush_blush.png")

    group 1 auto:
        attribute 1a default:
            grey("/CHR/sima3b/sima3b_1_1a.png")

        attribute 1c:
            grey("/CHR/sima3b/sima3b_1_1c.png")

        attribute 1d:
            grey("/CHR/sima3b/sima3b_1_1d.png")

        attribute 1e:
            grey("/CHR/sima3b/sima3b_1_1e.png")

        attribute 1g:
            grey("/CHR/sima3b/sima3b_1_1g.png")

    group 2 auto:
        attribute 2a default:
            grey("/CHR/sima3b/sima3b_2_2a.png")

        attribute 2b:
            grey("/CHR/sima3b/sima3b_2_2b.png")

        attribute 2c:
            grey("/CHR/sima3b/sima3b_2_2c.png")

        attribute 2d:
            grey("/CHR/sima3b/sima3b_2_2d.png")

    group 3 auto:
        attribute 3a default:
            grey("/CHR/sima3b/sima3b_3_3a.png")

        attribute 3b:
            grey("/CHR/sima3b/sima3b_3_3b.png")

        attribute 3c:
            grey("/CHR/sima3b/sima3b_3_3c.png")

        attribute 3d:
            grey("/CHR/sima3b/sima3b_3_3d.png")

    ypos 1230
layeredimage ermy1_grey:
        group clothes:
            attribute pose1 default:
                grey("/CHR/ermy/ermy1_pose_pose1.png")
            attribute pose2:
                grey("/CHR/ermy/ermy1_pose_pose2.png")
        group blush:
            attribute noblush default:
                "null_image"
            attribute blush:
                grey("/CHR/ermy/ermy1_blush_blush.png")
        group 1 auto:
            attribute 1a default:
                grey("/CHR/ermy/ermy1_1_1a.png")
            attribute 1b:
                grey("/CHR/ermy/ermy1_1_1b.png")
            attribute 1c:
                grey("/CHR/ermy/ermy1_1_1c.png")
            attribute 1d:
                grey("/CHR/ermy/ermy1_1_1d.png")
            attribute 1e:
                grey("/CHR/ermy/ermy1_1_1e.png")
            attribute 1f:
                grey("/CHR/ermy/ermy1_1_1f.png")
            attribute 1g:
                grey("/CHR/ermy/ermy1_1_1g.png")
            attribute 1h:
                grey("/CHR/ermy/ermy1_1_1h.png")
        group 2 auto:
            attribute 2a default:
                grey("/CHR/ermy/ermy1_2_2a.png")
            attribute 2b:
                grey("/CHR/ermy/ermy1_2_2b.png")
            attribute 2c:
                grey("/CHR/ermy/ermy1_2_2c.png")
            attribute 2d:
                grey("/CHR/ermy/ermy1_2_2d.png")
        group 3 auto:
            attribute 3a default:
                grey("/CHR/ermy/ermy1_3_3a.png")
            attribute 3b:
                grey("/CHR/ermy/ermy1_3_3b.png")
            attribute 3c:
                grey("/CHR/ermy/ermy1_3_3c.png")
            attribute 3d:
                grey("/CHR/ermy/ermy1_3_3d.png")
        ypos 1270
layeredimage teya1_grey:
    group clothes:
        attribute regular default:
            grey("/CHR/teya1/teya1_clothes_regular.png")
        attribute fancy:
            grey("/CHR/teya1/teya1_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/sima1/sima1_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/teya1/teya1_1_1a.png")
        attribute 1b:
            grey("/CHR/teya1/teya1_1_1b.png")
        attribute 1c:
            grey("/CHR/teya1/teya1_1_1c.png")
        attribute 1d:
            grey("/CHR/teya1/teya1_1_1d.png")
        attribute 1e:
            grey("/CHR/teya1/teya1_1_1e.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/teya1/teya1_2_2a.png")
        attribute 2b:
            grey("/CHR/teya1/teya1_2_2b.png")
        attribute 2c:
            grey("/CHR/teya1/teya1_2_2c.png")
        attribute 2d:
            grey("/CHR/teya1/teya1_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/teya1/teya1_3_3a.png")
        attribute 3b:
            grey("/CHR/teya1/teya1_3_3b.png")
        attribute 3c:
            grey("/CHR/teya1/teya1_3_3c.png")
        attribute 3d:
            grey("/CHR/teya1/teya1_3_3d.png")
    ypos 1230
layeredimage teya2_grey:
    group clothes:
        attribute regularhand1 default:
            grey("/CHR/teya2/teya2_clothes_regularhand1.png")
        attribute fancyhand1:
            grey("/CHR/teya2/teya2_clothes_fancyhand1.png")
        attribute regularhand2:
            grey("/CHR/teya2/teya2_clothes_regularhand2.png")
        attribute fancyhand2:
            grey("/CHR/teya2/teya2_clothes_fancyhand2.png")
        attribute regularhand3:
            grey("/CHR/teya2/teya2_clothes_regularhand3.png")
        attribute fancyhand3:
            grey("/CHR/teya2/teya2_clothes_fancyhand3.png")
        attribute regularhand4:
            grey("/CHR/teya2/teya2_clothes_regularhand4.png")
        attribute fancyhand4:
            grey("/CHR/teya2/teya2_clothes_fancyhand4.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/teya2/teya2_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/teya2/teya2_1_1a.png")
        attribute 1b:
            grey("/CHR/teya2/teya2_1_1b.png")
        attribute 1c:
            grey("/CHR/teya2/teya2_1_1c.png")
        attribute 1d:
            grey("/CHR/teya2/teya2_1_1d.png")
        attribute 1e:
            grey("/CHR/teya2/teya2_1_1e.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/teya2/teya2_2_2a.png")
        attribute 2b:
            grey("/CHR/teya2/teya2_2_2b.png")
        attribute 2c:
            grey("/CHR/teya2/teya2_2_2c.png")
        attribute 2d:
            grey("/CHR/teya2/teya2_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/teya2/teya2_3_3a.png")
        attribute 3b:
            grey("/CHR/teya2/teya2_3_3b.png")
        attribute 3c:
            grey("/CHR/teya2/teya2_3_3c.png")
        attribute 3d:
            grey("/CHR/teya2/teya2_3_3d.png")
    ypos 1230
layeredimage teya3_grey:
    group clothes:
        attribute regular default:
            grey("/CHR/teya3/teya3_clothes_regular.png")
        attribute fancy:
            grey("/CHR/teya3/teya3_clothes_fancy.png")
    group blush:
        attribute noblush default:
            "null_image"
        attribute blush:
            grey("/CHR/teya3/teya3_blush_blush.png")
    group 1 auto:
        attribute 1a default:
            grey("/CHR/teya3/teya3_1_1a.png")
        attribute 1b:
            grey("/CHR/teya3/teya3_1_1b.png")
        attribute 1c:
            grey("/CHR/teya3/teya3_1_1c.png")
        attribute 1d:
            grey("/CHR/teya3/teya3_1_1d.png")
        attribute 1e:
            grey("/CHR/teya3/teya3_1_1e.png")
    group 2 auto:
        attribute 2a default:
            grey("/CHR/teya3/teya3_2_2a.png")
        attribute 2b:
            grey("/CHR/teya3/teya3_2_2b.png")
        attribute 2c:
            grey("/CHR/teya3/teya3_2_2c.png")
        attribute 2d:
            grey("/CHR/teya3/teya3_2_2d.png")
    group 3 auto:
        attribute 3a default:
            grey("/CHR/teya3/teya3_3_3a.png")
        attribute 3b:
            grey("/CHR/teya3/teya3_3_3b.png")
        attribute 3c:
            grey("/CHR/teya3/teya3_3_3c.png")
        attribute 3d:
            grey("/CHR/teya3/teya3_3_3d.png")
    ypos 1230
return

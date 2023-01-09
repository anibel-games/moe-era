init python:
    config.cache_surfaces = False
init python:
    config.image_cache_size_mb = 300
init:
    $ cloudtrans = ImageDissolve("gui_button/cloudtrans.png", 3.0, 16)
init python:
    slots = renpy.list_slots()
    def delete_slot(number = 0, all = False):
        slots = renpy.list_slots()
        saveGames = renpy.list_saved_games()
        slots_file_name = {}
        for count, i in enumerate(slots):
            slots_file_name[count] = [i, str(saveGames[count][0])]
        if number != 0:
            renpy.unlink_save(slots_file_name[number - 1][1])
        elif all:
            for i in slots_file_name:
                renpy.unlink_save(slots_file_name[i][1])
init python:
    def change_language_callback():
        if _preferences.language == "chinese":
            store.winnie_v = 0
        elif _preferences.language == "chinese_trad":
            store.winnie_v = 0
        else:
            store.winnie_v = 1

    config.interact_callbacks.append(change_language_callback)
init python:
    style.mm_root.background = None
init:
    image movie = Movie(size=(config.screen_width, config.screen_height))
init python:
    style.mm_root.background = None
init python:
    config.keymap['self_voicing'].remove('v')
    config.keymap['self_voicing'].remove('V')

init python:
    config.keymap['accessibility'].remove('K_a')
init python:
    g = Gallery()

    g.button("cg_nana_4_2")
    g.condition("persistent.unlock_cg_nana_4_2")
    g.image("cg_nana_4")

    g.button("cg_all_2_2")
    g.condition("persistent.unlock_cg_all_2_2")
    g.image("cg_all_2_2")

    g.button("cg_nana_8_1")
    g.condition("persistent.unlock_cg_nana_8_1")
    g.image("cg_nana_8_1")

    g.button("cg_nana_8_2")
    g.condition("persistent.unlock_cg_nana_8_2")
    g.image("cg_nana_8_2")

    g.button("cg_sima_3_1")
    g.condition("persistent.unlock_cg_sima_3_1")
    g.image("cg_sima_3_1")

    g.button("cg_marta_7_1")
    g.condition("persistent.unlock_cg_marta_7_1")
    g.image("cg_marta_7_1")

    g.button("cg_nana_7_1")
    g.condition("persistent.unlock_cg_nana_7_1")
    g.image("cg_nana_7")

    g.button("cg_sima_1_1")
    g.condition("persistent.unlock_cg_sima_1_1")
    g.image("cg_sima_1")

    g.button("cg_marta_3_2")
    g.condition("persistent.unlock_cg_marta_3_2")
    g.image("cg_marta_3")

    g.button("cg_marta_1_1")
    g.condition("persistent.unlock_cg_marta_1_1")
    g.image("cg_marta_1_1")

    g.button("cg_marta_2_5")
    g.condition("persistent.unlock_cg_marta_2_5")
    g.image("cg_marta_2")

    g.button("cg_all_3all")
    g.condition("persistent.unlock_cg_all_3")
    g.image("cg_all_3all")

    g.button("cg_barashek")
    g.condition("persistent.unlock_cg_barashek")
    g.image("cg_barashek")

    g.button("cg_sima_2_1")
    g.condition("persistent.unlock_cg_sima_2_4")
    g.image("cg_sima_2")

    g.button("cg_sima_4_1")
    g.condition("persistent.unlock_cg_sima_4_1")
    g.image("cg_sima_4")

    g.button("cg_sima_6_2")
    g.condition("persistent.unlock_cg_sima_6_2")
    g.image("cg_sima_6_2")

    g.button("cg_sima_7_1")
    g.condition("persistent.unlock_cg_sima_7_1")
    g.image("cg_sima_7_1allg")

    g.button("cg_marta_4_1")
    g.condition("persistent.unlock_cg_marta_4_1")
    g.image("cg_marta_4")

    g.button("cg_marta_5_3")
    g.condition("persistent.unlock_cg_marta_5_3")
    g.image("cg_marta_5")

    g.button("cg_marta_6_1")
    g.condition("persistent.unlock_cg_marta_6_1")
    g.image("cg_marta_6_1allg")

    g.button("cg_nana_3_1")
    g.condition("persistent.unlock_cg_nana_3_1")
    g.image("cg_nana_3_1")

    g.button("cg_nana_5_1")
    g.condition("persistent.unlock_cg_nana_5_1")
    g.image("cg_nana_5_1")

    g.button("cg_nana_6_1")
    g.condition("persistent.unlock_cg_nana_6_1")
    g.image("cg_nana_6_1")

    g.button("cg_nana_9_6")
    g.condition("persistent.unlock_cg_nana_9_6")
    g.image("cg_nana_9")

    g.button("cg_photo")
    g.condition("persistent.unlock_cg_photo")
    g.image("cg_photo")

    g.button("cg_teya")
    g.condition("persistent.unlock_cg_teya")
    g.image("cg_teya")

    g.transition = dissolve
init:
 transform star_rotation0:
     yalign 0.5 xalign 0.5
     rotate 0
     linear 3 rotate 1.5
     linear 3 rotate 0
     rotate 0
     repeat

 transform star_rotation1:
     yalign 0.5 xalign 0.5
     rotate 0
     linear 3 rotate 3
     linear 3 rotate 0
     rotate 0
     repeat

 transform clock_hands0:
     yalign 0.5 xalign 0.5
     linear 12 rotate 360
     rotate 0
     repeat

 transform clock_hands1:
     yalign 0.5 xalign 0.5
     linear 144 rotate 360
     rotate 0
     repeat

 transform balls0:
     alpha 0
     linear 6 alpha 1
     linear 6 alpha 0
     repeat

 transform balls1:
     alpha 1
     linear 6 alpha 0
     linear 6 alpha 1
     repeat
init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("cg/eye.png", .5, ramplen=256, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("cg/eye.png", 1, ramplen=256, reverse=True, time_warp=eyewarp)
  eye_open_fast = ImageDissolve("cg/eye.png", .12, ramplen=256, reverse=False, time_warp=eyewarp)
  eye_shut_fast = ImageDissolve("cg/eye.png", .2, ramplen=256, reverse=True, time_warp=eyewarp)
init:
    define flash = Fade(0.1, 0.0, 0.2, color="#fff")
init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist
                self.child = child

            def __call__(self, t, sizes):
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)
        Shake = renpy.curry(_Shake)
init:
    $ sshake = Shake((0, 1, 0, 0), 1, dist=15)
init:
    image movie = Movie(size=(config.screen_width, config.screen_height))
init offset = -1
init:
    $ config.keymap['game_menu'].remove('K_ESCAPE')
    $ config.keymap['game_menu'].remove('mouseup_3')
init -2 python:
    style.input_window.left_margin = 30
    style.input_window.right_margin = 30
    style.input_window.left_padding = 10
    style.input_window.right_padding = 10
    style.input_window.top_padding = 10
    style.input_text.size = 60
    style.input_prompt.size = 60
init python:
    config.character_id_prefixes.append('namebox')
init python:
    config.overlay_screens.append("quick_menu")
style tmenu_button_text is text:
    xalign .014
    yalign .92
style tpref_button_text is text:
    xalign .033
    yalign .75
style thist_button_text is text:
    xalign .038
    yalign .58
style tload_button_text is text:
    xalign .053
    yalign .408
style tsave_button_text is text:
    xalign .053
    yalign .235
style what_imo is text:
    font "Courgette-Regular.ttf"
    color "000000"
    ypos -670
    size 40
    xpos 730
    xalign 0.0
    xmaximum 450
    xsize 450
    outlines [(0, "#fff", 0, 0)]
style who_sophie is text:
    font "Lora-Bold.ttf"
    xalign 0.0
    xpos 0
    ypos -100
    size 50
style what_sophie is text:
    ypos -10
    xalign 0.0
    xpos 200
    xsize 1520
    xmaximum 1520
style what_imo1 is what_imo
style what_credits1 is text:
    size 100
    font "ProximaNova-Bold.otf"
    color  "FFFFFF"
    xalign .5
    yalign .5
    outlines [(3, "222222", 0, 0),(3, "222222C8", 1, 1),(3, "222222DC", 1, 2)]
style what_credits2 is text:
    size 60
    font "ProximaNova-Bold.otf"
    color  "FFFFFF"
    xalign .5
    yalign .5
    outlines [(3, "222222", 0, 0),(3, "222222C8", 1, 1),(3, "222222DC", 1, 2)]
style what_credits3 is text:
    size 40
    font "ProximaNova-Bold.otf"
    color  "FFFFFF"
    xalign .5
    yalign .5
    outlines [(3, "222222", 0, 0),(3, "222222C8", 1, 1),(3, "222222DC", 1, 2)]
style cake_tooltip is text:
    size 60
    font "ProximaNova-Bold.otf"
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
    color  "FFFFFF"
style ermy_close_tooltip is text:
    size 30
    font "ProximaNova-Bold.otf"
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
    color  "FFFFFF"
style earwig is text:
    font "earwig_factory.ttf"
style earwig1 is text:
    font "earwig_factory.ttf"
    xpos 700
    ypos -200
    size 150
style earwig2 is text:
    font "earwig_factory.ttf"
    xpos 700
    ypos -200
    size 150
style earwig3 is text:
    font "earwig_factory.ttf"
    xpos 1300
    ypos 500
    size 130
style earwig5 is text:
    font "earwig_factory.ttf"
    xpos 300
    ypos 800
    size 60
style earwig6 is text:
    font "earwig_factory.ttf"
    xpos 200
    ypos 350
    size 100
style earwig9 is text:
    font "earwig_factory.ttf"
    xpos 10
    ypos 620
    size 120
style earwig8 is text:
    font "earwig_factory.ttf"
    xpos 1600
    ypos -30
    size 90
style earwig7 is text:
    font "earwig_factory.ttf"
    xpos 1600
    ypos 320
    size 80
style earwig4 is text:
    font "earwig_factory.ttf"
    xpos 1620
    ypos 750
    size 50
style bebas is text:
    font "BebasNeue.ttf"
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
    color  "FFFFFF"
style menu_button is text:
    color "FFFFFF"
    outlines [(4, "000000", 0, 0)]
    font "ProximaNova-Bold.otf"
    size 44
style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
    size 60
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text_style:
    font 'ProximaNova-Bold.otf'
    color 'adadad'
    hover_color 'ffffff'
    insensitive_color '606060'
    selected_color 'ffffff'
    size 42
    text_align 0.0
    xalign 0.0
    yalign 0.5
style button_text is button_text_style
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    color 'C0C0C0'
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
style say_label:
    outlines [(1, "222222", 0, 0),(1, "222222C8", 1, 1),(1, "222222DC", 1, 2)]
    color  "FFFFFF"
style say_dialogue:
    outlines [(1, "222222", 0, 0),(1, "222222C8", 1, 1),(1, "222222DC", 1, 2)]
    color  "FFFFFF"
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
style window is default
style choice_vbox is vbox
style choice_button is button
style choice_vbox:
    xalign 0.5
    ypos 500
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines [(1, "222222", 0, 0),(1, "222222C8", 1, 1),(1, "222222DC", 1, 2)]
    color  "FFFFFF"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt:
    size 48
style confirm_button is gui_medium_button
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 68
style skip_frame is empty
style skip_text:
    color  "FFFFFF"
    size 80
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_triangle:
    font "DejaVuSans.ttf"
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")
style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text
style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding
style nvl_entry:
    xfill True
    ysize gui.nvl_height
style nvl_label:
    xpos 300
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
style nvl_dialogue:
    xpos 100
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
style thevast is bebas:
    xpos 900
    ypos 100
    size 105
style will is bebas:
    xpos 980
    ypos 330
    size 125
style anything is bebas:
    xpos 1070
    ypos 560
    size 260
style butyou is bebas:
    xpos 950
    ypos 100
    size 160
style oneofthem is bebas:
    xpos 1000
    ypos 330
    size 180
style quast is bebas:
    xpos 1700
    ypos 330
    size 180
style rightt is bebas:
    xpos 1200
    ypos 560
    size 260
style agameby:
    size 90
    font "ProximaNova-Bold.otf"
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
    color  "FFFFFF"
style thisisawork:
    size 60
    xsize 1550
    xalign .5
    text_align .5
    font "ProximaNova-Bold.otf"
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
    color  "FFFFFF"
style quick_button:
    properties gui.button_properties("quick_button")
style quick_button_text:
    properties gui.button_text_properties("quick_button")
style menu_spacing1:
    spacing 35
    xalign 0.955
    yalign 0.48
style menu_spacing2:
    spacing 20
    xalign 0.955
    yalign 0.48
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is navigation_button_text
style main_menu_title is navigation_button_text
style main_menu_version is navigation_button_text
style main_menu_frame:
    xsize 420
    yfill True
style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"
style game_menu_navigation_frame:
    xsize 420
    yfill True
style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
style help_content_frame:
    left_margin 300
    right_margin 400
    top_margin 30
    bottom_margin 30
style help_menu_outer_frame:
    bottom_padding 30
    top_padding 30
style game_menu_viewport:
    xsize 1380
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 15
style game_menu_label:
    xpos 75
    ysize 180
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
style page_label:
    color "ADADAD"
    hover_color "FFFFFF"
    size 54
style page_label_text:
    color "ADADAD"
    hover_color "FFFFFF"
    size 54
style page_button:
    color "ADADAD"
    hover_color "FFFFFF"
    size 54
style page_button_text:
    color "ADADAD"
    hover_color "FFFFFF"
    size 54
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text:
    color  "FFFFFF"
    size 34
style slot_name_text is slot_button_text
style page_label:
    xpadding 75
    ypadding 5
style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 338
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font 'SourceHanSerifSC-Bold.otf'
    size 36
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text:
    properties gui.button_text_properties("check_button")
    font 'SourceHanSerifSC-Bold.otf'
    size 36
style slider_slider:
    xsize 450
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 675
style history_window is empty
style history_name is gui_label
style history_label is gui_label
style history_label_text is gui_label_text
style history_window:
    xfill True
    ysize gui.history_height
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    justify True
style history_label:
    xfill True
style history_label_text:
    xalign 0.5
style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 375
    right_padding 30
style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
translate russian style menu_spacing1:
    xalign 0.959
    yalign 0.48
translate russian style menu_spacing2:
    xalign 0.959
    yalign 0.48
translate belarusian style menu_spacing1:
    xalign 0.959
    yalign 0.48
translate belarusian style menu_spacing2:
    xalign 0.959
    yalign 0.48
translate japanese style menu_spacing1:
    spacing 20
    xalign 0.955
    yalign 0.52
translate chinese style menu_spacing1:
    spacing 20
    xalign 0.935
    yalign 0.52
translate chinese_trad style menu_spacing1:
    spacing 20
    xalign 0.935
    yalign 0.52
translate japanese style menu_spacing2:
    spacing 10
    xalign 0.955
    yalign 0.52
translate chinese style menu_spacing2:
    spacing 10
    xalign 0.935
    yalign 0.52
translate chinese_trad style menu_spacing2:
    spacing 10
    xalign 0.935
    yalign 0.52
translate japanese style who_sophie:
    font "SourceHanSerifSC-Bold.otf"
translate chinese style who_sophie:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style who_sophie:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style what_sophie:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate japanese style nvl_dialogue:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate japanese style say_dialogue:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate japanese style say_label:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate japanese style choice_button_text:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate japanese style history_text:
    outlines [(2, "222222", 0, 0),(2, "222222C8", 1, 1),(2, "222222DC", 1, 2)]
translate chinese style thevast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 100
    size 160
translate japanese style thevast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 100
    size 120
translate chinese_trad style thevast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 100
    size 160
translate chinese style will:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 350
    size 140
translate japanese style will:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 350
    size 120
translate chinese_trad style will:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 350
    size 140
translate chinese style anything:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1200
    ypos 600
    size 220
translate japanese style anything:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 600
    size 120
translate chinese_trad style anything:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1200
    ypos 600
    size 220
translate russian style thevast:
    xpos 910
    ypos 100
    size 90
translate russian style will:
    xpos 1020
    ypos 300
    size 130
translate russian style anything:
    xpos 1122
    ypos 540
    size 130
translate belarusian style thevast:
    xpos 910
    ypos 100
    size 90
translate belarusian style will:
    xpos 1020
    ypos 300
    size 130
translate belarusian style anything:
    xpos 1122
    ypos 540
    size 130
translate chinese style butyou:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 140
    size 120
translate japanese style butyou:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 140
    size 80
translate chinese_trad style butyou:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 140
    size 120
translate chinese style oneofthem:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1000
    ypos 400
    size 120
translate japanese style oneofthem:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 400
    size 100
translate chinese_trad style oneofthem:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1000
    ypos 400
    size 120
translate chinese style quast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1840
    ypos 400
    size 140
translate japanese style quast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1750
    ypos 400
    size 100
translate chinese_trad style quast:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1840
    ypos 400
    size 140
translate chinese style rightt:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1300
    ypos 660
    size 200
translate japanese style rightt:
    font "SourceHanSerifSC-Bold.otf"
    xpos 950
    ypos 660
    size 100
translate chinese_trad style rightt:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1300
    ypos 660
    size 200
translate russian style butyou:
    xpos 960
    ypos 100
    size 100
translate russian style oneofthem:
    xpos 1070
    ypos 300
    size 130
translate russian style quast:
    xpos 1525
    ypos 300
    size 130
translate russian style rightt:
    xpos 1170
    ypos 520
    size 180
translate belarusian style quast:
    xpos 1525
    ypos 300
    size 130
translate belarusian style rightt:
    xpos 1170
    ypos 520
    size 180
translate chinese_trad style ermy_close_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style ermy_close_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate chinese style ermy_close_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate russian style ermy_close_tooltip:
    font "ProximaNova-Bold.otf"
translate russian style cake_tooltip:
    font "ProximaNova-Bold.otf"
translate belarusian style ermy_close_tooltip:
    font "ProximaNova-Bold.otf"
translate belarusian style cake_tooltip:
    font "ProximaNova-Bold.otf"
translate chinese style cake_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style cake_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style cake_tooltip:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig:
    font "ProximaNova-Bold.otf"
translate chinese style earwig:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style earwig:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style earwig3:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1000
    ypos 500
    size 110
translate japanese style earwig7:
    font "SourceHanSerifSC-Bold.otf"
    size 70
translate chinese style earwig7:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig7:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig7:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig7:
    font "ProximaNova-Bold.otf"
translate japanese style earwig5:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1200
    ypos 130
    size 70
translate japanese style earwig8:
    font "SourceHanSerifSC-Bold.otf"
    size 74
translate chinese style earwig8:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig8:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig8:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig8:
    font "ProximaNova-Bold.otf"
translate japanese style earwig9:
    font "SourceHanSerifSC-Bold.otf"
    size 100
translate chinese style earwig9:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig9:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig9:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig9:
    font "ProximaNova-Bold.otf"
translate japanese style earwig6:
    font "SourceHanSerifSC-Bold.otf"
    size 90
translate chinese style earwig6:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig6:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig6:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig6:
    font "ProximaNova-Bold.otf"
translate japanese style earwig5:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1200
    ypos 130
    size 70
translate chinese style earwig5:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig5:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig5:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig5:
    font "ProximaNova-Bold.otf"
translate japanese style earwig4:
    font "SourceHanSerifSC-Bold.otf"
    xpos 1320
    ypos 450
    size 110
translate chinese style earwig4:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig4:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig4:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig4:
    font "ProximaNova-Bold.otf"
translate chinese style earwig3:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style earwig3:
    font "SourceHanSerifSC-Bold.otf"
translate russian style earwig3:
    font "ProximaNova-Bold.otf"
translate belarusian style earwig3:
    font "ProximaNova-Bold.otf"
translate japanese style earwig2:
    font "SourceHanSerifSC-Bold.otf"
    xpos 620
    ypos -320
    size 150
translate chinese style earwig2:
    font "SourceHanSerifSC-Bold.otf"
    xpos 720
    ypos -170
    size 150
translate chinese_trad style earwig2:
    font "SourceHanSerifSC-Bold.otf"
    xpos 720
    ypos -170
    size 150
translate russian style earwig2:
    font "ProximaNova-Bold.otf"
    xpos 650
    size 150
translate belarusian style earwig2:
    font "ProximaNova-Bold.otf"
    xpos 650
    size 150
translate japanese style earwig1:
    font "SourceHanSerifSC-Bold.otf"
    xpos 650
    ypos -220
    size 150
translate chinese style earwig1:
    font "SourceHanSerifSC-Bold.otf"
    xpos 690
    ypos -100
    size 150
translate chinese_trad style earwig1:
    font "SourceHanSerifSC-Bold.otf"
    xpos 690
    ypos -100
    size 150
translate russian style earwig1:
    font "ProximaNova-Bold.otf"
    xpos 650
    size 150
translate belarusian style earwig1:
    font "ProximaNova-Bold.otf"
    xpos 650
    size 150
translate chinese_trad style earwig:
    font "SourceHanSerifSC-Bold.otf"
translate russian style bebas:
    font "ProximaNova-Bold.otf"
translate belarusian style bebas:
    font "ProximaNova-Bold.otf"
translate chinese style bebas:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style bebas:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style bebas:
    font "SourceHanSerifSC-Bold.otf"
translate russian style menu_button:
    size 40
translate belarusian style menu_button:
    size 32
translate chinese style menu_button:
    font "SourceHanSerifSC-Bold.otf"
translate japanese style menu_button:
    font "SourceHanSerifSC-Bold.otf"
translate chinese_trad style menu_button:
    font "SourceHanSerifSC-Bold.otf"
translate chinese style what_imo:
    font "SourceHanSerifSC-Bold.otf"
    color "000000"
    size 40
translate japanese style what_imo:
    font "SourceHanSerifSC-Bold.otf"
    color "000000"
    size 36
translate chinese_trad style what_imo:
    font "SourceHanSerifSC-Bold.otf"
    color "000000"
    size 40
translate russian style what_imo:
    font "Caveat-Bold.ttf"
    color "000000"
    size 42
translate russian style what_imo1 is what_imo
translate belarusian style what_imo:
    font "Caveat-Bold.ttf"
    color "000000"
    size 42
translate belarusian style what_imo1 is what_imo
translate chinese style what_imo1 is what_imo
translate chinese_trad style what_imo1 is what_imo
translate japanese style what_imo1 is what_imo
translate chinese style button_text_style:
    font  "SourceHanSerifSC-Bold.otf"
    size 44
translate japanese style button_text_style:
    font  "SourceHanSerifSC-Bold.otf"
    size 44
translate chinese_trad style button_text_style:
    font  "SourceHanSerifSC-Bold.otf"
    size 44
translate russian style button_text_style:
    size 42
translate russian style tmenu_button_text:
    xalign .005
    yalign .915
translate russian style tpref_button_text:
    xalign .0235
    yalign .75
translate russian style thist_button_text:
    xalign .036
    yalign .577
translate russian style tload_button_text:
    xalign .026
    yalign .4035
translate russian style tsave_button_text:
    xalign .025
    yalign .234
translate belarusian style button_text_style:
    size 36
translate belarusian style tmenu_button_text:
    xalign .005
    yalign .915
translate belarusian style tpref_button_text:
    xalign .0235
    yalign .75
translate belarusian style thist_button_text:
    xalign .036
    yalign .577
translate belarusian style tload_button_text:
    xalign .026
    yalign .4035
translate belarusian style tsave_button_text:
    xalign .025
    yalign .234
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    textbutton _("Return"):
        style "return_button"
        xalign 0.98
        action Return()
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
screen help_menu(title, scroll=None, yinitial=0.0):
    key "K_ESCAPE" action Return()
    add "cg_invite"
    add "gui_shade"
    tag menu
    style_prefix "game_menu"
    frame:
        style "help_menu_outer_frame"
        hbox:
            frame:
                style "help_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
screen help():
    tag menu
    default device = "keyboard"
    use help_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23
            hbox:
                xpos 250
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
    textbutton "Return" action Return() xalign 0.95 yalign 0.95
screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")
    hbox:
        label _("Escape")
        text _("Accesses the game menu.")
    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")
    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")
    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")
    hbox:
        label "H"
        text _("Hides the user interface.")
screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")
    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")
    hbox:
        label _("Mouse Wheel")
        text _("Rolls forward to later dialogue.")
screen gamepad_help():
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")
    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")
    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")
    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
screen input(prompt):
    style_prefix "input"
    window:
        yalign .5
        xalign .5
        background None
        has vbox xalign 0.5 yalign 0.5
        text prompt xalign 0.5
        input id "input" font "SourceHanSerifSC-Bold.otf"
screen choice(items):
    style_prefix "choice"
    add "menu_dark":
        at transform:
            alpha 0
            linear .5 alpha 1
    vbox:
        for i in items:
            textbutton i.caption action i.action
screen load():
    add "room_v1"
    add "gui_shade"
    tag menu
    key "K_ESCAPE" action Return()
    use file_slots1(_("Load"))
screen file_slots1(title):
    tag menu
    textbutton "Return" action Return() xalign 0.5 yalign 0.95 text_size 54
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:
        order_reverse True
        button:
            style "page_label"
            key_events True
            xalign .5
            yalign 0.02
            action page_name_value.Toggle()
            input:
                style "page_label_text"
                value page_name_value
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.5
            yalign 0.38
            spacing gui.slot_spacing
            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    action FileAction(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 1
                    text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
        hbox:
            style_prefix "page"
            xalign 0.5
            yalign 0.85
            spacing gui.page_spacing
            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")
            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")
            for page in range(1, 4):
                textbutton "[page]" action FilePage(page)
screen quick_menu():
    zorder 100
    key "K_ESCAPE" action [Show("quick_menu_buttons_roll_in")]
    key "pad_guide_press" action [Show("quick_menu_buttons_roll_in")]
    key "pad_start_press" action [Show("quick_menu_buttons_roll_in")]
    if quick_menu:
        imagebutton:
            yalign 1.0
            xalign 0
            idle "idle_mask"
            hovered If(renpy.get_screen("quick_menu_pause"), true=NullAction(), false=Show("quick_menu_buttons_roll_in"))
            action NullAction()
screen quick_menu_buttons_roll_in():
    zorder 101
    image "right_menu":
        at transform:
            xpos -700
            linear .5 xpos 0
    timer 0.5 action [Show("quick_menu_pause"), Hide("quick_menu_buttons_roll_in")]
screen quick_menu_buttons_roll_out():
    zorder 101
    image "right_menu":
        at transform:
            xpos 0
            linear .5 xpos -700
    timer 0.35 action [Hide("quick_menu_pause"), Hide("quick_menu_buttons_roll_out")]
screen quick_menu_pause():
    zorder 104
    imagebutton:
        xpos 500
        idle "hide_mask"
        action [Hide("quick_menu_pause"),Show("quick_menu_buttons_roll_out")]
    image "right_menu"
    key "K_ESCAPE" action [Hide("quick_menu_pause"),Show("quick_menu_buttons_roll_out")]
    key "pad_y_press" action [Hide("quick_menu_pause"),Show("quick_menu_buttons_roll_out")]
    vbox:
        ypos 100
        xpos 50
        spacing 50
        textbutton ("Save") text_style "quick_button_text" action [Hide("quick_menu_pause"),ShowMenu('save')]
        textbutton ("Load") text_style "quick_button_text" action [Hide("quick_menu_pause"),ShowMenu('ingameload')]
        textbutton ("History") text_style "quick_button_text" action [Hide("quick_menu_pause"),ShowMenu('history')]
        textbutton ("Options") text_style "quick_button_text" action [Hide("quick_menu_pause"),ShowMenu('preferences')]
        textbutton ("Skip") text_style "quick_button_text" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Main menu") text_style "quick_button_text" action MainMenu()
screen save():
    image "gui_shade"
    image "right_menu"
    key "K_ESCAPE" action Return()
    vbox:
        ypos 100
        xpos 50
        spacing 50
        textbutton ("Save") text_style "quick_button_text" action [Hide("save"),ShowMenu('save')]
        textbutton ("Load") text_style "quick_button_text" action [Hide("save"),ShowMenu('ingameload')]
        textbutton ("History") text_style "quick_button_text" action [Hide("save"),ShowMenu('history')]
        textbutton ("Options") text_style "quick_button_text" action [Hide("save"),ShowMenu('preferences')]
        textbutton ("Skip") text_style "quick_button_text" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Main menu") text_style "quick_button_text" action MainMenu()
    use file_slots_s(_("Save"))
screen file_slots_s(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:
        order_reverse True
        button:
            style "page_label"
            key_events True
            xalign 0.3
            yalign 0.1
            action page_name_value.Toggle()
            input:
                style "page_label_text"
                value page_name_value
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.8
            yalign 0.58
            spacing gui.slot_spacing
            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    action FileSave(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 1
                    text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
        hbox:
            style_prefix "page"
            xalign 0.7
            yalign 0.1
            spacing gui.page_spacing
            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")
            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")
            for page in range(1, 4):
                textbutton "[page]" action FilePage(page)
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen ingameload():
    image "right_menu"
    image "gui_shade"
    key "K_ESCAPE" action Return()
    vbox:
        ypos 100
        xpos 50
        spacing 50
        textbutton ("Save") text_style "quick_button_text" action [Hide("ingameload"),ShowMenu('save')]
        textbutton ("Load") text_style "quick_button_text" action [Hide("ingameload"),ShowMenu('ingameload')]
        textbutton ("History") text_style "quick_button_text" action [Hide("ingameload"),ShowMenu('history')]
        textbutton ("Options") text_style "quick_button_text" action [Hide("ingameload"),ShowMenu('preferences')]
        textbutton ("Skip") text_style "quick_button_text" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Main menu") text_style "quick_button_text" action MainMenu()
    tag menu
    use file_slots_l(_("Load"))
screen file_slots_l(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:
        order_reverse True
        button:
            style "page_label"
            key_events True
            xalign 0.3
            yalign 0.1
            action page_name_value.Toggle()
            input:
                style "page_label_text"
                value page_name_value
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.8
            yalign 0.58
            spacing gui.slot_spacing
            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    action FileLoad(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 1
                    text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
        hbox:
            style_prefix "page"
            xalign 0.7
            yalign 0.1
            spacing gui.page_spacing
            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")
            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")
            for page in range(1, 4):
                textbutton "[page]" action FilePage(page)
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen preferences():
    image "right_menu"
    image "gui_shade"
    key "K_ESCAPE" action Return()
    vbox:
        ypos 100
        xpos 50
        spacing 50
        textbutton ("Save") text_style "quick_button_text" action [Hide("preferences"),ShowMenu('save')]
        textbutton ("Load") text_style "quick_button_text" action [Hide("preferences"),ShowMenu('ingameload')]
        textbutton ("History") text_style "quick_button_text" action [Hide("preferences"),ShowMenu('history')]
        textbutton ("Options") text_style "quick_button_text" action [Hide("preferences"),ShowMenu('preferences')]
        textbutton ("Skip") text_style "quick_button_text" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Main menu") text_style "quick_button_text" action MainMenu()
    hbox:
        xpos 500
        ypos 100
        box_wrap True
        spacing 155
        if renpy.variant("pc"):
            vbox:
                style_prefix "radio"
                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")
        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
    null height (4 * gui.pref_spacing)

    vbox:
        xpos 500
        ypos 400
        style_prefix "slider"
        label _("Text Speed")
        bar value Preference("text speed")
        label _("Auto-Forward Time")
        bar value Preference("auto-forward time")
    vbox:
        xpos 1000
        ypos 400
        style_prefix "slider"
        label _("Music Volume")
        hbox:
            bar value Preference("music volume")
        label _("Sound Volume")
        hbox:
            bar value Preference("sound volume")

    frame:
        xpos 1550
        ypos 95
        style_prefix "radio"
        has vbox
        label _("Language")
        imagebutton:
            if persistent.lang == 1:
                idle language_english_hover
            else:
                idle language_english
            hover language_english_hover
            action [Language(None), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), SetVariable("persistent.lang", 1)]
            xpos -28
            ypos 10
        imagebutton:
            if persistent.lang == 2:
                idle language_russian_hover
            else:
                idle language_russian
            hover language_russian_hover
            action [Language("russian"), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), SetVariable("persistent.lang", 2)]
            xpos -20
            ypos 20
        imagebutton:
            if persistent.lang == 3:
                idle language_japanese_hover
            else:
                idle language_japanese
            hover language_japanese_hover
            action [Language("japanese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 40), SetVariable("persistent.lang", 3)]
            xpos -43
            ypos 30
        imagebutton:
            if persistent.lang == 4:
                idle language_ch_hover
            else:
                idle language_ch
            hover language_ch_hover
            action [Language("chinese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), SetVariable("persistent.lang", 4)]
            xpos -28
            ypos 40
        imagebutton:
            if persistent.lang == 5:
                idle language_chtr_hover
            else:
                idle language_chtr
            hover language_chtr_hover
            action [Language("chinese_trad"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), SetVariable("persistent.lang", 5)]
            xpos -28
            ypos 50
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen history():
    image "right_menu"
    image "history_dark"
    key "K_ESCAPE" action Return()
    tag menu
    predict False
    viewport:
        style_prefix "history"
        yinitial 1.0
        mousewheel True
        draggable True
        xanchor 0.0
        xpos 320
        yanchor 0.0
        ypos 50
        ymaximum 890
        xmaximum 1550
        vbox:
            for h in _history_list:
                window:
                    has fixed:
                        yfit True
                    if h.who:
                        label h.who:
                            style "history_name"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    text h.what
        if not _history_list:
            label _("The dialogue history is empty.")
    vbox:
        ypos 100
        xpos 50
        spacing 50
        textbutton ("Save") text_style "quick_button_text" action [Hide("history"),ShowMenu('save')]
        textbutton ("Load") text_style "quick_button_text" action [Hide("history"),ShowMenu('ingameload')]
        textbutton ("History") text_style "quick_button_text" action [Hide("history"),ShowMenu('history')]
        textbutton ("Options") text_style "quick_button_text" action [Hide("history"),ShowMenu('preferences')]
        textbutton ("Skip") text_style "quick_button_text" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton ("Main menu") text_style "quick_button_text" action MainMenu()
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    key "game_menu" action no_action
screen skip_indicator():
    zorder 110
    style_prefix "skip"
    frame:
        xalign .99
        yalign -.02
        hbox:
            spacing 9
            text _("")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"
    add SideImage() xalign 0.0 yalign 1.0
screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id
screen cats_1_screen():
    $ cats_2_1 = Image("/images/cg/cats/cats_2_1.png")
    $ cats_2_2 = Image("/images/cg/cats/cats_2_2.png")
    $ cats_2_3 = Image("/images/cg/cats/cats_2_3.png")
    $ cats_2_4 = Image("/images/cg/cats/cats_2_4.png")
    imagebutton:
        idle cats_2_1
        focus_mask True
        action [Hide("cats_1_screen"), Show("cats_2_1_screen")]
    imagebutton:
        idle cats_2_2
        focus_mask True
        action [Hide("cats_1_screen"), Show("cats_2_2_screen")]
    imagebutton:
        idle cats_2_3
        focus_mask True
        action [Hide("cats_1_screen"), Show("cats_2_3_screen")]
screen cats_2_1_screen():
    add "/images/cg/cats/cat_day1a.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_1_screen"), Show("cats_1_screen")]
screen cats_2_2_screen():
    add "/images/cg/cats/cat_day2b.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_2_screen"), Show("cats_1_screen")]
screen cats_2_3_screen():
    add "/images/cg/cats/cat_day3b.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_3_screen"), Show("cats_1_screen")]
screen cats_2_1_screen2():
    add "/images/cg/cats/cat_day1a.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_1_screen2"), Show("cats_2_screen")]
screen cats_2_2_screen2():
    add "/images/cg/cats/cat_day2b.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_2_screen2"), Show("cats_2_screen")]
screen cats_2_3_screen2():
    add "/images/cg/cats/cat_day3b.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_3_screen2"), Show("cats_2_screen")]
screen cats_2_4_screen2():
    add "/images/cg/cats/cat_day4a.jpg"
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action [Hide("cats_2_4_screen2"), Show("cats_2_screen")]
screen cats_2_screen():
    $ cats_2_1 = Image("/images/cg/cats/cats_2_1.png")
    $ cats_2_2 = Image("/images/cg/cats/cats_2_2.png")
    $ cats_2_3 = Image("/images/cg/cats/cats_2_3.png")
    $ cats_2_4 = Image("/images/cg/cats/cats_2_4.png")
    imagebutton:
        idle cats_2_1
        focus_mask True
        action [Hide("cats_2_screen"), Show("cats_2_1_screen2")]
    imagebutton:
        idle cats_2_2
        focus_mask True
        action [Hide("cats_2_screen"), Show("cats_2_2_screen2")]
    imagebutton:
        idle cats_2_3
        focus_mask True
        action [Hide("cats_2_screen"), Show("cats_2_3_screen2")]
    imagebutton:
        idle cats_2_4
        focus_mask True
        action [Hide("cats_2_screen"), Show("cats_2_4_screen2")]
screen lpg_screen_1():
    $ lpg_2a = Image("/images/bg/lpg/lpg_2a.png")
    $ lpg_2a_hover = Image("/images/bg/lpg/lpg_2a_hover.png")
    imagebutton:
        idle lpg_2a
        hover lpg_2a_hover
        action [Hide("lpg_screen_1"), Jump("lbl_lpg_2")]
        focus_mask True
screen lpg_screen_2():
    $ lpg_2a = Image("/images/bg/lpg/lpg_2a.png")
    $ lpg_2a_hover = Image("/images/bg/lpg/lpg_2a_hover.png")
    imagebutton:
        idle lpg_2a
        hover lpg_2a_hover
        action [Hide("lpg_screen_2"), Jump("lbl_lpg_3")]
        focus_mask True
screen cake_base_select():
    $ tard = im.Scale("cakegame/tard/tard_filling_none.png", 356, 352)
    $ cake1 = im.Scale("cakegame/cake/cake_filling_none.png", 500, 527)
    $ ml1 = im.Scale("cakegame/ml/ml_filling_none.png", 500, 527)
    $ tard_hover = im.Scale("cakegame/tard/tard_filling_none.png", 374, 370)
    $ cake1_hover = im.Scale("cakegame/cake/cake_filling_none.png", 525, 553)
    $ ml1_hover = im.Scale("cakegame/ml/ml_filling_none.png", 525, 553)
    default tt=Tooltip("")
    default tc=Tooltip("")
    default tm=Tooltip("")
    imagebutton:
        idle tard
        hover tard_hover
        hovered tt.Action("Tard")
        action [SetVariable("base_type", 1), Hide("cake_base_select"), Jump("base_type_selected") ]
        xalign 0.94
        yalign 0.11
        focus_mask True
    imagebutton:
        idle cake1
        hover cake1_hover
        hovered tc.Action("Cake")
        action [SetVariable("base_type", 2), Hide("cake_base_select"), Jump("base_type_selected")]
        xalign 0.67
        yalign 0.02
        focus_mask True
    imagebutton:
        idle ml1
        hover ml1_hover
        hovered tm.Action("Mille-feuille")
        action [SetVariable("base_type", 3), Hide("cake_base_select"), Jump("base_type_selected")]
        xalign 0.83
        yalign 0.62
        focus_mask True
    frame:
        text tt.value:
            style "cake_tooltip"
        xalign .88
        yalign .4
    frame:
        text tc.value:
            style "cake_tooltip"
        xalign .64
        yalign .4
    frame:
        text tm.value:
            style "cake_tooltip"
        xalign .8
        yalign .75
screen thats_illegal():
    text "That's illegal!":
        xalign .5
        yalign .5
        style "cake_tooltip"
        size 200
        at transform:
            alpha 0
            linear .5 alpha 1
            pause 1
            linear .5 alpha 0
    timer 2 action Hide('thats_illegal')
screen cake_filling_select():
    $ peach = Image("cakegame/peach.png")
    $ cherry = Image("cakegame/peach.png")
    $ strawberry = Image("cakegame/peach.png")
    $ ketchup = im.Scale("cakegame/ketchup.png", 363, 363)
    $ rum = im.Scale("cakegame/rum.png", 227, 260)
    $ tooth = im.Scale("cakegame/tooth.png", 345, 345)
    $ cream = im.Scale("cakegame/cream.png", 363, 363)
    $ custard = im.Scale("cakegame/custard.png", 227, 263)
    $ choco = im.Scale("cakegame/choco.png", 291, 291)
    $ ketchup_hover = Image("cakegame/ketchup.png")
    $ rum_hover = Image("cakegame/rum.png")
    $ tooth_hover = Image("cakegame/tooth.png")
    $ cream_hover = Image("cakegame/cream.png")
    $ custard_hover = Image("cakegame/custard.png")
    $ choco_hover = Image("cakegame/choco.png")

    default tk=Tooltip("")
    default tr=Tooltip("")
    default tp=Tooltip("")
    default tcr=Tooltip("")
    default tcu=Tooltip("")
    default tco=Tooltip("")
    default tri=Tooltip("")
    imagebutton:
        idle ketchup
        hover ketchup_hover
        hovered tk.Action("Ketchup")
        action [SetVariable("filling_type", 1), Hide("cake_filling_select"), Jump("filling_type_selected")]
        xalign 0.8
        yalign 0.67
        focus_mask True
    imagebutton:
        idle rum
        hover rum_hover
        hovered tr.Action("Rum raisin")
        action Show("thats_illegal")
        xalign 0.63
        yalign 0.68
        focus_mask True
    imagebutton:
        idle tooth
        hover tooth_hover
        hovered tp.Action("Tooth paste")
        action [SetVariable("filling_type", 3), Hide("cake_filling_select"), Jump("filling_type_selected")]
        xalign 0.95
        yalign 0.2
        focus_mask True
    imagebutton:
        idle cream
        hover cream_hover
        hovered tcr.Action("Cream")
        action [SetVariable("filling_type", 4), Hide("cake_filling_select"), Jump("filling_type_selected")]
        xalign 0.8
        yalign 0.05
        focus_mask True
    imagebutton:
        idle custard
        hover custard_hover
        hovered tcu.Action("Custard")
        action [SetVariable("filling_type", 5), Hide("cake_filling_select"), Jump("filling_type_selected")]
        xalign 0.93
        yalign 0.68
        focus_mask True
    imagebutton:
        idle choco
        hover choco_hover
        hovered tco.Action("Chocolate paste")
        action [SetVariable("filling_type", 6), Hide("cake_filling_select"), Jump("filling_type_selected")]
        xalign 0.63
        yalign 0.135
        focus_mask True
    frame:
        text tk.value:
            style "cake_tooltip"
        xalign .78
        yalign .84
    frame:
        text tp.value:
            style "cake_tooltip"
        xalign .94
        yalign .38
    frame:
        text tr.value:
            style "cake_tooltip"
        xalign .64
        yalign .84
    frame:
        text tco.value:
            style "cake_tooltip"
        xalign .7
        yalign .38
    frame:
        text tcu.value:
            style "cake_tooltip"
        xalign .94
        yalign .84
    frame:
        text tcr.value:
            style "cake_tooltip"
        xalign .77
        yalign .38
screen cake_topping_select():
    $ peach = im.Scale("cakegame/peach.png", 350, 350)
    $ cherry = im.Scale("cakegame/cherry.png", 350, 356)
    $ strawberry = im.Scale("cakegame/strawberry.png", 350, 356)
    $ pepe = im.Scale("cakegame/pepe.png", 151, 145)
    $ yoba = im.Scale("cakegame/yoba.png", 150, 142)
    $ peach_hover = Image("cakegame/peach.png")
    $ cherry_hover = Image("cakegame/cherry.png")
    $ strawberry_hover = Image("cakegame/strawberry.png")
    $ pepe_hover = Image("cakegame/pepe.png")
    $ yoba_hover = Image("cakegame/yoba.png")
    default tpea=Tooltip("")
    default tchr=Tooltip("")
    default tstr=Tooltip("")
    default tpe=Tooltip("")
    default tyo=Tooltip("")

    imagebutton:
        idle peach
        hover peach_hover
        hovered tpea.Action("Peach")
        action [SetVariable("topping_type", 1), Hide("cake_topping_select"), Jump("topping_type_selected")]
        xalign 0.92
        yalign 0.1
        focus_mask True
    imagebutton:
        idle cherry
        hover cherry_hover
        hovered tchr.Action("Cherries")
        action [SetVariable("topping_type", 2), Hide("cake_topping_select"), Jump("topping_type_selected")]
        xalign 0.67
        yalign 0.1
        focus_mask True
    imagebutton:
        idle strawberry
        hover strawberry_hover
        hovered tstr.Action("Strawberries")
        action [SetVariable("topping_type", 3), Hide("cake_topping_select"), Jump("topping_type_selected")]
        xalign 0.78
        yalign 0.7
        focus_mask True
    imagebutton:
        idle pepe
        hover pepe_hover
        hovered tpe.Action("Strange candy emblem")
        action [SetVariable("topping_type", 4), Hide("cake_topping_select"), Jump("topping_type_selected")]
        xalign 0.93
        yalign 0.73
        focus_mask True
    imagebutton:
        idle yoba
        hover yoba_hover
        hovered tyo.Action("Chocolate in tinfoil")
        action [SetVariable("topping_type", 5), Hide("cake_topping_select"), Jump("topping_type_selected")]
        xalign 0.6
        yalign 0.73
        focus_mask True

    frame:
        text tpea.value:
            style "cake_tooltip"
        xalign .9
        yalign .45
    frame:
        text tchr.value:
            style "cake_tooltip"
        xalign .66
        yalign .45
    frame:
        text tstr.value:
            style "cake_tooltip"
        xalign .79
        yalign .9
    frame:
        text tpe.value:
            style "cake_tooltip"
        xalign .9
        yalign .9
    frame:
        text tyo.value:
            style "cake_tooltip"
        xalign .79
        yalign .9
screen pianogame_scr1():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action [SetVariable("note1", 1), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action [SetVariable("note1", 7), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action [SetVariable("note1", 6), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action [SetVariable("note1", 2), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action [SetVariable("note1", 5), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action [SetVariable("note1", 3), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action [SetVariable("note1", 4), Hide("pianogame_scr1"), Jump("pianogame2")]
        focus_mask True
screen pianogame_scr_note1():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action Jump("pianogame_note1_1")
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action Jump("pianogame_note1_7")
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action Jump("pianogame_note1_6")
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action Jump("pianogame_note1_2")
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action Jump("pianogame_note1_5")
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action Jump("pianogame_note1_3")
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action Jump("pianogame_note1_4")
        focus_mask True
screen pianogame_scr_note2():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action Jump("pianogame_note2_1")
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action Jump("pianogame_note2_7")
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action Jump("pianogame_note2_6")
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action Jump("pianogame_note2_2")
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action Jump("pianogame_note2_5")
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action Jump("pianogame_note2_3")
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action Jump("pianogame_note2_4")
        focus_mask True
screen pianogame_scr_note3():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action Jump("pianogame_note3_1")
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action Jump("pianogame_note3_7")
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action Jump("pianogame_note3_6")
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action Jump("pianogame_note3_2")
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action Jump("pianogame_note3_5")
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action Jump("pianogame_note3_3")
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action Jump("pianogame_note3_4")
        focus_mask True
screen pianogame_scr_note4():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action Jump("pianogame_note4_1")
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action Jump("pianogame_note4_7")
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action Jump("pianogame_note4_6")
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action Jump("pianogame_note4_2")
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action Jump("pianogame_note4_5")
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action Jump("pianogame_note4_3")
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action Jump("pianogame_note4_4")
        focus_mask True
screen pianogame_scr_note5():
    imagebutton:
        idle piano_1_1top
        hover piano_1_1top_hover
        action Jump("pianogame_note5_1")
        focus_mask True
    imagebutton:
        idle piano_7_7top
        hover piano_7_7top_hover
        action Jump("pianogame_note5_7")
        focus_mask True
    imagebutton:
        idle piano_6_6top
        hover piano_6_6top_hover
        action Jump("pianogame_note5_6")
        focus_mask True
    imagebutton:
        idle piano_2_2top
        hover piano_2_2top_hover
        action Jump("pianogame_note5_2")
        focus_mask True
    imagebutton:
        idle piano_5_5top
        hover piano_5_5top_hover
        action Jump("pianogame_note5_5")
        focus_mask True
    imagebutton:
        idle piano_3_3top
        hover piano_3_3top_hover
        action Jump("pianogame_note5_3")
        focus_mask True
    imagebutton:
        idle piano_4_4top
        hover piano_4_4top_hover
        action Jump("pianogame_note5_4")
        focus_mask True
screen scr_game_progress_d1():
    imagebutton:
        idle "room_day_progress"
        hover "room_day_progress_hover"
        action Show("scr_game_progress2_d1")
        focus_mask True
screen scr_game_progress_d2():
    imagebutton:
        idle "room_day_progress"
        hover "room_day_progress_hover"
        action Show("scr_game_progress2_d2")
        focus_mask True
screen scr_game_progress_d3():
    imagebutton:
        idle "room_day_progress"
        hover "room_day_progress_hover"
        action Show("scr_game_progress2_d3")
        focus_mask True
screen scr_game_progress_d4():
    imagebutton:
        idle "room_day_progress"
        hover "room_day_progress_hover"
        action Show("scr_game_progress2_d4")
        focus_mask True
screen scr_game_progress2_d1():
    zorder 90
    button:
        xysize (config.screen_width, config.screen_height)
        action Hide("scr_game_progress2_d1")
    image "game_progress_d1"
screen scr_game_progress2_d2():
    zorder 90
    button:
        xysize (config.screen_width, config.screen_height)
        action Hide("scr_game_progress2_d2")
    image "game_progress_d2"
screen scr_game_progress2_d3():
    zorder 90
    button:
        xysize (config.screen_width, config.screen_height)
        action Hide("scr_game_progress2_d3")
    image "game_progress_d3"
screen scr_game_progress2_d4():
    zorder 90
    button:
        xysize (config.screen_width, config.screen_height)
        action Hide("scr_game_progress2_d4")
    image "game_progress_d4"

screen ermy_gui():
    imagebutton:
        idle "ermy_gui"
        action None
screen close_ermy_game():
    $ ermy_close = Image("room/ermy_close.png")
    default tec=Tooltip("")
    imagebutton:
        idle "ermy_close"
        hovered tec.Action("Close Ermy's game")
        action Jump("close_game")
        xalign 0.98
        yalign 0.93
        focus_mask True
    frame:
        text tec.value:
            style "ermy_close_tooltip"
        xalign .99
        yalign 0.98
screen sat_next():
    textbutton "Next track":
        text_size 70
        action Jump("chopin")
        xalign 0.95
        yalign 0.08
screen cpn_next():
    textbutton "Move on":
        text_size 70
        action Jump("ermy_piano_end")
        xalign 0.95
        yalign 0.08
screen sch_next():
    textbutton "Next track":
        text_size 70
        action Jump("satie")
        xalign 0.95
        yalign 0.08
screen scr_intro_you_see():
    timer 0.5 action Play('sound', 'sound/bang.ogg')
    timer 1.25 action Play('sound', 'sound/bang.ogg')
    timer 2 action Play('sound', 'sound/bang.ogg')
    text "The vast majority of people":
        at transform:
            alpha 0
            pause .5
            alpha 1
        style "thevast"
    text "will never amount to":
        at transform:
            alpha 0
            pause 1.25
            alpha 1
        style "will"
    text "anything.":
        at transform:
            alpha 0
            pause 2
            alpha 1
        style "anything"
screen scr_intro_but_you():
    text "But you're not":
        style "butyou"
        at transform:
            alpha 0
            pause 1
            linear .5 alpha 1
    text "one of them":
        style "oneofthem"
        at transform:
            alpha 0
            pause 1
            linear .5 alpha 1
            alpha 1
    text ",":
        style "quast"
        at transform:
            alpha 0
            pause 1
            linear .5 alpha 1
    text "right?":
        style "rightt"
        at transform:
            alpha 0
            pause 2.5
            linear .5 alpha 1
screen scr_call():
    image Solid("ffffff"):
        at transform:
            rotate 45
            xalign .5
            yalign 1
        size (2520, 1280)
screen language_english():
    on "show" action [Language(None), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), Hide("language_english"), SetVariable("persistent.lang", 1)]
screen language_russian():
    on "show" action [Language("russian"), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), Hide("language_russian"), SetVariable("persistent.lang", 2)]
screen language_japanese():
    on "show" action [Language("belarusian"), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), Hide("language_belarusian"), SetVariable("persistent.lang", 3)]
screen language_belarusian():
    on "show" action [Language("japanese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 40), SetVariable("persistent.lang", 4)]
screen language_chinese():
    on "show" action [Language("chinese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), Hide("language_chinese"), SetVariable("persistent.lang", 5)]
screen language_chinese_trad():
    on "show" action [Language("chinese_trad"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), Hide("language_chinese_trad"), SetVariable("persistent.lang", 6)]
screen preferences1():
    key "K_ESCAPE" action Return()
    tag menu
    add "cg_invite"
    add "gui_shade"
    hbox:
        xpos 350
        ypos 200
        box_wrap True
        spacing 215
        if renpy.variant("pc"):
            vbox:
                style_prefix "radio"
                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")
        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
    null height (4 * gui.pref_spacing)

    vbox:
        xpos 350
        ypos 500
        style_prefix "slider"
        label _("Text Speed")
        bar value Preference("text speed")
        label _("Auto-Forward Time")
        bar value Preference("auto-forward time")
    vbox:
        xpos 900
        ypos 500
        style_prefix "slider"
        label _("Music Volume")
        hbox:
            bar value Preference("music volume")
        label _("Sound Volume")
        hbox:
            bar value Preference("sound volume")

    frame:
        xpos 1500
        ypos 195
        style_prefix "radio"
        has vbox
        label _("Language")
        imagebutton:
            if persistent.lang == 1:
                idle language_english_hover
            else:
                idle language_english
            hover language_english_hover
            action [Language(None), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), SetVariable("persistent.lang", 1)]
            xpos -28
            ypos 10
        imagebutton:
            if persistent.lang == 2:
                idle language_russian_hover
            else:
                idle language_russian
            hover language_russian_hover
            action [Language("russian"), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), SetVariable("persistent.lang", 2)]
            xpos -20
            ypos 20
        imagebutton:
            if persistent.lang == 3:
                idle language_belarusian_hover
            else:
                idle language_belarusian
            hover language_belarusian_hover
            action [Language("belarusian"), gui.SetPreference("font", 'ProximaNova-Bold.otf'), gui.SetPreference("size", 40), SetVariable("persistent.lang", 3)]
            xpos -4
            ypos 30
        imagebutton:
            if persistent.lang == 4:
                idle language_japanese_hover
            else:
                idle language_japanese
            hover language_japanese_hover
            action [Language("japanese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 40), SetVariable("persistent.lang", 4)]
            xpos -43
            ypos 40
        imagebutton:
            if persistent.lang == 5:
                idle language_ch_hover
            else:
                idle language_ch
            hover language_ch_hover
            action [Language("chinese"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), SetVariable("persistent.lang", 5)]
            xpos -28
            ypos 50
        imagebutton:
            if persistent.lang == 6:
                idle language_chtr_hover
            else:
                idle language_chtr
            hover language_chtr_hover
            action [Language("chinese_trad"), gui.SetPreference("font", "SourceHanSerifSC-Bold.otf"), gui.SetPreference("size", 46), SetVariable("persistent.lang", 6)]
            xpos -28
            ypos 60
    textbutton "Return" action Return() xalign 0.95 yalign 0.95
    textbutton "Help" action ShowMenu("help") xalign 0.05 yalign 0.95

screen scr_marta_phony():
    text "phony":
        at transform:
            rotate 23
            alpha 0
            pause .5
            alpha 1
        xpos 1600
        ypos 320
        size 80
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate 23
            alpha 0
            pause 1
            alpha 1
        xpos 200
        ypos 350
        size 100
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate -12
            alpha 0
            pause 1.5
            alpha 1
        xpos 100
        ypos 60
        size 110
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate 113
            alpha 0
            pause 1.8
            alpha 1
        xpos 10
        ypos 620
        size 120
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate -90
            alpha 0
            pause 2
            alpha 1
        xpos 1300
        ypos 500
        size 130
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate 37
            alpha 0
            pause 2.1
            alpha 1
        xpos 1600
        ypos -30
        size 90
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate 0
            alpha 0
            pause 2.2
            alpha 1
        color "7F1917"
        style "earwig1"
    text "phony":
        at transform:
            rotate -42
            alpha 0
            pause 2.3
            alpha 1
        xpos 1300
        ypos 140
        size 100
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate 0
            alpha 0
            pause 2.4
            alpha 1
        xpos 300
        ypos 800
        size 60
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate -20
            alpha 0
            pause 2.5
            alpha 1
        xpos 1620
        ypos 750
        size 50
        color "7F1917"
        style "earwig"
    text "phony":
        at transform:
            rotate -25
            alpha 0
            pause 2.6
            alpha 1
        xpos 20
        ypos 0
        size 70
        color "7F1917"
        style "earwig"
screen scr_sima_right1():
    text "Right?":
        at transform:
            rotate 23
            alpha 0
            pause .5
            alpha 1
        color "3ec1d3"
        style "earwig7"
    text "Right?":
        at transform:
            rotate 23
            alpha 0
            pause 1
            alpha 1
        color "3ec1d3"
        style "earwig6"
    text "Right?":
        at transform:
            rotate -12
            alpha 0
            pause 1.5
            alpha 1
        xpos 100
        ypos 60
        size 110
        color "3ec1d3"
        style "earwig"
    text "Right?":
        at transform:
            rotate 113
            alpha 0
            pause 1.8
            alpha 1
        color "3ec1d3"
        style "earwig9"
    text "Right?":
        at transform:
            rotate -90
            alpha 0
            pause 2
            alpha 1
        color "3ec1d3"
        style "earwig3"
    text "Right?":
        at transform:
            rotate 37
            alpha 0
            pause 2.1
            alpha 1
        color "3ec1d3"
        style "earwig8"
    text "Right?":
        at transform:
            rotate 0
            alpha 0
            pause 2.2
            alpha 1
        color "3ec1d3"
        style "earwig2"
    text "Right?":
        at transform:
            rotate -42
            alpha 0
            pause 2.3
            alpha 1
        xpos 1300
        ypos 140
        size 100
        color "3ec1d3"
        style "earwig"
    text "Right?":
        at transform:
            rotate 0
            alpha 0
            pause 2.4
            alpha 1
        color "3ec1d3"
        style "earwig5"
    text "Right?":
        at transform:
            rotate -20
            alpha 0
            pause 2.5
            alpha 1
        color "3ec1d3"
        style "earwig4"
    text "Right?":
        at transform:
            rotate -25
            alpha 0
            pause 2.6
            alpha 1
        xpos 20
        ypos 0
        size 70
        color "3ec1d3"
        style "earwig"
screen inactivity_timer_d1():
    imagemap:
        idle "cg/idle.png"
        hotspot (0,0,1920,1080) action [SetVariable("inactivity", 0),ui.callsinnewcontext("inactivity_check_d1")]
    if inactivity_done_d1 == 0:
        timer 10.0 action [SetVariable("inactivity", 1),ui.callsinnewcontext("inactivity_check_d1")]
screen inactivity_timer_d2():
    imagemap:
        idle "cg/idle.png"
        hotspot (0,0,1920,1080) action [SetVariable("inactivity", 0),ui.callsinnewcontext("inactivity_check_d2")]
    if inactivity_done_d2 == 0:
        timer 10.0 action [SetVariable("inactivity", 1),ui.callsinnewcontext("inactivity_check_d2")]


screen no_skip():
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_SPACE" action NullAction()
    key "mousedown_4" action NullAction()
    key "K_PAGEUP" action NullAction()
    key "mousedown_5" action NullAction()
    key "K_PAGEDOWN" action NullAction()
    key "mouseup_3" action NullAction()
    key "mouseup_1" action NullAction()
    key "K_ESCAPE" action Return("1")
screen block_scr(t):
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_SPACE" action NullAction()
    key "mousedown_4" action NullAction()
    key "K_PAGEUP" action NullAction()
    key "mousedown_5" action NullAction()
    key "K_PAGEDOWN" action NullAction()
    key "mouseup_3" action NullAction()
    key "mouseup_1" action NullAction()
    key "K_ESCAPE" action Return("1")
    timer t action Hide("block_scr") repeat False
screen press_to_start():
    tag menu
    text("Press to start"):
        at transform:
            alpha 0
            pause 2
            block:
                linear 1.5 alpha .4
                linear 1.5 alpha .1
                repeat
        color "000000"
        xalign .98
        yalign .9
        size 80
        style "bebas"
    button:
        xysize (config.screen_width, config.screen_height)
        action Jump("post_x")
screen gallery():
    tag menu
    add "book1"
    grid 2 3:
        xalign 0.5
        yalign 0.45
        xspacing 500
        yspacing 30
        add g.make_button("cg_nana_4_2", "cg_nana_4_2small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_7_1", "cg_marta_7_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        if winnie_v == 1:
            add g.make_button("cg_nana_8_1", "cg_nana_8_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        if winnie_v == 0:
            add g.make_button("cg_nana_8_2", "cg_nana_8_2small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_all_2_2", "cg_all_2_2small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_sima_3_1", "cg_sima_3_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_nana_7_1", "cg_nana_7_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
    textbutton "Next" action ShowMenu("gallery2") xalign 0.9 yalign 0.95
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen gallery2():
    tag menu
    add "book1"
    grid 2 3:
        xalign 0.5
        yalign 0.45
        xspacing 500
        yspacing 30
        add g.make_button("cg_sima_1_1", "cg_sima_1_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_all_3all", "cg_all_3small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_3_2", "cg_marta_3_2small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_barashek", "cg_barasheksmall", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_2_5", "cg_marta_2_5small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_1_1", "cg_marta_1_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
    textbutton "Next" action ShowMenu("gallery3") xalign 0.9 yalign 0.95
    textbutton "Previous" action ShowMenu("gallery") xalign 0.1 yalign 0.95
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen gallery3():
    tag menu
    add "book1"
    grid 2 3:
        xalign 0.5
        yalign 0.45
        xspacing 500
        yspacing 30
        add g.make_button("cg_sima_2_1", "cg_sima_2_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_nana_5_1", "cg_nana_5_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_nana_6_1", "cg_nana_6_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_nana_9_6", "cg_nana_9_6small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_sima_4_1", "cg_sima_4_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_sima_6_2", "cg_sima_6_2small", locked = "shadesmall", xalign=0.5, yalign=0.5)
    textbutton "Next" action ShowMenu("gallery4") xalign 0.9 yalign 0.95
    textbutton "Previous" action ShowMenu("gallery2") xalign 0.1 yalign 0.95
    textbutton "Return" action Return() xalign 0.5 yalign 0.95
screen gallery4():
    tag menu
    add "book1"
    grid 2 3:
        xalign 0.5
        yalign 0.45
        xspacing 500
        yspacing 30
        add g.make_button("cg_sima_7_1", "cg_sima_7_1allsmall", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_4_1", "cg_marta_4_1small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_5_3", "cg_marta_5_3small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_marta_6_1", "cg_marta_6_1allsmall", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_teya", "cg_teya_small", locked = "shadesmall", xalign=0.5, yalign=0.5)
        add g.make_button("cg_photo", "cg_photosmall", locked = "shadesmall", xalign=0.5, yalign=0.5)
    textbutton "Previous" action ShowMenu("gallery3") xalign 0.1 yalign 0.95
    textbutton "Return" action Return() xalign 0.5 yalign 0.95

screen allrights():
    tag menu
    add "gui_shade"
    text "This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the products of the author’s imagination or used in a fictitious manner. Any resemblance to actual persons, living or dead, or actual events is purely coincidental.\n 2020 Comfy Company All Rights Reserved.":
        style "thisisawork"
        xalign .5
        yalign .5
    timer 4 action Return()
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action Return()
screen logo_scr():
    tag menu
    add "gui_shade":
        at transform:
            alpha 1
            pause 3.5
            linear .5 alpha 0
    image "images/comfycompany.png":
        xalign .5
        yalign .6
        at transform:
            alpha 0
            pause 1
            linear .5 alpha 1
            pause 1
            linear .5 alpha 0
    text "A game by":
        style "agameby"
        xalign .5
        yalign .15
        at transform:
            alpha 0
            linear .5 alpha 1
            pause 2
            linear .5 alpha 0
screen selfie():
    tag menu
    imagemap:
        ground "hide_mask"
        hotspot (0, 0,1920, 1080) focus_mask None action Jump("main_menu")
screen navigation():
    imagebutton:
        yalign 0.015
        xalign 0.97
        idle "logo"
        action None
        at transform:
            alpha 0
            pause 1
            linear 1 alpha 1
    image "mainmenu_scroll":
        yalign 0.95
        xalign 0.995
        at transform:
            alpha 0
            pause 1
            linear 1 alpha 1
    key "K_ESCAPE" action Return()
    vbox:
        at transform:
            alpha 0
            pause 1.5
            linear 1 alpha 1
        style_prefix "navigation"
        style "menu_spacing1"
        yalign 0.68
        if persistent.game_done1 == True:
            yalign 0.7
        if persistent.game_done1 == True:
            style "menu_spacing2"

        if persistent.game_done1 == True:
            textbutton _("Continue") action Start():
                text_color "BCFFBD"
                if persistent.game_done2 == True:
                    text_color "FFA8F0"
        textbutton _("New Game") action [SetVariable("restart", 1), Start()]

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences1")

        textbutton _("Gallery") action ShowMenu("gallery")

        if renpy.variant("pc"):

            textbutton _("Quit") action Quit(confirm=not main_menu)
screen main_menu():
    tag menu
    style_prefix "main_menu"
    if persistent.game_done1 == True:
        add "mainmenugirls":
            at transform:
                alpha 0
                pause 1
                linear 1 alpha 1
    frame:
        pass
    use navigation
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
return

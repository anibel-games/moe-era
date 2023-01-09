init python:
    style.nvl_window.top_margin = 70
    style.nvl_window.bottom_margin = 70
    style.nvl_vbox.box_spacing = 10
define config.name = _("MoeEra")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _p("""
""")
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.rollback_enabled = False
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 0
default preferences.afm_time = 15
default preferences.fullscreen = True
define config.save_directory = "MoeEra"
define config.window_icon = "gui/icon.ico"
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
init python:
    build.directory_name = "MoeEra"
    build.executable_name = "MoeEra"
    build.include_update = False
    build.classify("game/**", "archive")
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
define build.itch_project = "comfycompany/moeera"

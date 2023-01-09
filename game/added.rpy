label backrooms_d1:
    play music "music/no_will.ogg"
    $ renpy.pause(3, hard=True)
    $ renpy.music.play("images/movies/backroom.webm", channel="movie", loop=True)
    scene movie with fade
    "It feels like I ended up in some sort of a tilted picture."
    "If I decide to go straight... What's behind that corner in front of me, I wonder?"
    "Truth to be told, I'm both curious and scared to check it out."
    "Can't stop the feeling that someone silently observes me." #
    "And why there's a different wallpaper on each wall?"#
    "I decide to come closer and inspect that weird red... arcade machine, I think." #
    jump lbl_lpg_1
label lbl_lpg_1:
    scene black with fade
    $ renpy.music.play("images/movies/lpg.webm", channel="movie", loop=True)
    scene movie
    show lpg_0
    show lpg_1
    show lpg_2a as lpg_2
    with fade
    pause
    "\"Life Purpose Generator\", whoa, now that's what I call a name! \"Press X to win.\""
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_1 behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_8 behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_7 behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    show lpg_2a as lpg_2 with dissolve
    "Now it looks more of a slot machine. Whatever! I press the button." #
    "Three numbers, \"187\". What does it mean? Okay, I'll give it one more try."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_1 behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_8 behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_7 behind lpg_1 as lpg_i3:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_4 behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_2 behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_0 behind lpg_1 as lpg_i6a:
        yalign .2
        xalign .625
        pause 1
        linear 2 yalign .99
    show lpg_i_4 behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 2
        linear 1 yalign .56
    $ renpy.pause(3, hard=True)
    "\"424\". Doesn't ring any bells. I think all three numbers should be the same to win something."
    "Well, a life purpose is worth giving it another go, that's for sure."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_4 behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_2 behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_4 behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_0 behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_0 behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_2 behind lpg_1 as lpg_i3:
        yalign .2
        xalign .623
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "It gets more and more random over time."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_0 behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_0 behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_2 behind lpg_1 as lpg_i3:
        yalign .56
        xalign .623
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_3 behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_1 behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_3 behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "\"002\", \"313\", what is this? One last attempt and I call it a day."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_3 behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_1 behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_3 behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_ni behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ni behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_ni behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "To my greatest surprise, I get three in a row... Three hieroglyphs."
    "If I'm not mistaken, it means \"Japan\" in, well, Japanese.."
    "Quite entertaining slot machine, I must admit." #
    "Everything gets blurry..."
    scene black
    with fade
    stop movie
    "Japan, huh?"
    stop sound fadeout 1.5
    stop music fadeout 1.5
    $ renpy.pause(3, hard=True)
    jump day1
label d1_nana:
    $ persistent.unlock_cg_nana_4_2 = 1
    show cg_nana_4_2 as nana2 with fade
    n "How did you manage to fall asleep in such a weird pose? Was it that difficult to lay on the desk?"
    p "Who knows? By the way, the dream was so bizzare. I managed to remember it." #
    n "Hey, tell me! Will you? Pretty please? Was there anything lewd?"
    show cg_nana_4_1 as nana2 with dissolve
    n "What about me? Did I appear in your dream? Ha, you're blushing! It's confession time!"
    p "It was a pure and innocent dream, Nana. Here goes..."
    "I do a quick recap of what happened in my dream."
    show cg_nana_4_2 as nana2 with dissolve
    p "So I ended up with \"Japan\", and then I woke up."
    n "Нow boring! And what's so special about Japan? I mean, we're here right now."
    n "Where else could they come up with such a marvellous idea like bringing us all here together?"
    n "By they way, if we talk about marvellous... You must see this!" #fixed in None
    hide nana2 with fade
    return
label after_meditation:
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima1 1g 2a 3a at d32 as sima
    show marta3 1b 2a 3a regular1 at d31 as marta
    with dissolve
    "I still have a few more minutes before our class starts, so I decide to go talk to someone."
    menu:
        "Talk to Nana.":
            if game_restarted2 == 1:
                if persistent.game_done2 == True:
                    if persistent.girl1_done == "N":
                        jump catgirl_extra0
                    if persistent.girl2_done == "N":
                        jump catgirl_extra0
                    else:
                        $ nana_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_6

            if game_restarted1 == 1:
                if persistent.game_done1 == True:
                    if persistent.girl1_done == "N":
                        jump catgirl_extra0
                    if persistent.girl2_done == "N":
                        jump catgirl_extra0
                    else:
                        $ nana_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_3

            $ acn_p = 2
            hide sima
            hide marta
            show nana1close 1a 2a 3a regular2 at u11 as nana
            $ renpy.pause(.5, hard=True)
            show nana3close 1e 2a 3a at u11 as nana with dissolve
            n "What, do you expect me to invite you to that cafe?"
            show nana3close 1d 2a 3b at u11 as nana with dissolve
            n "Well, who knows, if your offer something cool in return..." #
            show nana1close regular1 1d 2c 3a at u11 as nana with dissolve
            n "How much cash do you have on ya?"
            show nana1close regular2 1a 2a 3a at u11 as nana with dissolve
            p "Hey, I just wanted to talk for a while before the lesson starts."
            show nana1close regular2 1e 2a 3d at u11 as nana with dissolve
            n "For a while? Well, it's quite some time, you know. And time is money!"
            show nana1close regular2 1a 2a 3d at u11 as nana with dissolve
            p "How much is worth, say, one hour of your time?"
            show nana1close regular1 1e 2d 3c  blush at u11 as nana with dissolve
            n "How dare you asking a girl about stuff like this!" #
            show nana3close 1e 2a 3d noblush at u11 as nana with dissolve
            n "A short talk, say, 2-3 minutes or so... 10 thousand yen."
            show nana3close 1a 2a 3d at u11 as nana with dissolve
            "I forgot the exchange ratio but I think it's quite a lot.."
            "Having remembered my dream, I decide to mock Nana a little."
            p "Alright, I'm ready to pay, but you need to throw in one life purpose for me."
            show nana1close regular2 1c 2a 3a at u11 as nana with dissolve
            n "Jeez, you're going over it again! Just forget about it, okay?"
            show nana1close regular2 1f 2a 3d at u11 as nana with dissolve
            p "Okay, okay... It was just too realistic to forget."
            show nana2close 1d 2a 3d at u11 as nana with dissolve
            n "Of course! Nothing but a sheer truth, [player_name], that's what that dream is."
            show nana2close 1c 2a 3a at u11 as nana with dissolve
            n "Like, seriously? Don't you know about the Occam razor, [player_name]?"#
            show nana3close 1b 2a 3b at u11 as nana with dissolve
            n "Ha, desperately trying to remember! And they told everyone is so smart here..."#
            show nana3close 1e 2a 3a at u11 as nana with dissolve
            n "According to him, the most obvious explanation to something is likely to be true."
            show nana1close regular2 1e 2a 3a at u11 as nana with dissolve
            n "You were tired, fell asleep, saw us... And yeah, we're in Japan. See the point?"
            show nana1close regular2 1d 2b 3d at u11 as nana with dissolve
            n "Something tells me you don't even have 10 thousand yen on ya to begin with. Oh well, forget it." #shortened in None
            show nana1close regular2 1a 2a 3a at u11 as nana with dissolve
            p "I can't believe I owe you money even though you made fun of me."
            show nana3close 1e 2a 3b at u11 as nana with dissolve
            n "Ha! Well, I'm unbelievable!"
            return
        "Talk to Sima":
            if game_restarted2 == 1:
                if persistent.game_done2 == True:
                    if persistent.girl1_done == "S":
                        jump catgirl_extra0
                    if persistent.girl2_done == "S":
                        jump catgirl_extra0
                    else:
                        $ sima_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_7
            if game_restarted1 == 1:
                if persistent.game_done1 == True:
                    if persistent.girl1_done == "S":
                        jump catgirl_extra0
                    if persistent.girl2_done == "S":
                        jump catgirl_extra0
                    else:
                        $ sima_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_4
            $ acs_p = 2
            hide marta
            hide nana
            with dissolve
            show sima1close 1a 2a 3a at u11 as sima with dissolve
            p "How are you?"
            show sima1close 1d 2a 3a at u11 as sima with dissolve
            s "Good, thanks."
            show sima1close 1g 2a 3a at u11 as sima with dissolve
            "She looks at me with her brilliant eyes, and then smiles."
            show sima2close 1c 2a 3d regular2 at u11 as sima with dissolve
            s "That's the toughest part of the conversation, right?"
            show sima2close 1e 2a 3a regular2 at u11 as sima with dissolve
            s "When you have to say something, but nothing comes on your mind."#
            show sima2close 1d 2b 3b regular2 at u11 as sima with dissolve
            s "To tell you the truth, I struggle with this just like you do." #
            show sima3aclose 1c 2a 3d at u11 as sima with dissolve
            s "I mean, I could've told you about a dream I saw once, but I don't see dreams."
            show sima3aclose 1a 2a 3d at u11 as sima with dissolve
            "Can't be any better to tell her about the dream I had today."
            show sima3aclose 1d 2c 3a at u11 as sima with dissolve
            s "Wow, so exciting! And you say we stood in... shining arcs?"
            show sima3aclose 1a 2c 3a at u11 as sima with dissolve
            p "Yeah, and everything was blinking around you."
            show sima3bclose 1d 2a 3b at u11 as sima with dissolve
            s "As if it was a Botticelli or Leonardo Da Vinci painting!"
            show sima2close 1d 2c 3a regular1 at u11 as sima with dissolve
            s "If you haven't seen their masterpiece, go and take a look! Mesmerizing..."
            show sima3bclose 1d 2a 3b at u11 as sima with dissolve
            s "If your dream was true, it'd be so entertaining."
            show sima3aclose 1c 2b 3a at u11 as sima with dissolve
            s "Each day would be more and more exciting! Shame it's not going to happen."
            show sima3aclose 1e 2b 3d at u11 as sima with dissolve
            s "I mean, it's unlikely that studies would be included in these four day, and you're here..."
            show sima3aclose 1d 2a 3a at u11 as sima with dissolve
            s "From another side, I enjoy studying, so who knows..."
            show sima2close 1d 2a 3a regular2 at u11 as sima with dissolve
            s "No. After all, your dream can't be true."
            show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
            p "Why do you think so?"
            show sima2close 1d 2a 3a regular1 at u11 as sima with dissolve
            s "Think about it... How is it possible to change anything in just four days?"
            show sima2close 1c 2c 3a regular1 at u11 as sima with dissolve
            s "By the way, it's very easy to test whether or not you're sleeping."
            show sima2close 1e 2a 3a regular1 at u11 as sima with dissolve
            p "Like, in a dream it's not possible to think of it as a dream?"
            show sima2close 1c 2c 3a regular2 at u11 as sima with dissolve
            s "What? No, of course not. It's much easier... {w} Like this! {w=.25}{nw}"
            show sima2close 1e 2a 3a regular2 at ui11 as sima with dissolve:
                zoom 1
                linear .25 zoom 1.03
                linear .25 zoom 1
            "Sima pinches me!"
            p "Ouch!"
            show sima3bclose 1e 2c 3b at u11 as sima with dissolve
            s "See? In a dream, you're unlikely to feel anythng. Good morning!"
            show sima3aclose 1a 2a 3a at u11 as sima with dissolve
            p "Don't think it was convincing enough. I need to pinch you as well."
            show sima3aclose 1d 2a 3d at u11 as sima with dissolve
            s "I'm afraid we don't know each other well enough to do this."
            return
        "Talk to Marta":
            if game_restarted2 == 1:
                if persistent.game_done2 == True:
                    if persistent.girl1_done == "M":
                        jump catgirl_extra0
                    if persistent.girl2_done == "M":
                        jump catgirl_extra0
                    else:
                        $ marta_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_8
            if game_restarted1 == 1:
                if persistent.game_done1 == True:
                    if persistent.girl1_done == "M":
                        jump catgirl_extra0
                    if persistent.girl2_done == "M":
                        jump catgirl_extra0
                    else:
                        $ marta_plusset = True
                        call catgirl_extra4 from _call_catgirl_extra4_5
            $ acm_p = 2
            hide sima
            hide nana
            show marta3close 1a 2a 3a regular1 at d11 as marta
            p "Hey, what's up?"
            show marta2close 1e 2a 3a regular1 at u11 as marta with dissolve
            m "Nothing much. What do you want? I'm busy."
            show marta2close 1a 2a 3a regular1 at u11 as marta with dissolve
            p "..."
            show marta3close 1ee 2a 3b regular2 at u11 as marta with dissolve
            m "Just kidding! I'm great, and what about you?"
            show marta3close 1b 2a 3a regular1 at u11 as marta with dissolve
            p "Same! See, I fell asleep right behind my desk, then had a really weird dream..."
            show marta2close 1d 2c 3a regular1 at u11 as marta with dissolve
            m "Whoa. Tell me about it."
            show marta2close 1a 2a 3a regular1 at u11 as marta with dissolve
            "That's exactly what I do next."
            show marta2close 1e 2a 3a regular2 at u11 as marta with dissolve
            m "Not bad! And not finished... You better had a continuation." #
            show marta2close 1g 2a 3a regular1 at u11 as marta with dissolve
            p "Yeah, I just thought, you know... What if it was not a dream?"
            show marta2close 1e 2a 3a regular1 at u11 as marta with dissolve
            m "Like, that your life story is actually empty and all?"
            show marta2close 1a 2a 3a regular1 at u11 as marta with dissolve
            p "Yeah."
            show marta3close 1e 2a 3a regular1 at u11 as marta with dissolve
            m "Relax, a whole lot of people have the same issue."
            show marta3close 1g 2a 3a regular1 at u11 as marta with dissolve
            m "You have an upper hand now that you're young. Change your life and all..."
            show marta2close 1e 2a 3a regular1 at u11 as marta with dissolve
            m "From another side... You know, by our age..."
            show marta1close 1c 2a 3b at u11 as marta with dissolve
            m "Some people already have money, fame, you name it."
            show marta1close 1e 2a 3a at u11 as marta with dissolve
            m "Meanwhile, we're here, reading books. Oh well. We're going to make it."
            show marta1close 1a 2a 3a at u11 as marta with dissolve
            p "Sure thing. However, it's better to plan long term soon and all, right?"
            show marta2close 1b 2a 3a regular2 at u11 as marta with dissolve
            m "Ha, and I have everything carefully planned already!"
            show marta2close 1a 2a 3a regular1 at u11 as marta with dissolve
            p "So what are you going to do?"
            show marta3close 1e 2a 3a regular1 at u11 as marta with dissolve
            m "Like I told you! What if you decide to steal my plan?"
            show marta3close 1d 2a 3a regular1 at u11 as marta with dissolve
            m "Well, it's nothing special... Maybe I'll tell you later."
            return
label drinking_tea:
    n "Yummy!"
    m "Better than your imaginary cakes, huh?"
    n "Hey, go easy on my fancy cakes!"
    m "Alright, alright. Yeah, and thanks for the cookies, Sima."
    s "You're welcome! I'll bring more if you like it. How's the tea?"
    n "Your highness, the tea is..."
    m "The tea is awesome, cut it short."
    s "Glad you liked it! I found an awesome shop with sencha, genmaicha and all."
    n "Whoa, you know a lot about it! I bet it's also very expensive..."
    s "Yes, but it's well worth the money."
    m "By the way, Sima, is it true that you have a Hermes scarf?"#
    s "It is true, but I only wear it on weekends... occasionally."
    m "I would wear it 24/7!"
    s "Don't you think others would judge you?"
    n "The brand is this famous?"
    m "Oh yeah."
    n "I'll save money and buy it on a sale!"
    m "Nana, this brand doesn't put their goods on sale, they don't need it."
    n "How foolish of them!"
    s "I'd rather say it's foolish to discuss these topics when we have [player_name] here..."
    m "Oh yeah. [player_name] is highly unlikely to appreciate it."
    n "Let's talk about something fun then!"
    m "Deal, here's the story... Yesterday, this guy calls me again, then..."
    n "The one who expressed his feelings to you with a, oh my, a love letter?"
    s "Nana, don't make fun of knights in shining armor, they're almost extinct."
    n "Welcome to the jungle!"
    m "Yeah, he calls me then..."
    p "..."
    s "[player_name], I'm sorry. We're getting distracted again."
    m "Right. Well, I tried my best. Go ahead and shoot your topic of choice."
    n "Where do you want to work? I'm talking about the future."
    s "Haven't though about it yet."#
    n "What about a marriage? Oh, right, we shouldn't forget about [player_name]!"#
    n "[player_name], what about your marriage?"
    s "Nana!"
    n "What? I'm just eating my cookie!"
    "Actually, I'm totally cool with everything. It's warm and comfortable here."
    "I feel like a fat cat laying out in the sun."
    return
label after_club_nana:
    show nana1_redtint 1e 2a 3a regular1 at u11 as nana with dissolve
    n "[player_name], what do you like the most — morning or evening?"
    show nana1_redtint 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Where's the \"day\" option?"
    show nana1_redtint 1c 2a 3d regular2 at u11 as nana with dissolve
    n "Hey, it's too boring. It's not an answer worth replying."
    show nana1_redtint 1a 2a 3d regular2 at u11 as nana with dissolve
    p "Dangerous statement, Nana..."
    show nana3_redtint 1e 2a 3d at u11 as nana with dissolve
    n "C'mon! I bet you also consider yourself smarter than others."
    show nana3_redtint 1a 2a 3d at u11 as nana with dissolve
    p "Well..."
    show nana3_redtint 1d 2d 3a at u11 as nana with dissolve
    n "Well then, you better answer honestly... and cleverly!"
    show nana3_redtint 1f 2d 3a at u11 as nana with dissolve
    p "Why do you hate \"others\" that much?"
    show nana2_redtint 1d 2a 3d at u11 as nana with dissolve
    n "It's not like I hate them! It's just I don't have anything to talk about with them."#
    show nana2_redtint 1a 2a 3d at u11 as nana with dissolve
    p "Name one topic you can discuss with me that you can't discuss with them."
    show nana2_redtint 1c 2a 3a at u11 as nana with dissolve
    n "Easy!"
    show nana3_redtint 1c 2a 3d at u11 as nana with dissolve
    n "When travelling abroad, far, far away, do you like to..."
    show nana3_redtint 1e 2a 3a at u11 as nana with dissolve
    n "Say, check out a random grocery store to try out some weird local food?"
    show nana1_redtint 1e 2a 3a regular1 at u11 as nana with dissolve
    n "And then just sit for a while and listen? Listen to the people and ambiance."
    show nana1_redtint 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Of course I like doing what you said. What's so special about it?."#
    show nana1_redtint 1c 2b 3d regular2 at u11 as nana with dissolve
    n "The majority of people would call your trip a waste of time, because you haven't seen much."
    show nana2_redtint 1d 2a 3d at u11 as nana with dissolve
    n "The best practice is to jam pack everything in two days, visiting touristic shrines only..."
    show nana2_redtint 1c 2a 3a at u11 as nana with dissolve
    n "Then fly away, saying that the country is nothing special and tourist-infested."
    show nana2_redtint 1b 2b 3b at u11 as nana with dissolve
    n "Learning a few words in local language? Nope, just speak really slow in your mother tongue."#
    show nana1_redtint 1c 2d 3d regular2 at u11 as nana with dissolve
    n "It's the kind of people that leave reviews on the internet."
    show nana1_redtint 1f 2a 3a regular2 at u11 as nana with dissolve
    p "Sounds silly, as everything would looks the same had I travel like this."#
    show nana1_redtint 1e 2d 3a regular1 at u11 as nana with dissolve
    n "They don't even notice the world, they need to show others that they travel more then them." #fixed in None
    show nana1_redtint 1a 2c 3c regular2 at u11 as nana with dissolve
    p "I guess you've travelled a lot, haven't you, Nana?"
    show nana1_redtint 1e 2c 3c blush regular1 at u11 as nana with dissolve
    n "Well, not that much, but I managed to understand everything about travel!"
    show nana1_redtint 1a 2c 3a noblush regular2 at u11 as nana with dissolve
    p "Got it. And how's Japan treating you?"
    show nana1_redtint 1e 2b 3a regular2 at u11 as nana with dissolve
    n "Kind of silly to ask me about this, you know how much time I've spent here..."
    show nana1_redtint 1f 2b 3a regular2 at u11 as nana with dissolve
    p "How is that relevant to my question?"
    show nana3_redtint 1e 2a 3a at u11 as nana with dissolve
    n "The grass is always greener on the other side, [player_name]."
    show nana3_redtint 1a 2a 3a at u11 as nana with dissolve
    p "I see."
    show nana3_redtint 1c 2a 3d at u11 as nana with dissolve
    n "I really love my country though, don't get it wrong, okay?"#
    show nana3_redtint 1a 2a 3d at u11 as nana with dissolve
    p "For me, pretty much everything seems perfect here."
    show nana1_redtint 1e 2a 3a regular2 at u11 as nana with dissolve
    n "Of course, you're a visitor! It's one of the best countries to visit as a tourist."
    show nana1_redtint 1d 2a 3d regular2 at u11 as nana with dissolve
    n "My favorite thing about Japan is that people here are considerate of others. Well, mainly..."
    show nana1_redtint 1e 2a 3a regular2 at u11 as nana with dissolve
    n "You can craft your own world and be sure you'll find similarly minded people."
    show nana2_redtint 1d 2a 3d at u11 as nana with dissolve
    n "It's very peaceful here if you don't ask for much and live in the country."
    show nana2_redtint 1b 2a 3a at u11 as nana with dissolve
    n "But then you start working in Tokyo, doing daily morning commutes from Chiba via Chuo-Sobu line..." #fixed in None
    show nana2_redtint 1g 2a 3a at u11 as nana with dissolve
    p "Doesn't ring any bells for me."
    show nana1_redtint 1e 2a 3a regular2 at u11 as nana with dissolve
    n "Why would it? You're an exchange student, after all."
    show nana1_redtint 1d 2b 3d regular2 at u11 as nana with dissolve
    n "Alright, let's go with something you can understand: it's awesome here if you don't stand out."
    show nana2_redtint 1c 2a 3d at u11 as nana with dissolve
    n "As for me... honestly, I fail to fit in."
    show nana2_redtint 1a 2a 3d at u11 as nana with dissolve
    p "I've also noticed how polite everyone is."
    show nana2_redtint 1d 2d 3a at u11 as nana with dissolve
    n "Politeness here has a solid foundation. However, sometimes it becomes as solid as a concrete wall."
    show nana2_redtint 1c 2b 3b at u11 as nana with dissolve
    n "Oh, and don't forget — if you're an outsider, you'll be considered as an outsider forever."
    show nana1_redtint 1e 2a 3a regular1 at u11 as nana with dissolve
    n "By the way, people here really love France! France is like the European version of Japan."
    show nana1_redtint 1a 2a 3a regular2 at u11 as nana with dissolve
    p "What? They have nothing in common!"
    show nana1_redtint 1d 2a 3a regular2 at u11 as nana with dissolve
    n "The ambiance, the vibe is somewhat similar. But this topic is also too complex for a lot of people."
    return
label after_club_sima:
    show sima2_redtint 1c 2b 3a regular2 at u11 as sima with dissolve
    s "I'm so sorry we somewhat left you alone at the club. We got dragged away..."
    show sima2_redtint 1a 2b 3a regular2 at u11 as sima with dissolve
    p "It's okay, don't worry! But it's so nice of you to be worried, you know."
    show sima2_redtint 1g 2b 3a regular2 at u11 as sima with dissolve
    p "I really managed to unwind... Just chilling, listening to your debates..."
    p "You guys really like to argue. Well, everyone does."
    show sima2_redtint 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Everyone like to argue, few know what it's all about. Arguing means exchanging opinions, right?"
    show sima2_redtint 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Sure."
    show sima2_redtint 1c 2b 3d regular2 at u11 as sima with dissolve
    s "Guess what, people tend to think that the key point of a debate is to win it."
    show sima3a_redtint 1c 2a 3d at u11 as sima with dissolve
    s "They don't even understand that there are no right and wrong opinions, it's all subjective."
    show sima3a_redtint 1a 2a 3d at u11 as sima with dissolve
    p "It's a rather complex concept, don't think too many would get it."
    show sima3a_redtint 1d 2a 3a at u11 as sima with dissolve
    s "That's why now I'd rather stay away from arguing than wasting my time."
    show sima3a_redtint 1a 2a 3a at u11 as sima with dissolve
    p "Meaning that before you used to like debates?"
    show sima2_redtint 1d 2a 3a regular1 at u11 as sima with dissolve
    s "You bet, but it all went downhill after one day..."
    show sima2_redtint 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Tell me the story."
    show sima2_redtint 1c 2a 3a regular2 at u11 as sima with dissolve
    s "Well, they tried to gather a women volleyball team to represent my city at one big tournament."#
    show sima1_redtint 1d 2a 3a at u11 as sima with dissolve
    s "Before that team was comprised mainly of girls from the same school."#
    show sima1_redtint 1c 2a 3a at u11 as sima with dissolve
    s "They had the best training grounds, great coach, lots of experience..."
    show sima1_redtint 1d 2a 3d at u11 as sima with dissolve
    s "Then it was decided that they don't give other girls any chance to play at all."
    show sima1_redtint 1d 2a 3b at u11 as sima with dissolve
    s "Next thing you know, they said that half of the roster should be filled from other schools."
    show sima1_redtint 1c 2a 3a at u11 as sima with dissolve
    s "And their reasoning? Equality."
    show sima1_redtint 1a 2a 3a at u11 as sima with dissolve
    p "What happened next?"
    show sima2_redtint 1d 2d 3a regular1 at u11 as sima with dissolve
    s "They booted me out when I said they don't understand what equality means."
    show sima2_redtint 1a 2a 3a regular1 at u11 as sima with dissolve
    p "What do you mean?"
    show sima2_redtint 1d 2d 3d regular1 at u11 as sima with dissolve
    s "Equality is when the team consists of the best players in town, regardless of their schools."
    show sima2_redtint 1a 2a 3d regular1 at u11 as sima with dissolve
    p "Something tells me the new team didn't win the tournament."
    show sima2_redtint 1c 2a 3b regular2 at u11 as sima with dissolve
    s "They were destroyed."
    show sima2_redtint 1d 2b 3a blush regular2 at u11 as sima with dissolve
    s "My, I probably picked yet another boring topic..."
    show sima2_redtint 1a 2b 3a regular2 at u11 as sima with dissolve
    p "Nah, I'm fine with it. Seriously."
    show sima2_redtint 1d 2c 3a regular1 at u11 as sima with dissolve
    s "No way! We must start a casual chit-chat like normal people do."#
    show sima2_redtint 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Chit-chat about what?"
    show sima2_redtint 1d 2c 3c regular1 at u11 as sima with dissolve
    s "Um, well... I like cats! And fancy dresses... and everything!"
    show sima2_redtint 1c 2b 3a regular2 at u11 as sima with dissolve
    s "Sometimes I talk about sophisticated things, but it's not on purpose."
    show sima2_redtint 1a 2b 3a regular2 noblush at u11 as sima with dissolve
    "I try my best to hide a smile."
    return
label after_club_marta:
    show marta3_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    m "How's your life story going, [player_name]?"
    show marta3_redtint 1ee 2a 3a regular2 at u11 as marta with dissolve
    m "One page per hour, I hope?"
    show marta3_redtint 1bb 2a 3a regular2 at u11 as marta with dissolve
    "I feel a little bit uncomfortable."
    show marta3_redtint 1b 2a 3a regular1 at u11 as marta with dissolve
    p "Oh well, you know, maybe not so fast..."
    show marta2_redtint 1b 2a 3a regular1 at u11 as marta with dissolve
    m "Great! That means I can relax a bit. I was so nervous when I got here!"
    show marta2_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Why?"
    show marta2_redtint 1e 2a 3a regular2 at u11 as marta with dissolve
    m "Everyone was supposed to be super smart here. What I would've been the worst?"#
    show marta2_redtint 1b 2a 3a regular1 at u11 as marta with dissolve
    m "Jeez, it scares me even to think about it. Glad everything turned out to be ok."
    show marta2_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Am I that stupid?"
    show marta2_redtint 1b 2a 3a regular2 at u11 as marta with dissolve
    m "Please notice that I'm not the first one to say it!"#
    show marta3_redtint 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Anyway, I fit in perfectly here. Should I stay in Japan forever?"
    show marta3_redtint 1e 2a 3b regular1 at u11 as marta with dissolve
    m "I'd become an English teacher, enjoy the cherry blossoms and all."
    show marta3_redtint 1d 2a 3a regular1 at u11 as marta with dissolve
    m "From another side, it will be too hot in summer."#
    show marta2_redtint 1b 2a 3a regular1 at u11 as marta with dissolve
    m "Let it be the backup plan, but I'm open for offers. Let me know if they mention me there."
    show marta2_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Where?"
    show marta2_redtint 1b 2c 3a regular2 at u11 as marta with dissolve
    m "In your life story, of course! I guess someone wise writes it."
    show marta2_redtint 1b 2a 3d regular1 at u11 as marta with dissolve
    m "Anyway, people are really interesting here, although this place is bit weird."#
    show marta2_redtint 1g 2a 3d regular1 at u11 as marta with dissolve
    p "Imaginary cakes, huh?"
    show marta2_redtint 1e 2a 3d regular2 at u11 as marta with dissolve
    m "Nah, it's nothing. I've just never seen a class of just 5 people."
    show marta2_redtint 1e 2c 3a regular2 at u11 as marta with dissolve
    m "And how come Teya can teach us all subjects? It's not possible!"
    show marta2_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Well, she must be the only one."
    show marta2_redtint 1b 2a 3c regular2 at u11 as marta with dissolve
    m "Yeah. Then again, we have a whole floor dedicated only for us..."
    show marta2_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "Pretty cool, I've told all my friends about it."
    show marta3_redtint 1gg 2a 3a regular2 at u11 as marta with dissolve
    m "Keeping the plebs out? Maybe, but..."
    show marta3_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    m "I need to stop complicating things. Let's go."
    show marta3_redtint 1e 2a 3a regular1 at u11 as marta with dissolve
    m "But even before that I insist that you admire my outfit!"
    show marta3_redtint 1b 2a 3a regular1 at u11 as marta with dissolve
    "I'm ashamed to admit I don't even know an appropriate word for it."
    p "It's cool."
    show marta2_redtint 1b 2a 3a regular2 at u11 as marta with dissolve
    m "I designed it! Looks like what they wear in Harvard, see?"
    show marta2_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Don't think I remember their colors, to be honest."
    show marta2_redtint 1e 2c 3c regular1 at u11 as marta with dissolve
    m "How could you? Harvard is so cool! I dream of getting there."
    show marta2_redtint 1a 2a 3a regular1 at u11 as marta with dissolve
    p "But the requirements are so high..."
    show marta2_redtint 1d 2d 3d regular1 at u11 as marta with dissolve
    m "Now you talk like one of those people from other floors here in this building."
    show marta2_redtint 1e 2d 3c regular2 at u11 as marta with dissolve
    m "No excuses! I'll be there!"
    show marta2_redtint 1d 2d 3c regular2 at u11 as marta with dissolve
    p "What if you won't make it through admission process?"#
    show marta1_redtint 1e 2d 3d at u11 as marta with dissolve
    m "Conditionals are for losers."
    show marta3_redtint 1e 2a 3a regular1 at u11 as marta with dissolve
    m "We're going to make it."
    show marta3_redtint 1g 2a 3a regular1 at u11 as marta with dissolve
    m "You know, last week Sima listened to some Russian rock, and I asked to translate the text."
    show marta3_redtint 1gg 2c 3b regular2 at u11 as marta with dissolve
    m "\"Good morning, the last hero...\""
    show marta3_redtint 1ee 2a 3a regular2 at u11 as marta with dissolve
    m "What do you know, it's me!"
    return
label cats_dorsia:
    scene cats_1 with fade
    show screen cats_1_screen
    n "But you haven't seen everything! Check it out! "
    s "What a cute kitty. But look at this..."
    m "Ha! Yo know nothing about cute cats!"          #fixed in None
label cats_1:
    "The girls put their phones on the desk, so each cat could be seen and compared to others."
    "For me, they're all good, but judging by the looks on the girls' faces, it's not that easy."
    n "We need a judge here! I hereby propose [player_name] to fill his role!"#
    m "Agreed!"
    s "Approved!."          #fixed in None
    n "Well, which cat is the cutest one around?"
    "Whoops, I better come up with an answer decent enough."#
    "Should I say that they're all great?"
    "No, I think I know a better answer."
    p "Let me show you another picture, ladies."
    hide screen cats_1_screen
    scene cats_2 with dissolve
    show screen cats_2_screen
    "I put my phone on the table, with my cat on the screen."
    n "Meh... I hereby propose to strip [player_name] of his position as a judge!"
    m "Agreed!"
    s "Approved!"
    "There was an attempt."
    play music "music/lets_read.ogg" fadeout 1.5 fadein 1.5
    hide screen cats_2_screen
    hide screen cats_2_1_screen
    hide screen cats_2_2_screen
    hide screen cats_2_3_screen
    hide screen cats_2_1_screen2
    hide screen cats_2_2_screen2
    hide screen cats_2_3_screen2
    hide screen cats_2_4_screen2
    scene black with fade
    $ renpy.pause(1, hard=True)
    return
label teya_talk:
    show teya2 1a 2a 3a regularhand4 at u11 as teya
    "Shorly after the class ends, Teya leaves the class and stands near the door."
    p "Thanks for the lesson!"
    show teya2 1c 2a 3a regularhand1 at u11 as teya with dissolve
    t "Oh, [player_name]. You're welcome!... Glad to see you liked it."
    show teya2 1a 2a 3a regularhand4 at u11 as teya with dissolve
    p "And do you like to teach us here?"
    show teya1 1e 2a 3b blush at u11 as teya with dissolve
    t "You're special... In a good sense of this word."
    show teya2 1e 2a 3a regularhand2 noblush at u11 as teya with dissolve
    t "It's important for me that you guys have your own opinion."
    show teya2 1a 2a 3a regularhand4 at u11 as teya with dissolve
    p "Where did you work before?"
    show teya2 1c 2a 3a regularhand1 at u11 as teya with dissolve
    t "Oh my, too many places to remember."
    show teya2 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "Is it new for your to teach almost all subjects at once?" #fixed in None
    show teya3 1c 2a 3b at u11 as teya with dissolve
    t "Yeah. They say it's an experiment, you know."
    show teya3 1c 2a 3a at u11 as teya with dissolve
    t "However, it's true that I know a lot of subjects quite well."
    show teya2 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "I take it you work as a teach for a long time."#
    show teya2 1e 2d 3c regularhand2 at u11 as teya with dissolve
    t "Look at him! Are you going to ask me how old I am next?"
    show teya2 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "No, of course not. However, I don't even your home country."#
    show teya1 1e 2a 3b at u11 as teya with dissolve
    t "How come? Oh you! That means you haven't even read my profile in the booklet."
    show teya1 1a 2a 3a at u11 as teya with dissolve
    "I actually lost it somewhere."
    show teya1 1c 2a 3d at u11 as teya with dissolve
    t "I'm from Europe, but that's about all I'm going to uncover! Women are mysterious, you see."
    show teya2 1e 2a 3a regularhand4 at u11 as teya with dissolve
    t "I have to run. See you!!"
    hide teya with dissolve
    return
label lbl_lpg_2:
    scene black with fade
    $ renpy.pause(1.5, hard=True)
    play music "music/no_will.ogg"
    $ renpy.pause(1.5, hard=True)
    $ renpy.music.play("images/movies/backroom.webm", channel="movie", loop=True)
    scene movie with eye_open
    "Again at this place!"
    "And again everything is tilted around me. I'm getting nauseous..."
    "Strange, I don't think I've ever experienced the same dream before."
    "Or maybe I just don't remember..."
    "Arcade machine... or is that slot machine? Anyway, I need to get closer to it."#
    scene black with fade
    $ renpy.music.play("images/movies/lpg.webm", channel="movie", loop=True)
    scene movie
    show lpg_0
    show lpg_1
    show lpg_2a as lpg_2
    with fade
    pause
    "This time I push the button right when I get close to the machine."
    "Random numbers? Japan? What will I see this time?"
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_qr behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_cr behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_ur behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    show lpg_2a as lpg_2 with dissolve
    "\"ЙЦУ\"?"
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_qr behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_cr behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_ur behind lpg_1 as lpg_i3:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_rr behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_tr behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_yr behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "\"КЕН\"?"
    "Today is cyrillic day."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_rr behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 2 yalign .99
    show lpg_i_tr behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause 1
        linear 2 yalign .99
    show lpg_i_yr behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1.5
        linear 2 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_pr behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 2 yalign .56
    show lpg_i_ur behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause 1
        linear 2 yalign .56
    show lpg_i_sr behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1.5
        linear 2 yalign .56
    $ renpy.pause(3, hard=True)
    "The machine spins a little bit longer this time."
    "\"РУС\"?"
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_pr behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ur behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_sr behind lpg_1 as lpg_i3:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_pr behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ur behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_sr behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "Alright, I got it, but why the winning sound? The letters are different." #fixed in None
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_pr behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ur behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_sr behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_pr behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ur behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_sr behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "But the machine doesn't care about what I think and keeps on spinning."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_pr behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ur behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_sr behind lpg_1 as lpg_i3:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_pr behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ur behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_sr behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "Over and over I have the same letters appearing on the screen.."
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_pr behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ur behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_sr behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(1, hard=True)
    scene black
    with fade
    stop movie
    stop sound fadeout 1
    stop music fadeout 1
    $ renpy.pause(2, hard=True)
    jump day2
label street_before_d2:
    $ renpy.music.set_volume(.18, 0, channel = "sound")
    play sound "sound/russia_road.ogg" fadein 1.5 loop
    $ renpy.music.set_volume(.06, 0, channel = "music")
    play music ["<silence 4.0>", "sound/SOSPetlya.ogg"] fadein 2 noloop
    "Every day I follow pretty much the same route, but today it feels different."
    "I notice Sima standing near the grocery store."
    show sima3a_grey 1a 2a 3a at u11 as sima
    p "Good morning!"
    show sima2_grey 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Hey there! We live pretty close to each other, huh..."
    show sima2_grey 1c 2a 3a regular2 at u11 as sima with dissolve
    s "I'm surprised we haven't met before. I mean, on the way to school."
    show sima2_grey 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Who're you waiting for?"
    show sima2_grey 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Nana and Marta. Guess what, they're late again! Oh well, being ten minutes late in Russia is nothing."
    show sima1_grey 1a 2a 3a at u11 as sima with dissolve
    p "You won't believe, but I woke up with a feeling that I should be in Japan."#
    p "Weird, right?"
    show sima3a_grey 1c 2a 3a at u11 as sima with dissolve
    s "I don't think it's weird. It'd be extremely boring if your dreams resembled real life."
    show sima3a_grey 1a 2a 3a at u11 as sima with dissolve
    p "You think so?"
    show sima3a_grey 1d 2a 3d at u11 as sima with dissolve
    s "I'm sure about it! Some people like to make the movies which are just too realistic."#
    show sima1_grey 1d 2a 3a at u11 as sima with dissolve
    s "Sometimes they're so realistic I can't really force myself to keep watching."
    show sima1_grey 1c 2b 3d at u11 as sima with dissolve
    s "I mean, I'm dreaming about my own world yet they try remind me of my own."#
    show sima2_grey 1e 2a 3a regular1 at u11 as sima with dissolve
    s "Okay, [player_name], this world is just as fine! Let's go, shall we?"
    show sima2_grey 1a 2a 3a regular2 at u11 as sima with dissolve
    p "I wonder why they gathered us here in Russia."
    show sima2_grey 1c 2c 3a regular1 at u11 as sima with dissolve
    s "Well, where else do they like to set targets this ambitious?"
    show sima3a_grey 1c 2a 3a at u11 as sima with dissolve
    s "\"An experiment worthy of the Soviet school of education.\". Remember?"
    show sima3a_grey 1a 2a 3a at u11 as sima with dissolve
    p "Yeah, I do... Well, do you like it here?"
    show sima2_grey 1d 2a 3b regular1 at u11 as sima with dissolve
    s "Sure, I love my country, it's great!"
    show sima2_grey 1a 2a 3a regular1 at u11 as sima with dissolve
    p "You may know that a lot of people have mixed bag opinions about it."
    show sima1_grey 1c 2d 3d at u11 as sima with dissolve
    s "Screw them! They just don't get what Russia is about."
    show sima1_grey 1a 2d 3d at u11 as sima with dissolve
    p "I wonder what."
    show sima1_grey 1d 2a 3a at u11 as sima with dissolve
    s "What do you think?"
    show sima1_grey 1a 2a 3a at u11 as sima with dissolve
    p "Well... It's huge. Moscow and Red Square. AK-47."
    show sima3a_grey 1c 2b 3d at u11 as sima with dissolve
    s "Meh."
    show sima3a_grey 1d 2a 3a at u11 as sima with dissolve
    s "Byy the way, I think that Moscow doesn't represent Russia all too well."#
    show sima2_grey 1d 2c 3a regular1 at u11 as sima with dissolve
    s "Russia is like an endless country road with tyre shops, small towns and grocery stores along the way."#
    show sima2_grey 1c 2a 3b regular1 at u11 as sima with dissolve
    s "First you hate it, then you admit it, then you get to like it. Trust me, I know what I'm talking about."
    show sima2_grey 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Whoa, you're like a philosopher."
    show sima2_grey 1e 2a 3a regular1 at u11 as sima with dissolve
    s "Maybe I aspire to become one!"
    show sima2_grey 1e 2a 3a regular1 at d11 as sima
    "Absorbed in our discussion, we haven't even noticed Marta and Nana until they were really close."
    show sima2_grey 1g 2a 3a regular2 at d32 as sima
    show marta3_grey 1a 2a 3a regular1 at di31 as marta
    show nana3_grey 1a 2a 3d at di33 as nana
    with dissolve
    show nana3_grey 1a 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show nana3_grey 1d 2a 3d at u33 as nana with dissolve
    n "What are you guys talking about here?"
    show nana3_grey 1d 2a 3d at d33 as nana
    show marta3_grey 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show nana3_grey 1a 2a 3d at d33 as nana
    show sima3a_grey 1g 2a 3a at d32 as sima
    show marta3_grey 1ee 2a 3a regular2 at u31 as marta
    with dissolve
    m "I bet that [player_name] talks about something weird like his dreams or whatever."#
    show marta3_grey 1ee 2a 3a regular2 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta3_grey 1b 2a 3a regular1 at d31 as marta
    show sima3a_grey 1g 2a 3b at d32 as sima
    with dissolve
    p "But they were so vivid!"
    show marta3_grey 1b 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta3_grey 1ee 2a 3b regular2 at u31 as marta
    show sima3a_grey 1g 2a 3a at d32 as sima
    with dissolve
    m "Told you!"
    show marta3_grey 1ee 2a 3b regular2 at d31 as marta
    show nana3_grey 1a 2a 3d at u33 as nana
    $ renpy.pause(.001, hard=True)
    show marta3_grey 1b 2a 3a regular1 at d31 as marta
    show nana1_grey 1e 2a 3a regular1 at u33 as nana
    with dissolve
    n "[player_name], if we turned out to be princesses in your dream, you better tell us."#
    show marta3_grey 1b 2a 3a regular1 at u31 as marta
    show nana1_grey 1e 2a 3a regular1 at d33 as nana
    $ renpy.pause(.001, hard=True)
    show marta2_grey 1b 2a 3a regular1 at u31 as marta
    show nana1_grey 1g 2a 3a regular2 at d33 as nana
    show sima3a_grey 1g 2a 3a at d32 as sima
    with dissolve
    m "And you better behave appropriately!"
    show sima3a_grey 1g 2a 3a at u32 as sima
    show marta2_grey 1b 2a 3a regular1 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_grey 1g 2a 3a regular1 at d31 as marta
    show nana1_grey 1g 2a 3a regular2 at d33 as nana
    show sima3a_grey 1d 2a 3a at u32 as sima
    with dissolve
    s "Alright, we really need to go. I don't want to be late."
    show sima3a_grey 1d 2a 3a at d32 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a_grey 1a 2a 3a at d32 as sima
    "Today we start from physical education."
    return
label ermy_wave_reaction:
    show teya2 1c 2c 3a regularhand1 at u11 as teya behind shade_bottom
    t "Ermy, I'm at a loss for words."
    show teya2 1a 2c 3a regularhand3 at d21 as teya behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show ermy1 pose2 1e 2a 3d noblush at u22 as ermy behind shade_bottom
    with dissolve
    e "Should I treat it as a compliment?"
    show ermy1 pose2 1e 2a 3d noblush at d22 as ermy behind shade_bottom
    show teya2 1a 2c 3a regularhand3 at u21 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1c 2b 3b regularhand3 at u21 as teya behind shade_bottom
    show ermy1 pose1 1a 2a 3d noblush at d22 as ermy behind shade_bottom
    with dissolve
    t "I don't know, but you sure have a lively imagination."
    show teya2 1a 2a 3a regularhand3 at d31 as teya behind shade_bottom
    show ermy1 pose1 1a 2a 3d noblush at d33 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2a 3d at u32 as nana behind shade_bottom with dissolve
    n "I hope you don't do anything funny to foster your creativity!"
    show nana3 1e 2a 3d at d32 as nana behind shade_bottom
    show ermy1 pose1 1a 2a 3d noblush at u33 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 1c 2c 3a noblush at u33 as ermy behind shade_bottom
    show nana3 1a 2a 3d at d32 as nana behind shade_bottom
    with dissolve
    e "What are you talking about?"
    show ermy1 pose1 1c 2c 3a noblush at d33 as ermy behind shade_bottom
    show teya2 1a 2a 3a regularhand3 at u31 as teya behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show teya2 1e 2d 3a regularhand2 at u31 as teya behind shade_bottom
    show ermy1 pose1 1a 2a 3a noblush at d33 as ermy behind shade_bottom
    show nana3 1g 2a 3a at d32 as nana behind shade_bottom
    with dissolve
    t "Nana, how about you support the beginnings of your classmates?"
    show teya2 1a 2b 3a regularhand4 at d41 as teya behind shade_bottom
    show ermy1 pose1 1a 2a 3a noblush at d44 as ermy behind shade_bottom
    show nana3 1g 2a 3a at d42 as nana behind shade_bottom
    $ renpy.pause(.25, hard=True)
    show sima3a 1c 2a 3d at u43 as sima behind shade_bottom
    show ermy1 pose1 1a 2a 3c blush at d44 as ermy behind shade_bottom
    with dissolve
    s "Ermy, were these our eyes?"
    show sima3a 1c 2a 3d at d43 as sima behind shade_bottom
    show ermy1 pose1 1a 2a 3c blush at u44 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose2 1c 2c 3c blush at u44 as ermy behind shade_bottom
    show nana1 1g 2a 3d regular2 at d42 as nana behind shade_bottom
    show sima3a 1a 2a 3d at d43 as sima behind shade_bottom
    with dissolve
    e "No, just the stock images I got from the web!"#
    show ermy1 pose2 1c 2c 3c blush at d44 as ermy behind shade_bottom
    show sima3a 1a 2a 3d at u43 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose2 1a 2c 3c blush at d44 as ermy behind shade_bottom
    show nana1 1a 2a 3a regular2 at d42 as nana behind shade_bottom
    show sima3a 1e 2a 3a at u43 as sima behind shade_bottom
    with dissolve
    s "It's nice to see you like Rodin."
    show sima3a 1e 2a 3a at d43 as sima behind shade_bottom
    show ermy1 pose2 1a 2c 3c blush at u44 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 1e 2a 3d blush at u44 as ermy behind shade_bottom
    show nana1 1f 2d 3d regular2 at d42 as nana behind shade_bottom
    show sima3a 1a 2c 3a at d43 as sima behind shade_bottom
    with dissolve
    e "Who's the guy?"
    show sima3a 1a 2c 3a at u43 as sima behind shade_bottom
    show ermy1 pose1 1e 2a 3d blush at d44 as ermy behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose1 1a 2a 3d blush at d44 as ermy behind shade_bottom
    show sima3a 1c 2b 3c at u43 as sima behind shade_bottom
    with dissolve
    s "What? The thinking person in your video..."
    show ermy1 pose1 1a 2a 3d blush at u44 as ermy behind shade_bottom
    show sima3a 1c 2b 3c at d43 as sima behind shade_bottom
    $ renpy.pause(.001, hard=True)
    show ermy1 pose2 1b 2a 3a blush at u44 as ermy behind shade_bottom
    show sima3a 1a 2b 3a at d43 as sima behind shade_bottom
    show nana1 1f 2d 3d regular2 at d42 as nana behind shade_bottom
    show teya3 1a 2b 3b at d41 as teya behind shade_bottom
    with dissolve
    e "Oh, well, I just took it from other vaporwave videos!"
    show ermy1 pose2 1f 2a 3c blush at d44 as ermy behind shade_bottom with dissolve
    "Life lesson 101 for Ermy: sometimes it's better to keep silent to look smarter."
    return
label after_help_teya:
    scene black with fade
    $ renpy.pause(1, hard=True)
    scene hallway1_ru
    show teya1 1b 2a 3a at u11 as teya
    with fade
    "Teya decides to ask me something after the lesson."
    show teya1 1e 2a 3d at u11 as teya with dissolve
    t "[player_name], do you know why it's so great to be a teacher?"
    show teya1 1a 2a 3d at u11 as teya with dissolve
    p "Hm... Because you know more?"
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Because you have more power!"
    show teya2 1c 2a 3b regularhand2 at u11 as teya with dissolve
    t "See, for some reason no one has been cleaning the history class for like a week..." #fixed in None
    show teya2 1e 2b 3a regularhand1 at u11 as teya with dissolve
    t "Well, someone had asthma, and during the class that person collapsed and was taken to hospital."
    show teya3 1c 2b 3b at u11 as teya with dissolve
    t "From another side, I'm a new teacher here, I must earn respect and all that. Do you follow me?"#
    show teya3 1a 2b 3d at u11 as teya with dissolve
    p "Not really."
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "I said that I'll go ahead and clean the class all by myself! Right now!"
    show teya2 1a 2a 3a regularhand3 at u11 as teya with dissolve
    p "Can't imagine you cleaning the room."
    show teya3 1e 2a 3d at u11 as teya with dissolve
    t "Guess what, me neither! What a coincidence, right?"
    show teya3 1a 2a 3d at u11 as teya with dissolve
    p "..."
    show teya2 1e 2a 3b regularhand1 at u11 as teya with dissolve
    t "You got it, don't you? By my power, I demand that you clean that class."
    show teya2 1e 2a 3a regularhand2 at u11 as teya with dissolve
    t "Hey, what's with this face? I'll ask the girls to help you."
    hide teya with dissolve
    $ renpy.pause(1, hard=True)
    "She gets back after a while."
    return
label after_help_ermy:
    show teya3 1a 2a 3a at u11 as teya
    show teya3 1c 2a 3b at u11 as teya with dissolve
    t "From another side, maybe it's worth it to give the girls a break, so when I met Ermy..."#
    show teya2 1e 2a 3a regularhand2 at u11 as teya
    t "Long story short, he's going to wait for you in the history class. Onwards!" #fixed in None
    return
label after_help_nana:
    if persistent.game_done1 == None:
        show teya2 1a 2a 3a regularhand1 at u11 as teya
        $ renpy.pause(.001, hard=True)
        show teya2 1e 2a 3a regularhand1 at u11 as teya with dissolve
        t "Great news, everyone! Nana will help you. She'll be waiting in the class."
    scene black with fade
    play music "music/getting_warmer.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(1, hard=True)
    scene ru_classroom2 with fade
    "There's no one in the history class. That doesn't surprise me at all." #fixed in None
    "Knowing Nana, she's likely to be heading home right now."
    "I look at the class, trying to estimate the amount of time I'll have to spent here."#
    "Everything looks pretty clean. If the dust is not visible, it's not that bad."
    "I see a sign inscribed at the door. \"I love Lena\"."
    "I wonder who loves Lena this much. And who's Lena?"
    show black
    n "Got you!"
    p "Hi, Nana!"
    hide black
    show nana1close 1e 2d 3b regular1 at u11 as nana
    with eye_open
    n "And that's it? It's not like beautiful strangers cover your eyes every day."
    show nana1close 1a 2a 3a regular1 at u11 as nana with dissolve
    p "I don't think these strangers pant so much because they have to stay on their toes."
    show nana1close 1d 2d 3b regular1 at u11 as nana with dissolve
    n "It's your fault that you're so high" #fixed in None
    show nana3close 1e 2a 3d at u11 as nana with dissolve
    n "Did you really think I'm going to ditch you?"#
    show nana3close 1g 2a 3d at u11 as nana with dissolve
    p "I did."
    show nana3close 1d 2c 3a at u11 as nana with dissolve
    n "Well, I changed my mind!"
    show nana1close 1d 2a 3d regular2 at u11 as nana with dissolve
    n "But I don't really want to clean. Instead, I'll act as your moral support!"
    show nana1close 1g 2a 3d regular2 at u11 as nana with dissolve
    p "Like, entertaining me with a tale or something?"
    show nana1close 1e 2a 3a regular1 at u11 as nana with dissolve
    n "A mere tale stands nowhere near with my knowledge! Do you know about conspiracy theories?"
    show nana1close 1a 2a 3d regular2 at u11 as nana with dissolve
    p "Do you?"
    show nana1close 1d 2a 3a regular1 at u11 as nana with dissolve
    n "I'm a conspiracy expert."
    show nana1close 1d 2a 3a regular1 at ui11 as nana:
        ypos 1400
        linear .25 ypos 1360
        linear .25 ypos 1400
    n "The world is governed by families, or clans, who own pretty much every single business!"
    show nana1close 1c 2a 3d regular1 at u11 as nana with dissolve
    n "Politics are nothing but puppets in their hands."
    show nana1close 1e 2c 3c regular1 at ui11 as nana:
        ypos 1400
        linear .25 ypos 1350
        linear .25 ypos 1400
    n "Each year, a lot of talented scientists die misteriously! Their inventions remain hidded forever!"#
    show nana1close 1d 2c 3b regular1 at ui11 as nana:
        ypos 1400
        linear .25 ypos 1340
        linear .25 ypos 1400
    n "We can cure any disease, but if people don't get ill, pharmaceutical market is going bust!"#
    show nana1close 1g 2a 3a regular2 at u11 as nana with dissolve
    p "..."
    p "Nana, I think I'm going to buy a tin foil hat for you."
    show nana1close 1e 2d 3d regular2 at u11 as nana with dissolve
    n "Like I care! Okay, go ahead and clean this room in silence. It will be your punishment."
    show nana1close 1f 2a 3a regular2 at u11 as nana with dissolve
    p "You were completely different yesterday."
    show nana3close 1c 2a 3d at u11 as nana with dissolve
    n "That's why I'm never boring, [player_name]."
    show nana3close 1e 2b 3b at u11 as nana with dissolve
    n "Or would you like me to whine or discuss serious, personal topics?"
    show nana3close 1d 2a 3a at u11 as nana with dissolve
    n "I mean, you're one on one with a beautiful girl. No one around..."
    show nana3close 1e 2a 3d at u11 as nana with dissolve
    n "Hey, where are you looking?"
    show nana3close 1a 2a 3a at u11 as nana with dissolve
    p "Trying to locate a beautiful girl in this room."
    show nana1close 1e 2d 3c blush regular1 at ui11 as nana with dissolve:
        ypos 1400
        linear .25 ypos 1330
        linear .25 ypos 1400
    n "What did you say???"
    show nana1close 1d 2d 3d regular2 at u11 as nana with dissolve
    n "You asked for it!"
    show nana1close 1f 2a 3a noblush regular2 at u11 as nana with dissolve
    n "..."
    show nana1close 1c 2a 3a regular2 at u11 as nana with dissolve
    n "Why don't you say something?"
    show nana1close 1f 2a 3a regular2 at u11 as nana with dissolve
    p "Too busy, getting ready to run away."
    show nana1close 1e 2d 3b regular1 at u11 as nana with dissolve
    n "No way I'm going to chase you, [player_name]. It's too cliche."
    show nana1close 1f 2c 3a regular2 at u11 as nana with dissolve
    p "What if someone decided to invite you to a cafe? Is it cliche as well?"
    show nana3date 1c 2a 3d regular at u11 as nana with dissolve
    n "Depends on whether or not this someone is beautiful."
    show nana3date 1g 2a 3d regular at u11 as nana with dissolve
    p "Nana, I'll get disappointed in girls because of you."
    show nana3date 1e 2c 3c regular at u11 as nana with dissolve
    n "Then go ahead and invite Ermy! He'll accept, that's for sure."
    show nana1date 1g 2a 3b regular2 at u11 as nana with dissolve
    p "Oh you."
    show nana3date 1e 2b 3d regular blush at u11 as nana with dissolve
    n "Hey, um... just saying..."
    show nana3date 1c 2b 3a at u11 as nana with dissolve
    n "Why did you ask?"
    show nana3date 1f 2d 3a regular noblush at u11 as nana with dissolve
    p "No particular reason."
    show nana1date 1f 2d 3d regular2 at u11 as nana with dissolve
    n "You're getting on my nerves, [player_name]!"
    show nana3date 1d 2a 3d regular at u11 as nana with dissolve
    n "But it's not like I'm against it."
    show nana1 1c 2c 3c regular1 blush at d22 as nana
    show marta3 1g 2a 3c regular1 at u21 as marta
    $ renpy.pause(.5, hard=True)
    show marta3 1ee 2a 3a regular2 at u21 as marta with dissolve
    m "Busted! What do you guys think you're doing?"
    show marta3 1ee 2a 3a regular2 at d21 as marta
    $ renpy.pause(.001, hard=True)
    show marta3 1g 2a 3a regular1 at d21 as marta
    show nana1 1f 2c 3c blush regular2 at d22 as nana
    with dissolve
    "Marta really scared us."
    show marta3 1g 2a 3a regular1 at u21 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 at u21 as marta
    show nana1 1f 2a 3d noblush regular2 at d22 as nana
    with dissolve
    m "Look at this! You're doing... nothing! What a shame."
    show marta2 1b 2a 3a regular2 at d21 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d21 as marta with dissolve
    p "Marta, what are you doing here?"
    show marta2 1g 2a 3a regular1 at u21 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3d regular1 at u21 as marta with dissolve
    m "I became interested in history."
    show marta2 1e 2a 3d regular1 at d21 as marta
    show nana1 1f 2a 3d noblush regular2 at u22 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3d regular1 at d21 as marta
    show nana1 1e 2a 3d regular2 at u22 as nana
    with dissolve
    n "Like, today?"
    show marta2 1a 2a 3d regular1 at u21 as marta
    show nana1 1e 2a 3d regular2 at d22 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3a regular2 at u21 as marta
    show nana1 1f 2a 3a regular2 at d22 as nana
    with dissolve
    m "Well, why not?"
    show marta3 1ee 2a 3b regular2 at u21 as marta
    show nana1 1f 2c 3c regular1 blush at d22 as nana
    with dissolve
    m "And I was hoping to see you making history and all."
    show marta3 1g 2a 3a regular1 at u21 as marta
    show nana1 1f 2d 3a regular2 noblush at d22 as nana
    with dissolve
    m "You guys let me down. See ya tomorrow."
    scene black with fade
    "After this scene we decided to finally clean the class."
    scene black with fade
    scene ru_classroom2_night
    show nana2_ruclose 1f 2a 3d at u11 as nana
    with fade
    show nana2_ruclose 1d 2a 3d at u11 as nana with dissolve
    n "It's getting darker outside. The night's going to steal the sun!"
    show nana2_ruclose 1f 2a 3d at u11 as nana with dissolve
    p "The morning did the same today, remember?"
    show nana1_ruclose 1e 2d 3b regular1 at u11 as nana with dissolve
    n "It's a shame I wasted so much time here."
    show nana1_ruclose 1f 2d 3a regular1 at u11 as nana with dissolve
    p "What do you consider as time not wasted then?"
    show nana2_ruclose 1c 2d 3d at u11 as nana with dissolve
    n "Anything which is fun, of course."
    show nana2_ruclose 1f 2d 3b at u11 as nana with dissolve
    p "I fail to see how you could have fun cleaning this class."
    show nana1_ruclose 1e 2d 3b blush regular1 at u11 as nana with dissolve
    n "I never wanted to clean it in the first place."
    show nana1_ruclose 1f 2a 3a noblush regular2 at u11 as nana with dissolve
    $ renpy.pause(.5, hard=True)
    show nana1_ruclose 1c 2b 3a regular2 at u11 as nana with dissolve
    n "Whatever. Let's go home!"
    show nana1_ruclose 1a 2a 3a regular2 at u11 as nana with dissolve
    p "Yeah. No cookies from Sima today."
    show nana3_ruclose 1e 2c 3a at u11 as nana with dissolve
    n "Were there any yesterday?"
    show nana3_ruclose 1a 2a 3a at u11 as nana with dissolve
    p "Don't you remember? Back in our club?"
    show nana3_ruclose 1e 2c 3b at u11 as nana with dissolve
    n "What are you talking about?"
    show nana3_ruclose 1d 2a 3a at u11 as nana with dissolve
    n "Anyway, let's go!"
    show nana3_ruclose 1a 2a 3a at u11 as nana with dissolve
    "Nana is something."
    return
label after_help_sima:
    if persistent.game_done1 == None:
        show teya2 1a 2a 3a regularhand1 at u11 as teya
        $ renpy.pause(.001, hard=True)
        show teya2 1e 2a 3a regularhand1 at u11 as teya with dissolve
        t "Good news, everyone! Sima's going to help you. She will be in the class."
        scene black with fade
    play music "music/getting_warmer.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(1, hard=True)
    scene ru_classroom2
    show sima2close 1a 2a 3a regular2 at u11 as sima
    with fade
    "Sima was actually waiting for me in the history class." # fixed in None
    show sima2close 1g 2a 3a regular2 at u11 as sima with dissolve
    p "I hope you didn't wait for too long."
    show sima2close 1c 2a 3d regular2 at u11 as sima with dissolve
    s "Just a couple of minutes, nothing much. I was busy being envious."
    show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Envious about what?"
    show sima2close 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Envious about Lena, of course."
    show sima2close 1a 2a 3a regular1 at u11 as sima with dissolve
    p "Who's Lena?"
    show sima1close 1d 2a 3a at u11 as sima with dissolve
    s "Someone who's being loved!"
    show sima1close 1a 2a 3b at u11 as sima with dissolve
    p "Oh. I see."
    "It looks like Sima is eager to chat."
    show sima1close 1a 2c 3a at u11 as sima with dissolve
    p "How was your day?"
    show sima1close 1g 2c 3c at u11 as sima with dissolve
    "She almost started laughing."
    show sima2close 1d 2c 3b regular1 at u11 as sima with dissolve
    s "I'm so sorry! It's really inappropriate of me... but so funny!"
    show sima2close 1e 2a 3d regular1 at u11 as sima with dissolve
    s "I value the fact that you tried so hard to come up with a decent topic."
    show sima3aclose 1c 2a 3d at u11 as sima with dissolve
    s "I would've never found one myself."
    show sima3aclose 1a 2a 3a at u11 as sima with dissolve
    p "I just asked what, um, people ask... like, in general."
    show sima3aclose 1e 2a 3d at u11 as sima with dissolve
    s "Do you want me to answer in the same fashion?"
    show sima3aclose 1a 2a 3a at u11 as sima with dissolve
    p "How was your day?"
    show sima1close 1c 2a 3d at u11 as sima with dissolve
    s "It was OK."
    show sima1close 1a 2a 3d at u11 as sima with dissolve
    p "Just OK? Anything happened?"
    show sima1close 1c 2a 3a at u11 as sima with dissolve
    s "Not really."
    show sima1close 1a 2a 3d at u11 as sima with dissolve
    p "I see."
    p "By the way, thanks for the tea yesterday."
    show sima3bclose 1d 2a 3b at u11 as sima with dissolve
    s "It's excellent, right? I found this gem like a month ago."
    show sima3aclose 1c 2c 3b at u11 as sima with dissolve
    s "Or was it two months ago? Anyway, I was with my friends when..."
    show sima2close 1d 2a 3d regular1 at u11 as sima with dissolve
    s "You look bored already, and I haven't even started."
    show sima2close 1e 2a 3a regular2 at u11 as sima with dissolve
    s "Maybe it's better to stay silent from time to time."
    show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Now I tend to think you're right."
    p "However, I still want to discuss something really interesting... But I'm not a mind-reader."
    show sima2close 1c 2a 3a regular1 at u11 as sima with dissolve
    s "Well, your idea to thank me for something random wasn't half bad."
    show sima2close 1a 2a 3a regular1 at u11 as sima with dissolve
    "\"Random?\""
    show sima3aclose 1c 2a 3d at u11 as sima with dissolve
    s "It's better not to read my mind... What if I decided to think bad of you?"
    show sima3aclose 1e 2a 3a at u11 as sima with dissolve
    s "And hey, some thoughts are private!"
    show sima3aclose 1a 2a 3a at u11 as sima with dissolve
    p "I would pay a lot to know what girls think about me!"
    show sima2close 1e 2a 3b regular1 at u11 as sima with dissolve
    s "Then you'd soon find other girls you know nothing about."
    show sima2close 1a 2a 3d regular1 at u11 as sima with dissolve
    p "I don't really get it."
    show sima2close 1e 2a 3b regular1 at u11 as sima with dissolve
    s "See? It's not that easy to read me!"
    show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
    p "I've heard there are certain visual signs indicating that a girl likes you."
    show sima1close 1c 2a 3a at u11 as sima with dissolve
    s "Like what?"
    show sima1close 1a 2a 3a at u11 as sima with dissolve
    p "For instance, when she bites her upper lip."
    show sima1close 1c 2a 3b at u11 as sima with dissolve
    s "Interesting, interesting... Who said this?"
    show sima1close 1g 2a 3a at u11 as sima with dissolve
    p "I watched a video on the Internet."
    show sima1close 1e 2c 3d at u11 as sima with dissolve
    s "What kind of a video was that? Was there a muscular guy coming to, like, fix her PC?"
    show sima1close 1a 2c 3a at u11 as sima with dissolve
    p "Sima, how come you're aware of this kind of videos?"#
    show sima2close 1d 2c 3a blush regular1 at u11 as sima with dissolve
    s "I'm pretty knowledgeable! But let's go back on our topic."
    show sima2close 1c 2a 3d noblush regular1 at u11 as sima with dissolve
    s "If a girl bit her lip constantly, she'd look like a duck!"
    show sima2close 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Now that I think about it, I see a lot of girls like this every day."
    show sima3aclose 1d 2a 3a at u11 as sima with dissolve
    s "It's lip surgery. They're trying to look beautiful."
    show sima3aclose 1a 2a 3d at u11 as sima with dissolve
    p "For whom, I wonder..."
    show sima1close 1d 2a 3a at u11 as sima with dissolve
    s "Now I want to change the topic. Let's decide who does what... I'm talking about cleaning."
    show sima1close 1a 2a 3a at u11 as sima with dissolve
    p "Any ideas?"
    show sima1close 1d 2a 3b at u11 as sima with dissolve
    s "Sure. You could fill this bucket, get a mop and wash the floor. "
    show sima1close 1g 2a 3a at u11 as sima with dissolve
    p "What about you?"
    show sima2date 1e 2a 3a regular1 at u11 as sima with dissolve
    s "I'll be your personal muse, [player_name]!"
    show sima2date 1g 2a 3a regular2 at u11 as sima with dissolve
    p "I'm kind of picky when it come to muses, you know."#
    show sima3adate 1e 2a 3a at u11 as sima with dissolve
    s "What do you look for?"
    show sima3adate 1g 2c 3a blush at u11 as sima with dissolve
    p "I need my muse to call me a hero."
    show sima3adate 1c 2a 3d at u11 as sima with dissolve
    s "And?"
    show sima3adate 1a 2a 3d at u11 as sima with dissolve
    p "And reward a hero with a juicy kiss."#
    show sima2date 1c 2a 3a regular2 at u11 as sima with dissolve
    s "Reward for what?"
    show sima1 1a 2c 3c blush at d33 as sima
    $ renpy.pause(.2, hard=True)
    show nana1 1g 2c 3c regular1 at di31 as nana
    show marta2 1f 2c 3c regular1 blush at di32 as marta
    with dissolve
    show nana1 1g 2c 3c regular1 at u31 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3c regular1 at u31 as nana with dissolve
    n "Can Marta go in?"
    show marta2 1f 2c 3c regular1 blush at u32 as marta
    show nana1 1e 2c 3c regular1 at d31 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3d regular2 at d31 as nana
    show marta2 1e 2d 3c regular2 blush at u32 as marta
    with dissolve
    m "Nana!!!"
    show marta2 1e 2d 3c regular2 blush at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2d 3a regular1 blush at d32 as marta
    show sima1 1a 2a 3a blush at d33 as sima
    with dissolve
    "Enter Nana and Marta."
    show nana1 1g 2a 3d regular2 at u31 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2a 3d at u31 as nana with dissolve
    n "What? I saw your practically leaning on this door, so I thought I'd do you a favor and open it."
    show nana3 1e 2a 3d at d31 as nana
    show marta2 1f 2d 3a regular1 blush at u32 as marta
    $ renpy.pause(.001, hard=True)
    show marta1 1e 2d 3a at u32 as marta
    show sima1 1a 2d 3a blush at d33 as sima
    show nana3 1g 2a 3d at d31 as nana
    with dissolve
    m "But why would you sneak on me? Why would you cry out loud after that?"
    show nana3 1g 2a 3d at u31 as nana
    show marta1 1e 2d 3a at d32 as marta
    $ renpy.pause(.001, hard=True)
    show marta1 1f 2d 3a at d32 as marta
    show sima1 1a 2d 3b at d33 as sima
    show nana3 1e 2a 3d at u31 as nana
    with dissolve
    n "It's because I walk like a ninja! As for crying out loud, I just wanted to mind my manners."
    show nana3 1e 2a 3d at d31 as nana
    show marta1 1f 2d 3a at u32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2c 3a regular2 at u32 as marta
    show sima1 1a 2d 3d at d33 as sima
    show nana3 1g 2a 3d at d31 as nana
    with dissolve
    m "I intended to knock on the door anyway."
    show marta2 1d 2c 3a regular2 at d32 as marta
    show nana3 1g 2a 3d at u31 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2c 3a regular1 at d32 as marta
    show nana3 1e 2a 3a at u31 as nana
    with dissolve
    n "Sure, sure you did."
    show sima1 1a 2d 3d at u33 as sima
    show nana3 1e 2a 3a at d31 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1f 2c 3a regular1 at d32 as marta
    show nana3 1a 2a 3a at d31 as nana
    show sima1 1e 2d 3b noblush at u33 as sima
    with dissolve
    s "Girls, can I ask you a question..."
    show sima1 1e 2d 3b noblush at d33 as sima
    show marta2 1f 2c 3a regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1c 2c 3c regular2 at u32 as marta
    show sima1 1e 2d 3b noblush at d33 as sima
    with dissolve
    m "We were worried about you!"
    show marta2 1c 2c 3c regular2 at d32 as marta
    show nana3 1a 2a 3a at u31 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 regular2 1b 2a 3c at u31 as nana
    show marta2 1d 2c 3c regular1 at d32 as marta
    show sima1 1a 2d 3a at d33 as sima
    with dissolve
    n "Yeah, what if [player_name] is a pervert?"
    show nana1 regular2 1b 2a 3c at d31 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 regular2 1g 2a 3b at d31 as nana
    show marta3 1gg 2c 3a regular2 at d32 as marta
    with dissolve
    p "Hey, what did I do to deserve being called a pervert?"
    show nana1 regular2 1g 2a 3b at u31 as nana
    $ renpy.pause(.001, hard=True)
    show nana3 1e 2a 3d at u31 as nana
    show marta3 1b 2a 3a noblush regular1 at d32 as marta
    with dissolve
    n "Let's assume you got to like Sima..."
    show nana3 1e 2a 3d at d31 as nana
    show sima1 1a 2d 3a at u33 as sima
    $ renpy.pause(.001, hard=True)
    show nana3 1a 2a 3a at d31 as nana
    show sima1 1c 2d 3d blush at u33 as sima
    with dissolve
    s "Are you trying to say only perverts can like me?"
    show sima2 1e 2a 3b regular1 noblush at u33 as sima with dissolve
    s "Anyway, I'm happy you all are here now."
    show sima2 1e 2a 3b regular1 noblush at d33 as sima
    show marta3 1b 2a 3a noblush regular1 at u32 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1g 2a 3a regular1 at d33 as sima
    show marta2 1e 2c 3c regular2 at u32 as marta
    show nana1 regular1 1b 2a 3c at d31 as nana
    with dissolve
    m "See? Now, what do you want us to do with this guy?"
    show sima2 1g 2a 3a regular1 at u33 as sima
    show marta2 1e 2c 3c regular2 at d32 as marta
    $ renpy.pause(.001, hard=True)
    show sima2 1e 2a 3d regular1 at u33 as sima
    show marta2 1f 2a 3a regular1 at d32 as marta
    show nana1 regular2 1f 2a 3d at d31 as nana
    with dissolve
    s "I want you to help him clean. You see where the mop is, right?"
    scene black with fade
    scene ru_classroom2_night
    show sima3b_ruclose 1g 2a 3b at u11 as sima
    with fade
    "To my surprise, Nana and Marta actually helped me."
    show sima3b_ruclose  1g 2a 3a at u11 as sima with dissolve
    "Hey, Sima is not that righteous at all when she's less buttoned up."
    show sima3b_ruclose  1g 2a 3d blush at u11 as sima with dissolve
    "So, if I could unbutton her just a little bit more... Boy, it would be huge."#
    return
label after_help_marta:
    if persistent.game_done1 == None:
        show teya2 1a 2a 3a regularhand1 at u11 as teya
        $ renpy.pause(.001, hard=True)
        show teya2 1e 2a 3a regularhand1 at u11 as teya with dissolve
        t "Good news, everyone! Marta will help you. She's waiting in the class."
    scene black with fade
    play music "music/getting_warmer.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(1, hard=True)
    scene ru_classroom2
    show marta3close 1a 2a 3a regular1 at u11 as marta
    with fade
    "I met Marta right at the doors of the classroom."
    show marta3close 1ee 2a 3a regular2 at u11 as marta with dissolve
    m "Why do you think I agreed to help you?"
    show marta3close 1b 2a 3a regular1 at u11 as marta with dissolve
    p "Well, knowing you, you probably want to see who finishes the cleaning first."
    show marta1close 1f 2c 3a at u11 as marta with dissolve
    m "..."
    show marta1close 1c 2a 3b blush at u11 as marta with dissolve
    m "[player_name], c'mon, we're not in kindergarten."
    show marta1close 1f 2d 3d at u11 as marta with dissolve
    "Keez, what's wrong with me? It was such a cringy answer." #fixed in None
    show marta1close 1a 2a 3a at u11 as marta with dissolve
    p "Well, I could've gone with \"because you like me\", but I don't want to be lying."
    show marta2close 1f 2a 3a noblush regular1 at u11 as marta with dissolve
    "Marta looks at me for some time."
    show marta2close 1b 2a 3a regular1 at u11 as marta with dissolve
    m "I never knew you can see through people, [player_name]."#
    show marta2close 1a 2a 3a regular1 at u11 as marta with dissolve
    p "I-I just..."
    show marta3close 1d 2a 3a regular1 at u11 as marta with dissolve
    m "Well, what's wrong? Can't I feel this way?"
    show marta3close 1a 2a 3a regular1 at u11 as marta with dissolve
    p "It's just I never expected it in the first place..."#
    show marta2close 1e 2d 3d regular2 at u11 as marta with dissolve
    m "Want to me to take my words back?"#
    show marta2close 1f 2d 3a regular1 at u11 as marta with dissolve
    p "No, of course not! However, I thought you only like the cool guys and all..."
    show marta3date 1e 2c 3a regular1 at u11 as marta with dissolve
    m "Aren't you one of them?"
    show marta3date 1gg 2a 3a regular2 at u11 as marta with dissolve
    p "Who, me? Oh well, you know... I guess I'm pretty cool!"
    show marta2date 1b 2a 3a regular2 at u11 as marta with dissolve
    m "How about you prove it? I bet you can't finish here in less than ten minutes."
    show marta2date 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Well, the class is pretty big, so it's hard to say..."
    show marta3date 1e 2a 3a regular1 at u11 as marta with dissolve
    m "I'm sure you can handle this. Also..."
    show marta3date 1ee 2a 3b regular2 at u11 as marta with dissolve
    m "You'll be rewarded accordingly, [player_name]."
    show marta2date 1c 2b 3a regular1 blush at u11 as marta with dissolve
    m "You know what I'm talking about, don't you, [player_name]?"
    scene ru_classroom2_night
    show marta3_ruclose 1b 2a 3a noblush regular1 at u11 as marta
    with fade
    "Guess what, I actually managed to do it!"
    p "Well, Marta, what kind of reward were you talking about?"
    show marta3_ruclose 1ee 2a 3a regular2 at u11 as marta with dissolve
    m "You have it already."
    show marta3_ruclose 1g 2a 3b regular1 at u11 as marta with dissolve
    p "What do you mean?"
    show marta2_ruclose 1e 2a 3a regular2 at u11 as marta with dissolve
    m "You just proved nothing is impossible to yourself."
    show marta2_ruclose 1g 2a 3a regular1 at u11 as marta with dissolve
    p "What about my well-deserved kiss?"
    show marta3_ruclose 1ee 2c 3b regular2 at u11 as marta with dissolve
    m "Ha! So that's what you were thinking about!"
    show marta3_ruclose 1e 2a 3a regular1 at u11 as marta with dissolve
    m "[player_name], sorry, it was an experiment."
    show marta3_ruclose 1d 2b 3a regular1 at u11 as marta with dissolve
    m "I agreed to help you because I hate it when something is unfair. And your case was unfair."
    show marta2_ruclose 1e 2d 3a regular2 at u11 as marta with dissolve
    m "And then I hate when the teacher asks for something, but people remain silent."#
    show marta2_ruclose 1d 2a 3a regular1 at u11 as marta with dissolve
    m "From another side, I really don't like to clean."#
    show marta3_ruclose 1d 2a 3a regular1 at u11 as marta with dissolve
    m "So me and the girls came up with this funny idea of offering you a reward and all..."
    show marta2_ruclose 1e 2a 3a regular2 at u11 as marta with dissolve
    m "Sima said you'll see right through it."
    show marta2_ruclose 1d 2b 3a regular1 blush at u11 as marta with dissolve
    m "Nana thought otherwise, but she said you'll expect something perverted as a reward..."
    show marta3_ruclose 1ee 2a 3a regular2 at u11 as marta with dissolve
    m "Well, a kiss was my hypothesis. It turns out I was right."
    show marta3_ruclose 1g 2a 3a regular1 noblush at u11 as marta with dissolve
    "I feels myself so dumb! How come I couldn't figure it out? The whole setup was so primitive..."#
    p "You're a good actor, I give you that."#
    show marta2_ruclose 1b 2a 3a regular2 at u11 as marta with dissolve
    m "No, I'm a terrible actor. But when it comes down to the instincts, it's enough."
    show marta2_ruclose 1g 2a 3a regular1 at u11 as marta with dissolve
    p "I'm not that primitive as you may think."#
    show marta2_ruclose 1d 2b 3a regular1 at u11 as marta with dissolve
    m "I never intentended to call you primitive."#
    show marta3_ruclose 1d 2b 3a blush regular1 at u11 as marta with dissolve
    m "You know, had you not expected a kiss, I'd be extremely disappointed."
    play sound "<from 0 to 1>sound/door_knock.ogg"
    show marta3_ruclose 1a 2c 3a noblush regular1 at u11 as marta with dissolve
    $ renpy.pause(1, hard=True)
    s "Can I go in?"
    show marta2_runight 1e 2c 3a regular1 at u11 as marta with dissolve
    m "Sima? What are you doing here? Anyway, sure, come in."
    show marta2_runight 1a 2a 3a regular1 at d22 as marta
    $ renpy.pause(.25, hard=True)
    show sima2_runight 1c 2a 3a regular2 at u21 as sima with dissolve
    s "Thank you."
    show sima3a_runight 1a 2a 3d at d21 as sima
    show marta3_runight 1b 2a 3a regular1 at d22 as marta
    with dissolve
    "She has that curious look in her eyes, like she expected to see something here."
    show sima3a_runight 1a 2a 3d at u21 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1c 2a 3a at u21 as sima with dissolve
    s "I just wanted to ask if you guys need help."#
    show sima3a_runight 1c 2a 3a at d21 as sima
    show marta3_runight 1b 2a 3a regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1a 2c 3c blush at d21 as sima
    show marta3_runight 1ee 2a 3a regular2 at u22 as marta
    with dissolve
    m "No, we're pretty much done. [player_name] was a quickie."
    show marta3_runight 1ee 2a 3a regular2 at d22 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1a 2a 3a at d21 as sima
    show marta3_runight 1g 2a 3a regular1 at d22 as marta
    with dissolve
    "Something's off with that phrase."
    show sima3a_runight 1a 2a 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show sima1_runight 1e 2a 3a noblush at u21 as sima with dissolve
    s "Why is his face so red?"
    show sima1_runight 1e 2a 3a noblush at d21 as sima
    $ renpy.pause(.001, hard=True)
    show sima1_runight 1g 2a 3d at d21 as sima
    show marta2_runight 1a 2a 3d regular1 at d22 as marta
    with dissolve
    "I know Marta's going to throw me under the bus and tell Sima everything!"
    show marta2_runight 1a 2a 3d regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1b 2a 3a regular2 at u22 as marta with dissolve
    m "Why? Because it take a physical effort to clean this class, that's why!"#
    show marta2_runight 1b 2a 3a regular2 at d22 as marta
    show sima1_runight 1g 2a 3d at u21 as sima
    $ renpy.pause(.001, hard=True)
    show sima2_runight 1e 2a 3b regular1 at u21 as sima
    show marta2_runight 1g 2a 3a regular1 at d22 as marta
    with dissolve
    s "[player_name], you're a real knight in the shining armor!"
    show sima2_runight 1e 2a 3b regular1 at d21 as sima
    show marta2_runight 1g 2a 3a regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show sima2_runight 1a 2a 3a regular2 at d21 as sima
    show marta2_runight 1e 2a 3a regular2 at u22 as marta
    with dissolve
    m "That's right."
    show sima2_runight 1a 2a 3a regular2 at u21 as sima
    show marta2_runight 1e 2a 3a regular2 at d22 as marta
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1c 2a 3a at u21 as sima
    show marta2_runight 1a 2a 3a regular1 at d22 as marta
    with dissolve
    s "Oh well, shame I came for nothing then."
    show sima3a_runight 1c 2a 3a at d21 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1a 2c 3a at d21 as sima
    show marta2_runight 1a 2c 3a regular1 at d22 as marta
    with dissolve
    p "Do you have some tea left from yesterday?"
    show sima3a_runight 1a 2c 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1c 2a 3a at u21 as sima with dissolve
    s "Um, yeah..."
    show sima3a_runight 1e 2a 3b at u21 as sima with dissolve
    s "Not sure what you're talking about, but I actually have some good tea I can share."
    show sima3a_runight 1e 2a 3b at d21 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a_runight 1a 2a 3a at d21 as sima with dissolve
    "Eh, what?"
    show marta2_runight 1a 2c 3a regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1e 2a 3a regular2 at u22 as marta with dissolve
    m "Sima, do you know something about Anya?"
    show marta2_runight 1e 2a 3a regular2 at d22 as marta
    show sima3a_runight 1a 2a 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1a 2a 3a regular1 at d22 as marta
    show sima3a_runight 1e 2c 3a at u21 as sima
    with dissolve
    s "Who're you talking about?"
    show marta2_runight 1a 2a 3a regular1 at u22 as marta
    show sima3a_runight 1e 2c 3a at d21 as sima
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1e 2a 3a regular2 at u22 as marta
    show sima3a_runight 1a 2c 3a at d21 as sima
    with dissolve
    m "Something carved a sign here, at this door, it's a love message to that girl!"#
    show marta2_runight 1e 2a 3a regular2 at d22 as marta
    show sima3a_runight 1a 2c 3a at u21 as sima
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1a 2a 3a regular1 at d22 as marta
    show sima3b_runight 1a 2a 3b at u21 as sima
    with dissolve
    s "Oh, how romantic! I'm jealous.."
    show marta2_runight 1a 2a 3a regular1 at u22 as marta
    show sima3b_runight 1a 2a 3b at d21 as sima
    $ renpy.pause(.001, hard=True)
    show marta3_runight 1e 2a 3a regular1 at u22 as marta
    show sima3a_runight 1g 2a 3d at d21 as sima
    with dissolve
    m "Me too! [player_name], do you have some energy left in you?"
    show marta3_runight 1e 2a 3a regular1 at d22 as marta
    $ renpy.pause(.001, hard=True)
    show marta3_runight 1g 2a 3a regular1 at d22 as marta with dissolve
    p "Not sure."
    show marta3_runight 1g 2a 3a regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show sima3b_runight 1g 2a 3d at d21 as sima
    show marta3_runight 1ee 2a 3a regular2 at u22 as marta
    with dissolve
    m "How about making a new sign, huh? \"I love Sima and Marta.\""
    show sima3b_runight 1g 2a 3d at u21 as sima
    show marta3_runight 1ee 2a 3a regular2 at d22 as marta
    $ renpy.pause(.001, hard=True)
    show sima2_runight 1e 2a 3d regular1 at u21 as sima
    show marta3_runight 1a 2a 3a regular1 at d22 as marta
    with dissolve
    s "We don't need love triangles here, Marta..."
    show sima2_runight 1c 2a 3a regular1 at u21 as sima with dissolve
    s "If anything, [player_name] would have to make a choice!"
    show sima2_runight 1c 2a 3a regular1 at d21 as sima
    show marta3_runight 1a 2a 3a regular1 at u22 as marta
    $ renpy.pause(.001, hard=True)
    show sima2_runight 1a 2a 3a regular2 at d21 as sima
    show marta2_runight 1e 2a 3a regular1 at u22 as marta
    with dissolve
    m "[player_name], who would you choose?"
    show marta2_runight 1e 2a 3a regular1 at d22 as marta
    $ renpy.pause(.001, hard=True)
    show marta2_runight 1g 2a 3a regular1 at d22 as marta with dissolve
    "Wow, it's getting dangerous."#
    "Somehow I manage to laugh it away and continue with fairly normal conversation."#
    scene black with fade
    return
label lbl_lpg_3:
    scene black with fade
    play music "music/no_will.ogg" fadeout 1.5 fadein 1.5
    $ renpy.pause(3, hard=True)
    $ renpy.music.play("images/movies/backroom.webm", channel="movie", loop=True)
    scene movie with eye_open
    "You're kidding me..."
    "This room and arcade machine already feel familiar to me."
    "I don't even feel nauseous anymore."
    "I decide to move forward a bit just to see what's going on behind that corner."
    "But I can't, for some reason."
    "Then I decide to turn around and see what's happening there."
    "Nope. Can't."
    "Well, you're supposed to follow the script of this dream, I think."
    scene black with fade
    $ renpy.music.play("images/movies/lpg.webm", channel="movie", loop=True)
    scene movie
    show lpg_0
    show lpg_1
    show lpg_2a as lpg_2
    with fade
    pause
    "I approach the vending machine again."
    "Well, what are we going to see today? How about, say, Australia?"#
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_af behind lpg_1 as lpg_i1:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ar behind lpg_1 as lpg_i2:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_ae behind lpg_1 as lpg_i3:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    show lpg_2a as lpg_2 with dissolve
    "\"Fre\"? Is this a budget version of \"free\"?"
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_af behind lpg_1 as lpg_i1:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ar behind lpg_1 as lpg_i2:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_ae behind lpg_1 as lpg_i3:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_ad behind lpg_1 as lpg_i4:
        yalign .2
        xalign .445
        linear 1 yalign .56
    show lpg_i_ao behind lpg_1 as lpg_i5:
        yalign .2
        xalign .535
        pause .5
        linear 1 yalign .56
    show lpg_i_am behind lpg_1 as lpg_i6:
        yalign .2
        xalign .625
        pause 1
        linear 1 yalign .56
    $ renpy.pause(2, hard=True)
    "\"Dom\". Wait a second, I think I got it..."#
    show lpg_2b as lpg_2 with dissolve
    show lpg_i_ad behind lpg_1 as lpg_i4:
        yalign .56
        xalign .445
        linear 1 yalign .99
    show lpg_i_ao behind lpg_1 as lpg_i5:
        yalign .56
        xalign .535
        pause .5
        linear 1 yalign .99
    show lpg_i_am behind lpg_1 as lpg_i6:
        yalign .56
        xalign .625
        pause 1
        linear 1 yalign .99
    show lpg_2a as lpg_2 with dissolve
    $ renpy.pause(.5, hard=True)
    show lpg_i_au behind lpg_1 as lpg_i1:
        xalign .445
        block:
            yalign .2
            linear 1 yalign .56
            pause 2
            linear 1 yalign .99
            pause 1
            repeat
    show lpg_i_as behind lpg_1 as lpg_i2:
        xalign .535
        block:
            yalign .2
            pause .5
            linear 1 yalign .56
            pause 2
            linear 1 yalign .99
            pause .5
            repeat
    show lpg_i_aa behind lpg_1 as lpg_i3:
        xalign .625
        block:
            yalign .2
            pause 1
            linear 1 yalign .56
            pause 2
            linear 1 yalign .99
            repeat
    "So when the machine starts to show \"USA\", I realize where it's all going."
    "By the way, have I discussed my dreams with anyone?"
    "I can't remember where I actually am in the real life."#
    "From another side, if I did, I'd simply wake up."#
    "Fine..."
    scene black
    with fade
    stop movie
    stop sound fadeout 1
    stop music fadeout 1
    $ renpy.pause(1, hard=True)
    jump day3
label before_expo:
    show nana1 1c 2a 3d regular2 at d32 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d32 as nana
    show marta2 1a 2a 3a regular1 at d31 as marta
    show sima1 1a 2a 3a at d33 as sima
    with dissolve
    p "Marta, have you been to the states which are pinned on the map? Тhe one behind you."#
    show marta2 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3d regular2 at u31 as marta with dissolve
    m "Sure. It's my lovely country, and it's my obligation to know it well."#
    show marta2 1e 2a 3d regular2 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d31 as marta with dissolve
    p "Which state is your favorite?"
    show marta2 1g 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular2 at u31 as marta with dissolve
    m "Texas, by far."
    show marta2 1b 2a 3a regular2 at d31 as marta
    show nana1 1a 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1g 2a 3a regular1 at d31 as marta
    show nana3 1e 2a 3d at u32 as nana
    show sima1 1g 2a 3a at d33 as sima
    with dissolve
    n "Texas? So, like, you're fond of shooting ranges and pickup trucks?"
    show marta2 1g 2a 3a regular1 at u31 as marta
    show nana3 1e 2a 3d at d32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1d 2a 3d regular1 at u31 as marta
    show nana3 1g 2a 3d at d32 as nana
    with dissolve
    m "Very funny, but don't you forget about BBQ..."
    show sima3a 1a 2a 3a at d33 as sima
    show marta2 1d 2a 3a regular1 at u31 as marta
    with dissolve
    m "Well, it's actually true, at least to a certain extent, but..."
    show marta2 1b 2a 3d regular2 at u31 as marta
    show nana3 1a 2a 3a at d32 as nana
    with dissolve
    m "It's more about the people, how sincere they are and all."
    show marta2 1b 2a 3d regular2 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular2 at d31 as marta
    show sima3a 1a 2c 3a at d33 as sima
    show nana1 1a 2a 3a regular2 at d32 as nana
    with dissolve
    p "I've heard people in America are usually not that... sincere, you said?"
    show marta2 1a 2a 3a regular2 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta1 1e 2b 3b at u31 as marta
    show sima3a 1a 2a 3a at d33 as sima
    with dissolve
    m "There are two Americas, so let's go with the US. And even then you have to be more specific."
    show marta2 1e 2a 3a regular1 at u31 as marta
    show sima3a 1a 2a 3d at d33 as sima
    show nana1 1a 2a 3d regular2 at d32 as nana
    with dissolve
    m "See, each state is totally unique in the US. Well, big cities kind of look the same though..."
    show marta2 1e 2a 3a regular1 at d31 as marta
    show nana1 1a 2a 3d regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d31 as marta
    show nana3 1e 2a 3d at u32 as nana
    with dissolve
    n "And what's so special about Texas?"
    show marta2 1a 2a 3a regular1 at u31 as marta
    show nana3 1e 2a 3d at d32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2c 3a regular2 at u31 as marta
    show nana3 1a 2a 3d at d32 as nana
    with dissolve
    m "People are not that superficial there."#
    show marta2 1b 2c 3a regular2 at d31 as marta
    show nana3 1a 2a 3d at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d31 as marta
    show nana3 1d 2c 3a at u32 as nana
    with dissolve
    n "Are you talking about fake smiles and all?"
    show marta2 1a 2a 3a regular1 at u31 as marta
    show nana3 1d 2c 3a at d32 as nana
    $ renpy.pause(.001, hard=True)
    show marta2 1b 2a 3a regular1 at u31 as marta
    show nana3 1g 2a 3a at d32 as nana
    show sima1 1a 2a 3a at d33 as sima
    with dissolve
    m "No, it's nothing. Being superficial is about something else..."#
    show marta2 1e 2c 3a regular2 at u31 as marta
    show sima1 1a 2a 3b at d33 as sima
    with dissolve
    m "Always being excessively enthusiastic, showing off new cars, houses, etc..."
    show marta2 1d 2a 3d regular1 at u31 as marta
    show sima1 1a 2a 3a at d33 as sima
    show nana3 1a 2a 3d at d32 as nana
    with dissolve
    m "While being knee deep in mortgages, with Xanax as the best buddy." #fixed in None
    show nana3 1a 2a 3d at u32 as nana
    show marta2 1d 2a 3d regular1 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3d regular1 at u32 as nana
    show marta2 1a 2a 3a regular1 at d31 as marta
    show sima1 1g 2a 3d at d33 as sima
    with dissolve
    n "\"American dream\"!"#
    show nana1 1e 2c 3d regular1 at d32 as nana
    show marta2 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at d32 as nana
    show marta2 1e 2a 3a regular1 at u31 as marta
    show sima1 1g 2a 3a at d33 as sima
    with dissolve
    m "I don't think people remember what it is anymore."
    show marta2 1e 2a 3a regular1 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1a 2a 3a regular1 at d31 as marta
    show sima1 1a 2a 3a at d33 as sima
    with dissolve
    p "I think the whole world thinks everything is better in the US."
    show marta2 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3a regular2 at u31 as marta
    show sima3a 1a 2a 3a at d33 as sima
    with dissolve
    m "Appears to be better, [player_name], appears to be better."
    show marta2 1e 2a 3d regular2 at u31 as marta
    show nana1 1a 2a 3d regular2 at d32 as nana
    with dissolve
    m "Look, when we get our degrees and all... You know what will be the difference between us?"
    show marta1 1c 2a 3a at u31 as marta
    show sima2 1a 2a 3d regular2 at d33 as sima
    show nana1 1f 2a 3a regular2 at d32 as nana
    with dissolve
    m "You're going to brag about your new flat, while I'll be paying off my student loans."#
    show marta1 1c 2a 3a at d31 as marta
    show nana1 1f 2a 3a regular2 at u32 as nana
    $ renpy.pause(.001, hard=True)
    show marta1 1a 2a 3a at d31 as marta
    show sima2 1a 2a 3a regular2 at d33 as sima
    show nana1 1c 2a 3d regular2 at u32 as nana
    with dissolve
    n "Are you sure you love your country?"
    show nana1 1c 2a 3d regular2 at d32 as nana
    show marta1 1a 2a 3a at u31 as marta
    $ renpy.pause(.001, hard=True)
    show marta1 1e 2a 3b at u31 as marta
    show nana1 1a 2a 3a regular2 at d32 as nana
    with dissolve
    m "I do, and that's why I'm so concerned."
    return
label flyers_nana:
    play music "music/classes_theme.ogg" fadeout 1.5 fadein 1.5
    scene d3fairnana
    show nana3 1a 2a 3a at u11 as nana
    with fade
    "Nana ended up helping some random construction company."
    show nana3 1e 2a 3a at u11 as nana with dissolve
    n "Oh hi, [player_name]!"
    show nana3 1d 2a 3d at u11 as nana with dissolve
    n "Look, here I try to attract those who may work in the construction industry!"
    show nana3 1a 2a 3d at u11 as nana with dissolve
    p "How's it going for you?"
    show nana1 1e 2a 3a regular2 at u11 as nana with dissolve
    n "All good! Watch me distributing all the flyers in no more than five minutes!"
    show nana1 1d 2a 3b regular2 at u11 as nana with dissolve
    n "I know how to talk to people!"
    show nana1 1a 2a 3a regular2 at u11 as nana with dissolve
    p "What do I have to do?"
    show nana3 1e 2a 3d at u11 as nana with dissolve
    n "Just don't distract me and that's it."
    show nana3 1a 2a 3a at u11 as nana with dissolve
    p "Is that all?"
    show nana1 1c 2a 3d regular2 at u11 as nana with dissolve
    n "Alright, you can also hand me these flyers when needed..."
    show nana1 1d 2a 3a regular2 at u11 as nana with dissolve
    n "So I don't need to grab those stupid leaflets, ya know."
    show nana1 1e 2a 3a regular1 at u11 as nana with dissolve
    n "Alright! Ready, set... go!"
    show nana1 1a 2a 3a regular2 at u11 as nana with dissolve
    "Someone approaches the booth. I think it's a guy from another class."
    show nana1 1a 2a 3a regular2 at u22 as nana
    $ npc_name = "Guy"
    npc "Hey! Which class are you from?"
    show nana1 1c 2a 3d regular2 at u22 as nana
    with dissolve
    n "Well, what's the difference? Are you here looking for work or what?"
    show nana1 1a 2a 3d regular2 at u22 as nana
    with dissolve
    npc "I'm still studying, you know."
    show nana1 1e 2a 3a regular1 at u22 as nana
    with dissolve
    n "And you could've been working already! Everyone would be so proud of you!"
    show nana1 1f 2a 3d regular1 at u22 as nana
    with dissolve
    npc "I don't know. Construction work is kinda low-class..."
    show nana1 1e 2d 3b regular2 at u22 as nana
    with dissolve
    n "Hey, it's only the beginning! You're going to rule the whole site in the future."
    show nana1 1a 2a 3a regular2 at u22 as nana
    with dissolve
    npc "Well, it's the future, right, I need something fun from the very beginning..."
    show nana3 1e 2a 3d  at u22 as nana
    with dissolve
    n "You have it! Look here..."
    show nana3 1d 2a 3a  at u22 as nana
    with dissolve
    n "\"It's an adventure for real men!\""
    show nana3 1a 2a 3a  at u22 as nana
    with dissolve
    npc "Meaning the working conditions are terrible."
    show nana1 1d 2d 3b regular2 at u22 as nana
    with dissolve
    n "\"You can travel and get to know your country!\""
    show nana1 1a 2a 3a regular2 at u22 as nana
    with dissolve
    npc "Yeah, so I'll have to work in the middle of nowhere."
    show nana1 1e 2c 3c regular1 at u22 as nana
    with dissolve
    n "\"Adequate compensation!\""
    show nana1 1a 2a 3a regular2 at u22 as nana
    with dissolve
    npc "Like, when I have enough to pay for the food every month?"
    show nana1 1e 2d 3a regular2 at u22 as nana
    with dissolve
    n "Screw you! We don't need someone like you!"
    show nana1 1a 2d 3a regular2 at u22 as nana
    with dissolve
    npc "Whatever. I'm leaving."
    show nana1 1e 2c 3c regular1 at u22 as nana
    with dissolve
    n "Pff, as you wish. No, wait! Wait! I have to give you this handout..."
    show nana1 1a 2c 3a regular2 at u22 as nana
    with dissolve
    npc "I don't need it."
    show nana3 1c 2a 3d at u22 as nana
    with dissolve
    n "It's okay, just take it."
    show nana3 1a 2a 3d at u22 as nana
    with dissolve
    npc "No."
    show nana1 1e 2d 3c regular1 at u22 as nana
    with dissolve
    n "If you don't take it now, I'll scream and say you're harassing me!"
    show nana1 1f 2d 3d regular1 at u22 as nana
    with dissolve
    npc "What???"
    show nana1 1c 2d 3d regular2 at u22 as nana
    with dissolve
    n "Trying to touch my private parts!"
    show nana1 1g 2a 3a regular2 at u22 as nana with dissolve
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at u11 as nana
    "The guy takes the handout and almost runs away, his face being ruby red."
    show nana3 1e 2a 3d at u11 as nana with dissolve
    n "How's this for you?"
    show nana3 1g 2a 3d at u11 as nana with dissolve
    p "Um, how should I put it..."
    show nana3 1d 2a 3b at u11 as nana with dissolve
    n "[player_name], a victory is a victory!"
    show nana3 1a 2a 3a at u11 as nana with dissolve
    p "I know, but still..."
    show nana1 1e 2a 3a regular1 at u11 as nana with dissolve
    n "Hush! Here comes another one..."
    show nana1 1a 2a 3a regular2 at u11 as nana with dissolve
    "We see a humble-looking girl approaching us."
    play music "music/day2_main.ogg" fadeout 1.5 fadein 1.5
    show nana1 1a 2a 3a regular2 at u22 as nana
    $ renpy.pause(.25, hard=True)
    show nana1 1g 2a 3d regular2 at u22 as nana with dissolve
    with dissolve
    $ npc_name = "Girl"
    npc "Hey! What do you guys have here?"
    show nana3 1e 2a 3d at u22 as nana
    with dissolve
    n "An opportunity to be a construction worker, a dream job for every girl!"
    show nana3 1g 2a 3d at u22 as nana
    with dissolve
    npc "Are you kidding me?"
    show nana3 1e 2c 3a at u22 as nana
    with dissolve
    n "Well, look a this! A hard hat, fancy shoes and all, free of cost for you!"#
    show nana1 1f 2a 3d regular2 at u22 as nana
    with dissolve
    npc "Do you have a pink hard hat?"
    show nana1 1c 2a 3d regular2 at u22 as nana
    with dissolve
    n "No worries, we can paint it."
    show nana1 1f 2a 3d regular2 at u22 as nana
    with dissolve
    npc "Well, what do I have to do?"
    show nana3 1c 2a 3a at u22 as nana
    with dissolve
    n "Well, a construction site is a twilight world of swingers..."
    show nana1 1g 2a 3a regular2 at u22 as nana with dissolve
    $ renpy.pause(.001, hard=True)
    show nana1 1g 2a 3a regular2 at u11 as nana
    "Not saying a word, the girl turns around and leaves in a hurry."
    p "Nana, what on earth was that?"
    show nana3 1e 2a 3d at u11 as nana with dissolve
    n "What do you mean? When the wind blows, the whole site is swinging."
    show nana3 1g 2a 3a at u11 as nana with dissolve
    p "Don't try to play it dumb."#
    show nana1 1e 2a 3d regular2 at u11 as nana with dissolve
    n "Oh well, who cares? I don't need her anyway. A pink hat! What a nonsense."#
    show nana1 1g 2a 3a regular2 at u11 as nana with dissolve
    "Nana's performance continued to be like this" #fixed in None
    "However, the guy from that construction firm looked quite satisfied."#
    scene black with fade
    return
label flyers_marta:
    play music "music/classes_theme.ogg" fadeout 1.5 fadein 1.5
    scene d3fairmarta
    show marta2 1a 2a 3a regular1 at u11 as marta
    with fade
    "Marta was responsible for promoting one of the more famous universities around."
    show marta2 1e 2a 3a regular2 at u11 as marta with dissolve
    m "Hey, [player_name]! Look at this!"
    show marta2 1f 2a 3a regular1 at u11 as marta with dissolve
    p "What's up?"
    show marta1 1e 2a 3b at u11 as marta with dissolve
    m "It's the career day, yet I'm offering people to study more!"
    show marta1 1f 2a 3b at u11 as marta with dissolve
    p "Wait, but you're going to study yourself. It's normal for any high-skilled job."
    show marta1 1d 2a 3a at u11 as marta with dissolve
    m "Yeah, but it's so boring!"
    show marta1 1f 2a 3a at u11 as marta with dissolve
    p "If you wish, I can distribute the handouts for you. Do you want me to?"
    show marta2 1b 2a 3a regular2 at u11 as marta with dissolve
    m "Think you can handle this better than I do? Think again..."
    show marta2 1e 2d 3a regular1 at u11 as marta with dissolve
    m "Just fetch me the new ones while I'll be handing them here and there, got it?"#
    show marta2 1g 2a 3a regular1 at u11 as marta with dissolve
    p "Sure thing."
    "We have a first visitor, a girl from another class."#
    show marta2 1a 2a 3a regular1 at u22 as marta
    $ npc_name = "Girl"
    npc "Wow, I've heard a lot about this university! It's so cool to study there..."
    show marta3 1e 2a 3a at u22 as marta
    with dissolve
    m "You bet! Also, we have tuition fees and all..."
    show marta2 1b 2a 3a regular2 at u22 as marta with dissolve
    m "Great sporting facilities... go ahead and apply!"
    show marta2 1g 2a 3a regular1 at u22 as marta
    with dissolve
    npc "I'll do this! This is the place to become a psychologist."
    show marta2 1d 2c 3c regular1 at u22 as marta
    with dissolve
    m "Become who?"
    show marta2 1d 2d 3a regular1 at u22 as marta
    with dissolve
    npc "A psychologist. I want to help people."
    show marta2 1e 2d 3d regular2 at u22 as marta
    with dissolve
    m "Hey, this is a STEM-oriented university, you know..."
    show marta2 1f 2d 3d regular1 at u22 as marta
    with dissolve
    npc "Yeah? Well, I don't need STEM, it's for nerds."
    show marta2 1f 2c 3a regular1 at u22 as marta with dissolve
    npc "I'm inspired by emotions."
    show marta1 1f 2b 3b at u22 as marta
    with dissolve
    m "..."
    show marta1 1e 2b 3d at u22 as marta with dissolve
    m "So what you're going to do, find your clients after you graduate?"#
    show marta1 1f 2b 3d at u22 as marta
    with dissolve
    npc "No, I want to teach psychology."
    show marta1 1c 2d 3b at u22 as marta
    with dissolve
    m "Right, I should've figured."
    show marta1 1f 2d 3d at u22 as marta
    with dissolve
    npc "How come?"
    show marta2 1e 2d 3a regular2 at u22 as marta
    with dissolve
    m "I don't know, my intuition is quite good."#
    show marta2 1f 2d 3d regular1 at u22 as marta
    with dissolve
    npc "Are you trying to say being a psychologist is something bad?"
    "She gets visibly nervous."
    show marta2 1e 2d 3c regular2 at u22 as marta
    with dissolve
    m "No, I never said this."#
    show marta2 1c 2c 3a regular1 at u22 as marta with dissolve
    m "Why are you so nervous? Psychologists are supposed to be super calm, no?"
    show marta2 1a 2a 3a regular1 at u22 as marta
    with dissolve
    npc "Don't tell me how I should act! Who do you think you are?"
    show marta3 1ee 2a 3b regular2 at u22 as marta
    with dissolve
    m "I don't know. Can you give me a consultation?"
    show marta3 1ee 2a 3b regular2 at u11 as marta
    $ renpy.pause(.2, hard=True)
    show marta3 1b 2a 3a regular1 at u11 as marta with dissolve
    "The girl leaves."
    show marta3 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Did you see this?"
    show marta3 1b 2a 3a regular1 at u11 as marta with dissolve
    p "Hey, you were supposed to attract her, you know."
    show marta2 1e 2a 3a regular1 at u11 as marta with dissolve
    m "Who cares! I saved quite some time for this university."
    show marta2 1a 2a 3a regular1 at u11 as marta with dissolve
    "Another visitor approaches us."
    play music "music/day2_main.ogg" fadeout 1.5 fadein 1.5
    show marta2 1a 2a 3a regular1 at u22 as marta
    $ npc_name = "Visitor"
    npc "This booth is not job-related, right?"
    show marta2 1b 2a 3a regular1 at u22 as marta
    with dissolve
    m "No, it's too early for this. You need to know yourself better."
    show marta3 1e 2c 3a at u22 as marta with dissolve
    m "Like, take your time and all."
    show marta3 1a 2a 3a at u22 as marta
    with dissolve
    npc "Well, why not...."
    show marta2 1b 2a 3a regular2 at u22 as marta
    with dissolve
    m "So who do you want to be?"
    show marta2 1f 2b 3a regular1 at u22 as marta
    with dissolve
    npc "I enjoy philosophy."
    show marta1 1f 2b 3b at u22 as marta
    with dissolve
    m "..."
    show marta1 1f 2b 3b at u22 as marta
    with dissolve
    npc "Can I become a philosopher in this university?"#
    show marta1 1e 2b 3b at u22 as marta
    with dissolve
    m "Not sure. The competition is tough, we have a lot of philosophers around."
    show marta1 1d 2a 3a at u22 as marta with dissolve
    m "So which philosopher is your personal favorite?"
    show marta1 1f 2d 3d at u22 as marta
    with dissolve
    npc "I don't really know them too well."
    show marta2 1e 2d 3c regular2 at u22 as marta
    with dissolve
    m "wait, what?"#
    show marta2 1f 2d 3d regular1 at u22 as marta
    with dissolve
    npc "I'm just not that good at math, but I need a diploma anyway."
    show marta3 1e 2a 3a regular1 at u22 as marta
    with dissolve
    m "Then you're going to be the perfect fit."
    show marta3 1a 2a 3a regular1 at u22 as marta
    with dissolve
    npc "Cool? Can I fill in a form or something?"#
    show marta2 1b 2a 3a regular2 at u22 as marta
    with dissolve
    m "Sure thing! You see this girl? Yeah, the pink-haired one?."
    show marta3 1ee 2a 3a regular2 at u22 as marta
    with dissolve
    m "She'll give you a form to fill. It will say \"construction worker\", but it's just a slang."
    show marta3 1bb 2a 3a regular2 at u22 as marta
    with dissolve
    npc "Construction? How is this related to my degree in philosophy?"
    show marta2 1b 2a 3a regular2 at u22 as marta
    with dissolve
    m "Hey, come on! It's a metaphor... You build your life one brick after another..."#
    show marta2 1a 2a 3a regular1 at u22 as marta
    with dissolve
    "The guy looks happy with this answer, so he leaves."
    show marta2 1a 2a 3a regular1 at u11 as marta
    "it goes on like this."
    "A representative from this university sits close, but he doesn't pay any attention."
    "He's too busy with his phone it seems."
    scene black with fade
    return
label flyers_sima:
    play music "music/classes_theme.ogg" fadeout 1.5 fadein 1.5
    scene d3fairsima
    show sima2 1a 2a 3a regular2 at u11 as sima
    with fade
    "Sima helps some large company who seemingly sells everything in the world."
    show sima2 1d 2a 3a regular1 at u11 as sima with dissolve
    s "Hi, [player_name]! I'm glad you volunteered to help me here."
    show sima2 1g 2a 3a regular2 at u11 as sima with dissolve
    p "So, what's the job you advertise?"
    show sima3a 1c 2a 3a at u11 as sima with dissolve
    s "A manager."
    show sima3a 1g 2a 3a at u11 as sima with dissolve
    p "A manager of what?"
    show sima3a 1c 2b 3d at u11 as sima with dissolve
    s "Of a brand. It's called a brand manager."
    show sima3a 1g 2b 3a at u11 as sima with dissolve
    p "Oh, it means selling stuff?"
    show sima2 1e 2a 3b regular1 at u11 as sima with dissolve
    s "No, these are the guys from sales department."#
    show sima2 1g 2a 3a regular1 at u11 as sima with dissolve
    p "Then it means being responsible for the design and all, right?"
    show sima2 1c 2a 3b regular1 at u11 as sima with dissolve
    s "No, once again the other guys do this."
    show sima2 1a 2a 3a regular2 at u11 as sima with dissolve
    p "Well, what am I supposed to do then?"
    show sima3a 1d 2a 3d at u11 as sima with dissolve
    s "Be the one in charge of making things happen!."#
    show sima3a 1e 2a 3a at u11 as sima with dissolve
    s "Look, can you help me with the handouts? Just be ready to give me some more, okay?"
    show sima3a 1a 2a 3a at u11 as sima with dissolve
    "I see a first visitor, it's a girl from another class."
    show sima3a 1a 2a 3a at u22 as sima
    $ renpy.pause(.25, hard=True)
    show sima3a 1a 2a 3a at u22 as sima with dissolve
    $ npc_name = "Girl"
    npc "Oh wow, this company is so cool! Like, everyone would be excited to work there."
    show sima2 1d 2c 3a regular1 at u22 as sima
    with dissolve
    s "You bet! Would you like to be the part of this company?"
    show sima2 1g 2a 3a regular1 at u22 as sima
    with dissolve
    npc "Yeah, although I'm a bit concerned about one thing."
    show sima2 1c 2c 3a regular2 at u22 as sima
    with dissolve
    s "What exactly?"
    show sima2 1a 2c 3c regular2 at u22 as sima
    with dissolve
    npc "I've heard your company is sexist."
    show sima3a 1d 2a 3d at u22 as sima
    with dissolve
    s "In, um, what regard?"
    show sima3a 1a 2a 3d at u22 as sima
    with dissolve
    npc "I heard it's heavily biased against women."
    show sima2 1d 2d 3c regular1 at u22 as sima
    with dissolve
    s "Who told you this?"
    show sima2 1a 2d 3a regular2 at u22 as sima
    with dissolve
    npc "You know, they say that the work itself is far, the issue is with recruiting process."
    show sima2 1a 2a 3d regular2 at u22 as sima with dissolve
    npc "They mainly recruit males, and that's a problem."
    show sima3a 1c 2d 3d at u22 as sima
    with dissolve
    s "It can't be. Look, now I'm concerned as well... I'm going to ask a representative."
    show sima3a 1a 2a 3d at u22 as sima
    with dissolve
    npc "Cool, I'm waiting here."
    show black with fade
    hide black
    show sima2 1g 2a 3a regular2 at u22 as sima
    with fade
    "Sima comes back after a few minutes."
    show sima2 1e 2a 3b regular1 at u22 as sima with dissolve
    s "Okay, now I know everything. And I can assure you that everything is fair!"
    show sima2 1g 2a 3a regular2 at u22 as sima
    with dissolve
    npc "So..."
    show sima2 1d 2c regular2 3a at u22 as sima with dissolve
    s "So, the recruiting is totally fair because they do blind hiring."
    show sima2 1c 2a 3b regular2 at u22 as sima with dissolve
    s "You pass all the tests, then you do a written case, all anonymously."
    show sima3a 1e 2a 3a at u22 as sima with dissolve
    s "Your identity is only revealed once twenty best results are identified."#
    show sima3a 1d 2a 3b at u22 as sima with dissolve
    s "This year they plan to hire twenty interns again."
    show sima3a 1a 2a 3a at u22 as sima
    with dissolve
    npc "Oh, I see.Then, how come last year 15 males and only 5 females were hired?" #fixed in None
    show sima2 1a 2c 3c regular2 at u22 as sima
    with dissolve
    s "..."
    show sima2 1a 2c 3c regular2 at u22 as sima
    $ renpy.pause(.25, hard=True)
    show sima3a 1a 2a 3a at u11 as sima with dissolve
    "The girl puts on a smug face and leaves."
    show sima3a 1c 2b 3b at u11 as sima with dissolve
    s "What's wrong with her? I'm all for equality, I really support it!"
    show sima3a 1a 2b 3a at u11 as sima with dissolve
    "Another girl approaches our booth."
    play music "music/day2_main.ogg" fadeout 1.5 fadein 1.5
    show sima3a 1a 2b 3a at u22 as sima
    $ renpy.pause(.25, hard=True)
    show sima2 1g 2a 3a regular2 at u22 as sima with dissolve
    $ npc_name = "Visitor"
    npc "Hey! Wow, a big name here, didn't expect it."
    show sima2 1c 2b 3a regular2 at u22 as sima
    with dissolve
    s "You want to work here?"
    show sima2 1g 2b 3a regular2 at u22 as sima
    with dissolve
    npc "Of course! However, I'm afraid they won't let me get in."
    show sima1 1a 2b 3d at u22 as sima
    with dissolve
    "Sima gets a little bit more tense, knowing what's going to happen next."
    show sima1 1c 2b 3a at u22 as sima
    with dissolve
    s "Why do you think so?"
    show sima1 1a 2b 3a at u22 as sima
    with dissolve
    npc "What do you mean? I'm not good enough yet, simple as that."
    show sima1 1g 2c 3a at u22 as sima
    with dissolve
    npc "However, you'll see me becoming the best in no time!"
    show sima2 1d 2a 3c regular1 at u22 as sima
    with dissolve
    s "Oh, so that's what you mean... Sure, I'm sure you'll make it!"#
    show sima2 1c 2b 3a regular2 at u22 as sima with dissolve
    s "Look, aren't you afraid that the recruiting process will be unfair?"
    show sima2 1a 2b 3a regular2 at u22 as sima
    with dissolve
    npc "Do I need to have connections to get in or what?"
    show sima2 1d 2c 3c regular1 at u22 as sima
    with dissolve
    s "No, of course not! They use blind hiring."
    show sima2 1d 2a 3b regular2 at u22 as sima with dissolve
    s "You pass all the tests, then you do a written case, all anonymously."
    show sima3a 1e 2a 3a at u22 as sima with dissolve
    s "Your identity is only revealed once twenty best results are identified."
    show sima1 1d 2a 3b at u22 as sima with dissolve
    s "This year they plan to hire twenty interns."
    show sima1 1g 2a 3a at u22 as sima
    with dissolve
    npc "Ha, then everything depends only on me! Moreover, I'll call my friends... There will be 20 female interns!"
    show sima1 1g 2a 3a at u11 as sima
    $ renpy.pause(.25, hard=True)
    show sima1 1g 2a 3b at u11 as sima with dissolve
    "She takes a handout and leaves."
    show sima2 1d 2c 3a regular1 at u11 as sima with dissolve
    s "See, [player_name], it's all about your personality, everything else doesn't matter."
    show sima2 1g 2c 3a regular2 at u11 as sima with dissolve
    "I fully agree with this."
    scene black with fade
    return
label flowers_for_algernon_help:
    nvl clear
    $ config.nvl_list_length = None
    ermy_game "Flower for Algernon is a short science fiction story by Daniel Keyes, first published in 1959."
    ermy_game "The story is told by a serie of diary entries by Charlie, a man who underwent surgery to increase his intelligence."
    ermy_game "The surgery turns out to be successful, and now highly intelligent Charlie obtains a different perspective on the world."
    ermy_game "He realizes the limitations of people surrounding him, while they alienate him."
    ermy_game "Soon, however, his intelligence regresses to its original state."
    ermy_game "He tries to revert to normal, only to no avail, and can't stand the pity from his co-workers."
    nvl clear
    $ config.nvl_list_length = 3
    hide gui_shade with dissolve
    stop music fadeout 2
    jump choice_ready_d1
label flowers_for_algernon:
    scene jp_classroom_day
    show nana1 1a 2a 3a noblush regular2 at d11 as nana
    with fade
    show nana1 1a 2a 3a noblush regular2 at u11 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1d 2c 3a blush regular1 at u11 as nana with dissolve
    n "That's my favorite book, yay!"
    show cg_nana_8_2 with fade
    $ persistent.unlock_cg_nana_8_2 = 1
    n "In this day and time, it's much easier to be dumb rather than smart."
    n "People don't really understand a smart person... neither does he, heh."
    n "At least he knows his own limitations, as well as limitations of other people."
    n "Only a tiny fraction of people have an IQ higher than 150. Much less than 1 percent!"
    n "But the world is built by the 99 percent... They're stronger and bigger in numbers."
    n "A lot of really smart people end up being left alone, feeling desperate..."
    n "Daniel Keyes managed to show it extremely well in this book."
    n "By the way, Algernon is a name of the mouse that underwent the same experiment as Charlie."
    n "However, it started to revert into its original state much sooner than Charlie."
    n "His last wish is for someone to put flowers on Algernon's grave..."
    hide cg_nana_8_2
    show teya_ivanovna
    show teya2close 1c 2b 3d regularhand1 at u11 as teya
    with fade
    t "Such a nice and sad story!"
    hide teya_ivanovna
    hide teya
    show nana1 1a 2a 3a regular2 at d22 as nana
    show marta2 1a 2a 3d regular1 at d21 as marta
    with fade
    show marta2 1a 2a 3d regular1 at u21 as marta
    $ renpy.pause(.001, hard=True)
    show marta2 1e 2a 3d regular2 at u21 as marta with dissolve
    m "Do you think that being smart means a real tragedy?"
    show marta2 1e 2a 3d regular2 at d21 as marta
    show nana1 1a 2a 3a regular2 at u22 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2c 3a regular1 at u22 as nana
    show marta2 1a 2a 3d regular1 at d21 as marta
    with dissolve
    n "Yeah, it's very tough."
    show nana1 1e 2c 3a regular1 at d22 as nana
    show marta2 1a 2a 3d regular1 at u21 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2c 3a regular2 at d22 as nana
    show marta3 1e 2a 3a regular1 at u21 as marta
    with dissolve
    m "Nana, do you know why smart people tend to be poor pretty often?"
    show nana1 1f 2c 3d regular2 at d22 as nana
    show marta2 1b 2a 3a regular2 at u21 as marta
    with dissolve
    m "I mean if you're that cool, how can you literally... perish without a trace?"
    show nana1 1a 2c 3a regular2 at d22 as nana
    show marta3 1e 2a 3a regular1 at u21 as marta
    with dissolve
    m "I mean, one could've earned quite some money on foolishness of other people, right?"
    show nana1 1f 2d 3a regular2 at d22 as nana
    show marta3 1ee 2a 3a regular2 at u21 as marta
    with dissolve
    m "If not, maybe that one person is not that smart at all?"
    show nana1 1f 2d 3a regular2 at u22 as nana
    show marta3 1ee 2a 3a regular2 at d21 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2d 3a regular1 at u22 as nana
    show marta3 1b 2a 3a regular1 at d21 as marta
    with dissolve
    n "You don't get it, Marta!"
    show nana1 1e 2d 3a regular1 at d22 as nana
    show marta3 1b 2a 3a regular1 at u21 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1f 2d 3a regular1 at d22 as nana
    show marta3 1ee 2a 3a regular2 at u21 as marta
    with dissolve
    m "Yeah, maybe I'm not too smart either."
    show nana1 1f 2d 3a regular1 at d33 as nana
    show marta3 1a 2a 3a regular1 at d31 as marta
    $ renpy.pause(.25, hard=True)
    show sima3a 1a 2a 3a at u32 as sima
    $ renpy.pause(.001, hard=True)
    show sima3a 1d 2a 3a at u32 as sima with dissolve
    s "Marta, I think the root of the problem is that smart people see the world differently..."
    show nana1 1a 2b 3a regular2 at d33 as nana
    show sima3a 1c 2a 3d at u32 as sima
    with dissolve
    s "And they can't really observe it through the eyes of other people, so..."
    show sima3a 1c 2a 3d at d32 as sima
    show marta3 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima3a 1a 2a 3a at d32 as sima
    show marta2 1e 2a 3a regular2 at u31 as marta
    with dissolve
    m "What's the point in being smart if you can't even understand people around you?"
    show marta2 1e 2a 3a regular2 at d31 as marta
    show nana1 1a 2a 3a regular2 at u33 as nana
    $ renpy.pause(.001, hard=True)
    show nana1 1e 2a 3c regular1 blush at u33 as nana
    show sima1 1a 2a 3a at d32 as sima
    show marta2 1a 2a 3a regular1 at d31 as marta
    with dissolve
    n "Because your brain doesn't let you get down to their level."
    show nana1 1e 2a 3c regular1 blush at d33 as nana
    show marta2 1a 2a 3a regular1 at u31 as marta
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2b 3d at d33 as nana
    show sima1 1g 2a 3d at d32 as sima
    show marta2 1e 2d 3a regular1 at u31 as marta
    with dissolve
    m "Whoa, so you think you're smarter than others, don't you?"
    show sima1 1g 2a 3d at u32 as sima
    show marta2 1e 2d 3a regular1 at d31 as marta
    $ renpy.pause(.001, hard=True)
    show nana2 1f 2b 3b at d33 as nana
    show sima3a 1d 2a 3a at u32 as sima
    show marta3 1gg 2a 3a regular2 at d31 as marta
    with dissolve
    s "What if we all are a part of that experiment, and Nana is the only one yet to revert?"
    show nana1 1a 2a 3a regular2 at d33 as nana
    show sima3b 1d 2a 3b at u32 as sima
    show marta3 1g 2a 3a regular1 at d31 as marta
    with dissolve
    s "Oh well... I like daisies, Nana!"
    show teya_ivanovna
    show teya2close 1a 2a 3a at u11 as teya
    with fade
    if game_restarted1 == 1:
        if persistent.game_done1 == True:
            scene black with fade
            $ renpy.pause(1, hard=True)
            jump street_nana
    if books_chosen == 1:
        call intermission from _call_intermission_3
    if books_chosen == 1:
        menu:
            "\"Crime and Punishment\"":
                $ as_p = 1
                $ books_chosen = 2
                play music "music/book2_day1.ogg" fadeout 2 fadein 2
                jump crime
            "\"The Catcher in the Rye\"":
                $ am_p = 1
                $ books_chosen = 2
                play music "music/book2_day1.ogg" fadeout 2 fadein 2
                jump catcher
    else:
        jump lessonp2
label day5_something_familiar:
    show teya2 1a 2a 3a fancyhand4 at u11 as teya with dissolve
    p "Strangely enough, the girls always reminded me of someone..."
    show teya2 1e 2a 3d fancyhand1 at u11 as teya with dissolve
    t "What's so strange about that? You met the three sisters of fate."
    show teya2 1c 2a 3a fancyhand2 at u11 as teya with dissolve
    t "Each one of them is like a collective character, you see."
    show teya2 1a 2a 3a fancyhand4 at u11 as teya with dissolve
    p "Okay, what about that room with the arcade machine in it?"
    show teya1 1c 2c 3a fancy at u11 as teya with dissolve
    t "What are you talking about?"
    show teya1 1a 2a 3a fancy at u11 as teya with dissolve
    "I do a quick re-cap of my dreams."
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "That's pretty funny! Do you want an honest answer? I don't know."
    show teya3 1c 2a 3a fancy at u11 as teya with dissolve
    t "See, a human brain always tries to justify everything."
    show teya1 1e 2a 3b fancy at u11 as teya with dissolve
    t "It went to a safe mode right after we first met, so he made up this room."#
    show teya2 1e 2a 3a fancyhand1 at u11 as teya with dissolve
    t "But hey, you have a great imagination!"
    show teya2 1a 2a 3a fancyhand4 at u11 as teya with dissolve
    p "You too."
    show teya1 1c 2a 3b fancy at u11 as teya with dissolve
    t "Oh dear..."
    show teya1 1e 2a 3a fancy at u11 as teya with dissolve
    t "Why humans always waste everything I give them?"#
    show teya1 1d 2d 3d fancy at u11 as teya with dissolve
    t "I've actually done my best! Three beautiful girls, new countries, interesting activities..."
    show teya1 1c 2b 3b fancy at u11 as teya with dissolve
    t "But while you were busy playing that slot machine, time passed by."
    show teya1 1a 2a 3a fancy at u11 as teya with dissolve
    p "But each day was like a serie of episodes poorly sewn together."#
    show teya2 1e 2a 3a fancyhand2 at u11 as teya with dissolve
    t "That's how the vast majority of people treats life, [player_name]."
    show teya3 1c 2a 3b fancy at u11 as teya with dissolve
    t "In return, life also treats them accordingly. If I were to grade lives of others..."
    show teya2 1e 2d 3a fancyhand2 at u11 as teya with dissolve
    t "\"A serie of episodes poorly sewn together\" deserves nothing more than a C grade."
    show teya1 1e 2d 3a fancy at u11 as teya with dissolve
    t "Being envious of others, seeking for reasons to justify your own failure."
    show teya1 1c 2d 3b fancy at u11 as teya with dissolve
    t "Arguing that you're still young and can afford to relax until you're well in your 30s."
    show teya2 1e 2c 3a fancyhand2 at u11 as teya with dissolve
    t "And I'd give you an A grade for sewing your own life."
    show teya2 1e 2a 3b fancyhand4 at u11 as teya with dissolve
    t "Even if there's no happy ending, there's something to remember."
    return
label day5_after_spiral:
    show br_f as br with dissolve
    t "You know what all cycles have in common closer to the end, [player_name]?"
    show m_c as m with dissolve
    t "Humans stop being considerate of others."
    show br_n as br with dissolve
    t "You can understand your purpose in life only after your understand that of others."#
    show m_o as m with dissolve
    t "Their purpose is no better or worse than yours."
    show br_f as br with dissolve
    t "Maybe there's no purpose at all, but..."
    show br_n as br with dissolve
    t "You never know until you try to find one."
    show m_c as m with dissolve
    t "And you had Ermy to act as mirror, if you know what I'm talking about."#
    return

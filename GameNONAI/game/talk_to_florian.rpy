default florian_first_asked = False
default florian_second_asked = False
default florian_third_asked = False
default florian_fourth_asked = False
default florian_fifth_asked = False

label talk_to_florian:
    scene backyard night1
    with fade

    show florian worried
    with dissolve

    florian "So... what do you want to know?"

    while not (florian_first_asked and florian_second_asked and florian_third_asked and florian_fourth_asked and florian_fifth_asked):
        menu:
            "Where were you?" if not florian_first_asked:
                $ florian_first_asked = True
                me "Where were you?"
                florian "bla bla bla"
            "Second question" if not florian_second_asked:
                $ florian_second_asked = True
                me "Second question"
                florian "bla bla bla"
            "Third question" if not florian_third_asked:
                $ florian_third_asked = True
                me "Third question"
                florian "bla bla bla"
            "Tell me about" if not florian_fourth_asked:
                $ florian_fourth_asked = True
                me "Tell me about"
                florian "bla bla bla"
            "Tell me about" if not florian_fifth_asked:
                $ florian_fifth_asked = True
                me "Tell me about"
                florian "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
default florian_first_asked = False
default florian_second_asked = False
default florian_third_asked = False

label talk_to_florian:
    scene backyard night1
    with fade

    show florian worried
    with dissolve

    florian "hey, what's up?"

    while not (florian_first_asked and florian_second_asked and florian_third_asked):
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

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
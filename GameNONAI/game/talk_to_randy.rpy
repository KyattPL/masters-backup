default randy_first_asked = False
default randy_second_asked = False
default randy_third_asked = False

label talk_to_randy:
    scene mkitchen night
    with fade

    show randy worried
    with dissolve

    randy "hey, what's up?"

    while not (randy_first_asked and randy_second_asked and randy_third_asked):
        menu:
            "Where were you?" if not randy_first_asked:
                $ randy_first_asked = True
                me "Where were you?"
                randy "bla bla bla"
            "Second question" if not randy_second_asked:
                $ randy_second_asked = True
                me "Second question"
                randy "bla bla bla"
            "Third question" if not randy_third_asked:
                $ randy_third_asked = True
                me "Third question"
                randy "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
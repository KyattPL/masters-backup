default randy_first_asked = False
default randy_second_asked = False
default randy_third_asked = False
default randy_fourth_asked = False
default randy_fifth_asked = False

label talk_to_randy:
    scene mkitchen night
    with fade

    show randy worried
    with dissolve

    randy "So... what do you want to know?"

    while not (randy_first_asked and randy_second_asked and randy_third_asked and randy_fourth_asked and randy_fifth_asked):
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
            "Tell me about" if not randy_fourth_asked:
                $ randy_fourth_asked = True
                me "Fourth question"
                randy "bla bla bla"
            "Tell me about" if not randy_fifth_asked:
                $ randy_fifth_asked = True
                me "Fifth question"
                randy "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
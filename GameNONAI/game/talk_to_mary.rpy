default mary_first_asked = False
default mary_second_asked = False
default mary_third_asked = False
default mary_fourth_asked = False
default mary_fifth_asked = False

label talk_to_mary:
    scene interior entrance night
    with fade

    show mary shock
    with dissolve

    mary "So... what do you want to know?"

    while not (mary_first_asked and mary_second_asked and mary_third_asked and mary_fourth_asked and mary_fifth_asked):
        menu:
            "Where were you?" if not mary_first_asked:
                $ mary_first_asked = True
                me "Where were you?"
                mary "bla bla bla"
            "Second question" if not mary_second_asked:
                $ mary_second_asked = True
                me "Second question"
                mary "bla bla bla"
            "Third question" if not mary_third_asked:
                $ mary_third_asked = True
                me "Third question"
                mary "bla bla bla"
            "Tell me about" if not mary_fourth_asked:
                $ mary_fourth_asked = True
                me "Fourth question"
                mary "bla bla bla"
            "Tell me about" if not mary_fifth_asked:
                $ mary_fifth_asked = True
                me "Fifth question"
                mary "bla bla bla"

    "Hmm... I guess I'm done with her"
    jump interrogate_loop
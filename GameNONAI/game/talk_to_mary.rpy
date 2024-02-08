default mary_first_asked = False
default mary_second_asked = False
default mary_third_asked = False

label talk_to_mary:
    scene interior entrance night
    with fade

    show mary shock
    with dissolve

    mary "hey, what's up?"

    while not (mary_first_asked and mary_second_asked and mary_third_asked):
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

    "Hmm... I guess I'm done with her"
    jump interrogate_loop
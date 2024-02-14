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
            "Tell me about yourself" if not mary_first_asked:
                $ mary_first_asked = True
                me "Tell me a bit about yourself. What did you see tonight?"
                mary "bla bla bla"
            "Tell me about Adam" if not mary_second_asked:
                $ mary_second_asked = True
                me "Tell me about Adam."
                mary "bla bla bla"
            "Tell me about Florian" if not mary_third_asked:
                $ mary_third_asked = True
                me "Tell me about Florian."
                mary "bla bla bla"
            "Tell me about Nathaniel" if not mary_fourth_asked:
                $ mary_fourth_asked = True
                me "Tell me about Nathaniel."
                mary "bla bla bla"
            "Tell me about Randy" if not mary_fifth_asked:
                $ mary_fifth_asked = True
                me "Tell me about Randy."
                mary "bla bla bla"

    "Hmm... I guess I'm done with her"
    jump interrogate_loop
default nathaniel_first_asked = False
default nathaniel_second_asked = False
default nathaniel_third_asked = False
default nathaniel_fourth_asked = False
default nathaniel_fifth_asked = False

label talk_to_nathaniel:
    scene mroom night1
    with fade

    show nathaniel worried
    with dissolve

    nathaniel "So... what do you want to know?"

    while not (nathaniel_first_asked and nathaniel_second_asked and nathaniel_third_asked and nathaniel_fourth_asked and nathaniel_fifth_asked):
        menu:
            "Tell me about yourself" if not nathaniel_first_asked:
                $ nathaniel_first_asked = True
                me "Tell me about yourself. What did you see tonight?"
                nathaniel "bla bla bla"
            "Tell me about Adam" if not nathaniel_second_asked:
                $ nathaniel_second_asked = True
                me "Tell me about Adam."
                nathaniel "bla bla bla"
            "Tell me about Florian" if not nathaniel_third_asked:
                $ nathaniel_third_asked = True
                me "Tell me about Florian."
                nathaniel "bla bla bla"
            "Tell me about Mary" if not nathaniel_fourth_asked:
                $ nathaniel_fourth_asked = True
                me "Tell me about Mary."
                nathaniel "bla bla bla"
            "Tell me about Nathaniel" if not nathaniel_fifth_asked:
                $ nathaniel_fifth_asked = True
                me "Tell me about Nathaniel."
                nathaniel "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
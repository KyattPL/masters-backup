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
            "Tell me about yourself" if not florian_first_asked:
                $ florian_first_asked = True
                me "Tell me a bit about yourself. What did you see tonight?"
                florian "bla bla bla"
            "Tell me about Adam" if not florian_second_asked:
                $ florian_second_asked = True
                me "Tell me about Adam."
                florian "bla bla bla"
            "Tell me about Mary" if not florian_third_asked:
                $ florian_third_asked = True
                me "Tell me about Mary."
                florian "bla bla bla"
            "Tell me about Nathaniel" if not florian_fourth_asked:
                $ florian_fourth_asked = True
                me "Tell me about Nathaniel."
                florian "bla bla bla"
            "Tell me about Randy" if not florian_fifth_asked:
                $ florian_fifth_asked = True
                me "Tell me about Randy."
                florian "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
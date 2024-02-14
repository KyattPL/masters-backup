default adam_first_asked = False
default adam_second_asked = False
default adam_third_asked = False
default adam_fourth_asked = False
default adam_fifth_asked = False

label talk_to_adam:
    scene bedroom02 night
    with fade

    show adam serioustalksweat
    with dissolve

    adam "So... what do you want to know?"

    while not (adam_first_asked and adam_second_asked and adam_third_asked and adam_fourth_asked and adam_fifth_asked):
        menu:
            "Tell me about yourself" if not adam_first_asked:
                $ adam_first_asked = True
                me "Where were you?"
                adam "bla bla bla"
            "Tell me about Florian" if not adam_second_asked:
                $ adam_second_asked = True
                me "Second question"
                adam "bla bla bla"
            "Tell me about Mary" if not adam_third_asked:
                # python:
                #     question = renpy.input("What do you want to know?", length=64)
                #     question = question.strip()
        
                # $ adam_third_asked = True
                # me "[question]"
                # adam "bla bla bal"
                $ adam_third_asked = True
                me "Third question"
                adam "bla bla bla"
            "Tell me about Nathaniel" if not adam_fourth_asked:
                $ adam_fourth_asked = True
                me "Fourth question"
                adam "bla bla bla"
            "Tell me about Randy" if not adam_fifth_asked:
                $ adam_fifth_asked = True
                me "Fifth question"
                adam "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
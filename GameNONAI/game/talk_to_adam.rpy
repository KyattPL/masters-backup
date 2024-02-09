default adam_first_asked = False
default adam_second_asked = False
default adam_third_asked = False

label talk_to_adam:
    scene bedroom02 night
    with fade

    show adam serioustalksweat
    with dissolve

    adam "hey, what's up?"

    while not (adam_first_asked and adam_second_asked and adam_third_asked):
        menu:
            "Where were you?" if not adam_first_asked:
                $ adam_first_asked = True
                me "Where were you?"
                adam "bla bla bla"
            "Second question" if not adam_second_asked:
                $ adam_second_asked = True
                me "Second question"
                adam "bla bla bla"
            "Third question" if not adam_third_asked:
                # python:
                #     question = renpy.input("What do you want to know?", length=64)
                #     question = question.strip()
        
                # $ adam_third_asked = True
                # me "[question]"
                # adam "bla bla bal"
                $ adam_third_asked = True
                me "Third question"
                adam "bla bla bla"

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
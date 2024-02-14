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
                me "Tell me a little bit about yourself. What did you see?"
                adam "Well, you know..."
                adam "Life's not that easy when you're poor."
                adam "I live in a dingy apartment above my father's bakery."
                adam "I'd like to earn enough money in the future to go study abroad or something."
                adam "This Florian douchebag tried to buy out my dad's bakery..."
                adam "Anyways, I wanted to see if Sylvia arrived and is up at night."
                adam "That's when I saw her body in the hallway..."
                adam "Sorry, don't know much else."
            "Tell me about Florian" if not adam_second_asked:
                $ adam_second_asked = True
                me "Tell me about Florian."
                adam "Florian? Yeah, I know him from high school."
                adam "You know, it's true that I'm a little bit jealous of him. His rich and kind afterall."
                adam "I know that he fell in love with Sylvia."
                adam "Well to be honest, I also liked her..."
                adam "But yeah, she wouldn't be interested in me anyway right?"
            "Tell me about Mary" if not adam_third_asked:
                # python:
                #     question = renpy.input("What do you want to know?", length=64)
                #     question = question.strip()
        
                # $ adam_third_asked = True
                # me "[question]"
                # adam "bla bla bal"
                $ adam_third_asked = True
                me "Tell me about Mary."
                adam "Mary? I mean I barely know her."
                adam "I met her only a couple of times."
                adam "I know that she struggles financially."
                adam "Never read her novels though. I don't know if she deserves more."
            "Tell me about Nathaniel" if not adam_fourth_asked:
                $ adam_fourth_asked = True
                me "Tell me about Nathaniel."
                adam "Yeah, him..."
                adam "Hate that guy, he tried to buy out my father's bakery."
                adam "They say he's a great businessman."
                adam "I mean, sure, but he could be a little bit more compassionate you know?"
            "Tell me about Randy" if not adam_fifth_asked:
                $ adam_fifth_asked = True
                me "Tell me about Randy."
                adam "Oh, the 'prodigy'?"
                adam "Yeah, he's a great pianist and all..."
                adam "But he sounds a bit pretentious, don't like him."

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
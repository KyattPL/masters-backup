label interrogate_choice:
    me "Who should I talk to?"

    jump choose_character

label interrogate_loop:
    scene inthallway2 night2
    with fade

    if was_adam_questioned and was_florian_questioned and was_mary_questioned and was_nathaniel_questioned and was_randy_questioned:
        jump final_choice

    me "Hmm..."
    me "Okay, who's next?"

    jump choose_character

label choose_character:
    scene inthallway2 night2
    with fade

    menu choose_char_menu:
        "Talk to Adam" if not was_adam_questioned:
            $ was_adam_questioned = True
            jump talk_to_adam
        "Talk to Florian" if not was_florian_questioned:
            $ was_florian_questioned = True
            jump talk_to_florian
        "Talk to Mary" if not was_mary_questioned:
            $ was_mary_questioned = True
            jump talk_to_mary
        "Talk to Nathaniel" if not was_nathaniel_questioned:
            $ was_nathaniel_questioned = True
            jump talk_to_nathaniel
        "Talk to Randy" if not was_randy_questioned:
            $ was_randy_questioned = True
            jump talk_to_randy

    jump final_choice
label interrogate_choice:
    me "Who should I talk to?"

    jump choose_character

label interrogate_loop:
    me "Hmm..."
    me "Okay, who's next?"

    jump choose_character

label choose_character:
    scene basement1
    menu:
        "Talk to Adam":
            jump talk_to_adam
        "Talk to Florian":
            jump talk_to_florian
        "Talk to Mary":
            jump talk_to_mary
        "Talk to Nathaniel":
            jump talk_to_nathaniel
        "Talk to Randy":
            jump talk_to_randy
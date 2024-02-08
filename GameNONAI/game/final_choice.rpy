default chosen_murderer = ""

label final_choice:
    scene inthallway2 night2
    with fade

    me "So who's the killer?"

    menu:
        "Adam":
            $ chosen_murderer = "Adam"
        "Florian":
            $ chosen_murderer = "Florian"
        "Mary":
            $ chosen_murderer = "Mary"
        "Nathaniel":
            $ chosen_murderer = "Nathaniel"
        "Randy":
            $ chosen_murderer = "Randy"
        "Sylvia":
            $ chosen_murderer = "Sylvia"

label reveal_murderer:
    scene inthallway2 night2
    with fade

    me "I know who did it!"
    me "..."
    me "It was [chosen_murderer]!"

    if chosen_murderer == "Adam":
        show adam serioustalksweatlarge
        with dissolve

        adam "BUT IT WASN'T MEEEE!"
        adam "YOU'VE MADE A MISTAKE."
        
        hide adam
        with dissolve
    if chosen_murderer == "Florian":
        show florian worriedtalk
        with dissolve

        adam "BUT IT WASN'T MEEEE!"
        adam "YOU'VE MADE A MISTAKE."
        
        hide florian
        with dissolve
    if chosen_murderer == "Mary":
        show mary shock
        with dissolve

        adam "BUT IT WASN'T MEEEE!"
        adam "YOU'VE MADE A MISTAKE."
        
        hide mary
        with dissolve
    if chosen_murderer == "Nathaniel":
        show nathaniel worriedtalk
        with dissolve

        adam "BUT IT WASN'T MEEEE!"
        adam "YOU'VE MADE A MISTAKE."
        
        hide nathaniel
        with dissolve
    if chosen_murderer == "Randy":
        show randy worriedtalk
        with dissolve

        adam "BUT IT WASN'T MEEEE!"
        adam "YOU'VE MADE A MISTAKE."
        
        hide randy
        with dissolve
    if chosen_murderer == "Sylvia":
        me "She commited a suicide!"
        me "She was desperate and had no will to live!"
    
    if chosen_murderer != "Randy":
        scene dark
        with fade

        me "Oops..."
        me "I think I screwed up..."

        jump bad_end
    else:
        scene dark
        with fade

        me "No... It can't be..."
        me "I'm sure of it!"

        jump good_end
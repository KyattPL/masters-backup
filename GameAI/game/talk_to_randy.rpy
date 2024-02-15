default randy_first_asked = False
default randy_second_asked = False
default randy_third_asked = False
default randy_fourth_asked = False
default randy_fifth_asked = False

label talk_to_randy:
    scene mkitchen night
    with fade

    show randy worried
    with dissolve

    randy "So... what do you want to know?"

    while not (randy_first_asked and randy_second_asked and randy_third_asked and randy_fourth_asked and randy_fifth_asked):
        menu:
            "Tell me about yourself" if not randy_first_asked:
                $ randy_first_asked = True
                me "Tell me a bit about yourself. What did you see tonight?"
                randy "I'm mostly known for my piano skills."
                randy "I started playing piano when I was 4 years old."
                randy "By the time I was 18, I've won many competitions and performed at many venues."
                randy "Yes I had my problems with the law in the past... I had to learn how to deal wtih success."
                randy "I was smoking cigarettes outside during the night. Don't know about the specific time."
            "Tell me about Adam" if not randy_second_asked:
                $ randy_second_asked = True
                me "Tell me about Adam."
                randy "That bastard? He must be crazy."
                randy "The environment in which he grew up was not great."
                randy "I'm pretty sure I saw him looking at Sylvia in a weird way."
                randy "Who knows what he could do to her?"
            "Tell me about Florian" if not randy_third_asked:
                $ randy_third_asked = True
                me "Tell me about Florian."
                randy "Florian is obviously the most suspicious of the suspects."
                randy "I mean everyone knows that he tried to impress Sylvia."
                randy "I'm pretty sure Sylvia wasn't interested, if you know what I mean..."
            "Tell me about Mary" if not randy_fourth_asked:
                $ randy_fourth_asked = True
                me "Tell me about Mary."
                randy "She is where she deserves to be, to be perfectly honest."
                randy "Her novels are trash to say the least."
                randy "I'm sure she could use some real life inspiration."
            "Tell me about Nathaniel" if not randy_fifth_asked:
                $ randy_fifth_asked = True
                me "Tell me about Nathaniel."
                randy "That's the guy I like."
                randy "Yes he is harsh, so what? That's the way you do it."
                randy "I like his stubbornness. It doesn't make him a bad person though."

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
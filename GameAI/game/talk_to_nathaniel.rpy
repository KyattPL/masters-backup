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
                nathaniel "I've grown up in a poor famildy. I had to fight for myself and my siblings."
                nathaniel "I started my own business, selling anything I could."
                nathaniel "I've worked hard and overcome all kinds of difficulties."
                nathaniel "It's the world that made me tough..."
                nathaniel "I was in the kitchen during the night"
                nathaniel "I think I saw Randy smoking cigarettes outside, not sure what time was at that moment."
            "Tell me about Adam" if not nathaniel_second_asked:
                $ nathaniel_second_asked = True
                me "Tell me about Adam."
                nathaniel "Listen, I like him... I really do."
                nathaniel "Many will tell you that I'm evil because I want to buy his father's bakery."
                nathaniel "I'm offering a lot of money, and for now he has rejected the offer."
                nathaniel "I'm not forcing anyone to do anything for me. It's only business."
            "Tell me about Florian" if not nathaniel_third_asked:
                $ nathaniel_third_asked = True
                me "Tell me about Florian."
                nathaniel "Everyone acts like he's a good guy. I'm not sure why."
                nathaniel "To me he seems a bit arrogant and... manipulative."
                nathaniel "Just think about, he gets anything he wants..."
                nathaniel "What if he can't get it?"
            "Tell me about Mary" if not nathaniel_fourth_asked:
                $ nathaniel_fourth_asked = True
                me "Tell me about Mary."
                nathaniel "Yeah, I know she's not doing great."
                nathaniel "I've tried to connect her with book publishers many times before."
                nathaniel "To me, she could be desperate enough to kill... but what do I know."
            "Tell me about Randy" if not nathaniel_fifth_asked:
                $ nathaniel_fifth_asked = True
                me "Tell me about Randy."
                nathaniel "I like Randy. I think he's a genius."
                nathaniel "I know that he had his problems with the law..."
                nathaniel "But after the jail time, he became a better person."
                nathaniel "I'd like to believe that he is at least."

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
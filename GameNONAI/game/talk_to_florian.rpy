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
                florian "I come from a rich family, my father is a prominent lawyer."
                florian "He basically guaranteed the best schools for my education."
                florian "But it's not like I bought my degree. I've studied hard to be respected."
                florian "I've visited many countries and traveled to many places."
                florian "I wanted to settle down and try my luck with Sylvia."
                florian "I really liked her... And to think that I was sleeping when this happened..."
            "Tell me about Adam" if not florian_second_asked:
                $ florian_second_asked = True
                me "Tell me about Adam."
                florian "Oh yeah, he's a great guy"
                florian "We attented the same high school, I think."
                florian "I know that his family is poorer, but it doesn't make any difference to me."
            "Tell me about Mary" if not florian_third_asked:
                $ florian_third_asked = True
                me "Tell me about Mary."
                florian "Mary is... was Sylvia's best friend."
                florian "She was getting some inspiration for her novels from Sylvia, that's what I've heard."
                florian "I know that she's not doing great now..."
                florian "But one good novel could save her a lot of trouble."
            "Tell me about Nathaniel" if not florian_fourth_asked:
                $ florian_fourth_asked = True
                me "Tell me about Nathaniel."
                florian "Oh, him..."
                florian "I respect the work, but I'm not going to praise his methods."
                florian "He seems a bit cold and profit focused."
                florian "Apparently he has threatened Sylvia once... Not sure if that's true."
            "Tell me about Randy" if not florian_fifth_asked:
                $ florian_fifth_asked = True
                me "Tell me about Randy."
                florian "Yeah, I like his work. He's a great musician."
                florian "Some say he had some... problems with the law in the past."
                florian "Personally, I don't know anything about that."

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
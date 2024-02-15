default mary_first_asked = False
default mary_second_asked = False
default mary_third_asked = False
default mary_fourth_asked = False
default mary_fifth_asked = False

label talk_to_mary:
    scene interior entrance night
    with fade

    show mary shock
    with dissolve

    mary "So... what do you want to know?"

    while not (mary_first_asked and mary_second_asked and mary_third_asked and mary_fourth_asked and mary_fifth_asked):
        menu:
            "Tell me about yourself" if not mary_first_asked:
                $ mary_first_asked = True
                me "Tell me a bit about yourself. What did you see tonight?"
                mary "Well I write the best crime novels in this country."
                mary "It's sad that greatness is not appreciated enough nowadays."
                mary "Sylvia was my best friend, we discussed plots of my books together."
                mary "I'm so sorry that happened... I would've never wished for this to happen."
                mary "I was in the bathroom when I heard scream... It could've been Sylvia."
                mary "I didn't see anything."
            "Tell me about Adam" if not mary_second_asked:
                $ mary_second_asked = True
                me "Tell me about Adam."
                mary "Who? Oh this poor kid..."
                mary "Sorry, I barely know him."
                mary "Seems cute though."
            "Tell me about Florian" if not mary_third_asked:
                $ mary_third_asked = True
                me "Tell me about Florian."
                mary "Ahh, the 'Mr. Perfect'..."
                mary "Well, what can I say, he's quite charming."
                mary "I could see that he was trying to impress Sylvia a lot."
                mary "She even confessed to me once that she felt 'stalked' by him."
            "Tell me about Nathaniel" if not mary_fourth_asked:
                $ mary_fourth_asked = True
                me "Tell me about Nathaniel."
                mary "He's a great guy. I'm in good terms with him."
                mary "You can ask him for help anytime."
                mary "I'm not saying he'd do anything for free, but..."
                mary "He seems harsh but in my mind, he wouldn't hurt anyone."
            "Tell me about Randy" if not mary_fifth_asked:
                $ mary_fifth_asked = True
                me "Tell me about Randy."
                mary "Hahaha..."
                mary "Yeah, maybe he can play piano..."
                mary "But he's a shady character, I'll tell you that much."
                mary "As with many 'artists', he had his time with drugs."
                mary "Oh did I mention, he has assaulted a woman?"
                mary "Yeah... people can change they say, I'm not convinced."

    "Hmm... I guess I'm done with her"
    jump interrogate_loop
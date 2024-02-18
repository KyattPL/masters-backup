label talk_to_florian:
    scene backyard night1
    with fade

    show florian worried
    with dissolve

    florian "So... what do you want to know?"

    $ current_question = 1
    $ sessId = None

    while current_question <= 5:
        python:
            question = renpy.input(f"Remaining questions: {6 - current_question}", length=64)
            question = question.strip()

            if sessId is None:
                resp = query_inworld_api("florian", question, protagonist_name)
            else:
                resp = query_inworld_api("florian", question, protagonist_name, sessId)

        if sessId == None:
            $ sessId = resp['sessionId']
        
        $ current_question += 1
        me "[question]"
        while resp['textList']:
            florian "[resp['textList'][0]]"
            $ resp['textList'].pop(0)

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
default current_question = 1
default sessId = None

label talk_to_adam:
    scene bedroom02 night
    with fade

    show adam serioustalksweat
    with dissolve

    adam "So... what do you want to know?"

    while current_question <= 5:
        python:
            question = renpy.input("What do you want to know?", length=64)
            question = question.strip()
        
            resp = query_inworld_api("adam", question, protagonist_name)

        if sessId == None:
            $ sessId = resp['sessionId']
        
        $ current_question += 1
        me "[question]"
        while resp['textList']:
            adam "[resp['textList'][0]]"
            $ resp['textList'].pop(0)

    "Hmm... I guess I'm done with him"
    jump interrogate_loop
label talk_to_randy:
    scene mkitchen night
    with fade

    show randy worried
    with dissolve

    randy "So... what do you want to know?"

    $ current_question = 1
    $ sessId = None

    while current_question <= 10:
        python:
            prompt = "Remaining questions: {}.\nEx. questions: 'Where were you?', 'What do you know about X?'\nType 'exit' to quit.".format(
                11 - current_question)
            question = renpy.input(prompt, length=64)
            question = question.strip()

            if question.lower() == "exit":
                renpy.say(me, "Alright, let's end this conversation.")
                renpy.jump("interrogate_loop")

            if sessId is None:
                resp = query_inworld_api("randy", question, protagonist_name)
            else:
                resp = query_inworld_api(
                    "randy", question, protagonist_name, sessId)

        if sessId == None:
            $ sessId = resp['sessionId']

        $ current_question += 1
        me "[question]"
        while resp['textList']:
            randy "[resp['textList'][0]]"
            $ resp['textList'].pop(0)

    "Hmm... I guess I'm done with him"
    jump interrogate_loop

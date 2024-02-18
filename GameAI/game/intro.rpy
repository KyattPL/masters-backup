init python:
    def load_dotenv():
        """Load key-value pairs from a .env file and set them as environment variables."""
        from sys import platform
        import os

        if platform == "linux" or platform == "linux2":
            with open('/home/kyatt/Desktop/uczelnia/magisterskie/masters-backup/GameAI/game/.env') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=',  1)
                        os.environ[key] = value
        else:
            with open('F:\\uczelnia\\magister\\PRACA DYPLOMOWA\\GameAI\\game\\.env') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=',  1)
                        os.environ[key] = value

    load_dotenv()

    def query_inworld_api(char, prompt, protagonist="John", sessionId=None):
        import requests
        import os
        from requests.auth import HTTPBasicAuth

        BASE_URL = 'https://api.inworld.ai/studio/v1'
        WORKSPACE_ID = os.getenv('WORK_ID')
        STUDIO_API_KEY = os.getenv('STUDIO_KEY')
        STUDIO_API_SECRET = os.getenv('STUDIO_SECRET')
        AUTH_TOKEN = os.getenv('AUTH_TOKEN')

        url = f'https://studio.inworld.ai/v1/workspaces/{WORKSPACE_ID}/characters/{char}:simpleSendText'
        headers = {"Content-Type": "application/json", "authorization": f"Basic {AUTH_TOKEN}=="}
        myobj = {"character": f"workspaces/{WORKSPACE_ID}/characters/{char}", "text": f"{prompt}", "endUserFullname": f"{protagonist}", "endUserId":"12345"}

        if sessionId is not None:
            myobj['sessionId'] = sessionId

        x = requests.post(url, json=myobj, headers=headers).json()
        
        #x['textList']
        #x['sessionId']

        return x

label intro:
    python:
        inputPrompt = renpy.input("What is your name?: ", length=30)
        inputPrompt = inputPrompt.strip()

        protagonist_name = inputPrompt
    
    scene mansion front evening
    with fade

    "After a long day of driving through the winding roads, I finally reached the villa. It was a majestic building, surrounded by a lush garden and a high fence. I parked my car and grabbed my suitcase, feeling a mix of excitement and nervousness."
    "I was a bit too late to the party. Sylvia had invited me to her villa for a \"mysterious night\" party, along with some of her other friends. She said it would be a fun and thrilling experience, with puzzles, clues, and surprises. I wondered what she had planned for us."
    "I rang the doorbell and waited for someone to answer. I hoped that Sylvia wouldn't be mad at me for being late."

    scene interior entrance evening
    with fade

    show adam smile
    with dissolve
    adam "Hi! You finally arrived. What took you so long?"
    me "Hi! Sorry, I was a bit lost..."
    adam "No worries, others are already here. I'll bring them here."
    me "Okay, thanks."
    hide adam

    show florian smile
    with dissolve
    florian "Hi! Great to see you."
    me "Great to see you too!"
    me "Do you know what the plans are for today?"
    florian "No clue, I'm still waiting to see Sylvia. Hope she's alright."
    me "Oh, so she's not here?"
    florian "Apparently she had to pick something up from a store."
    hide florian

    show mary smile
    with dissolve
    mary "Good evening! What bring you here young man?"
    me "I... I was invited by Sylvia to the party?"
    mary "Oh, is that so?"
    mary "Well in that case, I welcome you to the 'night of mysteries' party."
    mary "If you ever think something is not as it should..."
    mary "Well, you're probably correct then!"
    mary "Tell me, have you read my recent murder novel?"
    me "Sorry, I didn't have a lot of free time recently."
    hide mary

    show nathaniel smile
    with dissolve
    nathaniel "Enough with that Mary. Hi!"
    me "Hey Nathaniel."
    nathaniel "If you ever need a loan, just call me."
    me "Thanks?"
    hide nathaniel

    show randy smile
    with dissolve
    randy "You! Yes you!"
    me "?"
    randy "Who's your favourite composer?"
    me "I don't know? Chopin?"
    randy "*sigh*"
    randy "Fine, you don't know what you're really missing."
    randy "Afterall, only the true artist can appreciate Mozart!"
    randy "I might give you a ticket to my concert in the future. You'll find out."
    me "Thanks, I guess."
    hide randy

    show florian smile
    with dissolve
    florian "Okay guys, I just got the info that Sylvia will arrive really late."
    florian "For now we can go take a quick nap or whatever you guys want."
    me "Sure, thanks."
    hide florian

    "Hmm..."
    "I do feel a bit tired."
    "I guess I'll go to bed for now."

    jump murder
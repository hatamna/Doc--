import os
from google import genai
from dotenv import load_dotenv


#DONT TOUCH THIS
load_dotenv()
client = genai.Client()

"""
def completer(prompt):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)"""


def completer(prompt):
    Nchat=client.chats.create(model="gemini-2.5-flash")
    res= Nchat.send_message(prompt) 
    return res.text


if __name__ == "__main__":
    test = completer("Say hello")
    print(test)
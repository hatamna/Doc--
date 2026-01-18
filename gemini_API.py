import os
from google import genai
from dotenv import load_dotenv, find_dotenv

#DONT TOUCH THIS
load_dotenv()
client = genai.Client()


response=client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=""
)

def senFin():
    Nchat=client.chats.create(model="gemini-2.5-flash")
    while True:
        msg = input("")
        if msg=="stop":
            break

        res= Nchat.send_message(msg) 
        print(res.text)

senFin()

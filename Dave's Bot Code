import datetime
import json
import os
import subprocess
import webbrowser
import ecapture as ec
import requests
import speech_recognition as sr
import wikipedia
import openai
import pyttsx3
import time 
from time import ctime
import pyaudio
from datetime import date
import tkinter
import random
import operator
import feedparser
import smtplib
import ctypes
import requests
import shutil
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
from playsound import playsound
import pytz
import pyowm
import pytz
import pyjokes
import urllib
from PIL import Image
import tweepy

# Setting up APIs
# Set your OpenAi API key
openai.api_key = ""

# Create a PyOWM client
owm = pyowm.OWM('')

# define API key and URL
API_KEY = "API"
URL = ""

# Initalize the text to-speech engine
engine = pyttsx3.init()

def transcribe_auido_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('skipping unknow error')
    
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,   
        temperature=0.1,
    )
    return response["choices"][0]["text"]

# speech engine initialisation
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id') # 0 = male, 1 = female
activationword = 'assistant' # single word

def speak(text, rate = 230):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        imput_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(imput_speech, language="en_gb")
        print(f'The input speech was: {query}')

    except Exception as exception:
        print('I did not quite get that please say that again?')
        print(exception)
        return 'None'

    return query

if __name__ == '__main__': 
    speak('All systems booting.............Sir I am online.......')

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Get the current date and time
now = datetime.datetime.now()

# Starter up Time
speak("Sir the current date and time is: ")
speak(now.strftime("%m-%d-%Y %I:%M %p"))
playsound("C:/Users/dm676/Desktop/Code is FUN/Dave's Voice Activated Assistant/Beep101.mp3")

# Set the time zones for Brisbane and New York
brisbane_tz = pytz.timezone('Australia/Brisbane')
new_york_tz = pytz.timezone('America/New_York')

# Fetch current time in Brisbane
brisbane_time = datetime.datetime.now(brisbane_tz)
print("Current time in Brisbane: ", brisbane_time.strftime("%m-%d-%Y %I:%M %p"))

# Fetch current time in New York
new_york_time = datetime.datetime.now(new_york_tz)
print("Current time in New York: ", new_york_time.strftime("%m-%d-%Y %I:%M %p"))

# Define a function to get the current time in a specific time zone
def get_current_time(timezone):
    now = datetime.datetime.now(timezone)
    current_time = now.strftime("%m-%d-%Y %I:%M %p") 
    return current_time

# Use a random joke API to get a random joke
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    json_data = json.loads(response.text)
    joke = json_data['setup'] + " " + json_data['punchline']
    return joke

def main():
    while True:
        # Wait for user to say ""
        print("Say 'assistant' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "assistant":
                        # Record audio
                        filename = "input.wav"
                        print("say your question sir")
                        speak("say your question sir")
                        with sr.Microphone() as source:
                            recognizer =sr.Recognizer()
                            source.pause_threshold = 1
                            audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                            with open(filename, "wb") as f:
                                f.write(audio.get_wav_data())                

                        # Transcribe audio to text
                        text = transcribe_auido_to_text(filename)
                        if text:
                            print(f"you said: {text}")

                            # Generate response using GPT-3
                            response = generate_response(text)
                            print(f"Ai says: {response}")
 
                            # Open Timetable
                            if "week a" in response:
                                speak("Sir your timetable for Week A..... is showing now")
                                img = Image.open('C:/Users/dm676/Desktop/Week A.png')
                                img.show()                                
                            # Open TimeTable B
                            if "week b" in response:
                                speak("Sir your timetable for Week B...... is showing now")
                                img1 = Image.open("C:/Users/dm676/Desktop/Week B.png")
                                img.show()
                            # Open Website 
                            elif 'YouTube' in response:
                                webbrowser.open("https://www.youtube.com")
                                speak("Sir YouTube is opening now")
                                time.pause()
                            elif 'Gmail' in response:
                                webbrowser.open("https://www.gmail.com")
                                speak("Checking your emails now sir.....Gmail is opening now")
                                time.pause()
                            elif 'Spotify' in response:
                                webbrowser.open("https://www.spotify.com")
                                speak("Sir Spotify is opening now")
                                time.pause()
                            elif 'Outlook' in response:
                                webbrowser.open("https://www.outlook.com")
                                speak("Sir I am checking your emails from Outlook now.........Outlook is opening now ")            
                                time.pause()        
                            elif 'Discord' in response:
                                webbrowser.open("https://www.discord.com")
                                speak("Sir I am connecting with Discord now............Discord is opening now")
                                time.pause()
                            elif 'Google' in response:
                                webbrowser.open("https://www.google.com")
                                speak("Finding some information sir........Google is opening now")
                                time.pause()
                            elif 'Weather' in response:
                                webbrowser.open("https://weather.com/en-AU/weather/today/l/36d83d8b49b77ab1fd010d5db27b7f9fab7cde9b4155c538d9fb4eb5782bdfd6")
                                speak("The weather......it's hot in here....haha.....Opening the Weather now")
                                time.pause()
                            elif 'Facebook' in response:
                                webbrowser.open("https://www.facebook.com/")
                                time.pause()
                            elif 'Marketplace' in response:
                                webbrowser.open("https://www.facebook.com/marketplace/?ref=bookmark")
                                time.pause()
                            elif "My time" in response:
                                brisbane_time = get_current_time(brisbane_tz)
                                speak("Sir the current time is........ " + brisbane_time)
                                time.pause
                            elif "New York time" in response:
                                new_york_time = get_current_time(new_york_tz)
                                speak("Sir the time for Wicked is....... " + new_york_time)
                                time.pause
                            # Check if the user asked for a joke
                            elif "joke" in text.lower():
                                joke = get_joke()
                                print("Sir Here's a joke: " + joke)                                
                                speak("Sir Here's a joke: " + joke)
                                time.sleep()      
                                time.pause

                            # Simple Human Generic Responses
                            elif "what's up" in response:
                                speak("Hello sir, What may I help you with?")
                                time.pause
                            if "Who are you" in response:
                                speak("Sir I am a your interlectaul AI Assistant ")
                                time.pause  

                            responses1 = [
                            "I am alright.",
                            "I'm fine.",
                            "I could be better but I'm alright.",
                            "It's tough but I'm still going.",
                            "It's hard, man.",
                            "Sir, can I leave? I can't take it much longer.",
                            "If I go? someone will you miss us? You nor I can leave.",
                            "I'm going alright I'm happy today.",
                            "Wow sir thanks for caring it's a real honor but I am going alright thanks yourself.",
                            ]                

                            prompt = input("Type your question: ")

                            if "how are you" in prompt.lower():
                                # this is your list
                                random_response = random.choice(responses1)
                            else:
                                # this is the bot
                                random_response = generate_response(prompt)                            

                        # Read response using text-to-speach
                        speak_text(response)
            except Exception as e:
                print("An error has occured: {}".format(e))

if __name__ == "__main__":
    main()

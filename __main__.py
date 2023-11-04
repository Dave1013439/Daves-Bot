# import openai
# import chatbot
import time, speech_recognition as sr, datetime, json, os, subprocess, webbrowser, ecapture as ec, pyttsx3, pyaudio, random, operator, feedparser, smtplib, ctypes, requests, shutil, threading
from time import ctime, sleep
import pyaudio
from datetime import date
# import tkinter
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
from playsound import playsound
# import pyowm
# import pyjokes
# import urllib
from PIL import Image
# import tweepy
# import pytz
from gtts import gTTS
# import discord
# import wikipedia
if os.name == "nt":
    import win32api
    from win32con import VK_MEDIA_PLAY_PAUSE, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, KEYEVENTF_EXTENDEDKEY

from pydub import AudioSegment
from pydub.playback import play

# Get the current date and time
now = datetime.datetime.now()

INITIAL_STATE = 0
AFTER_HOW_ARE_YOU = 1

current_state = INITIAL_STATE

# Get a random joke
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    json_data = json.loads(response.text)
    joke = json_data['setup'] + " " + json_data['punchline']
    return joke
# Open website
def open_website():
    website_url = "https://www.example.com"  # Replace with the URL you want to open
    webbrowser.open(website_url)
    print(f"Opening website: {website_url}")

def handle_user_input(user_input):
    global current_state
    if current_state == AFTER_HOW_ARE_YOU:
        # Check if the user's response contains "good," "alright," "fine," or "tired"
        if any(word in user_input for word in ["good", "alright", "fine", "tired"]):
            response = "That's good to hear, keep going sir."
            pyttsx3.speak(response)
            current_state = INITIAL_STATE
        else:
            print("User response not recognized. Please respond with 'good,' 'alright,' 'fine,' or 'tired'.")

# Starter up Time
pyttsx3.speak("Sir the current date and time is: ")
pyttsx3.speak(now.strftime("%m-%d-%Y %I:%M %p"))

def main():
    while True:
        try:
            # Listen for 60 seconds
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=60)  
                print("Processing...")
                
            # Recognize speech using Google Web Speech API
            command = r.recognize_google(audio).lower()
            print(f"Recognized: {command}")

            if "assistant" in command:
                handle_assistant_command()
            else:
                pyttsx3.speak("Sorry sir I could not understand you.......... Please try again")
            
        except sr.WaitTimeoutError:
            print("Sir I have not been used in 60 sec, I am shutting down now.")
            pyttsx3.speak("Sir I have not been used in 60 seconds, I am shutting down now.")
            time.sleep(1)
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")

def assistant_sound():
    sound_file = os.path.join(os.getcwd().replace("\\", "/"), "sounds/assistant_activated.mp3")
    playsound(sound_file)


def handle_assistant_command():
    r = sr.Recognizer()  # Initialize Recognizer here
    active_sound = threading.Thread(target=assistant_sound)
    active_sound.start()
    print("Assistant started. You have 1 minute to respond.")

    start_time = time.time()

    while time.time() - start_time < 60:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=60)
                
            command = r.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            command1 = r.recognize_google(audio).lower()

            if "orange powder" in command1:
                pyttsx3.speak("orange powder recognized")
# Will need
            if '80s playlist' in command1:
                webbrowser.open("https://open.spotify.com/playlist/1V4f7gzXjnHpSlR78q1Zpb?si=fcfbbbaa7d884c2a")
                pyttsx3.speak("80s playlist is playing now")
            if 'music playlist' in command1:
                webbrowser.open("https://open.spotify.com/playlist/5XZsfidCnnAZUaMznHN0Al?si=37cb71a5ddf54838")
                pyttsx3.speak("Sir your music playlist is playing now")
            if 'family friendly playlist' in command1:
                webbrowser.open("https://open.spotify.com/playlist/7mHRDFTl5YMNeorVfcYA1u?si=b35bb9b2c1d24f89")
                pyttsx3.speak("family friendly playlist is playing now")
            # Media Control Commands (Windows Only)
            if os.name == "nt":
                if 'play' in command1 or 'pause' in command1:
                    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
                    print("playing/pausing")
                if 'next' in command1 or 'skip' in command1:
                    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                    print("skipping")
                if 'previous' in command1 or 'go back' in command1:
                    print("going back")
                    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                    time.sleep(0.5)
                    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                if 'repeat' in command1:
                    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                    print("repeating")
            else: print("Feature only avalable on Windows")
# Would I also need the JOke API because BARD???
            # Check if the user asked for a joke
            if 'joke' in command:
                joke = get_joke()
                print("Sir Here's a joke: " + joke)                                
                pyttsx3.speak("Sir Here's a joke: " + joke)
                time.sleep(3)      

# NOT GOING TO USE BECAUSE BARD WILL DO IT FOR ME

            if "who are you" in command:
                pyttsx3.speak("Sir I am a your intellectual AI Assistant ")    
            if "how are you" in command:
                # this is your list
                responses1 = [
                "I am alright.",
                "I'm fine ..... thankyou for asking",
                "I could be better ......... but I'm alright.",
                "It's tough......... but I'm still going........ yay me.",
                "It's hard, mannn.",
                "Sir......can I leave?........I can't take it much longer.",
                "I'm feeling pretty good, thanks. How's your day shaping up?",
                "I'm going alright......... I'm happy today......... How are you",
                "Wow sir ...........thanks for caring.......... it's a real honor......... but I am going alright thanks ....yourself.",
                "I'm doing great, thanks! How about you?",
                "I'm good, just keeping busy. How are things with you?",
                "I'm feeling fantastic today! How's your day going?",
                "I'm doing well, thanks for asking. How's everything on your end?",
                "I'm pretty good, all things considered. How about yourself?",
                "I'm feeling quite positive today. How's your day been so far?",
                "I'm doing alright. How's life treating you these days?",
                "I'm hanging in there, thanks for asking. How about you?",
                "I'm not too bad, just taking it one step at a time. How are you doing?",
                "I'm okay, thanks for checking in. How's everything in your world?",
                ]     
                response = random.choice(responses1)
                pyttsx3.speak(response)
# REST WILL DO
           # Note taker

           # reminder

           # Discord Functions

        except sr.WaitTimeoutError:
            print("Sir I am locked. Say 'assistant' to unlock.")
            pyttsx3.speak("Sir I am locked. Say 'assistant' to unlock.")
            return
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        return None
    print()

if __name__ == "__main__":
    r = sr.Recognizer() 
    main()


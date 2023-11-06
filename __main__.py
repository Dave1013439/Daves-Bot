# import openai
# import chatbot
import time, speech_recognition as sr, datetime, json, os, subprocess, webbrowser, ecapture as ec, pyttsx3, pyaudio, random, operator, feedparser, smtplib, ctypes, requests, shutil, threading, pyautogui as pag, wikipedia
from time import ctime, sleep
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
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
# from PIL import Image
# import tweepy
# import pytz
from gtts import gTTS
# import discord
# import wikipedia
if os.name == "nt":
    import win32api
    from win32con import VK_MEDIA_PLAY_PAUSE, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, KEYEVENTF_EXTENDEDKEY, VK_VOLUME_DOWN, VK_VOLUME_UP, VK_VOLUME_MUTE
import module

# Get the current date and time
now = datetime.datetime.now()
user_home = os.path.expanduser("~")

INITIAL_STATE = 0
AFTER_HOW_ARE_YOU = 1

current_state = INITIAL_STATE

def googleTTS(text: str):
    tts = gTTS(text)
    tts.save("temp.mp3")
    playsound("temp.mp3")

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
# pyttsx3.speak("Sir the current date and time is: ")
# pyttsx3.speak(now.strftime("%m-%d-%Y %I:%M %p"))

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
                None
            
        except sr.WaitTimeoutError:
            print("Sir I have not been used in 60 sec, I am shutting down now.")
            # pyttsx3.speak("Sir I have not been used in 60 seconds, I am shutting down now.")
            time.sleep(1)
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")

def assistant_sound():
    try:
        sound_file = os.path.join(os.getcwd().replace("\\", "/"), "sounds/assistant_activated.mp3")
        playsound(sound_file)
        return True
    except: print("Error playing Sound Effect")


def handle_assistant_command():
    r = sr.Recognizer()  # Initialize Recognizer here
    active_sound = threading.Thread(target=assistant_sound)
    active_sound.start()
    print("Assistant started. You have one minute until timeout.")

    start_time = time.time()

    while 1 == 1: # time.time() - start_time < 60:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=60)
                
            command = command1 = r.recognize_google(audio).lower()
            commandl = command.split()
            print(f"Recognized: {command}")

            if "orange powder" in command1:
                pyttsx3.speak("orange powder recognized")

            if command1.startswith("write "):
                pag.typewrite(command1.lstrip("write "))

            if "dictate" in command1:
                print("Entering dictation mode")
                while 1:
                    try:
                        with sr.Microphone() as source:
                            d = r.recognize_google(r.listen(source, timeout=60))
                            print(d)
                        if d.lower().startswith("exit dictation"):
                            break
                        elif d.lower().startswith("new line") or d.startswith("next line"):
                            pag.write("\n")
                        elif d.lower().startswith("insert definition for"):
                            final = ""
                            q = d.split()
                            for item in range(2, len(q)):
                                final = f"{final} {q[item]}"
                            definition = wikipedia.summary(final, sentences=2)
                            print(f"Inserting: \n {definition}")
                            pag.write(definition)
                        elif d.lower().startswith("select"):
                            if "all" in d.lower():
                                pag.hotkey('ctrl', 'a')
                            #elif "left" in d.lower():
                            #    # pag.hotkey('ctrl', 'shift', 'left')
                            #    pag.keyDown('crtl')
                            #    pag.keyDown('shift')
                            #    time.sleep(0.05)
                            #    pag.press('left')
                            #    time.sleep(0.05)
                            #    pag.keyUp('crtl')
                            #    pag.keyUp('shift')
                            #elif "right" in d.lower():
                            #    # pag.hotkey('ctrl', 'shift', 'right')
                            #    pag.keyDown('crtl')
                            #    pag.keyDown('shift')
                            #    time.sleep(0.05)
                            #    pag.press('right')
                            #    time.sleep(0.05)
                            #    pag.keyUp('crtl')
                            #    pag.keyUp('shift')
                        elif d.lower().startswith("move"):
                            if "left" in d.lower():
                                pag.hotkey('crtl', 'left')
                            if "right" in d.lower():
                                pag.hotkey('crtl', 'right')
                        else:
                            print(f"Typing in: {d}") 
                            pag.write(d)
                    except sr.UnknownValueError:
                        print("unrecognized")

            if "mouse" in command1:
                print("Entering mouse mode")
                while 1:
                    try:
                        x, y = pag.position()
                        with sr.Microphone() as source:
                            d = r.recognize_google(r.listen(source, timeout=60))
                        if d.lower().startswith("exit"): break
                        if d.lower().startswith("light"): moveby = 20
                        elif d.lower().startswith("super"): moveby = 200
                        else: moveby = 100

                        if "move" in d:
                            if "up" in d: pag.moveTo(x, y - moveby)
                            elif "left" in d: pag.moveTo(x - moveby, y)
                            elif "down" in d: pag.moveTo(x, y + moveby)
                            elif "right" in d: pag.moveTo(x + moveby, y)
                        elif "drag" in d:
                            if "up" in d: pag.dragTo(x, y - moveby, 1)
                            elif "left" in d: pag.dragTo(x - moveby, y, 1)
                            elif "down" in d: pag.dragTo(x, y + moveby, 1)
                            elif "right" in d: pag.dragTo(x + moveby, y, 1)
                            
                        if "click" in d: pag.click()

                    except sr.UnknownValueError:
                        print("unrecognized")

            if "define" in command1:
                final = ""
                for item in commandl:
                    if item != "define":
                        final = f"{final} {item}"
                definition = wikipedia.summary(final, sentences=3)
                print(definition)
                pyttsx3.speak(definition)

                        

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
                if "volume up" in command1 or "louder" in command1:
                    win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
                if "volume down" in command1 or "quieter" in command1:
                    win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
                if "mute" in command1:
                    win32api.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)
            else: print("Feature only avalable on Windows")
            #if "set volume" in command1:
            #    cmdlist = command1.split()
            #    volume.SetMasterVolume(float(cmdlist[len(cmdlist-1)]) / 100, None)
# Would I also need the JOke API because BARD???
            # Check if the user asked for a joke
            if 'joke' in command:
                joke = get_joke()
                print("Sir Here's a joke: " + joke)                                
                pyttsx3.speak("Sir Here's a joke: " + joke)
                time.sleep(3)  

            if 'run module' in command1:
                module.runModule(commandl[len(commandl) - 1])


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
            # print("Sir I am locked. Say 'assistant' to unlock.")
            # pyttsx3.speak("Sir I am locked. Say 'assistant' to unlock.")
            return
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            pyttsx3.speak("Sorry sir I could not understand you. Please try again.")
            print("Could not understand audio")
        return None
    print()

if __name__ == "__main__":
    r = sr.Recognizer() 
    main()


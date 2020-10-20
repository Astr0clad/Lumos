import subprocess 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
import wolframalpha
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
from googlesearch import search
import main

webbrowser.register('chrome', None, "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def cmds():
    while True: 
            
        query = main.takeCommand().lower() 
        
        # All the commands said by user will be 
        # stored here in 'query' and will be 
        # converted to lower case for easily 
        # recognition of command 

        if "lumos" in query:
            query.replace("lumos", "")

            if 'wikipedia' in query: 
                main.speak('Searching Wikipedia...') 
                query = query.replace("wikipedia", "") 
                results = wikipedia.summary(query, sentences = 3) 
                main.speak("According to Wikipedia") 
                print(results) 
                main.speak(results) 

            elif 'open youtube' in query: 
                main.speak("Here you go to Youtube\n") 
                webbrowser.get('chrome').open("youtube.com") 

            elif 'open google' in query: 
                main.speak("Here you go to Google\n") 
                codePath = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)

            elif 'open discord' in query: 
                main.speak("Here you go to discord\n") 
                codePath = r"C:\\Users\\Colin\\AppData\\Local\\Discord\\Update.exe"
                os.startfile(codePath) 

            elif 'open spotify' in query: 
                main.speak("Here you go to spotify\n") 
                codePath = r"C:\\Users\\Colin\\AppData\\Roaming\\Spotify\\spotify.exe"
                os.startfile(codePath) 

            elif 'open stackoverflow' in query: 
                main.speak("Here you go to Stack Over flow.Happy coding") 
                webbrowser.get('chrome').open("stackoverflow.com") 
            
            elif 'how are you' in query: 
                main.speak("I am fine, Thank you") 
                main.speak("How are you") 

            elif 'fine' in query or "good" in query: 
                main.speak("It's good to know that your fine") 

            elif "change my name to" in query: 
                query = query.replace("change my name to", "") 
                assname = query 
                main.speak('okay')

            elif "change name" in query: 
                main.speak("What would you like to call me") 
                assname = takeCommand() 
                main.speak("Thanks for naming me") 

            elif "what's your name" in query or "What is your name" in query: 
                main.speak("My friends call me") 
                speak(assname) 
                print("My friends call me", assname) 

            elif 'exit' in query: 
                main.speak("Thanks for giving me your time") 
                exit() 

            elif "who made you" in query or "who created you" in query: 
                main.speak("I have been created by Astroclad.") 
                
            elif 'joke' in query: 
                main.speak(pyjokes.get_joke()) 

            elif 'search' in query or 'play' in query: 
                
                query = query.replace("search", "") 
                query = query.replace("play", "")		 
                webbrowser.open(query) 

            elif "who am i" in query: 
                main.speak("If you talk then definately your human.") 

            elif "why you came to world" in query: 
                main.speak("Thanks to Astroclad. further It's a secret") 

            elif 'is love' in query: 
                main.speak("It is 7th sense that destroy all other senses") 

            elif "who are you" in query: 
                main.speak("I am your virtual assistant created by Astroclad") 

            elif 'reason for you' in query: 
                main.speak("I was created as a Minor project by Astroclad") 

            elif 'shutdown system' in query: 
                main.speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                    
            elif 'empty recycle bin' in query: 
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                main.speak("Recycle Bin Emptied") 

            elif "don't listen" in query or "stop listening" in query: 
                main.speak("for how much time you want to stop lumos from listening commands") 
                a = int(takeCommand()) 
                time.sleep(a) 
                print(a) 

            elif "where is" in query: 
                query = query.replace("where is", "") 
                location = query 
                main.speak("User asked to Locate") 
                main.speak(location) 
                webbrowser.open("https://www.google.nl / maps / place/" + location + "") 

            elif "restart" in query: 
                subprocess.call(["shutdown", "/r"]) 
                
            elif "hibernate" in query or "sleep" in query: 
                main.speak("Hibernating") 
                subprocess.call("shutdown / h") 

            elif "log off" in query or "sign out" in query: 
                main.speak("Make sure all the application are closed before sign-out") 
                time.sleep(5) 
                subprocess.call(["shutdown", "/l"]) 

            elif "write a note" in query: 
                main.speak("What should i write") 
                note = takeCommand() 
                file = open('notes.txt', 'w') 
                main.speak("Should i include date and time") 
                snfm = takeCommand() 
                if 'yes' in snfm or 'sure' in snfm: 
                    strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                    file.write(strTime) 
                    file.write(" :- ") 
                    file.write(note) 
                else: 
                    file.write(note) 
            
            elif "show note" in query: 
                main.speak("Showing Notes") 
                file = open("notes.txt", "r") 
                print(file.read()) 
                main.speak(file.read(6)) 

            elif "wikipedia" in query: 
                webbrowser.get('chrome').open("wikipedia.com") 

            elif "Good Morning" in query: 
                main.speak("A warm" +query) 
                main.speak("How are you ") 
                main.speak(assname) 

            # most asked question from google Assistant 
            elif "how are you" in query: 
                main.speak("I'm fine, glad you asked me that")
            
            elif "what is" or "who is" in query:
                main.speak('thinking')
                if "lumos" in query:
                    query.replace("lumos", "")

                client = wolframalpha.Client("UK8JT2-ATP7JRHVYR")
                res = client.query(query)

                try: 
                    print(next(res.results).text)
                    main.speak(next(res.results).text)
                except StopIteration:
                    print("No results")
import subprocess 
import pyttsx3 
import speech_recognition as sr 
import os 
import winshell 
import feedparser 
import smtplib 
import ctypes 
import shutil 
import datetime
from clint.textui import progress 
import commands

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 

assname = "Lumos"
version = "Lumos V 1.0"

def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

def wishMe(): 
	hour = int(datetime.datetime.now().hour) 
	if hour>= 0 and hour<12: 
		speak("Good Morning !") 

	elif hour>= 12 and hour<18: 
		speak("Good Afternoon !") 

	else: 
		speak("Good Evening !") 

	assname =("Lumos") 
	speak("I am your Assistant") 
	speak(assname) 
	

def usrname(): 
	uname = "Colin" 
	speak("Welcome "+uname) 
	columns = shutil.get_terminal_size().columns 
	
	print("#####################".center(columns)) 
	print("Welcome ", uname.center(columns)) 
	print("#####################".center(columns)) 

	print("#####################".center(columns)) 
	print(version.center(columns)) 
	print("#####################".center(columns)) 
	
	speak("How can i Help you") 

def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone(device_index=2) as source: 
		r.adjust_for_ambient_noise(source)

		print("Listening...") 
		r.pause_threshold = 0.5
		audio = r.listen(source) 
	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "None"
	
	return query 

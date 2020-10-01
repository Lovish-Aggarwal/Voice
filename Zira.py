from pyttsx3 import *
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

engine=init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("...Good Morning")

    elif hour>=12 and hour<18:
        speak("...Good Afternoon")
    else:
        speak("...Good ...Evening")
    
    speak("...I am Zira... Sir , How may I Help You.....")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en in')
        print("User Said:",query)


    except Exception as e:
        print(e)
        speak("Sir,Please Say That Again")
        print("Say that again Please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()
    
    #Logic : ASli WAle
        if 'wikipedia' in query:
            speak('..Searching...Wikipedia')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("...Sir...ACcording To ...wikipedia")
            print(results)
            speak(results)
            #ABOVE Code can search any thing Through wikipediya and even read (Deafult as per code 2 Sentences) for you
            
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'Instagram' in query:
            webbrowser.open("Instagram.com")
       
        elif 'Codechef' in query:
            webbrowser.open("Codechef.com")
        
        
        elif 'Github' in query:
            webbrowser.open("github.com")
        
        elif 'Nvidia' in query:
            webbrowser.open("nvidia.com")
        
        elif 'studio' in query:
            os.startfile("C:\\Users\\Cvi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            #Change the Path according to Your System

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the Time is",strtime)

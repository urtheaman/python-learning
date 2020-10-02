import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pyaudio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say That Again Please!")
        speak("Say That Again Please!")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    speak("How May I Assist You?")

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'on google' in query:
            print('Searching Google...')
            speak('Searching Google...')
            query = query.replace('on google', '')
            browser = webdriver.Firefox()
            browser.get("http://www.google.com")
            assert "Google" in browser.title
            search = browser.find_element_by_name("q")
            search.send_keys(query)
            search.send_keys(Keys.RETURN)

        elif 'on amazon' in query:
            print('Searching Amazon...')
            speak('Searching Amazon...')
            query = query.replace('on amazon', '')
            browser = webdriver.Firefox()
            browser.get("http://www.amazon.in")
            assert "Amazon" in browser.title
            search = browser.find_element_by_id("twotabsearchtextbox")
            search.send_keys(query)
            search.send_keys(Keys.RETURN)

        elif 'on youtube' in query:
            print('Searching YouTube...')
            speak('Searching YouTube...')
            query = query.replace('on youtube', '')
            browser = webdriver.Firefox()
            browser.get("http://www.youtube.com")
            assert "YouTube" in browser.title
            search = browser.find_element_by_name("search_query")
            search.send_keys(query)
            search.send_keys(Keys.RETURN)

        elif 'exit' in query:
            print('This Is Jarvis. Shining Off Sir.')
            speak('This Is Jarvis. Shining Off Sir.')
            exit()
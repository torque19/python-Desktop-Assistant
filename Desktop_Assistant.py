import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def time():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")

    else:
        speak("Good Evening! sir")
    speak("This is Brahmastra Created by Tushar Jha")
    speak("Hey This is Password Protected AI. SO, can You tell me the Password for accessing the Brahmastra., Note Down You have only 1 attempt")
    print("I am Brahmastra Created by Tushar Jha, Memory 1 Tera byte, processor 8 , Cool")
    print("Can You tell me the Password for Operating the Brahmastra. , Note Down You have only 3 attempt")

def passw_recognition():
    #It takes microphone  password input from the user and if the password is correct it unlock it.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        password = r.recognize_google(audio, language='en-in') 
        print(f"User said: {password}\n")  
        
    except Exception as e:
        print("Say that again please...")   
        return "None" 
    return password

def task_recognition():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        question = r.recognize_google(audio, language='en-in') 
        print(f"User said: {question}\n")  
        
    except Exception as e:
        print(" can't Recognize Say that again please...")  
        return "None" 
    return question

if __name__=="__main__" :
    time()
    while True:
        password = passw_recognition().lower()
        if password == "abc":
            speak("Thankyou Sir, You can access the Brahamastra")
            print("Thankyou Sir, You can access the Brahamastra")
            speak("sir,which service do you like to get")
            print("sir,which service do you like to get")
            question = task_recognition().lower()
            if "youtube" in question:
                webbrowser.open("youtube.com")
            elif "calculator" in question:
                speak("Ok, I am in Calculator mode, you can perform any calculation")
            elif "Songs" in question:
                speak("Ok, I am in Music mode, Now You can listen song")
                break
            elif "how are you" in question:
                speak("I am good as always")
            else:
                speak("Sorry, Password is wrong, You can't access the brahmastra")
            break
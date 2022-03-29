#----------------------- Bella-The-Voice-Assistant------------------------------------------------------
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Bella, Please tell me How can I help you")

def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("I am Listening........................ ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..........................")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said : {query} \n")

    except Exception as e:
        print("Sorry, Can You say that again Please..............")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smptp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-mail@gmail.com','your-password')
    server.sendmail('your-mail@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\sandh\\PycharmProjects\\Bella-The-Voice-Assistant'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current Time is {strTime}")

        elif 'coding' in query:
            path="C:\\Users\\sandh\\AppData\\Local\\JetBrains\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What Should I Say?")
                content=takeCommand()
                to="dumy@gmail.com"
                sendEmail(to,content)
                speak("Email has been Sent")
            except Exception as e:
                speak("Sorry, I am unable to send this email")

        elif 'exit' in query:
            exit()

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
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you")
def takeCommand():
    # it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('santoshkumarmajhee3001@gmail.com','03072001dynamo')
    server.sendmail('santoshkumarmajhee3001@gmail.com', to,content)
    server.close()

if __name__=="__main__":
    wishMe()   
    while True:
    # if 1:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'How are you' in query:
            speak("I am fine sir")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak("Opening Goole")
            webbrowser.open('google.com')
        elif 'open stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir=""
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath="C:\\Users\\DYNAMO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to dynamo' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="dynamoroy371@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend dynamo bhai. I am not able to send this email")
        elif 'quit' or 'exit' or 'close' in query:
            speak("Alright! good bye")
            exit()

import pyttsx3
import datetime
import speech_recognition as sr
import google_auth_httplib2
import wikipedia
import smtplib
import webbrowser as wb
import os

from wikipedia import exceptions

engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
speed=100
engine.setProperty("rate",speed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(date)
def wishme():
    speak("welcome babu")
    
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening")
    else:
        speak("good night")
def take():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        
        print("listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("say that again")

        return "none"    

    return query 
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login()
    server.sendmail()
    server.close()
if __name__== "__main__":
    wishme()

    while True:
        query=take().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching..")
            query=query.replace("wikipedia","")
            result =wikipedia.summary(query,sentences
            =3)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say")
                content=take()
                to="ffh@gmai"
                sendmail(to,content)
                speak("the mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the message")
        elif "search in chrome" in query:
            speak("what should i search")
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application.exe %s"
            search=take().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
        elif "logout" in query:
            os.system("shutdown-l")
        elif "shutdown" in query:
            os.system("shutdown /s/t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play song" in query:
            songs_dir="C:\Users\mayank mishra\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[1]))

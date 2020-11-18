import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import random
import smtplib
import urllib
import urllib.request
# import numpy as np
from subprocess import call
import socket
# import cv2


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def cam():
#     url='http://192.168.0.42:8080/shot.jpg'
#     while True:
#         imgre=urllib.request.urlopen(url)
#         imgnp=np.array(bytearray(imgre.read()),dtype=np.uint8)
#         img=cv2.imdecode(imgnp,-1)
#         cv2.imshow('test',img)
#         q=take()
#         cv2.waitKey(5)        
#         if 'quit' in q:
#         # if ord('q')== cv2.waitKey(10):
#             exit(0)

def askname():
    speak("may i know ur name sir")
    name=take()
    speak("welcome {}".format(name))
    return name
    
def wishme(name):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning {} its {} in the morning".format(name,hour))
    elif hour>=12 and hour<16:
        speak("Good afternoon {} its {} in the afternoon".format(name,hour)) 
    else:
        speak("Good evening {} its {} in the evening".format(name,hour)) 
    speak("How can i help you!")   


def take():
    recording = sr.Recognizer()
    with sr.Microphone() as source: 
        recording.adjust_for_ambient_noise(source)
        print("Please Say something:")
        recording.pause_threshold=1
        recording.energy_threshold=200
        audio = recording.listen(source)
        
        
        
    try:
        print("Recgonizing...")
        query=recording.recognize_google(audio,language='en-IN')
        print("User said \n {}".format(query))
        # speak(query)  
    except Exception as e:
        print("say that again Please")
        return "None"
    return query 

def email(to1,content1):
    server=smtplib.SMTP('smtp.gmail.com',587)
    em="17cs061.leroy@sjec.ac.in"
    server.ehlo()
    server.starttls()
    server.login(em,'Sjec525#')
    server.sendmail(em,to1,content1)
    speak("email sent")

def findReceiver(name):
    contacts = {'silva':'dsilva.leroy10','mama':'lidwin1971','castellino':'sharrel.castelino'}
    try:
        receiverGmail = contacts[name]
        return receiverGmail
    except:
        return 0


    
if __name__ == "__main__":
    name=askname()
    wishme(name)
    while True:
        query=take().lower()        
        if 'thank you' in query:
            speak('anytime,goodbye ')
            exit(0)

        elif 'wikipedia' in query:
            query=query.replace("wikipedia","")
            speak("searching in wikipedia just a minute")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(result)

        elif 'music' in query:
            speak("playing music")
            song_dir="L:\\car songs mp3(1)"
            songs=os.listdir(song_dir)
            n=random.randint(0,99)
            print(n)
            os.startfile(os.path.join(song_dir,songs[n]))

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is {}".format(time))

        # elif 'camera' in query:
        #     cam()

        elif 'code' in query:
            code_path="C:\\Users\\Leroy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(code_path)

        elif 'what' in query or 'who' in query or 'where' in query or 'can you' in query:
            webbrowser.open("https://www.google.com/search?&q={}".format(query))
            speak(wikipedia.summary(query, sentences=2))       

        elif 'email' in query:
            try:
                speak("to whom")
                query=take().lower()
                receiver = query.split(" ")[len(query.split(" "))-1]
                to = findReceiver(receiver)
                to="{}@gmail.com".format(to)
                print(to)
                speak("What do u want to send")
                content=take()
                email(to,content)   
            except Exception as e:
                print(e)
                speak("sorry email not able to send")     
        else:
            li=['youtube','google','goal','moneycontrol'] 
            for char in li:
                if char in query:
                    if char=='youtube':
                        query=query.replace("youtube","")
                        webbrowser.open("https://www.youtube.com/results?search_query={}".format(query))
                    else:
                        speak('openning {}'.format(char))
                        webbrowser.open('{}.com'.format(char))     
                

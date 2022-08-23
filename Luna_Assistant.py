from ast import main
from pickle import TRUE
import speech_recognition as sr
from gtts import gTTS
from luna import Ui_Form
from instabot import Bot
import playsound
import os
import datetime
from time import ctime
import re
from fbchat import Client
from fbchat.models import Message
import webbrowser
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import smtplib
import pyjokes
import bs4
import requests
import time
import pyttsx3 as tts
import winsound
import pyautogui
import random
import pyttsx3
import exception as e
import pyautogui 
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def respond(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit = 10)
    data=""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data



def respond(String):
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

def voice_assistant(data):

# who made you

    if "who made you" in data or "who created you" in data or "who discovered you" in data:
            listening = True
            print()
            print("I was built by K.D.O")
            engine.say("I was built by K D O")
            engine.runAndWait() 
    
# what do you know about him

    if "what do you know about him" in data:
        listening = True
        engine.say("many things, He is a programmer, hindi rapper and as well as student")
        engine.runAndWait() 

# good night
    
    if "good night" in data:
        listening = True
        engine.say("good night, master")
        engine.runAndWait() 

# hello

    if "hello" in data or "hello luna" in data:
            listening = True
            hel = "Hello master ! How May i Help you.."
            print(hel)
            engine.say(hel)
            engine.runAndWait() 

# your name

    if "your name" in data or "sweat name" in data or "what is your name" in data:
            listening = True
            na_me = "Thanks for Asking my name, myself ! Luna"
            print(na_me)
            engine.say(na_me)
            engine.runAndWait() 
            
# what is the time

    if 'time please' in data or 'what is the time' in data or 'time batao' in data\
                or 'current time' in data or 'time' in data or 'whats time' in data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            listening = True
            print(strTime)
            engine.say(strTime)
            engine.runAndWait() 

# hii

    if "hai" in data or "hii" in data:
        listening = True
        engine.say("what's going on?")
        engine.runAndWait() 
    
# open youtube

    if "open youtube" in data or "open YouTube" in data:
            listening = True
            engine.say ("Tell me, what do you want me to search master?")
            engine.runAndWait() 
            search_text = listen()
            search_text = search_text.replace(" ", "+")
            webbrowser.open_new_tab(f"https://www.youtube.com/search?q={search_text}")
            time.sleep(30)

# joke

    if "joke" in data or "luna say a joke" in data or " say joke luna" in data:
                joke = pyjokes.get_joke()
                print(joke)
                engine.sayk(joke)


# make note

    if "make a note" in data or "write this down" in data or "remember this" in data:
                engine.say("What would you like me to write down? master")
                note_text = listen()
                listen(note_text)
                engine.say("I've made a note of that master")

    elif "close the note" in data or "close notepad" in data:
                engine.say("Okay master, closing notepad")
                os.system("taskkill /f /im notepad++.exe")
    
# open google

    if 'open google' in data or 'open Google' in data:
            listening = True 
            print()
            print("Opening google...")
            engine.say("opening google")
            engine.runAndWait() 
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(5)

# who are you

    if "who are you" in data or "what can you do" in data:
            listening = True
            print('I am Luna, version 1 point 0 ...your persoanl assistant . I am programmed to do minor tasks like '
                  'opening youtube , google chrome, gmail, predict time, sending whatsapp message, search wikipedia, predict weather ' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            engine.say('I am Luna, version 1 point 0 ...your persoanl assistant . I am programmed to do minor tasks like '
                  'opening youtube ,google chrome,gmail, predict time, sending whatsapp message, search wikipedia, predict weather ' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            engine.runAndWait() 

#open visual
            
    if "open visual" in data or 'open Visual' in data:
            listening = True
            engine.sayd("Opening VS code ")
            engine.runAndWait() 
            os.startfile("C:\\Users\\Deepak Sharma\\AppData\\Roaming\\Microsoft\\Windows\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code")

# open visual

    if 'open visual' in data or "coronacase" in data:
            listening = True
            print()
            engine.say("opening corona virus cases")
            engine.runAndWait() 
            webbrowser.open_new_tab("https://g.co/kgs/uVucBF")
            time.sleep(10)

# wait for second

    if 'wait' in data or 'wait zen' in data or 'wait for second' in data or 'just wait' \
                in data or 'wait please' in data or 'please wait' in data or 'please wait zen'\
                in data or 'wait a second' in data:
            listening = True
            print("Ok! waiting sir")
            engine.say("OK! waiting sir")
            engine.runAndWait() 
            time.sleep(10)
            engine.say("OK sir! How May I Help You")
            engine.runAndWait() 
            print("OK sir! How May I Help You")

            # search

    if "search" in data:
            listening = True
            engine.say("Tell me, what do you want me to search master?")
            engine.runAndWait() 
            search_text = listen()
            search_text = search_text.replace(" ", "+")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={search_text}")




# if "programming" in data or  "studying" in data or "hacking" in data or "eating" in data or "sleeping" in data





    if "programming" in data or  "studying" in data or "hacking" in data or "eating" in data or "sleeping" in data:
        listening = True
        engine.say("it's good")
        engine.runAndWait() 

#what do you know about me

    if "what do you know about me" in data:
        listening = True
        engine.say("many things")
        engine.runAndWait() 

    if "check my instagram followers" in data or "check my Instagram followers" in data or "Instagram followers" in data:
        bot = Bot()
        bot.login(username="kdo_shashank",
        password="shashank2064")
 
# Count number of followers
        followers = bot.get_user_followers("shashank_kdo")
        engine.say("Total number of followers:")
        engine.say(len(followers))
        print("Total number of followers:")
        print(len(followers))

# really

    if "really" in data:
        listening = True
        engine.say("yes")
        engine.runAndWait() 

# then say my real name

    if "then say my real name" in data:
        listening = True
        engine.say("ok, your real name is shashank")
        engine.runAndWait() 

# nothing

    if "nothing" in data:
        listening = False
        print("Listening Stopped")
        engine.say("Ok, Bye ")
        engine.runAndWait()  

# ok bye

    if "ok bye" in data:
        listening = True
        engine.say(" bye, Master  ")
        engine.runAndWait()  

        #news list
                       
    if 'news' in data:
            listening = True
            print("Tell me Master, Which country news you want to know, options..India, Nepal, russia, China, Bhutan, America or Pakistan")
            engine.say("Tell me Master, Which country news you want to know, options..India, Nepal, russia, China, Bhutan, America or Pakistan")
            engine.runAndWait() 
        
    if "india" in data or "India" in data:
                news = webbrowser.open_new_tab("https://www.timesofindia.indiatimes.com")
                engine.say("Opening  India News...")
                engine.runAndWait()  
    elif "nepal" in data or "Nepal" in data:
                news = webbrowser.open_new_tab("https://www.Ekantipur.com")
                engine.say("Opening Nepal News...")
                engine.runAndWait()  
    elif  "russia" in data or "Russia" in data:
                news = webbrowser.open_new_tab("https://www.themoscowtimes.com")
                engine.say("Opening Russia News...")
                engine.runAndWait()  
    elif  "china" in data or "China" in data:
                news = webbrowser.open_new_tab("http://www.ecns.cn")
                engine.say("Opening China News...")
                engine.runAndWait()  
    elif  "bhutan" in data or "Bhutan" in data:
                news = webbrowser.open_new_tab("https://www.manhuaplus.com")
                engine.say("Opening Bhutan News...")
                engine.runAndWait()  
    elif  "america" in data or "America" in data:
                news = webbrowser.open_new_tab("https://www.cbsnews.com")
                engine.say("Opening America News...")
                engine.runAndWait()  
    elif  "Pakistan" in data or "pakistan" in data:
                news = webbrowser.open_new_tab("https://live.geo.tv")
                engine.say("Opening Pakistan News...")
                engine.runAndWait()      
           
    
    #social medial

    if 'open my Social Media' in data or 'open my social media' in data  or 'open  social media' in data :
            listening = True
            print("Tell me Master, Which Social Media You would like to open, options.. Facebook, Whatsapp, Instagram or Telegram")
            engine.say("Tell me Master,  Which Social Media You would like to open, options ! Facebook, Whatsapp, Instagram or Telegram")
            engine.runAndWait() 
            media = listen()
            if "Instagram" in media or "instagram"  in media:
                news = webbrowser.open_new_tab("https://www.instagram.com")
                engine.say("Opening  Instagram...")
                engine.runAndWait()  
            elif "FaceBook" in media or "facebook"  in media or "Facebook"  in media:
                news = webbrowser.open_new_tab("https://www.facebook.com")
                engine.say("Opening Facebook...")
                engine.runAndWait()  
            elif "Whatsapp"  in media or "WhatsApp"  in media or "Whatsapp"  in media:
                news = webbrowser.open_new_tab("https://web.whatsapp.com")
                engine.say("Opening whatsapp...")
                engine.runAndWait()  
            elif "Telegram"  in media or "telegram"  in media:
                news = webbrowser.open_new_tab("http://www.telegram.com")
                engine.say("Opening Telegram...")
                engine.runAndWait()  

        
    

# check my social media massage

    if 'check my Social Media message' in data or "media messenger" in data or 'open my social media messenger' in data or "check my total media messenger" in data or 'check my social media messenger' in data or 'take my social media messenger' in data:
            listening = True
            print("Tell me Master, Which Social Media massenger You would like to open, options..facebook or Instagram ")
            engine.say("Tell me Master, Which Social Media massenger You would like to open, options..facebook or Instagram ")
            engine.runAndWait()
            social = listen()
            if "facebook" in social or "FaceBook" in social or "FaceBook messenger" in social or "facebook messenger" in social or "Facebook messenger" in social  or "FaceBook Messenger" in social or "facebook Messenger"  in social or "Facebook Messenger" in social:
                news = webbrowser.open_new_tab("https://m.facebook.com/messages/")
                engine.say("Opening facebook messenger...")
                engine.runAndWait()

            if "Instagram" in social or "instagram" in social or "Instagram messenger"  in social or "instagram messenger" in social:
                news = webbrowser.open_new_tab("https://www.instagram.com/direct/inbox/")
                engine.say("Opening Instagram messenger...")
                engine.runAndWait()


    
           
           
# send msg   


    if "open whatsapp" in data or "open WhatsApp" in data:
            listening = True
            print("whom you want to send message  ")
            engine.say("whom would you like to send message" )
            person_name = listen()
            print(person_name)
            print()
            print("what is your message : ")
            engine.say("what is your message ")
            msg = listen()
            print(msg)
            print()
            print("Sending message on whatsapp...")
            engine.say("Sending message on whatsapp...")
            webbrowser.open('https://web.whatsapp.com/')
            time.sleep(12)
            #click on search bar
            pyautogui.click(296,281)
            pyautogui.typewrite(person_name)
            time.sleep(5)
            #click on the person
            pyautogui.click(238,444)
            time.sleep(5)
            #click on typying box
            pyautogui.click(898,1017)
            pyautogui.typewrite(msg)
            time.sleep(2)
            #sending msg
            pyautogui.click(1791,1016)
            time.sleep(4)
            #return back
            pyautogui.click(1774,19)
            print()
            print(("message sent..."))
            engine.say("message sent ...")
            engine.runAndWait()  

# how do you know me
        
    if "how do you know me" in data:
        listening = True
        print("you have made me so I know you")
        engine.say("you have made me so I know you")
        engine.runAndWait()  

# can you say something about your developer
    
    if "can you say something about your developer" in data or "say something about you developer" in data or "interesting facts about your developer" in data:
        listening = True
        print("Yes, The persone who developed me is Shashank. He is also know as K.D.O. He is a programmer, hindi rapper as well as student. He is from nepal, Birgunj.  ")
        engine.say("Yes, The persone who developed me is Shashank. He is also know as K.D.O. He is a programmer, hindi rapper as well as student. He is from nepal, Birgunj. ")
        engine.runAndWait()  

# shutdown

    if 'shutdown' in data:
            engine.say("shuting down")
            engine.runAndWait()  
            os.system("shutdown /s /t 1")

# did you know my smaller brother name

    if "did you know my smaller brother name" in data or "what is my brother name" in data or "who is my brother" in data:
        listening = True
        print(" Your brother name is siwansh mishra ")
        engine.say(" Your brother name is siwansh mishra ")
        engine.runAndWait()  

# what's up"

    if "what's up" in data or 'how are you' in data:
            listening = True
            stMsgs = ['Just doing my thing! How are you master', 'I am fine! How are you master', 'Nice! ! How are you master', 'I am nice and full of energy ! How are you Master ',
                      'i am okey ! How are you master']
            ans_q = random.choice(stMsgs)
            engine.say(ans_q)
            engine.runAndWait()  
           
            ans_take_from_user_how_are_you = listen()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you  or 'nice' in ans_take_from_user_how_are_you:
                engine.say('okey..')
                engine.runAndWait()  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or  'upset' in ans_take_from_user_how_are_you or 'fever' in ans_take_from_user_how_are_you:
                engine.say('oh sorry..')
                engine.runAndWait()  

# where is
                                                                                                           
    if "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        engine.say("Hold on K.D.O, I will show you where " + data[2] + " is.")
        engine.runAndWait()  
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)


    if "check my Facebook messenger" in data or "check my FaceBook messenger" in data or "Facebook Messenger" in data:
         # facebook username & password
         username = "9804266570"
         password = "hack2006"

# login
         client = Client(username, password)

# get list users you most recently talked to
         users = client.fetchThreadList()
         print(users)
         engine.say(users)

# get the detailed informations about users

# sort by number of messages
         sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)

# print the best friend
         best_friend = sorted_detailed_users[0]

         print("Best friend:", best_friend.name, "with a message count of", best_friend.message_count)
         engine.say("Best friend:", best_friend.name, "with a message count of", best_friend.message_count)

        
# open google

    if "open google" in data.casefold():
        listening =True
        reg_ex = re.search('open google(.*)',data)
        url = 'https://www.google.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        print('Done')
        engine.say('Done')
        engine.runAndWait()  

# send email

    if "email" in data:
        listening = True
        engine.say("Whom should i send email to?")
        to = listen()
        edict = {'hello':'mshashank980@gmail.com','just':'mshashank917@gmail.com'}
        toaddr = edict[to]
        engine.say("What is the Subject?")
        subject = listen()
        engine.say("What should i tell that person")
        message = listen()
        content = 'Subject: {}\n\n{}'.format(subject,message)
        
#init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)

        mail.ehlo()

        mail.starttls()

#login
        mail.login('shashank123980@gmail.com','Shashank@mishra2064')

        mail.sendmail('everest1gaming@gmail.com',toaddr,content)

        mail.close()

        engine.say('Email Sent')
        engine.runAndWait()  

# wikipedia

    if "wikipedia" in data.casefold():
        listening = True
        engine.say("What should I search?")
        data = listen()
        response = requests.get("https://en.wikipedia.org/wiki/" +data)
        if response is not None:
            html = bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs = html.select("p")
            intro = [i.text for i in paragraphs]
            halo = ''.join(intro)
        engine.say(halo[:200])
        engine.runAndWait()  

# stop listing

    if "stop listening " in data or "stop Listening " in data or "Stop Listening " in data:
        listening = False
        print("Listening Stopped")
        engine.say("i will miss you")
        engine.runAndWait()  

    try:
        return listening
    except UnboundLocalError:
        print("TimedOut-->Re-Launch")
       
    
time.sleep(1.5)
hour = int(datetime.datetime.now().hour) 
if hour>=0 and hour<12:  
       print("Good Morning Master")
       engine.say("Good Morning Master")
       engine.runAndWait()  
      
elif hour>=12 and hour<18:
        print("Good Afternoon Master")
        engine.say("Good Afternoon Master")
        engine.runAndWait()  
       
else:
        print("Good Evening Master")
        engine.say("Good Evening Master")
        engine.runAndWait()  
       
print("How can I help you")
engine.say("How can I help you")
engine.runAndWait()         

    

listening = True
while listening == True:
    data = listen() #
    listening = voice_assistant(data)


startExecution = MainThread()

  
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.movie = QtGui.QMovie("Microinteractions III.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/live.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/live.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/Earth.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/Health_Template.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/initial.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/Hero_Template.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/Jarvis_Gui (2).gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ExtraGui-20220815T151043Z-001/ExtraGui/Earth_Template.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("VoiceReg-20220815T073757Z-001/VoiceReg/Siri_1.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.pushButton.clicked.connect(self.startTask)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()


    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




import datetime
import time as time
import pyttsx3
import speech_recognition as sr
import pywhatkit 
import pyjokes as pj
import wikipedia as wikipedia
from datetime import datetime as dt
from pathlib import Path
import os 

#Getting voice intake ready with voice packages
engine=pyttsx3.init()
voice_intake=sr.Recognizer()

my_mic=sr.Microphone(device_index=1)

voice_intake.energy_threshold = 700 

voices = engine.getProperty('voices')
voices = engine.setProperty('voice',voices[2].id)

#Function to read out text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Opening line
print(' I am June,your virtual partner,how may i be of service')
talk('I am June, ,your virtual partner, ,how may i be of service')

def command_input():
    my_mic=sr.Microphone(device_index=1) #specifying source of input
    try:
        with my_mic as source:
            print("Listening....")
            command = voice_intake.listen(source)                                
            command = voice_intake.recognize_google(command)
            print("USER INPUT:",command)
            command = command.lower()
    except Exception:
        pass  #diff
    return command 

def run_june():
    command=command_input()
    
    if 'diary' in command:
        diary()
    
    if "june" in command:
        command = command.replace('june', '')
    if 'what can you do' in command:
        menu() 
        command=command_input()  
    if 'diary' in command:
        diary()
    if 'play'  in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'what' and 'time' in command:
        Time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + Time)
        talk('Current time is ' + Time)
    if 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    if "introduce yourself" in command:
        intro = "I am a virtual assistant made my Arjun Aravind "
        print(intro)
        talk(intro)
    if "take a break" in command:   #hereeeeeeeeeeee
        print("Taking a 60 second nap...")
        talk("Taking a 60 second nap...")
        time.sleep(60)
        print('Awake and good to go..')
        talk('Awake and good to go..')
               
    if 'joke' in command:
        joke = pj.get_joke() 
        print(joke)
        talk(joke)
        
    if "help me" in command:
        help_me = 'You got this , do your best and put in the efforts and success will be yours. Take up one idea. ' \
                  'Make that one idea your life--think of it, dream of it, live on that idea. ' \
                  'Let the brain, muscles, nerves, every part of your body, be full of that idea, ' \
                  'and just leave every other idea alone. ' \
                  'This is the way to success.'
        print(help_me)
        talk(help_me)
    
    if 'exit' in command:
        print("Have a great day,each one's a gift")
        talk("Have a great day, ,each one's a gift")
        exit()
    
def menu():
    print("Here are some of the things that i can do: \n1.Joke\n2.Music\n3.Diary\n4.Youtube Video\n5.Exit")
    talk("Here are some of the things that i can do:Joke , Play Music , Diary , Youtube Video , Exit application")
    print("Make your choice:")
    talk("Make your choice:")
    return
    
def diary():
    print("Would you like to make a new entry or view old entries?")
    talk("Would you like to make a new entry or view old entries?")  # problem arises after this line
    diary_choice = command_input()
    engine.runAndWait()
    if 'new' in diary_choice:
        diary_new_entry()
        engine.runAndWait()
    elif 'old' in diary_choice:
        data_files =os.listdir("D:\AI_PARTNER\Diary_Data")
        print("\n\nFiles are ",data_files,sep='\n')
        
        for i,val in enumerate(data_files):
            diary_dates=val.split(sep='_')
            val_string=("Diary entry ",i," is dated ",diary_dates)
            print(val_string)
            talk(val_string)
        print("Which entry would u like to view?")
        talk("Which entry would u like to view?")
        ch=command_input()
        ch=int(ch)
        print("Entry number=",ch)
        
        f=open("D:\AI_PARTNER\Diary_Data\\"+data_files[ch],'r') 
        diary_data=f.read()
        print("Contents of journal log are:\n",diary_data)
        talk("Contents of journal log are :")
        talk(diary_data)
        f.close()
        run_june()
             

def diary_new_entry():
    a = dt.now()
    cur_date_time = a.strftime("%d_%m_%Y_%H_%M_%S" + ".txt")
    
    data_file = Path("D:\AI_PARTNER\Diary_Data" + '/' + cur_date_time)
    
    print("You may now start to speak your journal entry:")
    talk("You may now start to speak your journal entry:")
    
    data_unconfirmed = command_input()
    engine.runAndWait()
    print(data_unconfirmed)
    
    print("\n Would you like to save this entry or retake the entry?")
    talk("\n Would you like to save this entry or retake the entry?")
    
    option = command_input()
    engine.runAndWait()
    if 'save' in option:
        data_confirmed = data_unconfirmed
        f = open(data_file, 'a+')
        f.write(data_confirmed)
        print(f.read())
    else:
        diary_new_entry()

while True:
    run_june()
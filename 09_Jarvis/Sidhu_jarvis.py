import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import os
import datetime
import openai
from openai import OpenAI


with open("openaikey.txt", "r") as file:
    api_key = file.read().strip()
    client = OpenAI(api_key=api_key)


def Speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate' , 175)
    engine.setProperty('volume' , 1.0)
    engine.say(text)
    engine.runAndWait() 


engine = pyttsx3.init()
recognizer = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            if "jarvis" in command:
                Speak("Yes Mr Sidhu")
                print("Jarvis Activated")
                while True: 
                    with sr.Microphone() as source:
                        print("Listening...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio).lower()
                        print(command)
                        if command.startswith("open"):
                            sidhu = command.split(" ")
                            if sidhu[1] == "youtube":
                                Speak("Opening Youtube")
                                time.sleep(0.5)
                                webbrowser.open("https://www.youtube.com/")
                            elif sidhu[1] == "facebook":
                                Speak("Opening facebook")
                                time.sleep(0.5)
                                webbrowser.open("https://www.facebook.com/")
                            elif sidhu[1] == "linkedin":
                                Speak("Opening Linkedin")
                                time.sleep(0.5)
                                webbrowser.open("https://www.linkedin.com/")
                            elif sidhu[1] == "instagram" or sidhu[1] == "ig":
                                Speak("Opening Instagram")
                                time.sleep(0.5)
                                webbrowser.open("https://www.instagram.com/") 
                            elif sidhu[1] =="notepad":
                                Speak("Opening Notepad") 
                                time.sleep(0.5)
                                os.system("notepad.exe") 
                            elif sidhu[1] == "chrome":
                                Speak("Opening Chrome")
                                time.sleep(0.5)
                                os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe"')                                      
                            else:
                                Speak("Sorry Command Not Supported")
                        elif command == "play songs" or command == "play song":
                            Speak("Playing songs")
                            time.sleep(0.5)
                            webbrowser.open("https://www.youtube.com/watch?v=yuF7Pw-_YIE&list=RDyuF7Pw-_YIE&start_radio=1")                   
                        elif command == "stop" or command == "exit":
                            Speak("Goodbye Sir")
                            time.sleep(0.7)
                            break
                        elif command == "how are you":
                            Speak("Fine Sir How May I Help U")
                        elif command == "shutdown":
                            Speak("Jarvis Shutting Down")    
                            print("Jarvis Deactivated")
                            time.sleep(0.8)
                            exit()
                        elif command == "turnoff pc" or command == "turnoff computer":
                            Speak("Turning Off PC")
                            time.sleep(0.8)
                            os.system("shutdown /s /t 1")
                        elif command == "lock pc" or command == "lock computer":
                            Speak("Pc Locking")
                            time.sleep(0.8)
                            os.system("rundll32.exe user32.dll,LockWorkStation")
                        elif command == "restart pc" or command == "restart computer":
                            Speak("Restarting PC")      
                            time.sleep(0.8) 
                            os.system("shutdown /r /t 1")
                        elif command.startswith("search"):
                            if command.endswith("wikipedia"):
                                Speak("What do u want to search sir")
                                time.sleep(0.5)
                                with sr.Microphone() as source:
                                    print("Listening...")
                                    audio = recognizer.listen(source)
                                    command = recognizer.recognize_google(audio).lower()
                                    Speak(f"Searching {command} on wikipedia")
                                    time.sleep(0.8)
                                    webbrowser.open(f"https://en.wikipedia.org/wiki/{command}")
                            elif command.endswith("youtube") or command.endswith("yt"):
                                Speak("What do u want to search sir")
                                time.sleep(0.5)
                                with sr.Microphone() as source:
                                    print("Listening...")
                                    audio = recognizer.listen(source)
                                    command = recognizer.recognize_google(audio).lower()
                                    Speak(f"Searching {command} on youtube")
                                    time.sleep(0.8)
                                    webbrowser.open(f"https://www.youtube.com/results?search_query={command}")
                            elif command.endswith("browser") or command.endswith("google") :
                                Speak("What do u want to search sir")
                                time.sleep(0.5)
                                with sr.Microphone() as source:
                                    print("Listening...")
                                    audio = recognizer.listen(source)
                                    command = recognizer.recognize_google(audio).lower()
                                    Speak(f"Searching {command} on browser")
                                    time.sleep(0.8)
                                    webbrowser.open(f"https://www.bing.com/search?q={command}")
                        else:
                            try:
                                Speak("Thinking...")
                                response = client.chat.completions.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system", "content": "You are a helpful voice assistant."},
                                        {"role": "user", "content": command}
                                    ]
                                )
                                reply = response.choices[0].message.content
                                print("AI:", reply)
                                Speak(reply)
                            except Exception as e:
                                print("AI Error:", e)
                                Speak("Sorry, I couldn't process that.")
        if command == "shutdown":
            Speak("Jarvis Shutting Down")    
            print("Jarvis Deactivated")
            time.sleep(0.8)
            break    
    except Exception as e:
        print("AI Error:", e)
        Speak("Sorry, I couldn't process that.")
        

                           


                                                            



                                                            
                            



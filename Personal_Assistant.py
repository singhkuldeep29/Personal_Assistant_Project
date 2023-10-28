import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour<12 and hour>18:
        speak("Good Afternoon Sir!!")    

    else:
        speak("Good Evening Sir!!")

    speak ("Hello , I am your personal assitent How may I help you?")   

def takeCommand():
    # It takes microphone input from user and returns the string output

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1     
        audio = r.listen(source) 

    try:    
        print("Recognizing...")  
        query = r.recognize_google(audio , language='en-in')
        print(f"User said {query}\n")


    except Exception as e:
        # print(e)      ---- it shows the error in the console
        print("Say that again please....")
        return "None"    
    
    return query

if __name__ == "__main__":
    # speak("Kuldeep is a good boy")
    wishME()
    while True:
    # if 1:
        
        query = takeCommand().lower()

# logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searchinh wikipedia....")
            quer = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                
        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
                music_Dir = 'c:\\music'
                songs = os.listdir(music_Dir)
                print(songs)
                os.startfile(os.path.join(music_Dir, songs[0]))

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")        
             speak(f"The time is {strTime}")

        elif 'open vs code' in query:
             vs_path = "C:\\Users\\kulde\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(vs_path)   
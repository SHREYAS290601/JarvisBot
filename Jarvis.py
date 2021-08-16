import datetime
import os
import webbrowser
import pyowm
import pyttsx3
import speech_recognition as sr
import wikipedia

now = datetime.datetime.now()
engine = pyttsx3.init()
sound = engine.getProperty('voices')

engine.setProperty('voice', sound[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(ask):
    hour = now.hour
    if hour < 12:
        speak("Good Morning Mr.Shreyas")
    if hour in range(12, 18):
        speak("Good Afternoon Mr.Shreyas")
    if hour > 18:
        speak("Good Evening Mr.Shreyas")
    if ask == "yes":
        speak(
            "Hello for those who are new here I am a Voice assistant that Shreyas has created,Please tell me what to do...")
    else:
        speak("At your service sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print("User said", query)

    except Exception as e:
        print("Say that again please")
        return 'none'
    return query


def weatherCall(place):
    apiKEY = '860fc93a119e0820bd71a953b40cad09'
    owm = pyowm.OWM(apiKEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    weather = observation.weather
    temperature=weather.temperature('celsius')['temp']
    speak(f"The temperature in degree celsius{temperature}")


if __name__ == "__main__":
    speak("Sir do we have people with us?")
    ask = takeCommand()
    wishme(ask)
    while True:
        Listener = takeCommand().lower()

        if 'wikipedia' in Listener:
            speak('Searching...')
            Listener = Listener.replace("wikipedia", "")
            results = wikipedia.summary(Listener, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in Listener:
            webbrowser.open_new_tab("youtube.com")

        if 'open twitch' in Listener:
            webbrowser.open_new_tab("twitch.com")

        if 'open google' in Listener:
            webbrowser.open_new_tab("google.com")

        if 'open whatsapp' in Listener:
            webbrowser.open_new_tab("whatsapp.com")

        if 'open spotify' in Listener:
            webbrowser.open_new_tab("spotify.com")

        elif 'play me something' in Listener:
            music = 'C:\\Users\\Shreyas\\Music\\MINEEEE'
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))

        elif 'tell me the time' in Listener:
            strtime = now.strftime("%H:%M:%S")
            speak(f"The time is{strtime}")

        elif 'weather' in Listener:
            speak("HMM let me predict the weather...")
            place = Listener.replace("weather", "")
            weatherCall(place)

        elif 'play me the song' in Listener:
            speak("Searching...")
            speak("Playing your song on spotify")
            Listener=Listener.replace("play me the song","")
            webbrowser.open_new_tab(f"https://open.spotify.com/search/{Listener}")

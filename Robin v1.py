#Dependencies
import speech_recognition as speech
import pyttsx3
import datetime
import wikipedia
from googlesearch import search
import webbrowser
import os
import random
import requests
import time
import sys

#Variables
api_key_city = "41c3a1696ef8af2f9835409e70a60645"
api_key = "d3318ab7e1e1aa8f9524a810185d2ac1"
url_weather = "http://api.openweathermap.org/data/2.5/weather?"
listener = speech.Recognizer()
replier = pyttsx3.init()
rate = replier.getProperty('rate')

replier.setProperty('rate', rate - 50)

#Arrays (or maybe dictionaries added later too .. idk)
name_interaction = [

"Tell me",
"I am listening",
"Go ahead, ask me a question",
"Robin, at your service",
"What can I do for you"

]

asking_name_interaction = [

"You just called me with my name",
"Hi, this is Robin",
"You know my name",
"I am an AI Assistant named Robin",
"Hey, this is Robin"

]

creator_interaction = [

"I am created by Samyak",
"My creator is Samyak",
"Samyak is my owner and creator"

]

how_are_you_interaction = [

"I am fine!",
"My systems are online and working perfectly fine!",
"Me? Yeah, I'm fine!"

]

nothing_interaction = [

"I feel sad! Anyways I'm at your service anytime!",
"That's Unfortunate!"

]

thank_you_interaction = [

"Welcome!",
"It's my duty",
"My pleasure"

]

name_not_called_interaction = [

"Try to call me with my name!",
"Please call me with my name",
"I like helping you when you call me with my name"

]

#Functions
def TypeWritter(msg):
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def MainFuntion():
    TypeWritter("----------------------------------------------------------------------------------------------------")
    TypeWritter("\n--------------------------------------------------------------------------------------------------")
    TypeWritter("\nRobin is currently in development state! \nPlease do expect bugs! \nThere might be issues related to speech recognition due to different accents!\n")
    TypeWritter("\nDeveloped by Samyak! Hope you like it")
    TypeWritter("\n--------------------------------------------------------------------------------------------------")
    TypeWritter("\n----------------------------------------------------------------------------------------------------")
    print("\n")

    time.sleep(2)

    Intro()

    while True:
        run_robin()

def Time(i):
    _hour = datetime.datetime.now().hour

    if i == "Intro":
        if _hour > 5 and _hour < 12:
            greetings = "Good Morning!"
        elif _hour >= 12 and _hour < 18:
            greetings = "Good Afternoon!"
        else:
            greetings = "Good Evening!"

        return greetings

    elif i == "Outro":
        if _hour >= 18 or _hour < 5:
            greetings = "Good Night!"
        else:
            greetings = "Have a good day!"

        return greetings

def Intro():
    _greet = Time("Intro")

    print(_greet + " Robin is online!")
    replier.say(_greet + " Robin is online!")
    replier.runAndWait()

def weather_city_finder(city):
    complete_url_weather_city = url_weather + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url_weather_city)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temp = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]

        weather_desc = z[0]["description"]

        temp_celsius = (current_temp - 273.15)
        temp_celsius = "{:.2f}".format(temp_celsius)

        #Converting them to strings
        temperature = str(temp_celsius)
        humidity = str(current_humidity)
        weather = str(weather_desc)

        return True, temperature, humidity, weather

    else:
        return False, None, None, None

def weather_finder():
    my_ip_url = "https://ip.42.pl/raw"
    response_ip = requests.get(my_ip_url)

    my_ip = response_ip.text

    city_finder_url = "http://api.ipstack.com/" + my_ip +"?access_key=" + api_key_city
    res = requests.get(city_finder_url)

    a = res.json()

    city_name = a["city"]

    complete_url_weather = url_weather + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url_weather)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temp = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]

        weather_desc = z[0]["description"]

        temp_celsius = (current_temp - 273.15)
        temp_celsius = "{:.2f}".format(temp_celsius)

        #Converting them to strings
        temperature = str(temp_celsius)
        humidity = str(current_humidity)
        weather = str(weather_desc)

        return True, temperature, humidity, weather

    else:
        return False, None, None, None

def random_chooser(i):
    if i == 1 or i == 2:
        random_num = random.randrange(0, 5, 1)

    elif i == 3:
        random_num = random.randrange(0, 3, 1)

    elif i == 4:
        random_num = random.randrange(0, 2, 1)

    return random_num

def Speak(text):
    replier.say(text)
    replier.runAndWait()

def Search(text):
    query = text.strip()

    for url in search(query, tld = "co.in", num = 1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)

def Search_Google():
    webbrowser.open("https://webmail.licindia.in/owa/")

def Search_App(app):
    os.system(app)

def Open_Website(text):
    web = text.strip()

    webbrowser.open("https://" + web + ".com")

def Search_YT(text):
    query = text.strip()

    for url in search(query, tld = "co.in", num = 1, stop = 1, pause = 2):
        webbrowser.open("https://youtube.com/search?q=%s" % query)

def take_cmd():
    cmd = ""

    try:
        with speech.Microphone() as source:
            TypeWritter("\nRobin is now listening!")

            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
    except:
        pass

    TypeWritter("\nRobin is now not listening!")

    time.sleep(1)

    if cmd != None:
        return cmd

def give_cmd():
    cmd = ""

    try:
        with speech.Microphone() as source:
            TypeWritter("\nRobin is now listening!")

            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()

            if "yes" in cmd or "no" in cmd:
                print("User : " + cmd)
            else:
                print("User : " + cmd)

                print("Robin : Unable to understand your command")
                Speak("unable to understand your command")
    except:
        pass

    TypeWritter("\nRobin is now not listening!")

    time.sleep(1)

    if cmd != None:
        return cmd

def give_command():
    command = ""

    try:
        with speech.Microphone() as source:
            TypeWritter("\nRobin is now listening!")

            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "robin" in command:
                command = command.replace("robin", "", 1)
            else:
                print("User : " + cmd)

                print("Robin : Try to call me with my name!")
                Speak("try to call me with my name")

    except:
        pass

    TypeWritter("\nRobin is now not listening!")

    time.sleep(1)

    if command != None:
        return command

def robin_commands(cmd):
    if "play" in cmd:
        YT = cmd.replace("play", "", 1)
        YT = YT.strip()

        print("User : " + cmd)

        print("Robin : Do you want to open YouTube? (yes/no)")
        Speak("Do you want to open youtube")
        choose = give_cmd()

        if "yes" in choose:
            print("Robin : Opening youtube and searching " + YT)
            Speak("opening youtube and searching " + YT)
            Search_YT(YT)
        elif "no" in choose:
            print("Robin : Command cancelled successfully!")
            Speak("command cancelled successfully")

    elif "weather of city" in cmd:
        print("User : " + cmd)
        city_commanded = cmd.partition("city")[1]

        status, temp_city, hum_city, weather_city = weather_city_finder(city_commanded)

        if status == True:
            print(

            "Robin :\n Temperature is " + temp_city + " °C" +
            "\n Humidity is " + hum_city + " %" +
            "\n Weather is " + weather_city

            )

            Speak("temperature is " + temp_city + " degree celsius. Humidity is " + hum_city + " percent. Weather is " + weather_city)
        else:
            print("Robin : City not found or Services Offline!")
            Speak("city not found or services offline")

    elif "weather" in cmd:
        print("User : " + cmd)

        status, temp_here, hum_here, weather_here = weather_finder()

        if status == True:
            print(

            "Robin :\n Temperature is " + temp_here + " °C" +
            "\n Humidity is " + hum_here + " %" +
            "\n Weather is " + weather_here

            )

            Speak("temperature is " + temp_here + " degree celsius. Humidity is " + hum_here + " percent. Weather is " + weather_here)
        else:
            print("Robin : City not found or Services Offline!")
            Speak("city not found or services offline")

    elif "time" in cmd:
        print("User : " + cmd)

        time = datetime.datetime.now().strftime("%I:%M %p")

        print("Robin : It's " + time + " now")
        Speak("It's " + time + " now")

    elif "search wiki" in cmd:
        search_info = cmd.replace("search wiki", "", 1)
        info = wikipedia.summary(search_info, 3)

        print("User : " + cmd)

        print("Robin : " + info)
        Speak(info)

    elif "google search" in cmd:
        search_google = cmd.replace("google search", "", 1)
        search_google = search_google.strip()

        if "mail special" in cmd:
            print("User : " + cmd)

            print("Robin : Do you want to open Chrome? (yes/no)")
            Speak("Do you want to open chrome")
            option = give_cmd()

            if "yes" in option:
                print("Robin : Opening mail")
                Speak("Opening mail")
                Search_Google()
            elif "no" in option:
                print("Robin : Command cancelled successfully!")
                Speak("command cancelled successfully")

        else:
            print("User : " + cmd)

            print("Robin : Do you want to open Chrome? (yes/no)")
            Speak("Do you want to open chrome")
            response = give_cmd()

            if "yes" in response:
                print("Robin : Opening chrome and searching " + search_google)
                Speak("opening chrome and searching " + search_google)
                Search(search_google)
            elif "no" in response:
                print("Robin : Command cancelled successfully!")
                Speak("command cancelled successfully")

    elif "open website" in cmd:
        website = cmd.replace("open website", "", 1)
        website = website.strip()

        print("User : " + cmd)

        print("Robin : Do you want to open Chrome? (yes/no)")
        Speak("Do you want to open chrome")
        response = give_cmd()

        if "yes" in response:
            print("Robin : Opening " + website)
            Speak("opening " + website)
            Open_Website(website)
        elif "no" in response:
            print("Robin : Command cancelled successfully!")
            Speak("command cancelled successfully")

    elif "open app" in cmd:
        app = cmd.replace("open app", "", 1)
        app = app.strip()

        print("User : " + cmd)

        if app == "notepad" or app == "notes" or app == "note":
            app = "Notepad"
            print("Robin : Do you want to open " + app + "? (yes/no)")
            Speak("do you want to open " + app)
            response = give_cmd()
        elif app == "chrome" or app == "google" or app == "google chrome":
            app = "Google Chrome"
            print("Robin : Do you want to open " + app + "? (yes/no)")
            Speak("do you want to open " + app)
            response = give_cmd()
        elif app == "excel" or app == "ms excel" or app == "microsoft excel":
             app = "Microsoft Excel"
             print("Robin : Do you want to open " + app + "? (yes/no)")
             Speak("do you want to open " + app)
             response = give_cmd()
        else:
            print("Robin : App not found!")
            print("Currently supported apps : ")
            print("\n\t 1.Notepad \t 2.Google Chrome \n\t 3.Microsoft Excel")
            Speak("app not found")
            response = "no"

        if "yes" in response:
            if app == "Notepad":
                print("Robin : Opening " + app)
                Speak("opening " + app)
                app = "Notepad"
                Search_App(app)
            elif app == "Google Chrome":
                print("Robin : Opening " + app)
                Speak("opening " + app)
                app = "chrome"
                Search_App(app)
            elif app == "Microsoft Excel":
                print("Robin : Opening " + app)
                Speak("opening " + app)
                app = "excel"
                Search_App(app)

        elif "no" in response:
            print("Robin : Command cancelled successfully!")
            Speak("command cancelled successfully")

    elif "name" in cmd:
        print("User : " + cmd)

        random_number = random_chooser(2)
        print("Robin : " + asking_name_interaction[random_number])
        Speak(asking_name_interaction[random_number])

    elif "creator" in cmd or "created" in cmd or "owner" in cmd:
        print("User : " + cmd)

        random_number_Chosen = random_chooser(3)
        print("Robin : " + creator_interaction[random_number_Chosen])
        Speak(creator_interaction[random_number_Chosen])

    elif "how are you" in cmd:
        print("User : " + cmd)

        num_chosen = random_chooser(3)
        phrase_selected = how_are_you_interaction[num_chosen]

        print("Robin : " + phrase_selected)
        Speak(phrase_selected)

    elif "thank you" in cmd:
        print("User : " + cmd)

        _num = random_chooser(3)
        _phrase = thank_you_interaction[_num]

        print("Robin : " + _phrase)
        Speak(_phrase)

    elif "see you later" in cmd or "good night" in cmd or "bye" in cmd or "goodbye" in cmd or "good bye" in cmd or "later" in cmd:
        print("User : " + cmd)

        _greetings = Time("Outro")

        print("Robin going offline! " + _greetings)
        Speak("Robin going offline! " + _greetings)

        exit()

    else:
        print("User : " + cmd)

        print("Robin : Unable to understand your command!")
        Speak("Unable to understand your command")

def run_robin():
    cmd = take_cmd()

    if cmd != None:
        if cmd != "":
            if "robin" in cmd:
                print("User : " + cmd)
                cmd = cmd.replace("robin", "", 1)

                if "see you later" in cmd or "good night" in cmd or "open app" in cmd or "open website" in cmd or "google search" in cmd or "search wiki" in cmd or "time" in cmd or "play" in cmd or "name" in cmd or "creator" in cmd or "created" in cmd or "owner" in cmd or "weather" in cmd or "weather of city" in cmd or "how are you" in cmd or "thank you" in cmd:
                    robin_commands(cmd)

                elif "hi" in cmd or "hello" in cmd or "hey" in cmd or "" in cmd:
                    random_num_chosen = random_chooser(1)
                    print("Robin : " + name_interaction[random_num_chosen])
                    Speak(name_interaction[random_num_chosen])

                    given_commands = give_command()

                    if given_commands != None:

                        if "nothing" in given_commands:
                            print("User : " + given_commands)

                            _random_num = random_chooser(4)
                            _speech = nothing_interaction[_random_num]

                            print("Robin : " + _speech)
                            Speak(_speech)

                        else:
                            given_commands = given_commands.strip()
                            robin_commands(given_commands)

                else:
                    print("User : " + cmd)

                    print("Robin : Unable to understand your command!")
                    Speak("unable to understand your command")

            else:
                print("\nUser : " + cmd)

                _Random = random_chooser(4)
                _Phrase_Selected = name_not_called_interaction[_Random]

                print("Robin : " + _Phrase_Selected)
                Speak(_Phrase_Selected)
        else:
            TypeWritter("\nUser : No input")

#Main
MainFuntion()

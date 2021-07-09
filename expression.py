from datetime import datetime
from math import sqrt, cos, sin, tan, cosh, sinh, tanh, log, pi, log10
import re
import os
import wikipedia

import requests
from pyowm import OWM
from ss import *
import pyttsx3 as p
import speech_recognition as sr
import pyaudio
import webbrowser
import time
import random
import randfacts
from gtts import gTTS
from time import ctime
import process_ai
from google_trans_new import google_translator
from wit import Wit

translator = google_translator()
r = sr.Recognizer()
# ======== init voice kit =====

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
v = engine.getProperty('voices')
engine.setProperty('voice', v[1].id)


# ======== real talking =======
class  expression:
    def spr(data):
        engine.say(data)
        engine.runAndWait()
        return data


    def welcome():
        spr("Hello, I'm Amigo your voice assistant!")


    def myVoice():
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening..")
                audio = r.listen(source, 6)
                data = ''
                data = r.recognize_google(audio)
                return data
        except:
            return "Please try again."

    #=========== Google =====

    def google(req):
        try:
            req = req.lower()
            search = req.replace('search in google for', '')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            return "Here is what i found!"
        except:
            return "Connection Error"

    #========== youtube =====
    def youtube(req):
        try:
            req = req.lower()
            thing = req.replace('search in youtube for', "")
            url = f"https://www.youtube.com/results?search_query={thing}"
            webbrowser.get().open(url)
            return (f'Here is what I found for {thing} on youtube')
        except:
            return "Connection Error"
    #========== weather ====
    def weather(req):
        try:
            req = req.lower()
            place = req.replace('what is the weather in', "")
            owm = OWM(API_key='6bc957a9f5bc56565ab841c609dc2e59')
            obs = owm.weather_at_place(place)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            return f'Current weather in {place} is {k}. The maximum temperature is {x["temp_max"]:0.2f} and the minimum temperature is {x["temp_min"]:0.2f} degree celcius'
        except:
            return "Connection Error"

    #========= wikipedia ====
    def wiki(req):
        try:
            req = req.lower()
            print("i m here")
            ask = req.replace('search in wikipedia for', '')
            info = wikipedia.summary(ask, 2)
            return info
        except:
            return "Connection Error"

    #========= time ========
    def time():
        time = datetime.now().strftime('%I:%m %p')
        print(time)
        return 'Current time is ' + time

    # ========== jokes ======
    def joke():
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            json_data = requests.get(url).json()
            arr = ["", ""]
            arr[0] = json_data["setup"]
            arr[1] = json_data["punchline"]
            return (arr[0] + "  " + arr[1])
        except:
            return "Connection failed, Can you please say it again!"


    # ========== News =======
    def news():
        try:
            api_address = "http://newsapi.org/v2/top-headlines?country=us&apiKey=67f6a87fbe144407a61551aac5545686"
            json_data = requests.get(api_address).json()
            ar = []
            ar.append(json_data["articles"][1]["title"] + ".")
            return ar[0]
        except:
            return "Connection failed, Can you please say it again!"


    # ===================

    # ouvrir et fermer une application
    def openapp(app_name):
        try:
            app_name = app_name.lower()
            app_name = app_name.replace('open','').strip()
            os.startfile(app_name)
            return (app_name + " opend")
        except:
            return ("sorry I can't find the app")


    def closeapp(app_name):
        app_name = app_name.lower()
        app_name = app_name.replace('close', '').strip()
        os.system("TASKKILL /F /IM " + app_name + ".exe")
        return (app_name + " is closed ")


    # ========= Translate ======

    Mylanguages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                   'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
                   'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese': 'zh-cn',
                   'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
                   'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
                   'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu',
                   'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn',
                   'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
                   'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
                   'kurdish': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
                   'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
                   'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne',
                   'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
                   'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr',
                   'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl',
                   'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg',
                   'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur',
                   'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo',
                   'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}


    def translation(text, dist):
        distt = Mylanguages.get(dist)
        try:
            translate_text = translator.translate(text, lang_src='en', lang_tgt=distt)
            return translate_text
        except:
            return "Connection error"


    def ltol(texttotranslate):
        for i in Mylanguages:
            if bool(re.search(i, texttotranslate)) == True and bool(re.search('what is', texttotranslate)) == True:
                texttotranslate = texttotranslate.replace(' in ' + i, '').replace('what is ', '')
                texttrsn = translation(texttotranslate, i)
                break

        return texttrsn


    # ============= Basic Math ==============

    def calculate(expression):
        try:
            if "what is" in expression:
                expression = expression.replace('what is', '')
            if "calculate" in expression:
                expression = expression.replace('calculate', '')
            r = eval(expression.replace('ln', 'log10'))
            return (r)
        except:
            return ("expression invalid")


    def getappropriate(exp):
        if "translate" in exp:
            ltol(exp)
        elif "calculate" in exp:
            calculate(exp)
        elif "close" in exp:
            closeapp(exp)
        elif "open" in exp:
            openapp(exp)
        elif "news" in exp:
            news()
        elif "joke" in exp:
            joke()
        elif " " in exp:
            process_ai.chatbot_response(exp)
        else:
            return "Sorry, i am not familiar with this yet, How can i help you "


    def el():
        access_token = 'PA4WTPNO2RESP5I2MM7SXXU7IKARTVFN'
        client = Wit(access_token)
        res = client.message('set an alarm tomorrow at 7am')
        return res

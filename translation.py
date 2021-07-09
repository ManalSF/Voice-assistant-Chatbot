import re
from google_trans_new import google_translator

translator = google_translator()

# text="be my bc interpreter"
text = "Turn on interpreter mode"

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
    translate_text = translator.translate(text, lang_src='en', lang_tgt=distt)
    return translate_text
def s(texttotranslate):
    for i in Mylanguages:
        if(bool(re.search(i,texttotranslate))==True and bool(re.search('what is',texttotranslate))==True):
           texttotranslate=texttotranslate.replace(' in '+i,'').replace('what is ','')
           print(translation(texttotranslate,i))
           break

s('what is hello how are you ? in arabic')


def f(dist):
    s = ''
    while (dist not in Mylanguages or Mylanguages.get(dist) == None):
        dist = input("\nOops!. what language you want to translate to it \n language = ")
        # pour eviter le probleme de f(exit) on doit ajouter if.
        if dist == "quit" or dist == "exit": exit()
    while (s != "exit"):
        print("---------------------english to " + dist + "-----------------------")
        s = input()
        if s == "exit": break
        if s != "":
            translation(s, dist)

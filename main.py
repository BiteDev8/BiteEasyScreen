from colorama import Fore, Back, Style, init
from discord_webhook import DiscordWebhook
import pyscreenshot 
import schedule
import keyboard
import pyfiglet
import json
T = "BiteEasyScreen"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()
print(Fore.GREEN+"")
sauvegarde = ""
question_de_import = str(input("importer vos sauvegarde ?(n si c'est votre premiere fois)  y/n :"))
if question_de_import == "y" :    
    with open("data.json", "r") as f:
        data = json.load(f)
        raccourcie = data["raccourcie"]
        webhook = data["webhook"]
else :
    webhook =str(input("met ici ton webhook :"))
    raccourcie = str(input("Choisis ton raccourci en format ecrit (exemple : ctrl+alt+x): \n"))
    sauvegarde = str(input("sauvergardez les parametres ?  y/n :"))
webhook = str(webhook)
raccourcie = str(raccourcie)
if sauvegarde == "y" :
    Sauvegardejson = {"webhook" : webhook,
    "raccourcie" : raccourcie
    }

    with open("data.json", "w") as json_file:
        json.dump(Sauvegardejson, json_file)
    print("sauvegarde reussi")    
print(Fore.YELLOW+"En fonctionnement ! utilises ton raccourci pour recevoir ton ecran sur discord !")
print(Fore.RED+"alt+f4 ou ctrl+c pour arreter")
while True :
    keyboard.wait(raccourcie)
    x = "Noupi"  
    if x == "Noupi" :
        with open("data.json", "r") as f:
            data = json.load(f)
        webhook = data["webhook"]
        image = pyscreenshot.grab()  
        image.save("BiteScreen.png")
        webhook = DiscordWebhook(url=webhook, username="BiteScreen")
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        response = webhook.execute()

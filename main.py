import pyscreenshot 
from discord_webhook import DiscordWebhook
import schedule
import keyboard
from colorama import Fore, Back, Style, init
import pyfiglet

T = "BiteEasyScreen"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

print(Fore.GREEN+"")
webhook = str(input("met ici ton webhook :"))
Bite = str(input("Choisis ton raccourci en format ecrit (exemple : ctrl+alt+x): \n"))
print(Fore.YELLOW+"En fonctionnement ! utilises ton raccourci pour recevoir ton ecran sur discord !")
print(Fore.RED+"alt+f4 ou ctrl+c pour arreter")

while True :
    keyboard.wait(Bite)
    x = "Noupi"  
    if x == "Noupi" :
        image = pyscreenshot.grab()  
        image.save("BiteScreen.png")
        webhook = DiscordWebhook(url=webhook, username="BiteScreen")
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        with open("BiteScreen.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='BiteScreen.png')
        response = webhook.execute()
    else :
        pass
    

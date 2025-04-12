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

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('clear')

# Banner
def print_banner():
    print(f"""{b}

 /$$$$$$$                      /$$             /$$   /$$
| $$__  $$                    | $$            | $$  / $$ 
| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$      |  $$/ $$/  
| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$//$$$$$$\  $$$$/   
| $$  | $$| $$  \ $$| $$  \__/| $$$$$$/|______/ >$$  $$  
| $$  | $$| $$  | $$| $$      | $$_  $$        /$$/\  $$ 
| $$$$$$$/|  $$$$$$/| $$      | $$ \  $$      | $$  \ $$ 
|_______/  \______/ |__/      |__/  \__/      |__/  |__/  
                                                         
                                                         
			Author: Xyura01
""")

# Fungsi Dorking
def dorking():
    clear_screen()
    print_banner()
    try:
        dork = input(f" {b}{u}Dork Query{w}:{x} {y}")
        pages = int(input(f" {b}{u}Pages{w}:{x} {y}"))
        delay = int(input(f" {b}{u}Delay{w}:{x} {y}"))
        print()

        total = 0
        for result in search(dork, tld="com", lang="en", num=pages, start=0, stop=None, pause=delay):
            with open('results.txt', 'a') as f:
                f.write(f'{result}\n')
            total += 1
            print(f"{w}{total}) {g}{result}")
            if total >= pages:
                break

        print(f"\n{w}Saved to: {g}results.txt")

    except ValueError:
        exit(f"{r}Input error! Please enter valid numbers.")
    except KeyboardInterrupt:
        exit(f"\n{r}Interrupted by user. Exiting...{x}")

# Fungsi Admin Finder (tanpa delay)
def admin_finder():
    clear_screen()
    print_banner()
    try:
        domain = input(f" {b}{u}Domain{w}:{x} {y}")
        print()

        # Membaca daftar halaman login admin dari list.txt
        try:
            with open("list.txt", "r") as f:
                admin_pages = f.readlines()
                admin_pages = [page.strip() for page in admin_pages]
        except FileNotFoundError:
            exit(f"{r}File list.txt not found! Please create the file with admin pages list.")

        total = 0
        found_admin_pages = []
        for page in admin_pages:
            url = f"http://{domain}{page}"
            try:
                response = requests.get(url, timeout=5)  # default timeout tanpa input
                if response.status_code == 200:
                    print(f"{w}{total + 1}) {g}Found: {url}")
                    found_admin_pages.append(url)
                    total += 1
            except requests.exceptions.RequestException:
                continue

        if total == 0:
            print(f"{r}No admin login pages found for {domain}.")
        else:
            print(f"\n{w}Total Admin Pages Found: {g}{total}")
            with open("found_admin.txt", "a") as f:
                for admin_page in found_admin_pages:
                    f.write(f"{admin_page}\n")
            print(f"{w}Results saved to: {g}found_admin.txt")

    except KeyboardInterrupt:
        exit(f"\n{r}Interrupted by user. Exiting...{x}")

# Menu untuk memilih tools
def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{b}{u}Select a Tool:{w}\n")
        print(f"1) Dorking Tool")
        print(f"2) Admin Finder")
        print(f"0) Exit")
        
        choice = input(f" {b}{u}Your Choice:{w}{x} {y}")
        
        if choice == '1':
            dorking()
        elif choice == '2':
            admin_finder()
        elif choice == '0':
            print(f"{w}Exiting...{x}")
            exit()
        else:
            print(f"{r}Invalid choice! Please select a valid option.{x}")

# Menjalankan menu utama
main_menu()

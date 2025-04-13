# Author : Xyuraa
import requests
import os
import zipfile
from googlesearch import search
from threading import Thread, Queue
import time

# Warna
x = '\033[0m'
u = '\033[4m'
b = '\033[1;94m' 
g = '\033[0;92m'
y = '\033[0;33m'
w = '\033[0;37m'
r = '\033[0;91m'

# ... (clear_screen, print_banner, confirm_continue functions remain the same)
# ... (dorking and ip_lookup functions remain the same)

# Fitur 3: Brute Force ZIP (replaces bypass_admin_login)
def brute_force_zip():
    clear_screen()
    print_banner()
    print(f"{b}ZIP Password Brute Force{x}\n")
    
    try:
        # Input file ZIP
        zip_path = input(f" {b}{u}Path to ZIP file{w}:{x} {y}").strip()
        if not os.path.exists(zip_path):
            print(f"\n{r}File not found!{x}")
            return confirm_continue()

        # Input wordlist
        wordlist_path = input(f" {b}{u}Path to password wordlist (password.txt){w}:{x} {y}").strip()
        if not wordlist_path:
            wordlist_path = "password.txt"  # Default
            
        if not os.path.exists(wordlist_path):
            print(f"\n{r}Wordlist file not found!{x}")
            return confirm_continue()

        # Threading setup
        queue = Queue()
        found = False
        password = None

        def worker():
            nonlocal found, password
            while not queue.empty() and not found:
                test_pass = queue.get()
                try:
                    with zipfile.ZipFile(zip_path) as zf:
                        zf.extractall(pwd=test_pass.encode())
                    found = True
                    password = test_pass
                except (RuntimeError, zipfile.BadZipFile):
                    pass
                finally:
                    queue.task_done()

        # Read wordlist into queue
        with open(wordlist_path, 'r', errors='ignore') as f:
            for line in f:
                queue.put(line.strip())

        # Start threads
        thread_count = min(4, os.cpu_count() * 2)  # Conservative thread count
        threads = []
        for _ in range(thread_count):
            t = Thread(target=worker)
            t.start()
            threads.append(t)

        # Progress indicator
        print(f"\n{g}[+] Starting brute force...{x}")
        print(f"{w}Total passwords to try: {queue.qsize()}{x}")
        
        while not found and not queue.empty():
            print(f"{w}Trying... {queue.qsize()} remaining\r", end='')
            time.sleep(0.1)

        # Wait for completion
        queue.join()
        for t in threads:
            t.join()

        # Results
        clear_screen()
        print_banner()
        if found:
            print(f"\n{g}[+] PASSWORD FOUND!{x}")
            print(f"{w}File: {g}{zip_path}{x}")
            print(f"{w}Password: {g}{password}{x}")
            with open("cracked_zips.txt", "a") as f:
                f.write(f"{zip_path}:{password}\n")
            print(f"\n{w}Results saved to: {g}cracked_zips.txt{x}")
        else:
            print(f"\n{r}[-] Password not found!{x}")

        confirm_continue()

    except KeyboardInterrupt:
        print(f"\n{r}[-] Stopped by user!{x}")
        confirm_continue()
    except Exception as e:
        print(f"\n{r}[!] Error: {str(e)}{x}")
        confirm_continue()

# Menu utama (updated to show brute force instead of bypass)
def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{b}{u}Select a Tool:{w}\n")
        print(f"1) Dorking Tool")
        print(f"2) IP Lookup")
        print(f"3) Brute Force ZIP")  # Changed from "Bypass Admin Login"
        print(f"0) Exit")
        
        choice = input(f" {b}{u}Your Choice:{w}{x} {y}")
        
        if choice == '1':
            dorking()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            brute_force_zip()  # Changed from bypass_admin_login()
        elif choice == '0':
            print(f"{w}Exiting...{x}")
            exit()
        else:
            print(f"{r}Invalid choice! Please select a valid option.{x}")

# Jalankan
if __name__ == "__main__":
    main_menu()

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
                                                         
                  Author: Xyura01 (Modified by AI)
{x}""")

# Confirm
def confirm_continue():
    print(f"\n{b}Lanjut?{x}")
    print("1) Kembali ke Menu")
    print("0) Keluar")
    pilihan = input(f" {b}Pilih:{x} {y}")
    if pilihan == '1':
        return True
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
        delay = int(input(f" {b}{u}Delay (min 2s){w}:{x} {y}"))
        
        print(f"\n{g}[+] Searching...{x}")
        
        results = []
        try:
            for result in search(dork, num=pages, stop=pages, pause=max(2, delay)):
                results.append(result)
                print(f"{g}[+] Found: {w}{result}")
        except Exception as e:
            print(f"{r}[!] Error: {e}{x}")
            return confirm_continue()

        clear_screen()
        print_banner()
        print(f"{g}Hasil Dorking ({len(results)} hasil):\n{x}")
        
        with open('results.txt', 'w') as f:
            for i, res in enumerate(results, 1):
                print(f"{w}{i:2d}) {g}{res}")
                f.write(f"{res}\n")

        print(f"\n{w}Saved to: {g}results.txt")
    except ValueError:
        print(f"{r}Input harus angka!{x}")
    except Exception as e:
        print(f"{r}[!] Unexpected error: {e}{x}")
    finally:
        confirm_continue()

# Fitur 2: IP Lookup
def ip_lookup():
    clear_screen()
    print_banner()
    try:
        ip = input(f" {b}{u}Enter IP Address{w}:{x} {y}").strip()
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
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
        print(f"\n{r}Interrupted by user.{x}")
        confirm_continue()
    except Exception as e:
        print(f"{r}Failed to fetch IP info: {e}")
        confirm_continue()

# Fitur 3: Web Vulnerability Scanner (New)
def web_vuln_scanner():
    clear_screen()
    print_banner()
    print(f"{b}WEB VULNERABILITY SCANNER{x}\n")
    
    try:
        target_url = input(f" {b}{u}Target URL (contoh: https://example.com){w}:{x} {y}").strip()
        if not target_url.startswith(('http://', 'https://')):
            target_url = f"http://{target_url}"

        print(f"\n{g}[+] Memulai scan kerentanan...{x}")
        print(f"{w}Target: {g}{target_url}{x}\n")

        tests = [
            {"name": "SQL Injection", "payload": "' OR '1'='1"},
            {"name": "XSS", "payload": "<script>alert('XSS')</script>"},
            {"name": "Path Traversal", "payload": "../../../../etc/passwd"},
            {"name": "Command Injection", "payload": ";ls -la"}
        ]

        found_vulns = []
        for test in tests:
            try:
                vuln_url = f"{target_url}?test={requests.utils.quote(test['payload'])}"
                res = requests.get(vuln_url, timeout=5)
                
                if ("error" in res.text.lower() and "sql" in res.text.lower()) or \
                   ("warning" in res.text.lower() and "mysql" in res.text.lower()):
                    print(f"{r}[VULN] {w}{test['name']} terdeteksi!{x}")
                    found_vulns.append(test['name'])
                elif test['payload'] in res.text:
                    print(f"{r}[VULN] {w}{test['name']} mungkin rentan!{x}")
                    found_vulns.append(test['name'])
                else:
                    print(f"{g}[SAFE] {w}{test['name']} tidak terdeteksi{x}")
            
            except Exception as e:
                print(f"{r}[ERROR] Gagal test {test['name']}: {str(e)}{x}")

        if found_vulns:
            with open("vuln_results.txt", "a") as f:
                f.write(f"{target_url} | Vuln: {', '.join(found_vulns)}\n")
            print(f"\n{g}[+] Hasil disimpan di vuln_results.txt{x}")
        else:
            print(f"\n{y}[!] Tidak ada kerentanan yang ditemukan{x}")

        confirm_continue()

    except KeyboardInterrupt:
        print(f"\n{r}[!] Scan dihentikan{x}")
        confirm_continue()

# Menu utama
def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{b}{u}Select a Tool:{w}\n")
        print(f"1) Dorking Tool")
        print(f"2) IP Lookup")
        print(f"3) Web Vulnerability Scanner")
        print(f"0) Exit")
        
        choice = input(f" {b}{u}Your Choice:{w}{x} {y}")
        
        if choice == '1':
            dorking()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            web_vuln_scanner()
        elif choice == '0':
            print(f"{w}Exiting...{x}")
            exit()
        else:
            print(f"{r}Invalid choice! Please select a valid option.{x}")

# Jalankan
if __name__ == "__main__":
    main_menu()

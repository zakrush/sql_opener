import requests
import re
import colorama
from validator.valid_checkers import url_validator

colorama.init(autoreset=True)


def search_vuln(site):
    check_site = url_validator(site)
    if check_site:
        payloads = ["'", '"']
        is_vuln = False

        for payload in payloads:
            try:
                res = requests.get(site + payload)
            except Exception as e:
                print(f'{colorama.Fore.RED}Error: {site}: {e}')
                is_vuln = True
                break
            else:
                if 500 <= res.status_code <= 526 or res.status_code == 404:
                    print(f'{colorama.Fore.RED}{site} return {res.status_code}')
                    is_vuln = True
                    break
                else:
                    if re.search("SQL syntax", res.text) is not None:
                        print(site, '===>', colorama.Fore.GREEN + f"Vulnerable by {payload}")
                        is_vuln = True
                        break
        if not is_vuln:
            print(site, '===>', colorama.Fore.RED + 'Not Vulnerable!')
    else:
        print(f'{colorama.Fore.RED}ERROR: {site}  is not valid!')


def mass_search(file):
    try:
        with open(file, 'r') as f:
            for site in f.read().splitlines():
                search_vuln(site)
    except FileNotFoundError as e:
        print(e)

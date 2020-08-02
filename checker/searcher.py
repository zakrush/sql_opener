import requests
import re
import colorama
from validator.valid_checkers import url_validator

colorama.init(autoreset=True)


def check_request(site):
    """
    Checking response of site.
    :param site: given url with payload
    :return: turple. True or False(True if request return Exeption or 5** and 404 response) and result of request
    """
    try:
        res = requests.get(site)
    except Exception as e:
        return True, e
    else:
        if 500 <= res.status_code <= 526 or res.status_code == 404:
            return True, res
        else:
            return False, res


def printer(text):
    """For printing data about site response and Vulnarability"""
    print(text)


def search_vuln(site, is_print=True):
    """
    Checking site for SQL Injection Vulnarability
    :param site: Url for checking. e.g. http://example.org/searcher.php?id=1
    :param is_print: print or not result. Default is true
    :return: is_vuln and msg
    """
    check_site = url_validator(site)
    is_vuln, is_err = False, False
    msg = ''
    if check_site:
        payloads = ["'", '"']

        # cheking every payload
        for payload in payloads:
            is_err, res = check_request(site + payload)
            # checking result of request. Exeption or not
            if type(res) is not requests.models.Response:
                msg = f'\033[0;31mERROR: {site}: {res}'
                break
            else:
                if is_err:
                    print(f'\033[0;31m{site} return {res.status_code}')
                    break
                # if not 5** or 404 error search error
                else:
                    if re.search("SQL syntax", res.text) is not None:
                        msg = f"{site}   ===>  \033[0;32mVulnerable by {payload}"
                        is_vuln = True
                        break
        if not (is_vuln or is_err):
            msg = f"{site}  ===>  \033[0;35mNot Vulnerable!"

    else:
        msg = f'\033[0;31mERROR: {site}  is not valid!'
    # printing result if needed.
    if is_print:
        printer(msg)
    return is_vuln, msg


def mass_search(file):
    try:
        with open(file, 'r') as f:
            for site in f.read().splitlines():
                search_vuln(site)
    except FileNotFoundError as e:
        print(e)


# search_vuln('http://fdsafafaa.com/')
# search_vuln('http://leettime.net/sqlninja.com/tasks/basic_ch2.php?id=1')
# mass_search('/home/dmitriy/Pentest_Python/sql_opener/sites.txt')

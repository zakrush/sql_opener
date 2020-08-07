import requests
import re
import colorama
from validator.valid_checkers import url_validator, check_res, find_pattern
import exploit

colorama.init(autoreset=True)


def search_vuln(site, is_print=True, is_pattern=False):
    """
    Checking site for SQL Injection Vulnarability
    :param is_pattern: enabling finding tag of output
    :param site: Url for checking. e.g. http://example.org/searcher.php?id=1
    :param is_print: print or not result. Default is true
    :return: is_vuln and msg
    """
    check_site = url_validator(site)
    is_vuln, is_err = False, False
    msg, pattern, payload = '', '', ''
    if check_site:
        payloads = ["'", '"']

        # cheking every payload
        for payload in payloads:
            chk_res = check_res(site + payload)
            # checking result of request with payload. If check_res return oly one argunemt it give Exception
            if len(chk_res) == 4:
                is_err, msg = True, f'\033[0;31mERROR: {site}: {chk_res[2]}'
                break
            elif len(chk_res) == 3:
                is_err, msg = True, f'\033[0;31m{site} return {chk_res[1].status_code}'
                break
            # if not 5** or 4** error search error
            else:
                if re.search("SQL syntax", chk_res[0].text) is not None:
                    msg = f"{site}   ===>  \033[0;32mVulnerable by {payload}"
                    is_vuln = True
                    if is_pattern:
                        pattern = find_pattern(chk_res[0])
                    break
        if not (is_vuln or is_err):
            msg = f"{site}  ===>  \033[0;35mNot Vulnerable!"

    else:
        msg = f'\033[0;31mERROR: {site}  is not valid!'
    # printing result if needed.
    if is_print:
        print(msg)
    return is_vuln, msg, pattern, payload


def mass_search(file):
    try:
        with open(file, 'r') as f:
            for site in f.read().splitlines():
                search_vuln(site)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    # search_vuln('https://en7-vpr.sdamgia.ru/test?id=1"')
    # search_vuln('http://leettime.net/sqlninja.com/tasks/basic_ch2.php?id=1')
    mass_search('sites.txt')

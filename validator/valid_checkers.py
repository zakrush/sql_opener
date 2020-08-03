import re
import requests
from bs4 import BeautifulSoup


def find_pattern(response):
    soup = BeautifulSoup(response.text, 'lxml')
    param = soup.find(text=re.compile('SQL syntax')).parent.name
    return param


def url_validator(url):
    res = re.match(r'http(s)?://(www.)?[a-zA-Z0-9@:%._+~#=\-]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)', url)
    if res:
        return res.group()
    else:
        return None


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


def check_res(site):
    """
    Processing of check_request for minimum  condition  in finish functions.
    Return of this func processing by len of return with TypeError exeption.
    :param site: site for check
    :return: 4 arguments if res returned Exeption.
             3 arguments if response give 5** or 404 status code
             2 argument if all good.
    """
    err, res = check_request(site)
    if type(res) is not requests.models.Response:
        return True, err, res, site
    else:
        if err:
            return err, res, site
        else:
            return res, site

# http://leettime.net/sqlninja.com/tasks/basic_ch1.php?id=1

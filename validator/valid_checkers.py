import re


def url_validator(url):
    res = re.match(r'http(s)?://(www.)?[a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)', url)
    if res:
        return res.group()
    else:
        return None


# http://leettime.net/sqlninja.com/tasks/basic_ch1.php?id=1


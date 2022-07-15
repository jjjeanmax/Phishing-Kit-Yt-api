import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


def _getOpenphishFeed():
    url = "https://openphish.com/feed.txt"
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'lxml')

    with open('url.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())


# ------ Openphish Feed _______
url = 'https://www.wallet-polygon.login-en.com/'
url2 = 'https://dev-duesk546.pantheonsite.io/wp-admin/vrde/vr/73121/Login.html'
url3 = 'http://pagewsusatyrtsaccounts.co.vu/confirmid.php'
url4 = 'http://u1728166.plsk.regruhosting.ru/rSEhSIfaMi/index.php'


def listPhishingKit():
    # Input validation
    if len(sys.argv) == 1:
        print('Usage: %s <PUT URL>' % sys.argv[0])
        sys.exit(1)

    php_in_url = []
    try:
        url = ' '.join(sys.argv[1:])
        path = urlparse(url).path
        if 'php' in path:
            list_path = path.split("/")
            php_in_url.append(list_path[-1])

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        err = soup.find("title").get_text()
        if err == "Error":
            return ["Error Connection"]
        action = soup.find('form').get('action')
        res = [node.get('href') for node in soup.find_all('a', href=True)]
        res.extend(php_in_url)
        # webshell in php file
        if 'php' in action:
            res.append(action)
        else:
            pass
        return res
    except AttributeError:
        pass


try:
    print("Phishing kit AND Web shell:")
    print(" ")
    for file in listPhishingKit():
        print(file)
except TypeError as e:
    print(e)

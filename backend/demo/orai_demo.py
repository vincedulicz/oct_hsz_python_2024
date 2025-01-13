import requests
from bs4 import BeautifulSoup

def find_first_h1(soup):
    title = soup.find('h1') # első h1 tag
    if title:
        print("first h1 tag", title.text)

    # find all p
    ps = soup.find_all('p') # minden p tag
    for p in ps:
        print(p.text)

    # find_next_after_h1
    first_h1 = soup.find('h1')
    next_element = first_h1.find_next() if first_h1 else None

    if next_element:
        print("next element after h1:", next_element.text)

    # find parent of link
    link = soup.find('a')
    parent_div = link.find_parent('div') if link else None

    if parent_div:
        print(parent_div)

    # next sibling
    first_h1 = soup.find('h1')
    next_sibling = first_h1.find_next_sibling() if first_h1 else None

    if next_sibling:
        print(next_sibling)

    # find all prev before div
    first_div = soup.find('div')
    if first_div:
        prev_p = first_div.find_all_previous('p')
        for p in prev_p:
            print(p.text)

    # select
    titles = soup.select('h1')
    for title in titles:
        print("h1 tag:", title.text)

    # get text from div
    div_content = soup.find('div')
    if div_content:
        print(div_content.get_text())



def login_to_website():
    session = requests.Session()

    login_url = "https://example.com/login"
    credentials = {'username': 'user', 'password': 'pass'}

    response = session.post(login_url, data=credentials)

    if response.status_code == 200:
        print("login success")
    else:
        print("login failed")

    profile_url = 'https://example.com/profile'
    profile_response = session.get(profile_url)

    print(profile_response.text)


def cookie_session():
    session = requests.Session()

    url = 'http://example.com/set-cookie'
    response = session.get(url)

    print(session.cookies.get_dict()) # összes süti

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
    session.headers.update(headers)


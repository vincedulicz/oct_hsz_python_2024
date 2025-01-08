import requests


def kezdet_req():


    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:
        print("sikeres kérés:", response.json())
    else:
        print(f"hiba: {response.status_code}")



def prookt_img():
    url = "https://prooktatas.hu/assets/img/prooktatas-programozo-kepzes-online.png"

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open("letoltott_kep.jpg", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print("kép sikeresen letöltve")
    else:
        print(f"hiba: {response.status_code}")



def bs4():
    from bs4 import BeautifulSoup

    url = "https://telex.hu/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text
        print(f'Oldal címe: {title}')
    else:
        print("nem elérhető")


def telex_kep_letolto():
    import os

    url = "https://telex.hu/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        os.makedirs('images', exist_ok=True)

        for img in images:
            src = img.get('src')
            if src:
                img_url = src if src.startswith("http") else url + src

                img_response = requests.get(img_url, stream=True)

                if img_response.status_code == 200:
                    file_name = os.path.join("images", os.path.basename(img_url))

                    with open(file_name, "wb") as file:
                        for chunk in img_response.iter_content(1024):
                            file.write(chunk)
        print("minden kép letöltve")
    else:
        print("valami hiba")



def api_201():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}

    response = requests.post(url, json=data)
    if response.status_code == 201:  # created
        print("erőforrás létrejött: ", response.json())


def redirect():
    response = requests.get("http://httpbin.org/redirect/1", allow_redirects=False)
    print(f'átirányítás: {response.status_code}')


def api_404():
    response = requests.get("http://httpbin.org/status/404")
    print(f'404 példa: {response.status_code}')


def api_500():
    response = requests.get("http://httpbin.org/status/500")
    print(f'500 példa: {response.status_code}')


def github_api():
    url = "https://api.github.com/search/repositories"
    params = {'q': 'python', 'sort': 'stars'}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json()["items"][0]["full_name"])


def post_keres():
    url = "https://httpbin.org/post"
    data = {"name": "tesztElek", "language": "Python"}

    response = requests.post(url, json=data)

    print("válasz json", response.json())


def try_except():
    try:
        response = requests.get("https://prookatas.hu/", timeout=1)
        response.raise_for_status()
        print("sikeres kérés")
    except requests.exceptions.Timeout:
        print("időtúllépés")
    except requests.exceptions.RequestException as e:
        print("Hiba történt: ", e)


url = "https://jsonplaceholder.typicode.com/posts/1"
data = {"id": 1, "title": "foo", "body": "bar", "userId": 1}

response = requests.put(url, json=data)
print(response.status_code)
print(response.json())

response = requests.delete(url)

print(response.status_code)

response = requests.head(url)
print(response.headers)

response = requests.options(url)
print(response.headers)

headers = {"Auth": "Bearer token"}
response = requests.get(url, headers=headers)

cookies = {"session_id": "12345"}
response = requests.get(url, cookies=cookies)

proxies = {"http": "http://10.10.1.10:3128", "https": "https://10.10.1.10:1080"}
response = requests.get(url, proxies=proxies)


# Exceptions

"""
requests.exceptions.Timeout: Időtullépés
requests.exceptions.TooManyRedirects: Túl sok átirányítás
requests.exceptions.RequestException: Általános hiba
"""

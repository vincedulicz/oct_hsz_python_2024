import requests

def i_fel():
    response = requests.get("https://httpbin.org/get")
    print(response.json())

def ii_fel():
    params = {"name": "Student", "course": "Python"}
    response = requests.get("https://httpbin.org/get", params=params)
    print(response.json())

def iii_fel():
    data = {"title": "Hello", "message": "World"}
    response = requests.post("https://httpbin.org/post", json=data)
    print(response.json())

def iv_fel():
    headers = {"Authorization": "Bearer token123", "Custom-Header": "MyValue"}
    response = requests.get("https://httpbin.org/headers", headers=headers)
    print(response.json())

def v_fel():
    response = requests.get("https://httpbin.org/ip")
    print(response.json())

def vi_fel():
    try:
        response = requests.get("https://httpbin.org/delay/3", timeout=2)
        print(response.json())
    except requests.exceptions.Timeout:
        print("Időtullépés")

def vii_fel():
    response = requests.get("https://httpbin.org/redirect/2", allow_redirects=True)
    print("végső url:", response.url)

def viii_fel():
    auth = ("user", "pass")
    response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=auth)
    print(response.status_code, response.json())

def ix_fel():
    status_code = [200, 404, 500]
    for code in status_code:
        response = requests.get(f'https://httpbin.org/status/{code}')
        print(f'státuszkód: '
              f'{response.status_code} - '
              f'{"Sikeres" if response.ok else "Hiba"}'
              )

def x_fel():
    response = requests.get(
        "https://httpbin.org/cookies/set?cookie_name=cookie_value")
    cookie_response = requests.get("https://httpbin.org/cookies")
    print(cookie_response.json())


if __name__ == "__main__":
    i_fel()
    ii_fel()
    iii_fel()
    iv_fel()
    v_fel()
    vi_fel()
    vii_fel()
    viii_fel()
    ix_fel()
    x_fel()


http://bestgame4ever.com/client=1001&attackUser(2000)&cookies=cookies
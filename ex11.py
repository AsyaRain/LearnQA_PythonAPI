import requests

def test_get_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    cookies = response.cookies
    print("Куки: ", cookies)
    assert cookies, "No cookies found in the response"
import requests

def test_get_headers():
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)
    headers = response.headers
    print("Headers: ", headers)
    assert headers, "No headers found in the response"

    for header_name, header_value in headers.items():
        assert header_value, f"Header '{header_name}' has an empty value"
        print(f"Header '{header_name}' value: {header_value}")

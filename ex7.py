import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. http-запрос любого типа без параметра method
response_1 = requests.get(url)
print("1. Запрос без параметра method:", response_1.text)

# 2. http-запрос не из списка (например, HEAD)
response_2_1 = requests.head(url)
print("2.1. http-запрос не из списка:", response_2.text)
response_2_2 = requests.options(url)
print("2.2. http-запрос не из списка:", response_2_1.text)

# 3. Запрос с правильным значением method
valid_methods = ['GET', 'POST', 'PUT', 'DELETE']
response_3 = requests.post(url, data={'method': 'POST'})
print("3. Корректный запрос:", response_3.text)

# 4. Все возможные сочетания реальных типов запроса и значений параметра method
for method in valid_methods:
    for param_method in valid_methods:
        if method != param_method:
            if method == 'GET':
                response = requests.get(url, params={'method': param_method})
            else:
                response = requests.request(method, url, data={'method': param_method})

            if response.status_code == 200:
                print(f"4. Mismatch - Actual Method: {method}, Param Method: {param_method}, Response: {response.text}")
            else:
                print(f"4. Match - Actual Method: {method}, Param Method: {param_method}, Response: {response.text}")

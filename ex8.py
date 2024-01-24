import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
#Первый запрос без параметра токен
response = requests.get(url)

json_response = response.json()
token = json_response["token"]
seconds = json_response["seconds"]
print(f"Токен = {token}, секунды = {seconds}")

#Запрос с токеном без ожидания
response = requests.get(url, params = {"token": token})
json_response = response.json()

status = json_response.get("status")

if status == "Job is NOT ready":
    print(f"Запрос с токеном до ожидания времени: {json_response}")
else:
    print("Задача готова")

# Ожидание
time.sleep(seconds)

#запрос с ожиданием
response = requests.get(url, params = {"token": token})
json_response = response.json()

status_after = json_response.get("status")

if status_after == "Job is ready":
    result = json_response.get("result")
    print(status_after, "=", result)
else:
    print(f"Ошибка: {json_response}")
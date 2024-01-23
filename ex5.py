import json

string_as_json_format = '{"json_text": {"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}}'
obj = json.loads(string_as_json_format)
print(obj)
#добавим немного отступов для читаемости
formatted_json = json.dumps(obj['json_text'], indent=2)
print(formatted_json)

#или 2 вариант
string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(string_as_json_format)
key = 'message'

if 'messages' in obj and isinstance(obj['messages'], list):
    for message_obj in obj['messages']:
        if key in message_obj:
            print(message_obj[key])
else:
    print(f"Ключа {key} в JSON нет")


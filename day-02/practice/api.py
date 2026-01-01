import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print(dir(response))

print(response)

print(response.json())
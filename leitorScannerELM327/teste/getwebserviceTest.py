import json, requests

response = requests.get("http://18.231.62.135:5000/collection")

print(response.status_code)

# print(response.content)

# print(json.load(response.content))
# print(response.content.decode())
dados = response.content.decode('utf8')

print(type(response.content))
print(type(dados))
dadosJson = json.loads(dados)

print(dadosJson)

print(type(dadosJson))
print(len(dadosJson))
print(dadosJson[0])
print(dadosJson[0]['tipo_combustivel'])
print(dadosJson)

# print(dados)
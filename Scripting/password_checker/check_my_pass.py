import requests

url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'
res = requests.get(url)
print(res)

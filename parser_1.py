from random import choice
import requests

url = 'http://httpbin.org/ip'

with open ('proxy_list') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {'http': f'http://{ip}', 'https': f'https://{ip}'}
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success')
        except Exception as e:
            continue


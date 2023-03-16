import requests
from random import choice

url='http://httpbin.org/user-agent'
while line := open('user_agent.txt').read().split('\n'):
    user_agent = {'User-Agent': choice(line)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)


from fake_useragent import UserAgent

url = 'http://httpbin.org/user-agent'

for x in range(10):
    ua = UserAgent()
    fake_ua = {'User-Agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)



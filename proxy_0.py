import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': '*/*'
        }
        self.gen_link = []
        self.completed_proxy_list = []
        self.page_count = 1

    def gen_links_lst(self):
        for offset in range(0, 921, 64):
            link = f'https://hidemy.name/ru/proxy-list/?start={offset}'
            self.gen_link.append(link)

    def get_html(self):
        try:
            for link in self.gen_link:
                response = requests.get(url=link, headers=self.headers)
                soup = BeautifulSoup(response.text, 'lxml')
                ip_port = soup.find('tbody').find_all('tr')
                for row in ip_port:
                    ip = row.find_all('td')[0].text
                    port = row.find_all('td')[1].text
                    self.completed_proxy_list.append(f"{ip}:{port}\n")
                print(f'Page: {self.page_count}, find proxy: {len(self.completed_proxy_list)}')
                self.page_count += 1
        except requests.exceptions.RequestException as ex:
            print(ex)

    def save_proxy_in_txt(self):
        with open('proxy_list.txt', 'w') as file:
            for proxy in self.completed_proxy_list:
                file.write(proxy)
        file.close()

    def main(self):
        self.gen_links_lst()
        self.get_html()
        self.save_proxy_in_txt()


if __name__ == '__main__':
    parser = Parser()
    parser.main()

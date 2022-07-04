import logging
from urllib import robotparser

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(filename)s | %(levelname)s: %(message)s')

ROBOTSTXT_URL = 'https://ru.wikipedia.org/robots.txt'
START_PAGE = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
BASIC_URL = 'https://ru.wikipedia.org/'

class PageParser:
    ok_status = 200

    def __init__(self, base_url, robots_txt):
        self.base_url = base_url
        self.robots = robotparser.RobotFileParser()
        self.robots.set_url(robots_txt)
        self.robots.read()
        self.loaded = False
        self.animals = dict()

    def load(self):
        logger.debug(self.base_url)
        i = 1
        fin = False
        while self.base_url:
            logger.debug('Page parsing: %s' % i)
            i += 1
            self.response = httpx.get(self.base_url)

            self.loaded = True

            self.page_exists = True

            if not self.appropriate_status_code():
                self.page_exists = False
                return

            if not self.robots_permit():
                self.page_exists = False
                return

            self.source = BeautifulSoup(self.response.text, 'html.parser')
            body = self.source.body
            body_content = body.find(id='bodyContent')
            next_page = body_content.find_all('a', title='Категория:Животные по алфавиту', text='Следующая страница', href=True)
            if next_page:
                self.base_url = BASIC_URL + next_page[0].get('href')
            else:
                self.base_url = None
            category_tables = body.find_all('div', class_='mw-category-group')
            for table in category_tables:
                for li in table.find_all('li'):
                    animal = li.string
                    if isinstance(animal, str):
                        letter = animal[0]
                        if letter == 'A':
                            fin = True
                            break
                        self.animals[letter] = self.animals.get(letter, 0) + 1
                if fin:
                    break
            if fin:
                break

    def robots_permit(self):
        if not self.robots.can_fetch('*', self.base_url):
            return False
        logger.debug('Crawl delay {0}'.format(self.robots.crawl_delay(self.base_url)))
        return True

    def appropriate_status_code(self):
        code = self.response.status_code
        logger.debug(code)
        if code != self.ok_status:
            logger.debug(f"Page doesn't exist for page. Status code {code}")
            return False
        return True

    def return_result(self):
        for letter in sorted(list(self.animals.keys())):
            print('{}: {}'.format(letter, self.animals[letter]))

        return self.animals

def main():
    parser = PageParser(base_url=START_PAGE, robots_txt=ROBOTSTXT_URL)
    parser.load()
    parser.return_result()

if __name__ == '__main__':
    main()
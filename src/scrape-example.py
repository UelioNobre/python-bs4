import requests
from bs4 import BeautifulSoup
from rich import print


def get_html_page(url):
    page = requests.get(url)
    html_page = page.text

    soup = BeautifulSoup(html_page, "html.parser")
    return soup


def get_page_news(soup):
    news = []

    article_filter = {"class": "tec--card tec--card--medium"}
    tag_filter = {"class": "tec--card__info"}
    title_filter = {"class": "tec--card__title"}
    date_filter = {"class": "tec--timestamp__item z--font-semibold"}
    time_filter = {"class": "z--truncate z-flex-1"}

    for post in soup.find_all("article", attrs=article_filter):
        item = {}
        item["tag"] = (post.find("div", attrs=tag_filter).a.string).strip()
        item["title"] = (post.find("h4", attrs=title_filter).a.string).strip()
        item["link"] = (post.find("h4", attrs=title_filter).a["href"]).strip()
        item["date"] = (post.find("div", attrs=date_filter).string).strip()
        item["time"] = (post.find("div", attrs=time_filter).string).strip()
        news.append(item)

    return news


url = "https://www.tecmundo.com.br/novidades"
content_html = get_html_page(url)
news = get_page_news(content_html)

print(news)

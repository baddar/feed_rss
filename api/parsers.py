import feedparser


def get_feed_data(url):
    url = f'{url}'
    data = feedparser.parse(url)
    return data
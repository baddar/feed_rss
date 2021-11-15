import feedparser


def get_feed_data(url):
    data = feedparser.parse(url)
    print(data)
    return data
import feedparser


def get_feed_data(urls):
    items = []
    for url in urls:
        data = feedparser.parse(f'{url}')
        items.append(data.entries)
    
    

    return items


import feedparser


def get_feed_data(urls):
    items = []
    sorted_data = []
    for url in urls:
        data = feedparser.parse(f'{url}')
        for i in range(len(data.entries)):
            if data.entries[i].title not in items:
                items.append(data.entries[i])
            sorted_data = sorted(items, key=lambda item: item["published"])[:10]
    return sorted_data

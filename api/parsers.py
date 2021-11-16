import feedparser


def get_feed_data(urls):
    items = []
    sorted_data = []
    for url in urls:
        data = feedparser.parse(f'{url}')
        items.append(data.entries)
    for i in range(len(items)):
        sorted_data.append(sorted(items[i], key=lambda item: item.published)[:20])
    print(sorted_data)
    return sorted_data


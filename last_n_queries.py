__all__ = ['last_n_queries']

def last_n_queries(n=20):
    from urllib.request import build_opener

    if n < 1:
        print("n must be greater than zero")
        return 
    link = "http://stat.yandex.ru/queries/last20.xml"
    opener = build_opener()    
    opener.addheaders = [("User-agent", "Chrome/23.0"),
                        ("Cookie", "yandexuid=1240511381353477970")]
    while n > 20:
        page = opener.open(link).read().decode("UTF-8")
        for counter in range(20):
            index = page.find('''<a class="b-link" href="http://www.yandex.ru/yandsearch?text=''')
            start = 1 + page.find(">", index)
            end = page.find("</a>", index)
            print(page[start:end])
            page = page[end:]
        n -= 20
    page = opener.open(link).read().decode("UTF-8")
    for counter in range(n):
        index = page.find('''<a class="b-link" href="http://www.yandex.ru/yandsearch?text=''')
        start = 1 + page.find(">", index)
        end = page.find("</a>", index)
        print(page[start:end])
        page = page[end:]
            
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        last_n_queries(int(sys.argv[1]))
    else:
        last_n_queries()

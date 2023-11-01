import re

def extract_domain(url):
    pattern = r'(https?://)([a-zA-Z0-9.-]+)'
    match = re.match(pattern, url)
    if match:
        return match.group(2)
    else:
        return "error"

# Примеры использования:
test_urls = [
    "http://ya.ru/index.html",
    "https://wikipedia.org/",
     "ftp://some.server/",
    "https://ru.wikipedia.org/"
]

for url in test_urls:
    domain = extract_domain(url)
    print(f"Для ссылки {url} домен: {domain}")


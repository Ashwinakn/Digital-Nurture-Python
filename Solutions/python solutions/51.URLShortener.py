import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        hash_str = hashlib.md5(url.encode()).hexdigest()[:6]
        self.url_map[hash_str] = url
        return hash_str

    def lookup(self, short_url):
        return self.url_map.get(short_url, "URL not found")

def main():
    shortener = URLShortener()
    url = "https://www.google.com/"
    short = shortener.shorten(url)
    print(f"Short URL: {short}")
    print(f"Original URL: {shortener.lookup(short)}")

if __name__ == "__main__":
    main()

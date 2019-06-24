import requests
import xmltodict


def get_host(url):
    return url.split("//")[1].split("/")[0]


def get_name(url):
    return url.split(".")[1]




class SitemapParser:
    def __init__(self, urls=[], parent=""):
        self.urls = urls
        self.objs = []
        self.parent = parent

    def proccess_urls(self):
        for url in self.urls:
            sitemapurl = url

            response = requests.get(sitemapurl)
            list = xmltodict.parse(response.text)

            list2 = []
            for e in list["urlset"]["url"]:
                obj = {
                    "url": e["loc"],
                    "udpated": e["lastmod"]
                }

                list2.append(obj)
                break

            obj = {
                "host": get_host(sitemapurl),
                "name": get_name(sitemapurl),
                "size": len(list2),
                "urls": list2
            }

            self.objs.append(obj)

    def __proccess_patent(self):
        response = requests.get(self.parent)
        list = xmltodict.parse(response.text)

        for e in list["sitemapindex"]["sitemap"]:
            self.urls.append(e["loc"])

    def load(self):
        """
        load() populates the `objs` class properties with a dictionaries that look like:
        {
            "host": "www.example.com",
            "name": "example",
            "size": 2,
            "urls":[
                "https://www.example.com/welcome.html",
                "https://www.example.com/another_page"
            ]
        }
        """

        # If parent exists, load urls from the parent url
        if len(self.parent) > 0:
            self.__procces_parent()

        # Process URLs
        self.proccess_urls()


# Test #
if __name__ == "__main__":
    listStrings = [
        "https://www.walmart.com/sitemap_tp1.xml",
        "https://www.walmart.com/sitemap_bp1_https.xml"
    ]
    parser = SitemapParser(listStrings)

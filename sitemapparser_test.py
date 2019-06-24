import unittest
import sitemapparser


class TestSitemapparser(unittest.TestCase):
    def test_get_host(self):
        h = "https://www.example.com"

        host = sitemapparser.get_host(h)

        self.assertEqual("www.example.com", host)

    def test_get_name(self):
        h = "https://www.example.com"

        name = sitemapparser.get_name(h)

        self.assertEqual("example", name)

    def test_parse_case_two(self):
        url_example = [
            "https://www.walmart.com/sitemap_tp1.xml",
            "https://www.walmart.com/sitemap_bp1_https.xml"
        ]
        parser = sitemapparser.SitemapParser(url_example)

        parser.load()

        self.assertTrue(len(parser.objs) > 0)


if __name__ == '__main__':
    unittest.main()

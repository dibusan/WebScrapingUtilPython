import unittest
import robotstxt


class TestRobotsText(unittest.TestCase):

    def test_new_agent_ContainsKeys(self):
        agent = robotstxt.new_agent("Lorem")

        self.assertTrue(robotstxt.NAME_KEY in agent)
        self.assertTrue(robotstxt.ALLOW_KEY in agent)
        self.assertTrue(robotstxt.DISALLOW_KEY in agent)

    def test_is_comment_True(self):
        line = "# Some test line"

        self.assertTrue(robotstxt.is_comment(line))

    def test_is_comment_False_for_string(self):
        line = "This is not a comment line"

        self.assertFalse(robotstxt.is_comment(line))

    def test_is_comment_False_for_empty_line(self):
        line = "\n"

        self.assertFalse(robotstxt.is_comment(line))

    def test_parse(self):

        robot_parser = robotstxt.RobotsText(text=ROBOT_TEXT_EXAMPLE)

        robot_parser.parse()

        self.assertEqual(len(robot_parser.sitemaps), 5)

        self.assertEqual( len(robot_parser.user_agents), 3)

    def test_parse_with_url(self):
        robot_parser = robotstxt.RobotsText(url="https://www.walmart.com/robots.txt")

        robot_parser.parse()

        self.assertEqual(len(robot_parser.sitemaps), 5)



ROBOT_TEXT_EXAMPLE = """
#Sitemaps-https
Sitemap: https://www.walmart.com/sitemap_topic.xml
Sitemap: https://www.walmart.com/sitemap_browse.xml
Sitemap: https://www.walmart.com/sitemap_category.xml
Sitemap: https://www.walmart.com/sitemap_store_main.xml
Sitemap: https://www.walmart.com/sitemap_ip.xml

#Disallow select URLs
User-agent: *
Disallow: /0/
Disallow: /55875582/walmart-us/catalog/
Disallow: /account/
Disallow: /api/
Disallow: /collection/api/logger
Disallow: /cp/-201
Disallow: /cp/-302
Disallow: /cp/-306
Disallow: /cp/-309
Disallow: /cp/-506
Disallow: /cp/-509
Disallow: /cp/api/logger
Disallow: /cp/api/wpa
Disallow: /cservice/
Disallow: /cservice/ya_index.gsp
Disallow: /electrode/api/logger
Disallow: /email_collect/
Disallow: /giftregistry/
Disallow: /msp
Disallow: /nonConfig/api/wpa
Disallow: /popup_security.jsp
Disallow: /product/electrode/api/logger
Disallow: /product/electrode/api/wpa
Disallow: /reviews/
Allow: /reviews/product/
Disallow: /reviews/seller/
Disallow: /search
Disallow: /search/api/wpa
Disallow: /search/search-ng.do
Disallow: /solutions/
Disallow: /store/ajax/detail-navigation
Disallow: /store/ajax/local-store
Disallow: /store/ajax/preferred
Disallow: /store/ajax/search
Disallow: /store/ajax/visited-store
Disallow: /store/category/
Disallow: /store/electrode/api/fetch-coupons
Disallow: /store/electrode/api/logger
Disallow: /store/electrode/api/p13n
Disallow: /store/electrode/api/search
Disallow: /store/electrode/api/stores
Allow: /store/finder
Disallow: /store/popular_in_grade/
Disallow: /storeLocator/
Disallow: /storeLocator/ca_storefinder_results.do
Disallow: /tealeaf
Disallow: /topic/electrode/api/logger
Disallow: /topic/electrode/api/wpa
Disallow: /typeahead/
Disallow: /wmflows/

#Crawler specific settings
User-agent: Adsbot-Google

User-agent: Mediapartners-Google
"""

if __name__ == '__main__':
    unittest.main()

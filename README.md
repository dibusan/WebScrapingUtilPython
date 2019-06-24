# WebCrawlingUtil

## Objective
Provide useful functionality, common to any web crawling project

## Features
- RobotsText class parses the contents of a /robots.txt file into python data structures. It can receive the raw text or a url to fetch.
- SitemapParser class loads a list of given urls and extracts all urls within it. It can receive a sitemapindex url instead through the `parent` variable, which will load all the sitemaps on that index and then process them.

## Examples

### RobotsText
example.py
      from WebCrawlingUtil import RobotsText

      robot_parser = RobotsText(text=ROBOT_TEXT_EXAMPLE)

      robot_parser.parse()

      # Prints the list of sitemap URLs in the robots text if any
      print(robot_parser.sitemaps)

      # user_agents is a list of dictionaries each with User-Agent specific info found in the file
      # {
      #  'name':'Adsbot-Google',
      #  'Allow':[
      #    '/aaaa/\*',
      #    '/bbbb/\*'
      #  ],
      #  'Disallow':[
      #    '/yyyy/\*',
      #    '/xxxx/\*'
      #  ]
      #}

      print(robot_parser.user_agents)


### SitemapParser
example.py
      from WebCrawlingUtil import SitemapParser

      url_examples = [
          "https://www.example.com/sitemap_1.xml",
          "https://www.example.com/sitemap_2.xml"
      ]
      parser = SitemapParser(url_examples)

      parser.load()

      # load() populates the 'objs' class variable with a list of these objects:
      #{
      #   "host": "www.example.com",
      #    "name": "example",
      #    "size": 2,
      #    "urls":[
      #        "https://www.example.com/welcome.html",
      #        "https://www.example.com/another_page"
      #    ]
      #}

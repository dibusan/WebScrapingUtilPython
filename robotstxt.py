import requests


SITEMAP_KEY = "Sitemap"
USERAGENT_KEY = "User-agent"
DISALLOW_KEY = "Disallow"
ALLOW_KEY = "Allow"

NAME_KEY = "name"

SPACE = " "
COMMENT_HEADER = "#"


def new_agent(name):
    return {
        NAME_KEY: name,
        ALLOW_KEY: [],
        DISALLOW_KEY: []
    }


def is_comment(line):
    for c in line:
        if c != SPACE:
            return c == COMMENT_HEADER

    return False


def decompose(line):
    if line.strip() == "" or is_comment(line.strip()):
        return None, None

    key = line[:line.index(":")]
    val = line[line.index(":")+1:]

    return key, val


class RobotsText:
    def __init__(self, url="", text="", host="", name=""):
        self.url = url
        self.text = text
        self.host = host
        self.name = name
        self.sitemaps = []
        self.user_agents = []

    def __load_from_url(self):
        resp = requests.get(self.url)
        self.text = resp.text

    def parse(self):

        if self.url:
            self.__load_from_url()

        agent_is_open = False
        current_agent = None

        lines = self.text.split("\n")
        for line in lines:
            key, val = decompose(line)

            if not key:
                # key and val will be None when the line is a comment or empty
                continue

            if key == SITEMAP_KEY:
                self.sitemaps.append(val)
            elif key == USERAGENT_KEY:
                if agent_is_open:
                    # If there is an open agent then we are done with it, add it to the list and reset the agent.
                    self.user_agents.append(current_agent)

                agent_is_open = True
                current_agent = new_agent(val)

            elif agent_is_open and (key == ALLOW_KEY or key == DISALLOW_KEY):
                current_agent[key].append(val)

        # append the last agent seen
        self.user_agents.append(current_agent)

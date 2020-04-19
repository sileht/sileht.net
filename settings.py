SITENAME = "Random things I work on"
SITESUBTITLE = "From Mehdi Abaakouk (sileht)"

SITENAME = "Mehdi Abaakouk (sileht)"
SITESUBTITLE = "Random things I work on"

SITEIMAGE = "/static/logo.png"
SITEURL = ""
AUTHOR = "Mehdi Abaakouk"
TIMEZONE = "Europe/Paris"

LINKS = []
ICONS = [
    ("twitter", "http://twitter.com/sileht"),
    ("github", "http://github.com/sileht"),
    ("linkedin", "http://fr.linkedin.com/pub/mehdi-abaakouk/24/9b0/27/"),
    ("envelope", "mailto:sileht@sileht.net"),
    ("key", "https://keybase.io/sileht"),
]

THEME = "pelican-alchemy/alchemy"
HIDE_AUTHORS = True
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 30

TYPOGRIFY = True
MARKUP = ("rst", "md", "mkd")

STATIC_PATHS = ["static"]

ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
INDEX_SAVE_AS = "blog.html"

GOOGLE_ANALYTICS_UNIVERSAL = "UA-4618550-4"
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = "auto"

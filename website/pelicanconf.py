AUTHOR = 'Sébastien Deschamps'
SITENAME = 'AthIete - Better yourself'
SITEURL = "https://sebastiendes.github.io/athiete_web"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Liquipedia", "https://liquipedia.net/"),
    ("Pelican", "https://getpelican.com/"),
    ("Theme", "https://www.smashingmagazine.com/2009/08/designing-a-html-5-layout-from-scratch/")
)

# Social widget
SOCIAL = (
    ("LinkedIn - AthIete", "https://www.linkedin.com/company/athiete/"),
    ("LinkedIn - Sébastien Deschamps", "https://fr.linkedin.com/in/s%C3%A9bastien-deschamps"),
    ("Google Scholar", "https://scholar.google.com/citations?user=m5vG4GYAAAAJ&hl=fr&oi=ao")
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('AthIete', '/pages/athiete.html'), 
             ('Games', '/pages/games.html'),
            ('About Us', '/pages/about-us.html')]

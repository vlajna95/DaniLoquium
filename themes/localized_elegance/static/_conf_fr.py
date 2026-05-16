import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


DEFAULT_LANG = "fr"
LOCALE = "fr_FR.UTF-8" # DEFAULT_LANG

AUTHOR = "Danijela Popović"
SITENAME = "Dani apprend français 💙🤍❤📑 | DaniLoquium"
SITESUBTITLE = "Je suis Dani, et j'apprends français!"
COPYRIGHT = "Copyright © " + THE_YEARS[2] + " " + SITENAME + ". Tous les droits réservés."
HOMEPAGE_TITLE = "Page d'accueil"
DEFAULT_CATEGORY = "Un peu de tout"
DEFAULT_DATE_FORMAT = "📅 %A, %-d %B %Y 🕰 %H:%M"
# SITEURL = "http://localhost"
# SITEURL = "http://127.0.0.1:1789"
SITEURL = "http://" + DEFAULT_LANG + ".daniloquium.xyz" # "http://vlajna95.github.io/apprenDANIamo"

STYLE__BACKGROUND = "linear-gradient(to bottom, #800080, #8b0000)" # purple to red wine
STYLE__COLOR = "#fafafa" # almost white

PATH = "content_" + DEFAULT_LANG
OUTPUT_PATH = "/var/www/DaniLoquium_fr" # "output_" + DEFAULT_LANG
DELETE_OUTPUT_DIRECTORY = True

CATEGORIES_SAVE_AS = "categories/index.html" # direct template
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
CATEGORY_URL = "categories/{slug}"
TAGS_SAVE_AS = "etiquettes/index.html" # direct template
TAGS_URL = "etiquettes/"
TAG_URL = "etiquettes/{slug}"
TAG_SAVE_AS = "etiquettes/{slug}/index.html"
ARCHIVES_SAVE_AS = "archives/index.html" # direct template
ARCHIVES_URL = "archives/"
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/{date:%d}/index.html"
SEARCH_URL = "recherche"
SEARCH_SAVE_AS = SEARCH_URL + "/index.html" # direct template

MENUITEMS_TITLE = "Liens utiles"
MENUITEMS = [
	("Cours avancé de catalan", "http://ca.daniloquium.xyz"),
	("Cours d'espéranto 💚", "http://eo.daniloquium.xyz"),
	("Cours d'italien 🇮🇹", "http://it.daniloquium.xyz/"),
	("Cours de russe 🇷🇺", "http://ru.daniloquium.xyz/"),
]

HOMEPAGE_NOTES_FILE = os.path.join("cat_details", "fr", "intro.txt")

# EXPORT_OPTIONS.pop("pdf")

I18N_SUBSITES = {
	"sr": {
		"LOCALE": "sr_RS.UTF-8@latin",
		"DEFAULT_DATE_FORMAT": "📅 %A, %-d %B %Y 🕰 %H:%M",
		"DEFAULT_CATEGORY": "Razno",
		"SITENAME": "Dani uči francuski " + SITENAME[-2:],
		"SITESUBTITLE": "Ja sam Dani i učim francuski!",
		"COPYRIGHT": "Copyright © " + THE_YEARS[2] + " " + SITENAME + ". Sva prava zadržana.",
		"HOMEPAGE_TITLE": "Početna",
	},
}

"""
SITEURL = "http://fr.daniloquium.xyz/new"
THEME = "themes/bs3b"
BOOTSTRAP_THEME = "pulse"
BS3B_URL = "http://fr.daniloquium.xyz/new"

ABOUT_ME = "🇷🇸 Данијела Поповић / 🇪🇸🇦🇩 Daniela Pópovich / 🇷🇴 Daniela Popovici 😁"
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISABLE_SIDEBAR_TITLE_ICONS = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_ON_BREADCRUMBS = True
PYGMENTS_STYLE = "autumn"
TWITTER_CARDS = True
TWITTER_USERNAME = "DJ_Dani_Serbia"
"""

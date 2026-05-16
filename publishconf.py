import os
import sys
sys.path.append(os.curdir)
# import locale
from pelicanconf import *


DEFAULT_LANG = "sr"
LOCALE = ("sr_RS.utf8@latin", "sr_RS.utf8", "sr.utf8", "sr.UTF8", "sr.UTF-8", "src", "sr") or DEFAULT_LANG
# locale.setlocale(locale.LC_ALL, "sr_RS.utf8@latin")

AUTHOR = "Danijela Popović"
AUTHORS = {
	"Danijela Popović": {
		"url": "http://daniloquium.xyz",
		"blurb": ":pink_heart::light_blue_heart:",
	}
}
SITENAME = "DaniLoquium"
SITESUBTITLE = "Razne teme i formati"
COPYRIGHT = "© " + THE_YEARS[2] + " " + SITENAME + ". Sva prava ljubomorno zadržana."
HOMEPAGE_TITLE = "Početna"
DEFAULT_CATEGORY = "Razno"
DEFAULT_DATE_FORMAT = "📅 %A, %-d. %B %Y. 🕰 %H:%M"
SITEURL = "http://daniloquium.xyz"

STYLE__BACKGROUND = "linear-gradient(to bottom right, #ffe4e1, #e0ffff, #f5f5f5)" # misty rose, light cyan, white smoke
STYLE__COLOR = "#000000" # black
STYLE__DEFAULT_LIST_STYLE_TYPE = "hearts"

SPEAKABLE_TEXT_DEFAULT_LANGUAGE = "sr" # DEFAULT_LANG
MARKDOWN["extension_configs"]["plugins.dp_enhancements.dp_speaktext_extension"]["default_language"] = SPEAKABLE_TEXT_DEFAULT_LANGUAGE
# SPEAKABLE_TEXT_VOICE_CHANGER = True

PATH = "content"
OUTPUT_PATH = "output"
DELETE_OUTPUT_DIRECTORY = True

CATEGORIES_SAVE_AS = "kategorije/index.html" # direct template
CATEGORY_SAVE_AS = "kategorije/{slug}/index.html"
CATEGORY_URL = "kategorije/{slug}"
TAGS_SAVE_AS = "tagovi/index.html" # direct template
TAGS_URL = "tagovi/"
TAG_URL = "tagovi/{slug}"
TAG_SAVE_AS = "tagovi/{slug}/index.html"
ARCHIVES_SAVE_AS = "arhiva/index.html" # direct template
ARCHIVES_URL = "arhiva/"
YEAR_ARCHIVE_SAVE_AS = "arhiva/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "arhiva/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS = "arhiva/{date:%Y}/{date:%m}/{date:%d}/index.html"
SEARCH_URL = "pretraga"
SEARCH_SAVE_AS = SEARCH_URL + "/index.html" # direct template

ARTICLE_ORDER_BY = "date"
NEWEST_FIRST_ARCHIVES = False

MENUITEMS_TITLE = "Korisni linkovi"
MENUITEMS = []

HOMEPAGE_NOTES_FILE = os.path.join("cat_details", "intro.txt")
# RADIO_URL = "http://daniloquium.xyz:8008/tetkino"
# RADIO_NAME = "🩷 Tetkin radio 🩵"
# RADIO_DESCRIPTION = "Uvek najbolja muzika"
# RADIO_DESCRIPTION = os.path.join("cat_details", "tetkino", "radio_page_description.txt")

QUOTES = None

# DISQUS_SITENAME = "daniloquium"

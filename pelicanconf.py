# -*- coding: utf-8 -*- #
import os
from datetime import datetime
import gettext
from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from markdown import Markdown
import pymdownx.emoji
from pymdownx.blocks.admonition import Admonition
from category_details import *

_ = gettext.gettext


THEME = "themes/localized_elegance"
AUTHOR = "Danijela Popović"
AUTHORS = {
	"Danijela Popović": {
		"url": "http://daniloquium.xyz",
		"blurb": "I like languages, reading, writing, music, programming. Oh, and I'm the proudest and happiest aunt in the world. I sincerely and with all my heart love my sister's children; I am enchanted by them! :pink_heart::light_blue_heart:",
	}
}
SITEURL = "http://daniloquium.xyz"
LOGO = SITEURL + "/images/logo_transparent.png"
DISPLAY_BREADCRUMBS = True

PATH_METADATA = "(?P<category>.*)/.*"
# FILENAME_METADATA = "(?P<slug>.*)"
DEFAULT_METADATA = {"trans_id": "", "image": LOGO}
STATIC_PATHS = ["audio", "docs", "images"]
PAGE_EXCLUDES = ["code"] + STATIC_PATHS
ARTICLE_EXCLUDES = ["code"] + STATIC_PATHS
CACHE_PATH = "cache"
CHECK_MODIFIED_METHOD = "mtime"
DELETE_OUTPUT_DIRECTORY = True

INDEX_SAVE_AS = "index.html" # direct template
ARTICLE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}"
CATEGORY_URL = "categories/{slug}"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
DRAFT_SAVE_AS = ""
DRAFT_URL = ""
DRAFT_LANG_SAVE_AS = ""
DRAFT_LANG_URL = ""
TIPUE_SEARCH = True
RADIO_SAVE_AS = "radio/index.html" # direct template
RADIO_URL = "radio"

DIRECT_TEMPLATES = ["index", "categories", "tags", "archives", "search", "404", "radio"]
TEMPLATE_EXTENSIONS = [".html", ".css"]
THEME_TEMPLATES_OVERRIDES = [os.path.join(".", "themes", "localized_elegance", "templates", "custom_templates")]
TEMPLATE_PAGES = {
	"custom.css": os.path.join("theme", "css", "custom.css"),
	"speakable.js": os.path.join("theme", "js", "speakable.js"),
	"radio/radio_style.css": os.path.join("theme", "radio", "radio_style.css"),
	"radio/radio_script.js": os.path.join("theme", "radio", "radio_script.js"),
}

STYLE__DEFAULT_FONT_FAMILY = '"Merriweather", Georgia, serif'
STYLE__HEADING_FONT_FAMILY = '"Montserrat", sans-serif'
STYLE__BACKGROUND = "linear-gradient(to bottom, #f5f5dc, #3e2723)" # beige to dark brown
STYLE__COLOR = "#ffffff"
STYLE__HEADING_COLOR = STYLE__COLOR
STILE__LINK_COLOR = "#cccccc"
STYLE__DT_COLOR = "#ffff99" # bright yellow
STYLE__DD_COLOR = "#aedff7" # light blue
STYLE__DEFAULT_LIST_STYLE_TYPE = "dash" # dash, nice_alpha, index_finger, smiles, dogs, chicken, kitchen

RADIO_URL = "http://daniloquium.xyz/radio"
RADIO_NAME = "🌟 Radio Dani 🌟"
RADIO_DESCRIPTION = "Siempre contigo / Sempre amb tu / În totdeauna cu tine / Tojours avec toi / Immer bei dir / Always with you / Uvek sa tobom"
RADIO_PAGE_DESCRIPTION = ""

SPEAKABLE_TEXT_DEFAULT_CLASS = "speakable"
SPEAKABLE_TEXT_WRAPPER_ELEMENT = "span"
SPEAKABLE_TEXT_DEFAULT_LANGUAGE = "en-GB"
# SPEAKABLE_TEXT_DEFAULT_VOICE = "Google UK English Male"
SPEAKABLE_TEXT_DEFAULT_VOICES = {
	"ca": ["Microsoft Joana Online (Natural) - Catalan (Spain)", "Jordi"],
	"de-AT": ["Microsoft Ingrid Online (Natural) - German (Austria)", "Google Deutsch"],
	"de-DE": ["Microsoft Killian Online (Natural) - German (Germany)", "Microsoft Seraphina Online (Natural) - German (Germany)", "Anna", "Google Deutsch"],
	"de": ["Microsoft Killian Online (Natural) - German (Germany)", "Microsoft Seraphina Online (Natural) - German (Germany)", "Microsoft Katja Online (Natural - German (Germany)", "Microsoft Stefan - German (Germany)", "Anna", "Google Deutsch"],
	"en-AU": ["Microsoft William Online (Natural) - English (Australia)", "Lee"],
	"en-CA": ["Microsoft Liam Online (Natural) - English (Canada)", ],
	"en-GB": ["Microsoft Ryan Online (Natural) - English (United Kingdom)", "Jamie", "Stephanie", "Google UK English Male"],
	"en-IE": ["Microsoft Emily Online (Natural) - English (Ireland)", ],
	"en-NZ": ["Microsoft Mitchell Online (Natural) - English (New Zealand)", ],
	"en-US": ["Microsoft Andrew Online (Natural) - English (United States)", "Evan", "Google US English"],
	"es-ES": ["Microsoft Alvaro Online (Natural) - Spanish (Spain)", "Jorge", "Marisol", "Google español"],
	"fr": ["Microsoft Henri Online (Natural) - French (France)", "Google français"],
	"no": ["Microsoft Finn Online (Natural) - Norwegian (Bokmål Norway)", "Microsoft Finn Online (Natural) - Norwegian (Bokmal Norway)", "Google Norwegian"],
	"nb-NO": ["Microsoft Finn Online (Natural) - Norwegian (Bokmål Norway)", "Microsoft Finn Online (Natural) - Norwegian (Bokmal Norway)", "Google Norwegian"],
	"pt-BR": ["Microsoft Antonio Online (Natural) - Portuguese (Brazil)", "Microsoft Francisca Online (Natural) - Portuguese (Brazil)"],
	"ro": ["Microsoft Emil Online (Natural) - Romanian (Romania)", ],
}
# SPEAKABLE_TEXT_VOICE_CHANGER = False

QUOTES = []

SLUG_REGEX_SUBSTITUTIONS = [
	(r"[/]+", "_"),
	(r"[^\w\s-]", ""), # remove non-alphabetical/whitespace/'-' chars
	(r"(?u)\A\s*", ""), # strip leading whitespace
	(r"(?u)\s*\Z", ""), # strip trailing whitespace
	(r"[-\s]+", "-"), # reduce multiple whitespace or '-' to single '-'
]

# Main menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

HOMEPAGE_NOTES_FILE = ""
HOMEPAGE_NOTES = ""

# Blogroll
LINKS = [
	("🐓 Apprenons français", "http://fr.daniloquium.xyz"),
	("📗 DaniVojo – esperanto", "http://eo.daniloquium.xyz"),
	("💛 Catalantatge", "https://catalantatge.cat"),
	# ("DaniMundo", "https://danimundo.com"),
	# ("DP libros", "https://libros.danimundo.com"),
	# ("DP blog", "http://popovici.ml"),
]

# Social widget
SOCIAL = [
	("Facebook", "https://fb.me/laDani1995"),
	("Twitter", "https://twitter.com/DJ_Dani_Serbia"),
	("YouTube", "https://www.youtube.com/@la_Dani_1995"),
]

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
	(1, "{url}", "{save_as}"),
	(2, "{url}/{number}/", "{base_name}/{number}/index.html"),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Markdown and jinja settings

MARKDOWN = {
	"extension_configs": {
		"markdown.extensions.abbr": {},
		# "markdown.extensions.admonition": {},
		"markdown.extensions.attr_list": {},
		"markdown.extensions.def_list": {},
		"markdown.extensions.footnotes": {},
		"markdown.extensions.md_in_html": {},
		"markdown.extensions.meta": {},
		# "markdown.extensions.nl2br": {},
		"markdown.extensions.tables": {},
		"markdown.extensions.toc": {"title": "", "toc_depth": "2-6"},
		"pymdownx.emoji": {"title": "long", "alt": "unicode", "emoji_index": pymdownx.emoji.twemoji, "emoji_generator": pymdownx.emoji.to_alt}, # "emoji_generator": pymdownx.emoji.to_png, "options": {"image_path": SITEURL+"/images/emoji/"}}, # "https://cdnjs.cloudflare.com/ajax/libs/emojione/2.2.7/assets/png/32/"}}
		"pymdownx.details": {},
		"pymdownx.superfences": {"preserve_tabs": True},
		"pymdownx.highlight": {"css_class": "highlight", "use_pygments": True, "pygments_style": "autumn", "guess_lang": True, "pygments_lang_class": True, "auto_title": True, "auto_title_map": {"Bash": "", "Text only": ""}, "noclasses": True, "code_attr_on_pre": True},
		"pymdownx.inlinehilite": {},
		"pymdownx.snippets": {"base_path": ["content/code/", "content/", "../include/"], "encoding": "utf-8", "auto_append": ["../include/abbreviations.txt"]},
		"pymdownx.caret": {"smart_insert": False},
		"pymdownx.tilde": {"smart_delete": False},
		"pymdownx.mark": {},
		"pymdownx.tabbed": {},
		"pymdownx.tasklist": {},
		"pymdownx.blocks.admonition": {"types": ["note", "attention", "caution", "danger", "error", "tip", "hint", "warning", {"name": "important", "class": "important", "title": "Important"}]},
		# "pymdownx.blocks.definition": {},
		"pymdownx.blocks.details": {},
		"pymdownx.blocks.html": {},
		"pymdownx.blocks.tab": {"separator": "_"},
		"customblocks": {"generators": {"question": "customblocks.custom_generators:question", "h5p": "customblocks.custom_generators:h5p", "simple_cloze": "customblocks.custom_generators:simple_cloze", "advanced_cloze": "customblocks.custom_generators:advanced_cloze", "matching": "customblocks.custom_generators:matching", "ordering": "customblocks.custom_generators:ordering"}}, # {"generators": {"youtube": {}, "linkcard": {}}},
		"tablespan": {},
		"markdown_captions": {},
		"plugins.dp_enhancements.dp_underline_extension": {},
		"plugins.dp_enhancements.dp_speaktext_extension": {"default_language": SPEAKABLE_TEXT_DEFAULT_LANGUAGE, "default_class": SPEAKABLE_TEXT_DEFAULT_CLASS, "wrapper_element": SPEAKABLE_TEXT_WRAPPER_ELEMENT},
		# "plugins.dp_enhancements.dp_simple_wrap": {"tag": "span", "wrap_start": "@", "wrap_end": "@"},
		"plugins.dp_enhancements.dp_wrap": {
			"default_tag": "span",
			"wrap_start": "$",
			"wrap_end": "$",
			"separator": "|",
			"quick_types": [
				{"tag": "span", "wrap_start": "$!", "wrap_end": "!$", "classes": "fg-pink"},
				{"tag": "span", "wrap_start": "$#", "wrap_end": "#$", "classes": "fg-green"},
				{"tag": "span", "wrap_start": "$%", "wrap_end": "%$", "classes": "fg-turquoise"},
				{"tag": "span", "wrap_start": "$/", "wrap_end": "/$", "classes": "fg-violet"},
			],
		},
	},
	"output_format": "html5"
}
md_extensions = [e for e in MARKDOWN["extension_configs"].keys()]
md = Markdown(extensions=md_extensions, extension_configs=MARKDOWN["extension_configs"], output_format="html5")

JINJA_ENVIRONMENT = {
	"extensions": [
		"jinja2.ext.do",
		"jinja2.ext.i18n",
		"jinja2_humanize_extension.HumanizeExtension",
		# "plugins.dp_enhancements.dp_jinja2_extensions.SpeakableTextClassExtension",
	]
}

def years(start_year=2022):
	year = datetime.now().year
	if start_year == year:
		return (start_year, year, f"{year}")
	else:
		return (start_year, year, f"{start_year}-{year}")

THE_YEARS = years()

LANGUAGES_LOOKUP = {
	"en": "English",
	"es": "Español",
	"fr": "Français",
	"it": "Italiano",
	"eo": "Esperanto",
	"no": "Norsk (bokmal)",
	"pt": "Português",
	"ro": "Română",
	"ru": "Русский",
	"sr": "Srpski"
}

def lookup_lang_name(lang_code):
	return _(LANGUAGES_LOOKUP[lang_code])

def category_details(cat_name):
	if not cat_name in CATEGORY_DETAILS.keys():
		return ""
	cat_details_obj = CATEGORY_DETAILS[cat_name]
	if cat_details_obj.long_description != "":
		env = Environment(loader=ChoiceLoader([FileSystemLoader(os.path.join("themes", "localized_elegance", "templates"))]), **JINJA_ENVIRONMENT)
		jinja_processed = env.from_string(cat_details_obj.long_description).render()
		# print("long description:", cat_details_obj.long_description)
		# print("jinja processed:", jinja_processed)
		return md.convert(jinja_processed)
	else:
		return cat_details_obj.short_description

def subcategories(category):
	return ", ".join([str(d) for d in category.descendents])

def get_md_content(file_path=""):
	if file_path != "":
		with open(file_path, "r", encoding="utf-8") as the_file:
			file_content = the_file.read()
			env = Environment(loader=ChoiceLoader([FileSystemLoader(os.path.join("themes", "localized_elegance", "templates"))]), **JINJA_ENVIRONMENT)
			jinja_processed = env.from_string(file_content).render()
			return md.convert(jinja_processed)
	else:
		return ""

def markdown_jinja_filter(source_text):
	env = Environment(loader=ChoiceLoader([FileSystemLoader(os.path.join("themes", "localized_elegance", "templates"))]), **JINJA_ENVIRONMENT)
	jinja_processed = env.from_string(source_text).render()
	return md.convert(jinja_processed)

def get_speakable_text_class(x=""):
	return MARKDOWN["extension_configs"].get("plugins.dp_enhancements.dp_speakable_extension", {}).get("default_class", "speakable")


JINJA_FILTERS = {
	"cat_details": category_details,
	"subcats": subcategories,
	"lookup_lang_name": lookup_lang_name,
	"get_md_content": get_md_content,
	"md": markdown_jinja_filter,
	"speakable_filter": get_speakable_text_class,
}

# end of Markdown and jinja settings


PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jinja2content", "i18n_subsites", "neighbors", "tag_cloud", "post_stats", "extract_toc", "series", "share_post", "readtime", "more_categories", "similar_posts", "tipue_search", "seo", "sitemap", "sub_parts", "category_hierarchy", "dp_enhancements"]

EXPORT_OPTIONS = {}
"""
EXPORT_OPTIONS = {
	# +blank_before_header+definition_lists+fenced_code_attributes+fenced_code_blocks+footnotes+markdown_in_html_blocks+strikeout+subscript+superscript+task_lists+table_captions
	"docx": {"format": "docx", "label": "Word (.docx)", "options": []},
	"odt": {"format": "odt", "label": "ODT", "options": []},
	"rtf": {"format": "rtf", "label": "RTF", "options": []},
	"epub": {"format": "epub", "label": "ePub", "options": ["--epub-title-page=false"]},
	# "pdf": {"format": "pdf", "label": "PDF", "options": ["--pdf-engine=xelatex"]},
	"txt": {"format": "plain", "label": "txt", "options": ["--filter", os.path.join(PLUGIN_PATHS[0], "dp_enhancements", "pf_tables_to_dashed_lists.py")]},
	# "mediawiki.txt": {"format": "mediawiki", "label": "MediaWiki", "options": []},
}
"""

SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True

SITEMAP = {
	"format": "xml",
	"priorities": {
		"articles": 0.8,
		"indexes": 0.6,
		"pages": 0.8
	},
	"changefreqs": {
		"articles": "daily",
		"indexes": "hourly",
		"pages": "monthly"
	}
}

WORDS_PER_MINUTE = 180
READING_TIME_LOWER_LIMIT = 1
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = "alphabetically"
TAG_CLOUD_BADGE = True
SIMILAR_POSTS_MIN_SCORE = 0.6
SHARE_LINKS = [("facebook", "Facebook"), ("twitter", "Twitter"), ("WhatsApp", "whatsapp"), ("email", "Email"), ("linkedin", "LinkedIn"), ("reddit", "Reddit")]
TWITTER_USERNAME = "DJ_Dani_Serbia"
FEATURED_IMAGE = SITEURL + "/images/logo_transparent.png"
# FREELISTS_NAME = ""
# GITHUB_ACTIVITY_FEED = "https://github.com/vlajna95.atom"
# GITHUB_ACTIVITY_MAX_ENTRIES = 10
# PDF_STYLE = ["a4", "twelvepoint"]


TIMEZONE = "Europe/Belgrade"
DEFAULT_DATE_FORMAT = "%A, %-d. %B %Y. 🕰 %H:%M"

ARTICLE_TRANSLATION_ID = "trans_id"
PAGE_TRANSLATION_ID = "trans_id"

"""
SITESUBTITLE = "Dani uči francuski 📔"
COPYRIGHT = "Copyright © " + THE_YEARS[2] + " " + SITENAME + ". Sva prava zadržana."
DEFAULT_CATEGORY = "Razno"
HOMEPAGE_TITLE = "Početna"
"""
TITLE_SEPARATOR = "🎯"
PAGE_NUMBER_SEPARATOR = "::"
# LANDING_PAGE_TITLE = f"{SITENAME} — {SITESUBTITLE}"


I18N_TEMPLATES_LANG = "en"
I18N_UNTRANSLATED_ARTICLES = "remove"
I18N_UNTRANSLATED_PAGES = "remove"
I18N_GETTEXT_DOMAIN = "messages"
"""
I18N_SUBSITES = {
	"fr": {
		"LOCALE": "fr",
		"DEFAULT_DATE_FORMAT": "📅 %A, %-d %B %Y 🕰 %H:%M",
		"DEFAULT_CATEGORY": "Un peu de tout",
		"SITESUBTITLE": "J'apprends français (du serbe) 📔",
		"COPYRIGHT": "Copyright © " + THE_YEARS[2] + " " + SITENAME + ". Tous les droits réservés.",
		"HOMEPAGE_TITLE": "Page d'accueil",
	},
}
"""

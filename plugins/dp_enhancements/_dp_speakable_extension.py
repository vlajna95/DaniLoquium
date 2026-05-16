from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
import re
import xml.etree.ElementTree as etree # from markdown.util import etree


class SpeakableTextExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"default_language": ["en-GB", "Default language of the speakable text"],
			"default_class": ["speakable", "Default class for the wrapper of the speakable text"],
			"wrapper_element": ["span", "Default wrapper for the speakable text"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		md.inlinePatterns.register(SpeakableTextPattern(self.getConfigs()), "speakable_text", 175)


class SpeakableTextPattern(InlineProcessor):
	def __init__(self, config):
		super().__init__(r"@@(.+?)(?:\|(.+?))?@@")
		self.default_language = config["default_language"]
		self.default_class = config["default_class"]
		self.wrapper_element = config["wrapper_element"]
	
	def handleMatch(self, m, data):
		speakable_text = m.group(1).strip()
		language = m.group(2).strip() if m.group(2) else self.default_language
		speakable_class = self.default_class
		wrapper_element = self.wrapper_element
		el = etree.Element(wrapper_element)
		el.set("class", speakable_class)
		if language != self.default_language:
			el.set("lang", language) 
			el.set("data-lang", language) 
		el.text = speakable_text
		# return f"<{wrapper_element} class=\"{speakable_class}\" lang=\"{language}\">{speakable_text}</{wrapper_element}>"
		return el, m.start(0), m.end(0)


def makeExtension(*args, **kwargs):
	return SpeakableTextExtension(*args, **kwargs)

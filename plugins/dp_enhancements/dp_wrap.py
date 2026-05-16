from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import re
from xml.etree.ElementTree import Element
from pelican.utils import slugify


class WrappedTextExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"default_tag": ["span", "Default HTML tag if none is specified"],
			"wrap_start": ["@", "Starting symbol for wrapping elements"],
			"wrap_end": ["@", "Ending symbol for wrapping elements"],
			"separator": ["|", "The separator between the tag and its contents"],
			"quick_types": [[], "Predefined quick types"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		for qt in self.getConfig("quick_types"):
			tag = qt["tag"] if "tag" in qt else self.getConfig("default_tag")
			wrap_start = re.escape(qt["wrap_start"] if "wrap_start" in qt else self.getConfig("wrap_start"))
			wrap_end = re.escape(qt["wrap_end"] if "wrap_end" in qt else self.getConfig("wrap_end"))
			separator = self.getConfig("separator")
			pattern = rf"({wrap_start})\s*(.*?)\s*({wrap_end})"
			qt_name = "wrapped_text__" + slugify(tag + "_" + qt["classes"]).replace(" ", "_").replace("-", "_")
			md.inlinePatterns.register(WrappedText(pattern, tag, wrap_start, wrap_end, separator, qt["classes"]), qt_name, 175)
		default_wrap_start = re.escape(self.getConfig("wrap_start"))
		default_wrap_end = re.escape(self.getConfig("wrap_end"))
		default_pattern = rf"({default_wrap_start})\s*(.*?)\s*({default_wrap_end})"
		md.inlinePatterns.register(WrappedText(default_pattern, self.getConfig("default_tag"), default_wrap_start, default_wrap_end, self.getConfig("separator")), "wrapped_text", 175)


class WrappedText(InlineProcessor):
	def __init__(self, pattern, tag="", wrap_start="", wrap_end="", separator="", classes=""):
		super().__init__(pattern)
		self.tag = tag
		self.wrap_start = wrap_start
		self.wrap_end = wrap_end
		self.separator = separator
		self.classes = classes
	
	def handleMatch(self, m, data):
		full_match = m.group(2).strip()
		if self.separator and self.separator in full_match:
			el_tag, text = full_match.split(self.separator, 1)
		else:
			el_tag, text = self.tag, full_match
		el_tag = el_tag.strip()
		text = text.strip()
		el = Element(el_tag)
		el.text = text
		if self.classes:
			el.set("class", self.classes)
		return el, m.start(0), m.end(0)


def makeExtension(*args, **kwargs):
	return WrappedTextExtension(*args, **kwargs)

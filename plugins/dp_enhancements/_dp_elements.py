from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
# from markdown.blockprocessors import BlockProcessor
import re
import xml.etree.ElementTree as etree # from markdown.util import etree


ELEMENT_RE = r"\[\@\s*(.+?)(?:\s*\|\s*(.+?)?)?(?:\s*\|\s*(.+?)?)?\s*(?:\s*\|\s*(.+?)?)?\@\]"


class SpeakTextExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"tag": ["span", "Default element which will wrap the text"],
			"default_classes": ["adverbial", "Default classes for the wrapper element"],
			"wrap_start": ["+", "Start symbol(s) to begin the wrap"],
			"wrap_end": ["+", "End symbol(s) to finish the wrap"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		md.inlinePatterns.register(ElementWrap(self.getConfigs()), "dp_elements", 175)


class ElementWrap(InlineProcessor):
	def __init__(self, config):
		super().__init__(rf"{re.escape(config['wrap_start'])}\s*(.+?)\s*({re.escape(config['wrap_end'])})")
		self.default_tag = config["tag"]
		self.default_classes = config["default_classes"]
		self.wrap_start = config["wrap_start"]
		self.wrap_end = config["wrap_end"]
	
	def handleMatch(self, m, data):
		print("Match:", m, "\nData:", data, "\n", m.groups())
		wrapper_element = m.group(3).strip() if m.group(3) else self.default_tag
		wrapped_text = m.group(1).strip()
		classes = m.group(2).strip() if m.group(2) else self.default_classes
		el = etree.Element(wrapper_element)
		el.set("class", classes)
		el.text = wrapped_text
		return el, m.start(0), m.end(0)


"""
class SpeakTextBlock(BlockProcessor):
	def __init__(self, parser, config):
		super().__init__(parser)
		self.default_language = config["default_language"]
		self.default_class = config["default_class"]
		self.wrapper_element = config["wrapper_element"]
	
	def test(self, parent, block):
		# test if the block starts with @@
		m = re.match(SPEAKTEXT_RE, block, flags=re.DOTALL|re.UNICODE)
		return m
	
	def run(self, parent, blocks):
		# remove the block being processed from the list of blocks
		block = blocks.pop(0)
		# extract the speakable text from the block
		# previous code: speakable_text = blocks.pop(0).strip()[2:-2].strip()
		m = re.match(SPEAKTEXT_RE, block) #, flags=re.DOTALL|re.UNICODE)
		speakable_text = m.group(1).strip()
		language = m.group(2).strip() if m.group(2) else self.default_language
		speaktext_class = m.group(3).strip() if m.group(3) else self.default_class
		# print("Block:", self.wrapper_element, speaktext_class, language, "\n", speakable_text)
		# create the HTML element
		el = etree.Element(self.wrapper_element)
		el.set("class", speaktext_class)
		el.set("lang", language)
		el.set("tabindex", "0")
		el.text = speakable_text
		parent.append(el)
"""


def makeExtension(*args, **kwargs):
	return SpeakTextExtension(*args, **kwargs)

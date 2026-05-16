from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
# from markdown.blockprocessors import BlockProcessor
import re
import xml.etree.ElementTree as etree # from markdown.util import etree


SPEAKTEXT_RE = r"\[\@\s*(?P<display_text>.+?)(?:\s+\>\s*(?P<spoken_text>.+?))?(?:\s+\:\s*(?P<language>.+?))?(?:\s+\;\s*(?P<voice>.+?))?(?:\s+\.\s*(?P<class>.+?))?\@\]"
# SPEAKTEXT_RE = r"\[\@\s*(.+?)(?:\s*\|\s*(.+?)?)?(?:\s*\|\s*(.+?)?)?\s*(?:\s*\|\s*(.+?)?)?\@\]"
# r"(?<!\])\[@\s*(.+?)(?:\s*\|\s*(.+?))?(?:\s*\|\s*(.+?))?\s*@\](?!\[)"
# r"\@\@(.+?)(?:\s*\|\s*(.+?))?(?:\s*\|\s*(.+?))?\s*\@\@"
# SPEAKTEXT_BLOCK_RE = r"@@(.+?)(?:\s*\|\s*(.+?))?(?:\s*\|\s*(.+?))?\s*@@"
# r"@@(.+?)(?:\s*\|\s*(.+?))?(?:\s*\|\s*(.+?))?\s*@@"


class InlineSpeakText(InlineProcessor):
	def __init__(self, config):
		super().__init__(SPEAKTEXT_RE)
		self.default_language = config["default_language"]
		self.default_class = config["default_class"]
		self.wrapper_element = config["wrapper_element"]
	
	def handleMatch(self, m, data):
		# print("Match:", m, "\nData:", data, "\n", m.groups(), m.groupdict())
		display_text = m.group("display_text").strip()
		spoken_text = m.group("spoken_text") or ""
		language = m.group("language") or self.default_language
		speaktext_class = m.group("class") or self.default_class
		voice_name = m.group("voice")
		wrapper_element = self.wrapper_element
		# print("Inline:", wrapper_element, speaktext_class, language, voice_name, "\n", display_text, "\n")
		el = etree.Element(wrapper_element)
		el.set("class", speaktext_class)
		el.set("lang", language)
		el.set("data-lang", language)
		if voice_name:
			el.set("data-voice", voice_name)
		el.set("tabindex", "0")
		if spoken_text != display_text:
			el.set("data-text", spoken_text)
		el.text = display_text
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
		block = blocks.pop(0)
		m = re.match(SPEAKTEXT_RE, block) #, flags=re.DOTALL|re.UNICODE)
		display_text = m.group("display_text").strip()
		spoken_text = m.group("spoken_text") or ""
		language = m.group("language") or self.default_language
		speaktext_class = m.group("class") or self.default_class
		# create the HTML element
		el = etree.Element(self.wrapper_element)
		el.set("class", speaktext_class)
		el.set("lang", language)
		el.set("data-lang", language)
		el.set("tabindex", "0")
		if spoken_text != display_text:
			el.set("data-text", spoken_text)
		el.text = display_text
		parent.append(el)
"""


class SpeakTextExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"default_language": ["en-GB", "Default language of the speakable text"],
			"default_class": ["speakable", "Default class for the wrapper of the speakable text"],
			"wrapper_element": ["span", "Default wrapper for the speakable text"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		md.inlinePatterns.register(InlineSpeakText(self.getConfigs()), "speak_text_inline", 175)
		# md.parser.blockprocessors.register(SpeakTextBlock(md.parser, self.getConfigs()), "speak_text_block", 175)


def makeExtension(*args, **kwargs):
	return SpeakTextExtension(*args, **kwargs)

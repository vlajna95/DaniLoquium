from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor
import re


class SimpleWrapExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"tag": ["span", "HTML tag to be used"],
			"wrap_start": ["@", "Starting symbol for wrapping elements"],
			"wrap_end": ["@", "Ending symbol for wrapping elements"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		wrap_start = re.escape(self.getConfig("wrap_start"))
		wrap_end = re.escape(self.getConfig("wrap_end"))
		pattern = rf'({wrap_start})\s*(.+?)\s*({wrap_end})'
		md.inlinePatterns.register(SimpleTagInlineProcessor(pattern, self.getConfig("tag")), "simple_wrap", 175)


def makeExtension(*args, **kwargs):
	return SimpleWrapExtension(*args, **kwargs)

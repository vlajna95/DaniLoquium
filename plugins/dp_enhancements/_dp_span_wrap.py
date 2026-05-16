from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor
import re


class SpanWrapExtension(Extension):
	def __init__(self, **kwargs):
		self.config = {
			"tag": ["span", "HTML tag to be used"],
			"wrap_start": ["@", "Starting symbol for wrapping elements"],
			"wrap_end": ["@", "Ending symbol for wrapping elements"],
			"quick_types": [[], "Predefined quick types"],
		}
		super().__init__(**kwargs)
	
	def extendMarkdown(self, md):
		wrap_start = re.escape(self.getConfig("wrap_start"))
		wrap_end = re.escape(self.getConfig("wrap_end"))
		quick_types = self.getConfig("quick_types")
		# create patterns
		qt_patterns = [rf'({re.escape(qt["wrap_start"])})(.+?)({re.escape(qt["wrap_end"])})' for qt in quick_types]
		default_pattern = rf'({wrap_start})\s*([^\s{wrap_end}][^{wrap_end}]*)\s*({wrap_end})'
		# combine all patterns into one
		pattern = "|".join(qt_patterns + [default_pattern])
		# Register pattern with markdown processor
		md.inlinePatterns.register(SimpleTagInlineProcessor(pattern, self.getConfig("tag")), "span_wrap", 175)


def makeExtension(*args, **kwargs):
	return SpanWrapExtension(*args, **kwargs)

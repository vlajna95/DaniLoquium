from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor


UNDERLINE_RE = r"(--)(.+?)(--)"


class UnderlineExtension(Extension):
	def extendMarkdown(self, md):
		md.inlinePatterns.register(SimpleTagInlineProcessor(UNDERLINE_RE, "u"), "underline", 175)


def makeExtension(*args, **kwargs):
	return UnderlineExtension(*args, **kwargs)

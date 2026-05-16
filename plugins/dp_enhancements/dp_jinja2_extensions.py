from jinja2.ext import Extension
from jinja2 import nodes


class SpeakableTextClassExtension(Extension):
	tags = set(["speakable_text_class", ])
	
	def parse(self, parser):
		lineno = parser.stream.expect("name:speakable_text_class").lineno
		filter_name = nodes.Const("speakable_text_class")
		token = parser.stream.expect("name")
		filter_arg = nodes.Const(token.value)
		return nodes.Filter([filter_arg, ], filter_name, [], None, lineno=lineno)


"""
# Register the extension with Pelican
def add_jinja2_exts(pelican):
    pelican.env.jinja_env.add_extension(SpeakableTextClassExtension)

# Hook into Pelican's setup process
def register():
    pelican.plugins.signals.get_generators.connect(add_jinja2_exts)
"""
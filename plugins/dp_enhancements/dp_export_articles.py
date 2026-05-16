import os
# from pelican.generators import ArticlesGenerator
import subprocess
import tempfile
from bs4 import BeautifulSoup


plugin_path = os.path.join(os.getcwd(), "plugins", "dp_enhancements")


def convert_with_pandoc(input_path, output_path, output_format, title, author, language, abstract, keywords, *args):
	subprocess.run(["pandoc", input_path, "-o", output_path, "-t", output_format, "--filter", os.path.join(plugin_path, "pf_table_dimensions.py"), "--wrap=none", "--toc=false", "--metadata", "title="+title, "--metadata", "author="+author, "--metadata", "language="+language, "--metadata", "abstract="+strip_html_tags(abstract), "--metadata", "keywords="+keywords, *args])


def strip_html_tags(html_text):
	"""
	Removes HTML tags from the given HTML text.
	
	:param html_text: A string containing HTML content.
	:return: A string with HTML tags removed.
	"""
	soup = BeautifulSoup(html_text, "html.parser")
	return soup.get_text()


def remove_audios(html_content):
	"""
	Removes all instances of an h2 element followed by a figure containing an audio tag.
	
	:param html_content: The original HTML content as a string.
	:return: Modified HTML content as a string.
	"""
	soup = BeautifulSoup(html_content, "html.parser")
	for h2_element in soup.find_all("h2"):
		next_elem = h2_element.find_next_sibling()
		if next_elem and next_elem.name == "figure" and next_elem.find("audio"):
			# remove both the h2 element and the figure
			h2_element.decompose()
			next_elem.decompose()
	return str(soup)


def export_articles(generator):
	for article in generator.articles+generator.hidden_articles:
		base_output_path = os.path.join(generator.output_path, "_export", article.title)
		os.makedirs(os.path.dirname(base_output_path), exist_ok=True)
		html_output_path = base_output_path + ".html"
		css_styling = ""
		with open(os.path.join(plugin_path, "style.css"), "r", encoding="utf-8") as css_file:
			css_styling = css_file.read()
		html_content = f"""<!DOCTYPE html>
<html lang="{article.lang}">
<head>
<meta charset="utf-8" />
<title>{article.title}</title>
<style type="text/css">
{css_styling}
</style>
</head>
<body>
<h1>{article.title}</h1>
{article.content}
</body>
</html>"""
		# export to HTML
		with open(html_output_path, "w", encoding="utf-8") as article_file:
			article_file.write(html_content)
		# export to other formats
		temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".html")
		tmp_file = temp_file.name
		with open(temp_file.name, "w", encoding="utf-8") as file:
			file.write(remove_audios(html_content))
		article_tags = ", ".join([tag.name for tag in article.tags]) if hasattr(article, "tags") else ""
		export_options = generator.settings.get("EXPORT_OPTIONS", {})
		for export_extension, settings in export_options.items():
			convert_with_pandoc(tmp_file, base_output_path+"."+export_extension, settings["format"], article.title, article.author.name, article.lang, article.summary, article_tags, *settings["options"])
		# add links to the article content
		# article.content += f'<p><a href="{html_output_path}">Download as HTML</a></p>'
		# article.content += f'<p><a href="{docx_output_path}">Download as DOCX</a></p>'
		# article.content += f'<p><a href="{txt_output_path}">Download as TXT</a></p>'
		# article.content += f'<p><a href="{epub_output_path}">Download as ePub</a></p>'
		# article.content += f'<p><a href="{pdf_output_path}">Download as PDF</a></p>'

# category details class and dictionary
import os
import logging

log = logging.getLogger(__name__)


class CategoryDetails:
	name = ""
	short_description = ""
	long_description = ""
	
	def __init__(self, name, short_description="", desc_filename=""):
		"""Create an instance of the CategoryDetails class. 
		
		Parameters 
		- name (str): The name of the category, or the whole path to it if the categories are being extracted from the folder structure.
		- short_description (str): A short description of the category, potentially useful for a index of all categories.
		- long_description (str): A path to a file which contains the Markdown-formatted long description i.e. the page content for the index page of the category; this file must be inside the cat_details folder at the same level as the content/ folder and this file.
		
		Returns an instance of the CategoryDetails class.
		"""
		self.name = name
		self.short_description = short_description
		desc_file_path = os.path.join("cat_details", desc_filename)
		if not desc_filename in ["", " ", None] and os.path.isfile(desc_file_path):
			with open(desc_file_path, "r", encoding="utf-8") as f:
				self.long_description = f.read()
				log.info(f"Category long description loaded from {desc_file_path}")
		else:
			self.long_description = self.short_description
			log.info(f"Category long description not available at {desc_file_path}. Using the short description instead.")


CATEGORY_DETAILS = {
	"Razno":
		CategoryDetails("Razno",
			"Sve ono što ne znam u koju bi se drugu kategoriju uklopilo",
			"razno.txt"
		),
}

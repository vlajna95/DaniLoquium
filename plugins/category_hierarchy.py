from pelican import signals


"""
def category_hierarchy(categories):
	hierarchy = []
	for category, articles in categories:
		hierarchy.append({"shortname": category.shortname, "children": category.children})
	print(hierarchy)
	return hierarchy

def find_descendants(parent, categories):
	descendants = []
	for category in categories:
		# Skip the parent itself
		if category == parent:
			continue
		# Check if this category is a direct descendant of the parent
		if parent in category.ancestors:
			# Recursively find the descendants of this category
			children = find_descendants(category, categories)
			descendants.append({"shortname": category.shortname, "children": children})
	return descendants
"""


def category_hierarchy(categories):
	hierarchy = []
	for category, articles in categories:
		if "/" not in category.name: # top-level category
			children = get_children(category, categories)
			cat = {"cat_obj": category, "shortname": category.shortname, "children": children}
			for key in ["ancestors", "descendents", "name", "page_name", "parent", "save_as", "settings", "slug", "url"]:
				cat[key] = getattr(category, key)
			hierarchy.append(cat)
	return hierarchy

def get_children(parent, all_categories):
	children = []
	for category, articles in all_categories:
		if category.parent == parent: # assuming each category has a 'parent' attribute
			grandchildren = get_children(category, all_categories)
			cat = {"cat_obj": category, "shortname": category.shortname, "children": grandchildren}
			for key in ["ancestors", "descendents", "name", "page_name", "parent", "save_as", "settings", "slug", "url"]:
				cat[key] = getattr(category, key)
			children.append(cat)
	return children


def cat_hierarchy(article_generator):
	article_generator.context["category_hierarchy"] = category_hierarchy(article_generator.categories)


def register():
	signals.article_generator_finalized.connect(cat_hierarchy)

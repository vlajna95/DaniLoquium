import panflute as pf


import panflute as pf


def table_to_dashed_list(elem, doc):
	if isinstance(elem, pf.Table):
		rows = []
		for el in elem.content:
			# extract text from each row
			for row in el.content:
				cells_text = " – ".join([pf.stringify(cell) for cell in row.content])
				rows.append("- " + cells_text)
		# convert the list of items to a series of Plain elements
		return pf.Plain(pf.Str(" \n".join([row for row in rows])))


def main(doc=None):
	return pf.run_filter(table_to_dashed_list, doc=doc)


if __name__ == "__main__":
	main()

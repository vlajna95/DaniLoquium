import panflute as pf

def equalize_table_widths(elem, doc):
	if isinstance(elem, pf.Table):
		num_cols = len(elem.colspec)
		col_width = 1.0 / num_cols  # Width as a percentage
		# update the width of each column specification
		elem.colspec = [(cs[0], col_width) for cs in elem.colspec]


def main(doc=None):
    return pf.run_filter(equalize_table_widths, doc=doc)


if __name__ == '__main__':
    main()

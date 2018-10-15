"""Nester"""
def print_lol(the_list):
	"""Takes a list and print items inside the list recursively"""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

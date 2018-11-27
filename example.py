#!/usr/bin/python3

import explorer

extension = ['.py']


listFile = explorer.search_file("./", hide=True)
print(listFile)
print("\n")

listFile = explorer.search_file("./", extension, False)
print(listFile)
print("\n")

listDir = explorer.search_dir("./", hide=False)
print(listDir)
print("\n")

tree = explorer.tree("./")
print(tree)



"""
explorer
~~~~~~~~~~~~~~~~~~

some function to search in the file system
"""

"""

Import extern module

"""
import os

"""

Import intern module

"""

"""

Internal Constant, Class, Function

"""

"""

Exported Constant, Class, Function

"""

def search_file(
    path,
    extension = [],
    hide = False
    ):
  """
  Search recursively all file in the given path

  :param: path: path of the directory where search file
  :param: extension: (optional) the extension of file wanted
  :param: hide: (optional) if true, include the hidden file and folder
  """
  lstFile = []
  lenPath = len(path)
  for subpath, dirs, files in os.walk(path):
    for f in files:
      if subpath[-1] == '/':
        subpath = subpath[:-1]
      # end if
      filename = subpath + '/' + f
      lstFile.append(filename)
      tmp = filename.split('/')
      for t in tmp[1:]:
        if hide == False and t[0] == '.':
          lstFile.pop(-1)
          break
        # end if
      # end for
      if extension and lstFile:
        _, ext = os.path.splitext(f)
        if not ext in extension:
          lstFile.pop(-1)
        # end if
      # end if
    # end for
  # end for
  return lstFile

def search_dir(
    path,
    hide = False
    ):
  """
  Search recursively all directory in the given path

  :param: path: path of the directory where search directory
  :param: hide: (optional) if true, include the hidden directory
  """
  lstDir = []
  lenPath = len(path)
  for subpath, dirs, files in os.walk(path):
    for d in dirs:
      if subpath[-1] == '/':
        subpath = subpath[:-1]
      # end if
      dirname = subpath + '/' + d
      lstDir.append(dirname)
      tmp = dirname.split('/')
      for t in tmp[1:]:
        if hide == False and t[0] == '.':
          lstDir.pop(-1)
          break
        # end if
      # end for
    # end for
  # end for
  return lstDir

def tree(
    path,
    hide = False
    ):
  """
  Create a tree from the given path

  :param: path: path of the directory to create the tree
  :param: hide: (optional) if true, include the hidden file and folder
  """
  lstFile = search_file(path, hide)
  tree = {}
  for pathFile in lstFile:
    lstPath = pathFile.split('/')
    subTree = tree
    for p in lstPath:
      if not p in subTree.keys():
        subTree[p] = {}
      # end if
      subTree = subTree[p]
    # end for
  # end for
  return tree


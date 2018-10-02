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
      if extension:
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

"""

Internal Constant, Class, Function

"""



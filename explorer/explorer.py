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
  if path == '/':
    path = path
  elif path[-1] == '/':
    path = path[:-1]
  # end if
  for subpath, dirs, files in os.walk(path):
    for f in files:
      pop = False
      filename = subpath + ('/' if subpath[-1] != '/' else '') + f
      lstFile.append(filename)
      tmp = filename.split('/')
      for t in tmp[1:]:
        if hide == False and t[0] == '.':
          pop = True
          break
        # end if
      # end for
      if extension:
        _, ext = os.path.splitext(f)
        if ext != "" and not ext in extension:
          pop = True
        # end if
      # end if
      if pop == True and lstFile:
        lstFile.pop(-1)
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
  if path == '/':
    path = path
  elif path[-1] == '/':
    path = path[:-1]
  # end if
  for subpath, dirs, files in os.walk(path):
    for d in dirs:
      pop = False
      dirname = subpath + ('/' if subpath[-1] != '/' else '') + d
      lstDir.append(dirname)
      tmp = dirname.split('/')
      for t in tmp[1:]:
        if hide == False and t[0] == '.':
          pop = True
          break
        # end if
      # end for
      if pop == True and lstDir:
        lstDir.pop(-1)
      # end if
    # end for
  # end for
  return lstDir


import os

def get_root_path():
  file_path = os.path.realpath(__file__)
  dir_path = os.path.dirname(file_path)
  return os.path.abspath(os.path.join(dir_path, os.pardir))

def source_path(path):
  return os.path.join(get_root_path(), 'sources',  path)

import os

def create_file_if_not_exists(path: str) -> None:
  if not os.path.exists(path):
    with open(path, 'w'):
      pass
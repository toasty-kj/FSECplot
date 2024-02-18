import os

def create_file_if_not_exists(path: str) -> None:
  if not os.path.exists(path):
    with open(path, 'w'):
      pass

def validate_file_path(file_path:str):
   print(file_path)
   if os.path.exists(file_path):
     raise FileNotFoundError(f'file note found {file_path}')

def validate_file_path_list(file_path_list:[]):
  for i in file_path_list:
    validate_file_path(i)
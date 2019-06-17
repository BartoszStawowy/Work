import pathlib

def find_path_to_file(file_name):
   globa_path = pathlib.Path.home()
   for path in sorted(globa_path.rglob('*')):
           if str(file_name) in str(path):
               return str(path)

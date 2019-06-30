import pathlib

def find_path_to_file(file_name):
    global_path = pathlib.Path.cwd()
    for path in sorted(global_path.rglob('*')):
            if str(file_name) in str(path):
                return str(path)
            else:
                for path in sorted(global_path.parent.parent.rglob('*')):
                    if str(file_name) in str(path):
                        return str(path)

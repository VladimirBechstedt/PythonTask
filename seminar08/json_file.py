import json


def writing(arr):
    for absolute_path, parent_directory, file, directory, size in arr:
        my_dict = {
            "absolute_path": absolute_path,
            "parent_directory": parent_directory,
            "file": file,
            "directory": directory,
            "size": size
            }
        with open('info_dir.json', 'a', encoding='utf-8') as f:
            json.dump(my_dict, f, ensure_ascii=False, indent=2)

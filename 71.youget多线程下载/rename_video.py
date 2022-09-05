import os
import re

change_path = r"E:\Vedio\Java\青空の霞光-Java连载\5.JavaSE9-17新特性"
for base_path, document, files in os.walk(change_path):
    if not document:
        for f in files:
            file_type = os.path.splitext(f)[1]
            _name = re.search(r'\(P\d+\..*\)', f)
            if not _name:
                print(f"===Error: {f}.")
                continue
            file_name = _name[0].strip('()').replace(' ', '') if _name else None
            print(os.path.join(base_path, f))
            print(os.path.join(base_path, file_name + file_type))
            if file_name and file_type:
                os.rename(os.path.join(base_path, f),
                          os.path.join(base_path, file_name + file_type))

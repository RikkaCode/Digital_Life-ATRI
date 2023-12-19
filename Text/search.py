import os
import glob
import shutil

folder_path = 'path'


mp3_files = glob.glob(os.path.join(folder_path, 'ATRI*.mp3'))


for file_path in os.listdir(folder_path):
    if file_path.endswith('.mp3') and file_path not in mp3_files:
        full_path = os.path.join(folder_path, file_path)
        os.remove(full_path)

print("保留的mp3文件：")
for mp3_file in mp3_files:
    print(mp3_file)

import os
from pydub import AudioSegment


folder_path = 'path'


for file_name in os.listdir(folder_path):
    if file_name.endswith('.mp3'):
        file_path = os.path.join(folder_path, file_name)
        
        audio = AudioSegment.from_mp3(file_path)
        length_in_seconds = len(audio) / 1000  


        if length_in_seconds < 1:
            os.remove(file_path)
            print(f"已删除长度小于2秒的文件: {file_name}")

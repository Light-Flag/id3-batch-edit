import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError

folder_path = "C:/Your Path"
new_album_name = "New name"

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            audio = EasyID3(file_path)
        except ID3NoHeaderError:
            audio = EasyID3()
            audio.save(file_path)
            audio = EasyID3(file_path)

        audio["album"] = new_album_name
        audio.save()
        print(f"Updated: {filename}")
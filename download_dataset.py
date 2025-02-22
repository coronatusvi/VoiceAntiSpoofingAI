# """
# AASIST
# Copyright (c) 2021-present NAVER Corp.
# MIT license
# """

# import os

# if __name__ == "__main__":
#     cmd = "curl -o ./LA.zip -# https://datashare.ed.ac.uk/bitstream/handle/10283/3336/LA.zip\?sequence\=3\&isAllowed\=y"
#     os.system(cmd)
#     cmd = "unzip LA.zip"
#     os.system(cmd)

# extract file tar.gz to folder data

# import tarfile
# import os
# if __name__ == "__main__":
#     cmd = "git clone https://github.com/coronatusvi/ASVspoof2025_VN.git"
#     os.system(cmd)
# tar = tarfile.open("ASVspoof2025_VN/cv-corpus-20.0-delta-2024-12-06-vi.tar.gz")
# tar.extractall()
# tar.close()


from pydub import AudioSegment
import os

def convert_mp3_to_flac(mp3_path, flac_path):
    # Load mp3 file
    audio = AudioSegment.from_mp3(mp3_path)
    
    # Set parameters
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 2 bytes = 16 bits (s16)
    
    # Export as flac
    audio.export(flac_path, format="flac")

if __name__ == "__main__":
    mp3_path = "path/to/your/file.mp3"
    flac_path = "path/to/your/file.flac"
    
    convert_mp3_to_flac(mp3_path, flac_path)
    print(f"Converted {mp3_path} to {flac_path}")
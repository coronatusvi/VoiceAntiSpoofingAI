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


import tarfile
import os
from pydub import AudioSegment

def convert_mp3_to_flac(mp3_path, flac_path):
    try:
        audio = AudioSegment.from_mp3(mp3_path)
        
        # Set parameters
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
        audio = audio.set_sample_width(2)  # 2 bytes = 16 bits (s16)
        
        # Export as flac
        audio.export(flac_path, format="flac")
    except Exception as e:
        print(f"Error converting {mp3_path} to {flac_path}: {e}")

if __name__ == "__main__":
    repo_dir = "ASVspoof2025_VN"
    tar_path = os.path.join(repo_dir, "cv-corpus-20.0-delta-2024-12-06-vi.tar.gz")
    
    if not os.path.exists(repo_dir):
        os.system(f"git clone https://github.com/coronatusvi/ASVspoof2025_VN.git")

    if not os.path.exists(tar_path):
        print(f"Error: File {tar_path} does not exist.")
    else:
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=repo_dir)
        
        # Convert MP3 files to FLAC and delete the original MP3 files
        for root, dirs, files in os.walk(repo_dir):
            for file in files:
                if file.endswith(".mp3"):
                    mp3_path = os.path.join(root, file)
                    flac_path = os.path.splitext(mp3_path)[0] + ".flac"
                    convert_mp3_to_flac(mp3_path, flac_path)
                    os.remove(mp3_path)

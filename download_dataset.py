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

if __name__ == "__main__":
    repo_dir = "ASVspoof2025_VN"
    tar_path = os.path.join(repo_dir, "cv-corpus-20.0-delta-2024-12-06-vi.tar.gz")
    
    # Clone repository nếu chưa tồn tại
    if not os.path.exists(repo_dir):
        os.system(f"git clone https://github.com/coronatusvi/ASVspoof2025_VN.git")

    # Kiểm tra file .tar.gz có tồn tại không
    if not os.path.exists(tar_path):
        print(f"Error: File {tar_path}")
    else:
        
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=repo_dir)
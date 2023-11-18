import time
from tqdm import trange
import json
import os
import re


# get the deletedfiles infonation blk
current_dir = os.getcwd()
with open(current_dir + "\deletefiles.txt" , "r") as deletedfiles:
    content = deletedfiles.read()
    deleted_blk_files = re.findall(r'(\d+\.blk)', content)
    if "GenshinImpact" in content:
        Client_type = "OS"
    else:
        Client_type = "CN"







#get the path
# current_dir = os.getcwd()
# other_dir = os.path.join(current_dir, "GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/")
# files_and_subdirectories = os.listdir(other_dir)
# print(files_and_subdirectories)
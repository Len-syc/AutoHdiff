import os
import time
from tqdm import trange
import json
import os
import re

# with open("deletedfiles.txt" , "r") as deletedfiles:
text = """
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00003007.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00003928.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00042024.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00064097.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00065091.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00070296.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00114256.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00135503.blk
GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/00277647.blk
"""

blk_files = re.findall(r'(\d+\.blk)', text)
print(blk_files)









#get the path
# current_dir = os.getcwd()
# other_dir = os.path.join(current_dir, "GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/")
# files_and_subdirectories = os.listdir(other_dir)
# print(files_and_subdirectories)
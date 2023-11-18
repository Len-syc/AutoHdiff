import os
import time
from tqdm import trange
import json
import os
import os

current_dir = os.getcwd()
other_dir = os.path.join(current_dir, "GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/")
files_and_subdirectories = os.listdir(other_dir)
print(files_and_subdirectories)
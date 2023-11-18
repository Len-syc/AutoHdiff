import time
from tqdm import tqdm
import json
import os
import re
import requests
import sys

Client_down = input("your client_type CN or OS：")
while Client_down not in ["CN", "OS"]:
    print("Client type error!")
    Client_down = input("your client_type CN or OS：")

Client_type_down = input("your Client_Down_type Client or Audio：")
while Client_type_down not in ["CN", "OS"]:
    print("Client_Down_type type error!")
    Client_type_down = input("your Client_Down_type Client or Audio：")




current_dir = os.getcwd()
def autopatch_download(url, filename):
    response = requests.get(url, stream=True)

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)


autopatch_download('http://example.com/bigfile.zip',  current_dir + 'bigfile.zip')






# # get the path 
# get_dir = os.getcwd()
# other_dir = os.path.join(get_dir, "GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/")
# files_and_subdirectories = os.listdir(other_dir)
# print(files_and_subdirectories)


# get the deletedfiles infonation blk and client_type  
# current_dir = os.getcwd()
# with open(current_dir + "\deletefiles.txt" , "r") as deletedfiles:
#     files_deleted = deletedfiles.read()
#     deleted_blk_files = re.findall(r'(\d+\.blk)', files_deleted)
#     if "GenshinImpact" in files_deleted:
#         Client_type = "OS"
#     else:
#         Client_type = "CN"








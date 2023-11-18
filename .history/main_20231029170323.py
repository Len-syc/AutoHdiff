import time
from tqdm import tqdm
import json
import os
import re
import requests


Client_down = str(input("your client_type CN or OS"))
while "Client_down" is not "CN" or "OS":
    print("Client type error!")
    break

# # get the path 第二
# get_dir = os.getcwd()
# other_dir = os.path.join(get_dir, "GenshinImpact_Data/StreamingAssets/AssetBundles/blocks/00/")
# files_and_subdirectories = os.listdir(other_dir)
# print(files_and_subdirectories)




current_dir = os.getcwd()
def autopatch_download(url, filename):
    response = requests.get(url, stream=True)

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)


autopatch_download('http://example.com/bigfile.zip',  current_dir + 'bigfile.zip')






# get the deletedfiles infonation blk and client_type  第一
# current_dir = os.getcwd()
# with open(current_dir + "\deletefiles.txt" , "r") as deletedfiles:
#     files_deleted = deletedfiles.read()
#     deleted_blk_files = re.findall(r'(\d+\.blk)', files_deleted)
#     if "GenshinImpact" in files_deleted:
#         Client_type = "OS"
#     else:
#         Client_type = "CN"








import time
from tqdm import tqdm
import json
import os
import re
import requests
import sys
#####################################################################
directory_path = os.getcwd()
detect_list = os.listdir(directory_path)






start_model = input("model(1.只解压和替换,2.自动下载和解压替换,)")
Client_type_down = input("your Client_Down_type Client or Audio or full：")
while Client_type_down not in ["Client","Audio","full"]:
    print("Client_Down_type type error!")
    Client_type_down = input("your Client_Down_type Client or Audio：")
########################################################################








####################################### ----model 2
if start_model == "2":
    if "config.json" not in detect_list:
        print("！config配置文件不存在")
        sys.exit()
    with open(directory_path + "/config.json" , "r") as Autopatch_URL:
        json_data = json.load(Autopatch_URL)
        if "Autopatch_Client_URL" not in json_data or "Autopatch_Audio_URL" not in json_data:
            print("！not found Autopatch_Client_URL and Autopatch_Audio_URL please check config.json!")
            sys.exit()

    if Client_type_down == "Client":
        Download_URL = json_data["Autopatch_Client_URL"]
        down_type = "Client"
    elif Client_type_down == "Audio":
        Download_URL = json_data["Autopatch_Audio_URL"]
        down_type = "Audio"
    elif Client_type_down == "full":
        Download_URL_full_Client = json_data["Autopatch_Client_URL"]
        Download_URL_full_Audio = json_data["Autopatch_Audio_URL"]
        down_type = "full"
Autopatch_URL.close()
Download_file_directory = os.getcwd()
def autopatch_download(url, filename):
    response = requests.get(url, stream=True)

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
print("Download---------")
if down_type =="Client":
    autopatch_download(f"{Download_URL}",  Download_file_directory + "Client.zip")
elif down_type == "Audio":
    autopatch_download(f"{Download_URL_full_Client}",  Download_file_directory + "Client.zip")
elif down_type == "full":
    autopatch_download(f"{Download_URL_full_Audio}",  Download_file_directory + "Audio.zip")
else:
    print("欸·？")
    sys.exit()
###################################################################### -----model 2














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








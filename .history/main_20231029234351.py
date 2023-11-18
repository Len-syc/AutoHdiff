import time
from tqdm import tqdm
import json
import os
import re
import requests
import sys
import threading
#####################################################################
directory_path = os.getcwd()
detect_list = os.listdir(directory_path)






start_model = input("Level:[info] model(1.只解压和替换,2.自动下载和解压替换,):")
Confirm_type = input("Level:[info] do you want to jump the down?(y or n)")
if Confirm_type == "n":
    Client_type_down = input("Level:[info] your Client_Down_type Client or Audio or full:")
    while Client_type_down not in ["Client","Audio","full"]:
        print("Level:[Error] Client_Down_type type error!")
        Client_type_down = input("Level:[info] your Client_Down_type Client or Audio:")
elif Confirm_type == "y":
    Client_type = input("Level:[info] your Client_type Client or Audio or full:")
    while Client_type not in ["Client","Audio","full"]:
        print("Level:[Error] Client_type type error!")
        Client_type = input("Level:[info] your Client_type Client or Audio:")
########################################################################








####################################### ----model 2
if start_model == "2":
    if "config.json" not in detect_list:
        print("Level:[Fatal] ！config配置文件不存在")
        sys.exit()
    if Confirm_type == "y":
        print("Level:[info] 跳过下载")
    elif Client_type_down in ["Client","Audio","full"]:

        with open(directory_path + "/config.json" , "r") as Autopatch_URL:
            json_data = json.load(Autopatch_URL)
            if "Autopatch_Client_URL" not in json_data or "Autopatch_Audio_URL" not in json_data:
                print("Level:[Fatal] ！not found Autopatch_Client_URL and Autopatch_Audio_URL please check config.json!")
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
def download_file(url, filename, num_threads=1):
    response = requests.head(url)
    file_size = int(response.headers['content-length'])
    part = file_size // num_threads

    threads = []
    for i in range(num_threads):
        start = part * i
        if i == num_threads - 1:
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=download_part, args=(i, url, start, end, filename))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    with open(filename, 'wb') as f:
        for i in range(num_threads):
            part_filename = f'{filename}.part{i}'
            with open(part_filename, 'rb') as pf:
                f.write(pf.read())
            os.remove(part_filename)

def download_part(i, url, start, end, filename):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers)
    with open(f'{filename}.part{i}', 'wb') as f:
        f.write(response.content)
if Confirm_type == "n" and Client_type_down in ["Audio","Client","full"]:
    if down_type =="Client":
        download_file(Download_URL , Download_file_directory + "/Client.zip")
        print(f"Level:[info] 下载完成,URL:{Download_URL},Type:Client,path:{Download_file_directory}+/Client.zip")
    elif down_type == "Audio":
        download_file(Download_URL, Download_file_directory + "/Audio.zip")
        print(f"Level:[info] 下载完成,URL:{Download_URL},Type:Client,path:{Download_file_directory}+/Audio.zip")
    elif down_type == "full":
        download_file(Download_URL_full_Client, Download_file_directory + "/Client.zip" )
        download_file(Download_URL_full_Audio, Download_file_directory + "/Audio.zip" )
        print(f"Level:[info] 下载完成,URL:{Download_URL_full_Client},Type:Client,path:{Download_file_directory}+/Client.zip")
        print(f"Level:[info] 下载完成,URL:{Download_URL_full_Audio},Type:Client,path:{Download_file_directory}+/Audio.zip")
elif Confirm_type == "y":
    print("Level:[info] 加载中")
    print("Level:[info]加载压缩包中")
    for i in tqdm(range(40),desc="加载中",unit="s"):
        time.sleep(0.1)

########---compress


# if "." not in detect_list:
#         print("！config配置文件不存在")
if Confirm_type == "n":
    Client_type = Client_type_down

if down_type == "Client":
    if "Client.zip" not in detect_list:
        print("Level:[fatal] not found Client.zip!")
        sys.exit()
elif down_type == "Audio":
    if "Audio.zip" not in detect_list:
        print("Level:[fatal] not found Audio.zip!")
        sys.exit()
elif down_type == "full":
    full = ["Client.zip","Audio.zip"]
    if full not in detect_list:
        print("Level:[fatal] not found Audio.zip!")
        sys.exit()
            
########---compress


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

def Get_txt_Audio():
    get_dir = os.getcwd()
    with open(current_dir + "\hdiffiles.txt" , "r") as hdiffiles:
        files_deleted = hdiffiles.read()
        hdiff_pck_files = re.findall(r'(\d+\.pck)', files_deleted)
        if "GenshinImpact" in files_deleted:
            Client_area = "GenshinImpact"
        else:
            Client_area = "YuanShen"
    return hdiff_pck_files , Client_area
    other_dir = os.path.join(get_dir, f"{Client_area}_Data/StreamingAssets/AudioAssets/Chinese/")





import time
from tqdm import tqdm
import json
import os
import re
import requests
import sys
import threading
import zipfile
import shutil
directory_path = os.getcwd()
detect_list = os.listdir(directory_path)






start_model = input("Level:[info] model(1.只解压和替换,2.自动下载和解压替换,):")
Confirm_type = input("Level:[info] do you want to jump the down?(y or n)")
if Confirm_type == "n":
    down_type = input("Level:[info] your Client_Down_type Client or Audio or full:")
    while down_type not in ["Client","Audio","full"]:
        print("Level:[Error] Client_Down_type type error!")
        down_type = input("Level:[info] your Client_Down_type Client or Audio:")
elif Confirm_type == "y":
    Client_type = input("Level:[info] your Client_type Client or Audio or full:")
    while Client_type not in ["Client","Audio","full"]:
        print("Level:[Error] Client_type type error!")
        Client_type = input("Level:[info] your Client_type Client or Audio:")








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
if Confirm_type == "n" and down_type in ["Audio","Client","full"]:
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

if Confirm_type == "n":
    Client_type = down_type

#检测
if Client_type == "Client":
    if "Client.zip" not in detect_list:
        print("Level:[fatal] not found Client.zip!")
        sys.exit()
elif Client_type == "Audio":
    if "Audio.zip" not in detect_list:
        print("Level:[fatal] not found Audio.zip!")
        sys.exit()
elif Client_type == "full":
    full = ["Client.zip","Audio.zip"]
    if full not in detect_list:
        print("Level:[fatal] not found Audio.zip!")
        sys.exit()
            
#解压
print("Level:[info] 加载中")
print("Level:[info]加载压缩包中")
for i in tqdm(range(40),desc="加载中",unit="s"):
    time.sleep(0.1)
def unzip_file(zip_filepath, dest_path):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        with tqdm(total=len(file_list), desc="解压进度", ncols=80) as pbar:
            for file in file_list:
                zip_ref.extract(member=file, path=dest_path)
                pbar.update(1)
if down_type == "Client":
    print(f"Level:[info] 解压中{down_type}.zip")
    unzip_file("Client.zip",Download_file_directory)
elif down_type == "Audio":
    print(f"Level:[info] 解压中{down_type}.zip")
    unzip_file("Audio",Download_file_directory)
elif down_type == "full":
    print("Level:[info] 解压中Client.zip")
    print("Level:[info] 解压中Audio.zip")
    unzip_file("Client.zip",Download_file_directory)
    unzip_file("Audio",Download_file_directory)

########---compress

##### get the infonation from txt
#貌似audio只有hdiff 没有deleted 而且client hdiff只要copy and deleted 但是copy的没txt消息，所以用os.lister来获取
#audio在或许3.0后有改变(目录)
def Get_txt_Audio():#audio only
    get_dir = os.getcwd()
    if "hdiffiles.txt" not in os.listdir(get_dir):
        print("Level:[fatal] !hdiffiles.txt文件不存在,请检查")
        sys.exit()
    with open(get_dir + "\hdiffiles.txt" , "r") as hdiffiles:
        files_hdiff = hdiffiles.read()
        hdiff_pck_files = re.findall(r'(\d+\.pck)', files_hdiff)
        if "GenshinImpact" in files_deleted:
            Client_area = "GenshinImpact"
        else:
            Client_area = "YuanShen"
    Client_update_Audio_dir = os.path.join(get_dir, f"{Client_area}_Data/StreamingAssets/AudioAssets/Chinese/")
    return hdiff_pck_files , Client_area,Client_update_Audio_dir
def Get_txt_Client():#Client only
    get_dir = os.getcwd()
    if "deletefiles.txt" not in os.listdir(get_dir):
        print("Level:[fatal] !deletefiles.txt文件不存在,请检查")
        sys.exit()
    with open(get_dir + "\deletefiles.txt" , "r") as deleted_file:
        files_blk_deleted = deleted_file.read()
        deleted_blk_files = re.findall(r'(\d+\.blk)', files_blk_deleted)
        if "GenshinImpact" in deleted_blk_files:
            Client_area = "GenshinImpact"
        else:
            Client_area = "YuanShen"
    Client_update_Client_dir = os.path.join(get_dir, f"{Client_area}_Data/StreamingAssets/AssetBundles/blocks/00/")
    return deleted_blk_files,Client_area
def delete_blk(file_list, directory):
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Level:[info] 文件 {file_name} 已被删除")
        else:
            print(f"Level:[Error] 未找到文件 {file_name}")
def copy_files(source_directory, dest_directory):
    for file_name in os.listdir(source_directory):
        source_file_path = os.path.join(source_directory, file_name)
        dest_file_path = os.path.join(dest_directory, file_name)
        shutil.copy2(source_file_path, dest_file_path)
        print(f"Level:[info] 文件 {file_name} 已被复制到 {dest_directory}。")

# copy_files('/path/to/source/directory', '/path/to/dest/directory')
def rename_audio(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pck.hdiff'):
            new_filename = filename.replace('.pck.hdiff', '.pck')
            source = os.path.join(directory, filename)
            destination = os.path.join(directory, new_filename)
            os.rename(source, destination)
            print(f"Level:[info] 文件 {filename} 已被重命名为 {new_filename}")


###先path 然后dele 然后 copy
update_file_list = os.getcwd()
if Client_type == "Client":
    Client_update_source = os.path.join(update_file_list, "Client/")
    for i in tqdm(range(40),desc="加载中",unit="s"):
        time.sleep(0.1)
    Get_txt_Client()
    print("Level[info] deleted.txt数值获取成功!")
    delete_blk(deleted_blk_files,Client_update_Client_dir)
    print(f"Level:[debug] {deleted_blk_files}")
    print(f"Level:[debug] {Client_update_Client_dir}")
    print("Level:[info] deleted successfully!")
    print("Level:[info] copying.........")
    for i in tqdm(range(40),desc="加载中",unit="s"):
        time.sleep(0.1)
    copy_files(Client_update_source,directory_path)
    

elif Client_type == "Audio":
    audio_update_source = os.path.join(update_file_list, "audio/YuanShen_Data/StreamingAssets/AudioAssets/Chinese/")
    print(f"Level:[debug] {audio_update_source}")
    rename_audio()

elif Client_type == "full":
    Client_update_source = os.path.join(update_file_list, "Client/")
    audio_update_source = os.path.join(update_file_list, "audio/")

#     for i in tqdm(range(40),desc="加载中",unit="s"):
#         time.sleep(0.1)
#     Get_txt_Client()
#     print("Level[info] deleted.txt数值获取成功!")
#     delete_blk(deleted_blk_files,)
#     print("Level:[info] deleted successfully!")
#     print("Level:[info] copying.........")
#     for i in tqdm(range(40),desc="加载中",unit="s"):
#         time.sleep(0.1)
#     Hdiff_update(update_blk,blk_source,)
    
# elif Client_type == "Audio":
#     for i in tqdm(range(40),desc="加载中",unit="s"):
#         time.sleep(0.1)
#     Get_txt_Audio()
#     print("Level[info] hdifffiles.txt数值获取成功!")
#     rename_audio()#version over have change attention
#     print("Level:[info] Audio successfully!")
#     print("Level:[info] copying.........")
#     for i in tqdm(range(40),desc="加载中",unit="s"):
#         time.sleep(0.1)

###################################################################### -----model 2
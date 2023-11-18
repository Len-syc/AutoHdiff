import os
import time
from tqdm import trange
import json
import os
import os

# 获取当前目录
current_dir = os.getcwd()

# 跳转到当前目录中的其他目录
other_dir = os.path.join(current_dir, "yuanshen_data")

# 获取other_dir中的所有文件和子目录
files_and_subdirectories = os.listdir(other_dir)

print(files_and_subdirectories)

# file_path = os.getcwd()
# parent_dir = os.path.dirname(file_path)
# client_dir = os.path.join(parent_dir, "\yuanshen_data")
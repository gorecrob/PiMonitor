import os
from datetime import datetime
path="/tmp/motion/"
dest="/MalinaBencol/"
def upload_files():
    if not os.path.exists(path):
        return
    #os.stdir(path)
    dir_list = os.listdir(path)
    for file_name in dir_list:
        if file_name.endswith(".avi"):
            cmd = "/home/pi/dropbox_uploader.sh upload " + path + file_name + " "+ datetime.now().strftime('%Y-%m-%d') + "/" + file_name
            os.system(cmd)
            os.system("sudo rm /tmp/motion/" + file_name)
#if _name_ == "_main_":
upload_files()



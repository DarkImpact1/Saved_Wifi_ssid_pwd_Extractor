import os 
import sys
import subprocess

def file_extractor():
    path = os.getcwd()
    command = ["netsh", "wlan", "export", "profile", "key=clear"]
    subprocess.run(command,shell=True, capture_output=True).stdout.decode()
    return path 


def append_file(path):
    wifi_file=[]
    for files in os.listdir(path):
        if files.startswith("Wi-Fi") and files.endswith(".xml"):
            wifi_file.append(files)
    return wifi_file


def detail_extractor(file):
    wifi_id=[]
    wifi_password=[]
    for sub_file in file:
        with open(sub_file,"r") as f:
            for line in f.readlines()[3:]:
                if "<name>" in line:
                    line.strip()
                    name=line[9:-8]
                    wifi_id.append(name)
                if "keyMaterial" in line:
                    line.strip()
                    password = line[17:-15]
                    wifi_password.append(password)
    main_file = zip(wifi_id,wifi_password)
    return main_file

def make_doc(zip_file):
    for id,pwd in zip_file:
        sys.stdout = open("confidential.txt","a")
        print(f"SSID: {id} --------------- Password: {pwd}")
    sys.stdout = sys.__stdout__


def delete_files(path):
    os.chdir(path)
    for file in os.listdir(path):
        if file.startswith("Wi-Fi") and file.endswith(".xml"):
            os.remove(path+"\\"+file)
    print("done")

if __name__=="__main__":
    path = file_extractor()
    list_wifi = append_file(path)
    zip_file = detail_extractor(list_wifi)
    make_doc(zip_file)
    delete_files(path)
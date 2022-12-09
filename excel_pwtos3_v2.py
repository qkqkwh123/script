
import os
import pandas as pd
import win32com.client
import boto3
# import boto3.session
# from concurrent import futures
# from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import botocore
import shutil


BUCKET_NAME = 'event.amway.co.kr'
# file_name = 'C:\\test\\survey\\atv.jpg'
# KEY = 'survey/CM/6/7986321/family2/1669344189605_1670378615719.jpg'
########## 테스트 완료 S3 별도로####

s3 = boto3.resource('s3')

def download(KEY, file_name):
    #print(KEY)
    dir = file_name.replace("/","\\",10)
    dir_name = 'C:\\test\\'
    path2 = os.path.join(dir_name, dir)
    print(path2)
    s3 = boto3.resource('s3')
    
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, path2)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


    

def zip(name):
    print(name)
    shutil.make_archive(name, 'zip', 'C:\\test\\survey')






filename = "C:\\test\\파일_경로_20221208.xlsx"

# 엑셀 파일 읽어 오기
df = pd.read_excel(filename, engine='openpyxl')

# def download_object(key):
#     download_path = Path(LOCAL_DOWNLOAD_PATH) / key
#     # print("Downloading {key} to {download_path}")
#     print(str(download_path))
#     # client = boto3.client('s3')
    # client.download_file(bucket, key, str(download_path))    

for i in df.index:
    key = df.loc[i, "파일 경로"]
    # download_object(str(key))
    #print(os.path.dirname (key))
    test = os.path.dirname (key)
    print(test)
    Path("C:/test/"+test).mkdir(parents=True, exist_ok=True)

    
for i in df.index:
    key = df.loc[i, "파일 경로"]
    # download_object(str(key))
    #print(os.path.dirname (key))
    name = '2002'
    download(key,key)
    zip(name)


print(os.listdir(os.getcwd()))   #현재 디렉토리에 있는 파일 리스트





    ####



# file_name = 'image/atv_rider0001.jpg'
# bucket = 'flxr-yolo'
# key = 'image/atv_rider0001.jpg'

# # Download the file
# client = boto3.client('s3')
# client.download_file(bucket, key, file_name)





#
# try:
#     #     s3.Bucket(BUCKET_NAME).download_file(KEY, file_name)
#     # except botocore.exceptions.ClientError as e:
#     #     if e.response['Error']['Code'] == "404":
#     #         print("The object does not exist.")
#     # else:
#     #     raise
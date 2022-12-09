import pandas as pd
import win32com.client
import boto3
import boto3.session
from concurrent import futures
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

KEYS_TO_DOWNLOAD = [...] # all the files that you want to download
BUCKET_NAME = "event.amway.co.kr"
LOCAL_DOWNLOAD_PATH = "C:/test"  

def download_object(file_name):
    """Downloads an object from S3 to local."""

    s3_client = boto3.client("s3")
    download_path = Path(LOCAL_DOWNLOAD_PATH) / file_name
    print(f"Downloading {file_name} to {download_path}")
    s3_client.download_file(
        BUCKET_NAME,   # 버킷이름
        file_name,    # 다운로드 할 객체를 지정
        str(download_path)  #Download한 파일이저장될 위치를 지정
    )
    return "Success"

def download_parallel_multiprocessing():
    with ProcessPoolExecutor() as executor:
        future_to_key = {executor.submit(download_object, key): key for key in KEYS_TO_DOWNLOAD}

        for future in futures.as_completed(future_to_key):
            key = future_to_key[future]
            exception = future.exception()

            if not exception:
                yield key, future.result()
            else:
                yield key, exception

if __name__ == "__main__":
    for key, result in download_parallel_multiprocessing():
        print(f"{key}: {result}")




filename = 'C:/test/파일_경로_20221130_TEST.xlsx'

# 엑셀 파일 읽어 오기
df = pd.read_excel(filename, engine='openpyxl')



for i in df.index:
    file_name = df.loc[i, "파일 경로"]
    download_object(file_name)
    print(file_name)
    










    ##########
    


# filename = 'C:/test/파일_경로_20221130_TEST.xlsx'

# # 엑셀 파일 읽어 오기
# df = pd.read_excel(filename, engine='openpyxl')



# for i in df.index:
#     file_name = df.loc[i, "파일 경로"]
#     download_object(file_name)
#     print(file_name)
    
import os
import pandas as pd'
import win32com.client

bucket = 'event.amway.co.kr'
filepath = "C:/s3/Source"
filename = 'C:/test/파일_경로_20221130_TEST.xlsx'

# 엑셀 파일 읽어 오기
df = pd.read_excel(filename, engine='openpyxl')


for i in df.index:
    key = df.loc[i, "파일 경로"]
    print (bucket)
    # print('aws s3 cp s3://'+ str(bucket) + "//"+ str(key) + " " + filepath + key)
    os.system('aws s3 cp "s3://event.amway.co.kr/survey/CM/1/1007597/family1/20221128_133208_1669712042187.jpg" "C:\s3\Source\survey/CM/1/1007597/family1/20221128_133208_1669712042187.jpg"')
    # # # print(key)

    # ="aws s3 cp ""s3://event.amway.co.kr/"&A2&""" ""C:\s3\Source\"&A2&""""
    # aws s3 cp "s3://event.amway.co.kr/survey/CM/1/1007597/family1/20221128_133208_1669712042187.jpg" "D:\s3\Source\survey/CM/1/1007597/family1/20221128_133208_1669712042187.jpg"

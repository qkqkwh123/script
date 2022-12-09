import boto3
import os 


file_name = 'C:\\test\\sev\\sev\\KRAWSELP065 Information.jpg'
bucket = 'kor-prod-migration'
key = 'test/KRAWSELP065 Information.jpg'


prefix = 'dirname'
for object in bucket.objects.filter(Prefix = 'dirname'):
    if object.key == prefix:
        os.makedirs(os.path.dirname(object.key), exist_ok=True)
        continue;
    bucket.download_file(object.key, object.key)
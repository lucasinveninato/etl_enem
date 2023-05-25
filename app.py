import os
from dotenv import load_dotenv
import boto3
import logging

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

bucket_name = 'bucket-igti'
file_path = './enem'
s3_prefix = 'raw_data'

for root, dirs, files in os.walk(file_path):
    for file in files:
        local_file_path = os.path.join(root, file)
        s3_object_key = os.path.join(s3_prefix, os.path.relpath(local_file_path, file_path))
        s3.upload_file(local_file_path, bucket_name, s3_object_key)

logging.info('Upload succefull')
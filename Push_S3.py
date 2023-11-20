import boto3
import os
# Replace these with your AWS credentials and S3 bucket information
aws_access_key = "AKIAWVKQBF2LVYONJBRP"
aws_secret_key = "rqK3Q7kLls0OZYvd6/3sjf+XYTbByae3ZV+oZcZX"
aws_region = "ap-south-1"
bucket_name = 'sap-invoices-2'
# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)
# Create an S3 client
s3 = session.client('s3')
# Function to upload a file to S3
def upload_file_to_s3(file_path, s3_key):
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f'Uploaded {file_path} to S3 as {s3_key}')
    except Exception as e:
        print(f'Error uploading {file_path} to S3: {str(e)}')
# Upload a single file
# file_to_upload = '/path/to/local/file.txt'
# s3_key = 'folder/file.txt'
# upload_file_to_s3(file_to_upload, s3_key)
# Upload an entire folder
local_folder = r"/Users/finkraft/PycharmProjects/SAP_Concur/sap_100" # folder to push on s3 bucket
# s3_prefix = 'jivi/'
for root, dirs, files in os.walk(local_folder):
    for file in files:
        local_file_path = os.path.join(root, file)
        s3_file_key =  os.path.relpath(local_file_path, local_folder)
        upload_file_to_s3(local_file_path, s3_file_key)
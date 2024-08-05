import boto3
s3 = boto3.client('s3', region_name='ap-northeast-2')
bucket_name = 'aws-web-app-static-neehar'  
response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    'LocationConstraint': 'ap-northeast-2'})
print(f'Bucket {bucket_name} created successfully.')

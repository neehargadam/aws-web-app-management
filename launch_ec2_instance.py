import boto3
ec2 = boto3.client('ec2', region_name='ap-northeast-2')
instance_params = {
    'ImageId': 'ami-062cf18d655c0b1e8', 
    'InstanceType': 't2.micro',         
    'MinCount': 1,
    'MaxCount': 1,
    'KeyName': 'neehar-generic-test-key',         
    'SecurityGroupIds': ['sg-00d7aed5c999a79cd'], 
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Neehar-WebServerInstance'}
            ]
        }
    ]
}
response = ec2.run_instances(**instance_params)
instance_id = response['Instances'][0]['InstanceId']
print(f'EC2 instance launched with ID: {instance_id}')

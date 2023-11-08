import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

instanceName = ''
reservations = response['Reservations']

for reservation in reservations:
    instances = reservation['Instances']

    for instance in instances:
        for tag in instance['Tags']:
            if tag['Key'] == 'Environment':
                environmentTag = tag['Value']
                break
        if (environmentTag == 'Dev' and 'running' in instance['State']['Name']):
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
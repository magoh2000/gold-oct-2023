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
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instanceName = tag['Value']
                break
        print("InstanceID:", instance['InstanceId'], "|| Name:", instanceName, "|| State:", instance['State']['Name'], "|| Environment tag: ", environmentTag)
        if (environmentTag == 'Dev' and 'running' in instance['State']['Name']):
            print("Stopping", instance['InstanceId'], " -- ", instanceName)
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
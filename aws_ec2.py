#!/bin/python3
import boto3
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('AWS EC2'))

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)
imageId=[]
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        imageId=instance['InstanceId']
        print(f"Instance ID: {instance['InstanceId']}")

action=input("Enter the action <start|stop|describe> : ")

if action == 'stop':
    response_1 = ec2.stop_instances(InstanceIds=[imageId,],)
    print(response_1)
elif action == 'start':
    response_1=ec2.start_instances(InstanceIds=[imageId,],)
    print(response_1)
elif action == 'describe':
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("-"*50)
            private_ip = instance['PrivateIpAddress']
            if 'PublicIpAddress' in instance: 
                public_ip=instance['PublicIpAddress']
                print(f"Instance ID: {instance['InstanceId']},PrivatIP: {private_ip}, PublicIP: {public_ip}")
            else:
                print(f"Instance ID: {instance['InstanceId']}, PrivatIP: {private_ip} ")




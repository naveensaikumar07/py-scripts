#!/bin/python3
import boto3
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('AWS EC2'))

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        private_ip = instance['PrivateIpAddress']
        public_ip=instance['PublicIpAddress']
        print(f"Instance ID: {instance['InstanceId']}, PrivatIP: {private_ip} , PublicIP: {public_ip}")

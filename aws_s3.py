#!/bin/python3
import boto3
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('AWS S3'))

s3=boto3.client('s3')
response=s3.list_buckets()
print(response)
import json
import csv
import time
import boto3

client = boto3.client(
    'firehose',
    region_name='us-east-1'
    )

while True:
    input_data = csv.DictReader(open('banking_loss.csv'))

    for line in input_data:
        raw_data = {}
        raw_data.update(line)
        data = json.dumps(raw_data)
        response = client.put_record(
            DeliveryStreamName = 'Source',
            Record = {
                'Data':data
            }
        )
        print data
        time.sleep(1)
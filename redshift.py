import json
import csv
import time
import boto3

client = boto3.client('firehose')

while True:
    input_data = csv.DictReader(open('banking_loss.csv'))

    for line in input_data:
        raw_data = {}
        raw_data.update(line)
        data = json.dumps(raw_data)
        response = client.put_record(
            DeliveryStreamName = 'Redshift',
            Record = {
                'Data':data
            }
        )
        print data
        time.sleep(1)

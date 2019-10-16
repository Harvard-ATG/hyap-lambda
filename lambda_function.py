import requests
import boto3
import json

def lambda_handler(event, context):

    s3 = boto3.client("s3")
    r = requests.get('http://anth1130.omeka.fas.harvard.edu/api/items/')
    finds = []

    for idx, item in enumerate(r.json()):
        omeka_data = {
            'omekaId': item['id'],
            'externalURL': item['url'],
        }
        for text in item['element_texts']:
            omeka_data[text['element']['name']] = text['text']
        if item['files']['count'] > 0:
            files = requests.get(item['files']['url'])
            media = [{'urls': f['file_urls']} for f in files.json()]
        else:
            media = []
        finds.append({'id': str(idx), 'omekaData': omeka_data, 'media': media})

    s3.put_object(Bucket='atg-hyap-data', Key='omeka.json', Body=json.dumps({'data': {'finds': finds}}))
    return {
        'statusCode': 200,
        'body': json.dumps('Omeka data dumped!')
    }
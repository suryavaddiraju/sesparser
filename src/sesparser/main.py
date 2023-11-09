"""Copyright 2023 Vaddiraju Surya Teja

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""
import json
import boto3
from .headers import headers as hd
from .body import get_body as bdy
from .attachments import extract_attachments as attch
from .attachments import inline_handler as inattch
from .parse_it import parse_email_only
from .store_aws import handle_s3
from boto3.dynamodb.types import TypeSerializer
def offline(email_message,message_type="bytes",inline=True):
    email_object = parse_email_only(email_message,message_type)
    headers = hd(email_object)
    body = bdy(email_object)
    attachments = attch(email_object)
    output = {
        **headers,
        **body,
        **attachments,
    }
    if not inline:
        pass
    elif inline:
        attachments, body = inattch(attachments,body)
        output = {
            **headers,
            **body,
            **attachments,
        }
    return output

def online_dynamodb(inputs,table_name,region_name):
    dynamodb = boto3.client(
        'dynamodb',
        region_name=region_name,
    )
    requests = []
    serializer = TypeSerializer()
    for item in inputs:
        put_request = {
            'PutRequest': {
                'Item': {k: serializer.serialize(v) for k, v in item.items()}
            }
        }
        requests.append(put_request)
    request_items = {
        table_name: requests,
    }
    response = dynamodb.batch_write_item(
        RequestItems=request_items,
        ReturnConsumedCapacity='TOTAL',
        ReturnItemCollectionMetrics='NONE'
    )
    return response

def online(event,dynamodb=False,table_name="",region_name="us-east-1",inline=True):
    aa = event['Records'][0]['Sns']['Message']
    aa = json.loads(aa)
    bucket_name = aa['receipt']['action']['bucketName']
    main_object_key = aa['receipt']['action']['objectKey']
    a = aa['receipt']['recipients']
    recipient_list = list(set(b.lower() for b in a))
    s3 = boto3.client('s3')
    ff = s3.get_object(
        Bucket=bucket_name,
        Key=main_object_key
    )
    email_message = ff['Body'].read()
    output = offline(email_message,inline=inline)
    new_output = handle_s3(output,recipient_list,s3,bucket_name,main_object_key)
    if dynamodb:
        new_output = online_dynamodb(new_output,table_name,region_name)
    return new_output
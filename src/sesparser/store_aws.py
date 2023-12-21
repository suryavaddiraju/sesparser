# Copyright 2023 Vaddiraju Surya Teja

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
def handle_s3(output,recipient_list,s3,bucket_name,main_object_key):
    message_id = output["message_id"]
    raw_body = output["body"]["body"]
    raw_body_type = output["body"]["body_type"]
    output["body"]["location"] = {
        "store_type": "s3",
        "s3": {
            "bucket": bucket_name,
            "key": ""
        }
    }
    output["archive"] = {
        "store_type": "s3",
        "s3": {
            "bucket": bucket_name,
            "key": ""
        }
    }
    for attachment in output["attachments"]:
        attachment["location"] = {
            "store_type": "s3",
            "s3": {
                "bucket": bucket_name,
                "key": ""
            }
        }
    new_output = []
    for dd in recipient_list:
        e = dd.split('@')[1]
        f = dd.split('@')[0]
        recipient_email_folder = e+"/"+f
        body_file_id = "email_body"+"/"+recipient_email_folder+"/"+message_id
        response_s3 = s3.put_object(
            Body=raw_body,
            Bucket=bucket_name,
            Key=body_file_id,
            ContentType=raw_body_type,
            StorageClass= "STANDARD_IA",
        )
        deep_copy = copy.deepcopy(output)
        del deep_copy["body"]["body"]
        deep_copy["body"]["location"]["s3"]["key"] = body_file_id
        count = 0
        for attch in output["attachments"]:
            file_id = "email_attachments"+"/"+recipient_email_folder+"/"+message_id+"/"+attch["filename"]
            response_s3 = s3.put_object(
                Body=attch["data"],
                Bucket=bucket_name,
                Key=file_id,
                ContentType=attch["file_type"],
                StorageClass= "STANDARD_IA",
            )
            del deep_copy["attachments"][count]["data"]
            deep_copy["attachments"][count]["location"]["s3"]["key"] = file_id
            count += 1
        archive_file_id = "email_archives"+"/"+recipient_email_folder+"/"+message_id
        response_s3 = s3.copy_object(
            Bucket=bucket_name,
            Key=archive_file_id,
            CopySource={
                'Bucket': bucket_name,
                'Key': main_object_key
            },
            ContentType="message/rfc822",
            StorageClass= "GLACIER_IR"
        )
        deep_copy["archive"]["s3"]["key"] = archive_file_id
        deep_copy["recipient"] = dd
        new_output.append(deep_copy)
    del output
    response_s3 = s3.delete_object(Bucket=bucket_name,Key=main_object_key)
    return new_output
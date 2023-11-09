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
import mimetypes
import uuid
import base64

# This function gives file type bt giving file name
#E.g.: input = example.pdf => output = application/pdf
def get_file_type(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type or 'unknown'

# This function extracts attachment from part of email message
def extract_attachments_from_part(part):
    attachments = []
    content_disposition = part.get("Content-Disposition", None)
    if content_disposition:
        filename = part.get_filename()
        if not filename:
            filename = uuid.uuid4()
        attachment = {}
        attachment['filename'] = filename
        file_type = get_file_type(filename)
        if file_type == "unknown":
            file_type = "application/octet-stream"
        attachment['file_type'] = file_type
        attachment['data'] = part.get_payload(decode=True)
        attachment["size"] = len(attachment["data"])
        cid = part["Content-ID"]
        if cid:
            attachment["cid"] = cid.split("<")[1].split(">")[0]
        attachments.append(attachment)
    return attachments

# This function extracts all the attachments from email messages
def extract_attachments(email_message):
    attachments = []
    if email_message.is_multipart():
        for part in email_message.walk():
            attachment = extract_attachments_from_part(part)
            attachments.extend(attachment)
    else:
        attachment = extract_attachments_from_part(email_message)
        attachments.extend(attachment)
    attachments_data = {
        "attachments_count": len(attachments),
        "attachments": attachments
    }
    return attachments_data

# This function modifies email html body with attachments taken from above function
def inline_attachments(attachments_list, html_body):
    copied_list = attachments_list[:]
    for attachment in attachments_list:
        if "cid" in attachment:
            cid = attachment['cid']
            if ("cid:" + cid) in html_body:
                html_body = html_body.replace('cid:' + cid, 'data:' + attachment["file_type"] + ';base64,' + base64.b64encode(attachment['data']).decode('utf-8'), -1)
                copied_list.remove(attachment)
    return copied_list, html_body

#This function check if any html body is present in the email and if so gives the body to above function to replace with inline attachments
def inline_handler(attachments_data,body_data):
    if body_data["body"]["body_type"] == "text/html":
        new_attachments, new_body_data = inline_attachments(attachments_data["attachments"],body_data["body"]["body"])
        body_data["body"]["body"] = new_body_data
        body_data["body"]["size"] = len(new_body_data)
        attachments_data["attachments"] = new_attachments
        attachments_data["attachments_count"] = len(new_attachments)
        return attachments_data, body_data
    else:
        return attachments_data, body_data
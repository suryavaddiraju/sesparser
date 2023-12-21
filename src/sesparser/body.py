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

import chardet

def get_charset(email_message):
    if email_message.get_content_charset():
        return email_message.get_content_charset()
    elif email_message.get_charset():
        return email_message.get_charset()
    else:
        # Use chardet to detect character encoding
        raw_data = email_message.get_payload(decode=True)
        result = chardet.detect(raw_data)
        return result.get("encoding")

def get_body_from_part(part):
    charset = part.get_content_charset() or get_charset(part)
    payload = part.get_payload(decode=True)
    if payload:
        return payload.decode(charset)
    return None

def get_body(email_message):
    body_data = {}
    if email_message.is_multipart():
        html_body = None
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                plain_body = get_body_from_part(part)
            elif content_type == 'text/html':
                html_body = get_body_from_part(part)
                break
        if html_body:
            body_data["body"] = html_body
            body_data["body_type"] = "text/html"
        elif plain_body:
            body_data["body"] = plain_body
            body_data["body_type"] = "text/plain"
    else:
        charset = email_message.get_content_charset() or get_charset(email_message)
        other_payload = email_message.get_payload(decode=True)
        if other_payload:
            body_data["body"] = other_payload
            body_data["body_type"] = "application/octet-stream"
    body_data["size"] = len(body_data["body"])
    body_data_s = {}
    body_data_s["body"] = body_data
    return body_data_s
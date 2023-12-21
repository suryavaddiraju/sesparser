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

from email.header import decode_header
from email.utils import parseaddr,getaddresses
from datetime import datetime
import uuid
import pytz
def decode_header_value(value):
    decoded_value = decode_header(value)
    result = []
    for part, encoding in decoded_value:
        if isinstance(part, bytes):
            if encoding:
                result.append(part.decode(encoding))
            else:
                result.append(part.decode())
        else:
            result.append(part)
    return ''.join(result)

# This function converts Timestamp in email to YYYYMMDDHHMMSS in number format
def convert_to_utc(email_message):
    data = {}
    kk = email_message["Received"][-37:]
    time_stamp = datetime.strptime(kk, "%a, %d %b %Y %H:%M:%S %z (%Z)")
    utc_time = time_stamp.astimezone(pytz.UTC)
    utc_timestamp_str = utc_time.strftime("%Y%m%d%H%M%S")
    data["timestamp"] = int(utc_timestamp_str)
    return data

# This function gives all Security related data about the message
def security_results(email_message):
    data = {}
    auth_results = email_message["Authentication-Results"]
    data["spam-check"] = email_message["X-SES-Spam-Verdict"].lower()
    data["virus"] = email_message["X-SES-Virus-Verdict"].lower()
    if "spf=" in auth_results:
        value_spf = auth_results.split('spf=')[1].split(" ")[0]
        if value_spf == "pass":
            data["spf"] = value_spf
        else:
            data["spf"] = "fail"
    else:
        data["spf"] = "fail"
    if "dkim=" in auth_results:
        value_dkim = auth_results.split('dkim=')[1].split(" ")[0]
        if value_dkim == "pass":
            data["dkim"] = value_dkim
            sign = auth_results.split('dkim=')[1].split(" ")[1].split(";")[0]
            if "@" in sign:
                sign_value = sign.split("@")[1]
        else:
            data["dkim"] = "fail"
    else:
        data["dkim"] = "fail"
    if "dmarc=" in auth_results:
        value_dmarc = auth_results.split('dmarc=')[1].split(" ")[0]
        if value_dmarc == "pass":
            data["dmarc"] = value_dmarc
        else:
            data["dmarc"] = "fail"
    else:
        data["dmarc"] = "fail"
    if all(data[key] == "pass" for key in list(data)):
        data["folder"] = "inbox"
    else:
        data["folder"] = "spam"
    data["smtp_server"] = auth_results.split(' helo=')[1].split(";")[0]
    data["mailed_by"] = auth_results.split(' envelope-from=')[1].split("; ")[0].split("@")[1]
    if sign_value:
        data["signed_by"] = sign_value
    data["sender_ip"] = auth_results.split(' client-ip=')[1].split("; ")[0]
    return data

def all_message_id(email_message):
    data = {}
    message_id = email_message["Message-ID"]
    References = email_message["References"]
    In_Reply_To = email_message["In-Reply-To"]
    if message_id:
        data["message_id"] = ''.join(message_id.split())
    else:
        data["message_id"] = str(uuid.uuid4())
    if In_Reply_To:
        data["In_Reply_To"] = ''.join(In_Reply_To.split())
    else:
        data["In_Reply_To"] = ""
    if References:
        data["References"] = [ref.strip() for ref in References.split() if ref.strip()]
    else:
        data["References"] = []
    return data

def persons(email_message):
    persons = {
        'To': [],
        'Cc': [],
        'Bcc': [],
        "Reply-To": []
    }
    for recipient_field in ['To', 'Cc', "Reply-To"]:
        if recipient_field in email_message:
            recipients_list = getaddresses(email_message.get_all(recipient_field, []))
            for recipient in recipients_list:
                recipient_name, recipient_email = parseaddr(decode_header_value(recipient[1]))
                persons[recipient_field].append(recipient_email)
    if ("for" and "@") in email_message["Received"]:
        prov_bcc = email_message["Received"].split("for ")[1].split(";")[0]
        if prov_bcc not in persons["To"] and prov_bcc not in persons["Cc"]:
            persons["Bcc"].append(prov_bcc)
    sender_name, sender_email = parseaddr(decode_header_value(email_message['From']))
    persons["sender_name"] = sender_name
    persons["sender_email"] = sender_email
    return persons

def subject(email_message):
    data = {}
    subject = decode_header_value(email_message['Subject'])
    if not subject:
        subject = "(No Subject)"
    data["subject"] = subject
    return data

def other_headers():
    """This creates manual additional headers
    such as email read status and important marking status

    :return: The values of is_read and is_starred
    :rtype: dict
    """
    data = {}
    data["is_read"] = False
    data["is_starred"] = False
    return data

def headers(email_message):
    data = {
        **security_results(email_message),
        **other_headers(),
        **all_message_id(email_message),
        **convert_to_utc(email_message),
        **persons(email_message),
        **subject(email_message)
    }
    return data
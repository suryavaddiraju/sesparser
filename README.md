# sesparser

**sesparser** is a simple, yet elegant, Email parsing library received through AWS SES.

```python
>>> import sesparser
>>> s = sesparser.online('s3_ses_event')
>>> s.recipient
someone@example.com
>>> s = sesparser.online('s3_ses_event',dynamodb=True,table_name="core-mail-data-1")
{'UnprocessedItems': {}, 'ConsumedCapacity': [{'TableName': 'core-mail-data-1', 'CapacityUnits': 20.0}], 'ResponseMetadata': {'RequestId': 'H7210I9JBDH33CKJH1JO16QSEFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Nov 2023 03:20:55 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '98', 'connection': 'keep-alive', 'x-amzn-requestid': 'H7210I9JBDH33CKJH1JO16QSEFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2598397897'}, 'RetryAttempts': 0}}
>>> s.archive.s3.key
'<DS0PR02MB924561B21196B9EE08B3B93BC2AFA@DS0PR02MB9245.namprd02.prod.outlook.com>'
>>> s.timestamp
20231109233614
>>> print(s)
{"all_email_keys":"all_email_key_values"}
```

sesparser allows you to work on lambda extremely easily. There’s no need to manually add query strings to your function, or to decode your `eml` data — but nowadays, just use the `SNS-Event` method!

sesparser is one of the most downloaded Python packages today, pulling in around `30 downloads / week`— according to GitHub

[![Downloads](https://img.shields.io/badge/Downloads-200-blue.svg)](https://pepy.tech/project/sesparser)
[![Supported Versions](https://img.shields.io/badge/suported%20versions-Python%203.5%20above-blue.svg)](https://pypi.org/project/sesparser)
[![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/suryavaddiraju/sesparser/graphs/contributors)

## Installing sesparser and Supported Versions

sesparser is available on PyPI:

```console
$ python -m pip install sesparser
```

sesparser officially supports Python 3.7+.

## Supported Features & Best–Practices

sesparser is ready for the demands of building robust and reliable email parsing applications, for the needs of today.

- Handling inline attachments
- File placeholders
- cloud saving
- Data decoding
- Advanced multipart handler
- Different domains handler
- Handle offline too
- Extra layer detection of filenames
- Added support for AWS Lambda Layer
- Advanced Security Details
- Spam recognition
- DKIM,DMARC,SPF and other standard compliance
- Segregating on user recipient mail id
- Bulk processing

## API Reference and User Guide available on [Read the Docs](https://sesparser.readthedocs.io)

[![Read the Docs](https://raw.githubusercontent.com/suryavaddiraju/sesparser/main/ext/ss.png)](https://sesparser.readthedocs.io)

## Cloning the repository

```shell
git clone -c fetch.fsck.badTimezone=ignore https://github.com/suryavaddiraju/sesparser.git
```

---

[![SURYA VADDIRAJU](https://raw.githubusercontent.com/suryavaddiraju/sesparser/main/ext/kr.png)](https://surya.vaddiraju.in) [![Python Software Foundation](https://raw.githubusercontent.com/suryavaddiraju/sesparser/main/ext/psf.png)](https://www.python.org/psf)
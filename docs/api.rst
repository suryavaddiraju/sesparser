Developer Interface
===================

.. module:: sesparser

Main Interface
--------------
All of sesparser functionality can be accessed by these 2 methods.
They all return an instance of the python dictionary object.

.. autofunction:: online
.. autofunction:: offline

Handling Attachments
--------------------

.. autofunction:: sesparser.attachments.get_file_type
.. autofunction:: sesparser.attachments.extract_attachments_from_part
.. autofunction:: sesparser.attachments.extract_attachments
.. autofunction:: sesparser.attachments.inline_attachments
.. autofunction:: sesparser.attachments.inline_handler

Handling Body part
------------------

.. autofunction:: sesparser.body.get_charset
.. autofunction:: sesparser.body.get_body_from_part
.. autofunction:: sesparser.body.get_body

Parsing Email Headers
---------------------

.. autofunction:: sesparser.headers.decode_header_value
.. autofunction:: sesparser.headers.convert_to_utc
.. autofunction:: sesparser.headers.security_results
.. autofunction:: sesparser.headers.all_message_id
.. autofunction:: sesparser.headers.persons
.. autofunction:: sesparser.headers.subject
.. autofunction:: sesparser.headers.other_headers
.. autofunction:: sesparser.headers.headers

Core Backend
------------

.. autofunction:: sesparser.main.offline
.. autofunction:: sesparser.main.online_dynamodb
.. autofunction:: sesparser.main.online

Email Message Object Generation
-------------------------------

.. autofunction:: sesparser.parse_it.parse_email_only

AWS Backend Integration
-----------------------

.. autofunction:: sesparser.store_aws.handle_s3
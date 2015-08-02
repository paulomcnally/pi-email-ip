import mandrill
import os
import socket
import json

# load ips
ips = json.dumps([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

# send email
try:
    mandrill_client = mandrill.Mandrill(os.environ['MANDRILL_API_KEY'])
    message = {
        'from_email': 'device@raspberrypi.org',
        'from_name': 'Raspberry PI',
        'subject': 'Raspberry PI - IP',
        'html': ips,
        'text': ips,
        'important': False,
        'tags': ['raspberry-pi-ip'],

        'to':
            [
                {
                    'email': os.environ['TO_EMAIL'],
                    'name': os.environ['TO_NAME'],
                    'type': 'to'
                }
            ],
     }
    result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')

    print result

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
    raise

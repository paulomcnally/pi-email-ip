import mandrill
import sys
import socket
import json

# sys.argv[1] = ip
# sys.argv[2] = MANDRILL_API_KEY
# sys.argv[3] = TO_EMAIL
# sys.argv[3] = TO_NAME

# load ips
ips = json.dumps([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

# send email
try:
    mandrill_client = mandrill.Mandrill(sys.argv[2])
    message = {
        'from_email': 'device@raspberrypi.org',
        'from_name': 'Raspberry PI',
        'subject': 'Raspberry PI - IP',
        'html': sys.argv[1],
        'text': sys.argv[1],
        'important': False,
        'tags': ['raspberry-pi-ip'],

        'to':
            [
                {
                    'email': sys.argv[3],
                    'name': sys.argv[4],
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

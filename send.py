import sendgrid
import sys

# sys.argv[1] = ip
# sys.argv[2] = SENDGRID_APIKEY
# sys.argv[3] = TO_EMAIL

# send email
client = sendgrid.SendGridAPIClient(apikey=sys.argv[2])
message = sendgrid.Mail()

message.add_to(sys.argv[3])
message.set_from('device@raspberrypi.org')
message.set_subject('Raspberry PI - IP')
message.set_html(sys.argv[1])

client.send(message)

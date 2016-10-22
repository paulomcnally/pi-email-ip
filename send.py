import sendgrid

# sys.argv[1] = ip
# sys.argv[2] = SENDGRID_APIKEY
# sys.argv[3] = TO_EMAIL

# send email

sg = sendgrid.SendGridAPIClient(apikey=sys.argv[2])
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": sys.argv[3]
        }
      ],
      "subject": "Raspberry PI - IP"
    }
  ],
  "from": {
    "email": "device@raspberrypi.org"
  },
  "content": [
    {
      "type": "text/plain",
      "value": sys.argv[1]
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

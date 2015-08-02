PI Email IP
===========

Send IP address to email.

## Require

    $ pip install mandrill

* 1 - Set **MANDRILL_API_KEY** environment variable.
* 2 - Set **TO_EMAIL** environment variable.
* 3 - Set **TO_NAME** environment variable.

> On /home/pi/.profile added environment variables.

    export MANDRILL_API_KEY="... you're api key ..."
    export TO_EMAIL="foo@bar.com"
    export TO_NAME="Foo Bar"

To get a MANDRILL_API_KEY create an account on https://www.mandrill.com/

## Run script

    python send.py

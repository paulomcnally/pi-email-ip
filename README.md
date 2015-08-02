PI Email IP
===========

Send IP address to email with Raspberry Pi

## Require

    $ pip install mandrill

## Clone this repository

    $ git clone https://github.com/paulomcnally/pi-email-ip.git

## Edit ip file and change lines 8, 9 and 10.

    MANDRILL_API_KEY=""
    TO_EMAIL=""
    TO_NAME=""

> To get a MANDRILL_API_KEY create an account on http://mandrill.com/. TO_EMAIL is you're email addres and TO_NAME is you're name.

## Copy ip file

    $ sudo cp ip /etc/init.d/ip

## Set correct permissions

    $ sudo chmod 755 /etc/init.d/ip

## Added ip to start commands

    $ sudo update-rc.d ip defaults

## Run test

    $ sudo /etc/init.d/ip start

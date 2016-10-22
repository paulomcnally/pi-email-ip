PI Email IP
===========

Send local IP address to email with Raspberry Pi

## Require

    $ pip install sendgrid

## Clone this repository

    $ git clone https://github.com/paulomcnally/pi-email-ip.git

## Move to repository directory

    cd pi-email-ip

## Edit ip file and change lines 8, 9 and 10.

    SENDGRID_APIKEY=""
    TO_EMAIL=""
    TO_NAME=""

> To get a SENDGRID_APIKEY create an account on https://sendgrid.com/. TO_EMAIL is you're email address.

## Copy ip file

    $ sudo cp ip /etc/init.d/ip

## Set correct permissions

    $ sudo chmod 755 /etc/init.d/ip

## Added ip to start commands

    $ sudo update-rc.d ip defaults

## Run test

    $ sudo /etc/init.d/ip start

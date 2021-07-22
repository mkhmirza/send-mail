#!/usr/bin/python env

# sending email using python
import smtplib
# try to use this but, for me the data is not showing properly
# from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import argparse
import sys
import os
import sfunc


parser = argparse.ArgumentParser(description='Send Email using command line')
parser.add_argument('-s', '--subject', help='subject of the email')
# change email address to your, so you dont have to use this option again again
# use a gmail account as this only supports gmail service right now
parser.add_argument('-f', '--from', help="sender's email address", default='abc@example.com')
parser.add_argument('-t', '--to', help="recipient's email address")
parser.add_argument('-b', '--body', help='body of the email')
parser.add_argument('-a', '--attachment', help='attachement of the email')
parser.add_argument('-c', "--server", help="select a email server", default="gmail.com")
args = vars(parser.parse_args())

# get all values
subject = args['subject']
fromEmail = args['from']
toEmail = args['to']
body = args['body']
attachment = args['attachment']
server = args['server']

if server == "gmail.com":
    serverAddress = "smtp.gmail.com"
    port = 465

# reading password
EMAIL = fromEmail
with open('pass', 'r') as f:
    PASS = f.readline()

print("*****************************")
print('      Information            ')
print("*****************************")
print(f'Subject:     {subject}')
print(f'FromEmail:   {fromEmail}')
print(f'ToEmail:     {toEmail}')
print(f'Body:        {body}')
print('-----------------------------')
print(f'Server:      {server}')
print(f'Port:        {port}')
if attachment:
    print(f'Attachement: {attachment}')
print("*****************************")

print()
informationCorrect = input('Is the above information correct?(y/n): ').lower()

# information is correct
if informationCorrect == 'y':

    # if from email is correct
    if sfunc.matchEmail(fromEmail, server):

        # if using emailmessage:
        # msg = EmailMessage()
        # constructing a email message
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = fromEmail
        # sending to myself, change to whatever email to send to
        msg['To'] = toEmail

        text = MIMEText(body)
        msg.attach(text)

        # open the picture for attachment
        # use a loop if more than 1 attachment
        # files = [filename1, filename2]
        # uncomment the below code and indent change the filename in with open()
        # for i in files:
        # if attachment is given

        if attachment:
            # try to split if there are multiple attachements
            files  = attachment.split(',')

            for i in range(0, len(files)):
                with open(files[i], "rb") as f:
                    # reading a bytes of piture
                    data = f.read()
                    # getting filename for the attachment
                    fileName = f.name
                    # getting file extension for determining if its a pdf word or anything else                   
                    # _, fileExt = os.path.splitext(fileName)

                f = MIMEApplication(_data=data)
                # add header to the attachment
                f.add_header('Content-Disposition','attachment', filename=fileName)
        
                # add attachment to the message
                # use msg.add_attachment if using emailmessage
                msg.attach(f)

        # if using smtplib.SMTP uncomment the ehlo and startssl line
        # use SSL to not write the ehlo and startssl line
        # also change the port number
        with smtplib.SMTP_SSL(serverAddress, port) as smtp:
            # smtp.ehlo()
            # # encrypting the traffic
            # smtp.starttls()
            # smtp.ehlo()

            smtp.login(fromEmail, PASS)

            # uncomment this if not using email message import
            # subject = "Test Email From Python"
            # body = "This is a test message from python"
            # msg = f"Subject: {subject}\n\n{body}"

            # # sending email to me from me
            # smtp.sendmail(EMAIL, EMAIL, msg)

            # send message using send_message if using emailmessage import
            smtp.send_message(msg)

        print("Email Sent")
    else:
        print("Invalid Sender's Email..")
        sys.exit(0)

# information is not correct
else:
    print('Exiting...')
    sys.exit(0)

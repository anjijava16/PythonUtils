#=====================================================================================================
# ScritName          :
# Version            : v1.0
# Description        :
# Developed By       :
# Developed On       :
# Last Modified      :
# Last Modified Date :
# Modified by        :
#======================================================================================================
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#Getting the user parameters
user=sys.argv[1]
cycle_date = sys.argv[2]

#SMTP USER LOGIN CREDENTIALS
username = "XXXXXXX" 
password = "XXXXXXX" # Password
from_addr=""  # Email Address from the email you want to send an email
server = smtplib.SMTP('')

testing_report="/home/" + user + "/testing/testing_report.xlsx"


"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

# Create the body of the message (a HTML version for formatting).
html = """
Hi all,<br><br> Please find the attached testing report for the cycle date """ + cycle_date +"""<br><br><br>Regards,<br>

"""



email_list = ["@gmail.com"]
for to_addrs in email_list:
    msg = MIMEMultipart()

    msg['Subject'] = "Testing Report for cycle date " + cycle_date
    #msg["Message-id"] = email.Utils.make_msgid()
    msg['From'] = from_addr
    msg['To'] = to_addrs

    # Attach HTML to the email
    body = MIMEText(html, 'html')
    msg.attach(body)

    # Attach Cover Letter to the email
    cover_letter = MIMEApplication(open(testing_report, "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename="testing_report.xlsx")
    msg.attach(cover_letter)


    try:
        send_mail(username,password,from_addr, to_addrs, msg)
        print "Email successfully sent to", to_addrs
    except Exception as e:
        #print 'SMTPAuthenticationError'
        print e
        print "Email not sent to", to_addrs

		
		# Function that sends email.
def send_mail(username,password,from_addr, to_addrs, msg):
    server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

# Read email list txt
#email_list = [line.strip() for line in open('email.txt')]

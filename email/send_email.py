# DAVIDRVU - 2018

from checkPass import checkPass
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from printDeb import printDeb
import datetime
import os
import pandas as pd
import smtplib
import sys

def send_email(debug, keyring_email_sender, smtp_host, smtp_port, email_receiver, msg_subject, msg_body, attach_files):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )

    gmail_user, gmail_password = checkPass(debug, keyring_email_sender)

    try:  
        server_ssl = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server_ssl.ehlo()   # optional
        server_ssl.login(gmail_user, gmail_password)

        msg = MIMEMultipart()
        msg['From']    = gmail_user
        msg['To']      = ", ".join(email_receiver)
        msg['Subject'] = msg_subject
        body           = msg_body
        msg.attach(MIMEText(body, 'plain'))
        attached_files = 0
        if attach_files is not None:
            for file_path in attach_files:  # add files to the message
                attachment = MIMEApplication(open(file_path, 'rb').read(), _subtype="txt")
                attachment.add_header('Content-Disposition','attachment', filename=os.path.basename(file_path))
                msg.attach(attachment)
                attached_files = attached_files + 1
        text = msg.as_string()
        server_ssl.sendmail(gmail_user, email_receiver, text)
        server_ssl.close()
        print(str(datetime.datetime.now()) + " -> Email sent! attached_files = " + str(attached_files))
    except Exception as e:  
        print("Something went wrong... e = " + str(e))
    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")

def main():
    ##################################################
    ## PARAMETROS
    ##################################################
    debug = 0
    keyring_email_sender = "gmail_pricing_bot"
    smtp_host            = "smtp.gmail.com"
    smtp_port            = 465
    email_receiver       = ["xxxxxx@gmail.com", "xxxxxx@gmail.com"]
    msg_subject          = "TEST de Juanito Envía emails :)"
    attach_files         = ["C:/databases/test_bot1.csv", "C:/databases/test_bot2.xlsx", "C:/databases/selfie.jpg"]
    msg_body             = "Hola! \nSoy Juanito.\nAhora puedo enviar emails!\nEn el presente email adjunto " + str(len(attach_files)) + " archivos. \nSaludos! \nDATETIME_ID = " + str(datetime.datetime.now())
    ##################################################

    # Create Files
    pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]}).to_csv(attach_files[0], index = False)
    pd.DataFrame({'c': [7,8,9], 'd': [10,11,12]}).to_excel(pd.ExcelWriter(attach_files[1]),'Sheet1', index = False)

    # Send email 
    send_email(debug, keyring_email_sender, smtp_host, smtp_port, email_receiver, msg_subject, msg_body, attach_files)

    print("DONE!")

if __name__ == "__main__":
    main()

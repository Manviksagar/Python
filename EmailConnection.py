# smtplib module send mail

import smtplib
def emailfunction(bodytext):
    TO = 'Alluciti@gmail.com'


    SUBJECT = 'TEST MAIL From Python Code'
    TEXT = bodytext

    # Gmail Sign In
    gmail_sender = 'Alluciti@gmail.com'
    gmail_passwd = 'sagarforu'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()

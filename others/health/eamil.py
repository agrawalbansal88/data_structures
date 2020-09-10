import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from get_email_html import get_email_html

def send_email(to, name, sanity_suits, regression_suits):
    me ='noreply_master@cisco.com'
    you =  "ankuragr@cisco.com,"+to

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "SMF Health Report" + " - " + name
    msg['From'] = me
    msg['To'] = you
    final_html = get_email_html(sanity_suits, regression_suits)
    part2 = MIMEText(final_html, 'html')
    msg.attach(part2)
    try:
        s = smtplib.SMTP('mail.cisco.com')
        s.sendmail(me, you.split(','), msg.as_string())
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")

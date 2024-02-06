
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.utils import COMMASPACE, formatdate 

# send_to = input('send to:\n')
# subject = input('subject:\n')
# message = input('message:\n')
send_to = 'xuansijian@126.com'
subject = 'test'
message = 'hello'


def send_mail(send_from, send_to, subject, message, server, port, username, password, use_tls): 
    try:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to#COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        smtp = smtplib.SMTP(server, port)
        if use_tls:
            smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(send_from, send_to, msg.as_string())
            smtp.quit() 
    except:
        raise ValueError('Send failed')

send_from = "Sijian" 
# send_to = ["xuansijian@126.com"] 
# subject = subject
# message = message
server = "smtp.gmail.com" 
port = 587 
username = "sijian.xuan@gmail.com" 
password = "fyss ephw aoqz gqmn"
use_tls = True 

send_mail(send_from=send_from,
          send_to=send_to,
          subject=subject,
          message=message, 
          server=server,
          port=port, 
          username=username, 
          password=password, 
          use_tls=use_tls)


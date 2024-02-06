# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:26:03 2023

@author: sijian
"""

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.utils import COMMASPACE, formatdate
from tkinter import *
from tkinter import ttk

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


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="send_to").grid(column=0, row=1)
ttk.Entry(frm,text='',command=None).grid(column=1, row=1)

ttk.Label(frm, text="subject").grid(column=0, row=2)
ttk.Entry(frm,text='',command=None).grid(column=1, row=2)

ttk.Label(frm, text="message").grid(column=0, row=3)
ttk.Entry(frm,text='',command=None).grid(column=1, row=3)
root.mainloop()

























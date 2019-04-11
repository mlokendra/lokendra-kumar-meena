#made in jupyter notebook
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user =input("Enter Your Email Address")
email_password = input("Enter Your Passward")
email_send = input("Enter receiver's Email Address")
subject = '# facebok Vs me'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Let\'s see conversation between Facebook and me\nME-: (log in) \nFACEBOOK-: what\'s on your mind\nME-: ………….\nFACEBOOK-: check in and tell your friends where you are \nME-: NO, one of my friend searching for me, I have to give money\nME-: (scrolling) \nFACEBOOK-: people you may know\nME-: I don\'t know :@\nFACEBOOK-: what you don\'t know !!!\n                       You have one mutual friend, you like some common pages , moreover, She\'s a girl\nME-: Ehh….     Make sense'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
print(server)
server.quit()

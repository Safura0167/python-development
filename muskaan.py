import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email="exampleemail@gmail.com"
receiver_email="recipientemail@gmail.com"
subject="Test Email"
body="this is a test email sent using python."
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username =("enter your username")
smtp_password = ("enter your password")
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"]=subject
message.attach(MIMEText(body,"plain"))
try:
    with smtplib.SMTP(smtp_server,smtp_port)as server:
        server.starttls()
        server.login(smtp_username,smtp_password)
        server.sendmail(sender_email,receiver_email,message.as_string())
        print("........email sent.......")
except Exception as e:
    print(f"error:{e}")
if __name__=="__main__":
    subject = "Test Email"
body = "This is a test email sent using Python!"
to_email = "recipient@gmail.com"
    
sender_email = (subject, body, to_email)















import smtplib, ssl

def send_email(destinatario, email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender = "fgsj.developer@gmail.com"
    password = "agchjrljnktcmtpb"
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, destinatario, email)
        
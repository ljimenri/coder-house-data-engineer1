import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(**context):
    subject = "subject"
    from_address = "email.de.ch.ljimenez@gmail.com"
    password = "dfhhveivyfjrlcec"
    to_address = "artybandy@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    html_content = f"""
    <html>
    <body>
        <p>Hola!</p>
        <p>Proceso ETL finalizado exitosamente.</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html'))

    print(
    f"""
    subject:    {subject}
    from_address:   {from_address}
    password:   {password}
    to_address: {to_address}
    """
    )

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")